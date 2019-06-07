"""
    PushData2Rally
    Process Robot Framework 'output.xml' files and create corresponding
    entities in Rally.

    Created by:  Russell Briggs  08/2016

"""
import argparse
import backoff
from datetime import datetime
from dateutil.parser import parse
import logging
import os
from os.path import exists
from pyral import Rally, RallyRESTAPIError
import re
import sys
import xml.etree.ElementTree as ET
import urllib2

errout = sys.stderr.write

# TODO: Should not have to have this hack in here!!!
os.environ['https_proxy'] = 'https://web-proxy.corp.hpecorp.net:8088'
os.environ['HTTPS_PROXY'] = 'https://web-proxy.corp.hpecorp.net:8088'

log = logging.getLogger('rally_lib')
logging.basicConfig(format='%(asctime)-15s,%(levelname)s,%(name)s,%(message)s')
log.setLevel(logging.INFO)

RALLY = 'rally1.rallydev.com'


def get_metadata(root):
    metadata = {}
    for meta in root.findall('.//metadata'):
        for item in meta.findall('item'):
            metadata[item.attrib['name']] = item.text
    return metadata


def get_suites(e, folders):
    if e._children:
        for child in e._children:
            if e.tag == 'suite':
                folders[e.attrib['id']] = e.attrib
                folders[e.attrib['id']]['tests'] = []
                get_suites(child, folders)


def get_tests(e, folders):
    for test in e.findall('.//test'):
        text = ""
        log.info("\t{0} - {1}".format(test.attrib['id'], test.attrib['name']))
        i = test.attrib['id'].rfind("-")
        suite_id = test.attrib['id'][:i]

        if test._children:
            for child in test._children:
                if child.tag == 'status':
                    if child.attrib['status'] == 'FAIL':
                        text = child.text
                    folders[suite_id]['tests'].append(RobotTest(test, text))


def scrub(txt):
    regex = re.compile('(&|\+|\*|/|!|%|-|=|<|>|\?)')
    newtxt = regex.sub(' ', txt)
    regex = re.compile("\s+")
    newtxt = regex.sub(' ', newtxt.replace('\\', ' '))
    return newtxt


class RobotTest(object):
    def __init__(self, element, text):
        rep = re.compile(":")
        self.id = element.attrib['id'].strip()
        self.name = rep.sub(' ', element.attrib['name']).strip()
        try:
            self.doc = element.find('doc').text
        except:
            self.doc = ""
        status = element.find('status')
        self.status = str(status.attrib['status'])
        self.starttime = parse(status.attrib['starttime'])
        self.endtime = parse(status.attrib['endtime'])
        self.date = self.starttime.strftime('%Y-%m-%d')
        self.time = self.starttime.strftime('%H:%M:%S')
        self.duration = (self.endtime - self.starttime).total_seconds()
        self.text = text

    def __repr__(self):
        return self.name


def main():
    err = False
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-u', '--username', help='Rally username', required=True)
    parser.add_argument('-p', '--password', help='Rally password', required=True)
    parser.add_argument('--server',
                        help='Optional Rally server url.  Example: server_url:port    Default is "rally1.rallydev.com"',
                        required=False, default=RALLY)
    parser.add_argument('-w', '--workspace', help='Rally workspace.  Example: OneView', required=False,
                        default='OneView')
    parser.add_argument('-pr', '--project', help='Rally project.  Example: FVT-CRM', required=True)
    parser.add_argument('-sp', '--server_ping', help='Ping Rally server', required=False, default=False)
    parser.add_argument('-tf', '--testfolder', help='Parent Test Folder ID.  Example: TF24', required=True)
    parser.add_argument('-ts', '--testset', help='Test Set ID.  Example: TS21', required=False)
    parser.add_argument('-ty', '--type', help='Test Type: Functional|Regression', required=True)
    parser.add_argument('-wp', '--workproduct', help='Work Product: Example: OVS300', required=False)
    parser.add_argument('-hw', '--hardware', help='Hardware Platform: C-Series|T-Series|Rack Mount', required=False)
    parser.add_argument('xmlfile', metavar='path\\output.xml', type=str, nargs='+',
                        help='The Robot Framework output.xml file.  This can be located anywhere, named differently,\
                         and you can pass in multiple files.')
    parser.add_argument('-sr', '--skipresults',
                        help='Skip creating Test Case Results. Only Test Folders and Test Cases are created.',
                        required=False)

    args = parser.parse_args()

    for xfile in args.xmlfile:
        if not xfile.startswith("http") and not exists(xfile):
            errout("ERROR: Failed to find output.xml file: %s\n" % xfile)
            err = True

    rally = Rally(args.server, workspace=args.workspace, project=args.project, user=args.username,
                  password=args.password, server_ping=args.server_ping)
    wksp = rally.getWorkspace()

    # These are retry wrappers for the Rally verbs.  Rally often will return a RallyRESTAPIError, but simply retrying
    # the same operation again will succeed.  Retries are set to 5 times below.
    def backoff_hdlr(details):
        print ("RallyRESTAPIError encountered. Waiting {wait:0.1f} seconds afters {tries} tries".format(**details))

    @backoff.on_exception(backoff.expo,
                          RallyRESTAPIError,
                          max_tries=5,
                          on_backoff=backoff_hdlr)
    def get(*ags, **kwags):
        return rally.get(*ags, **kwags)

    @backoff.on_exception(backoff.expo,
                          RallyRESTAPIError,
                          max_tries=5,
                          on_backoff=backoff_hdlr)
    def create(*ags, **kwags):
        return rally.create(*ags, **kwags)

    @backoff.on_exception(backoff.expo,
                          RallyRESTAPIError,
                          max_tries=5,
                          on_backoff=backoff_hdlr)
    def update(*ags, **kwags):
        return rally.update(*ags, **kwags)

    def get_or_create_folder(name, pref):
        try:
            name = scrub(name)
            folder = get('TestFolder', query='((Name = "%s") AND (Parent = %s))' % (name, pref), instance=True)
        except RallyRESTAPIError, details:
            errout('ERROR: %s \n' % details)
            sys.exit(4)

        if not folder or hasattr(folder, 'resultCount'):
            tf_data = {"Workspace": wksp.ref,
                       "Name": name,
                       "Parent": pref,
                       }
            try:
                folder = create('TestFolder', tf_data)
                log.info("Creating Test Folder: {0}".format(name))
            except RallyRESTAPIError, details:
                errout('ERROR: %s \n' % details)
                sys.exit(4)
        return folder

    # make sure parent folder exists
    ptf = get('TestFolder', query="FormattedID = %s" % args.testfolder, instance=True)

    if not ptf or hasattr(ptf, 'resultCount'):
        errout("ERROR: Failed to find TestFolder %s\n" % args.testfolder)
        err = True

    if args.testset:
        # make sure test set exists
        ts = get('TestSet', query="FormattedID = %s" % args.testset, instance=True)

        if not ts or hasattr(ts, 'resultCount'):
            errout("ERROR: Failed to find TestSet %s\n" % args.testset)
            err = True

    if args.workproduct:
        # make sure work product exists
        wp = get('Requirement', query="FormattedID = %s" % args.workproduct, instance=True)

        if not wp or hasattr(wp, 'resultCount'):
            errout("ERROR: Failed to find WorkProduct\Requirement %s\n" % args.workproduct)
            err = True

    if err:
        sys.exit(1)

    for xfile in args.xmlfile:
        log.info("Reading %s" % xfile)
        # if xfile is an URL, retrieve output.xml from there
        if xfile.startswith("http"):
            tree = ET.parse(urllib2.urlopen(xfile))
        else:
            tree = ET.parse(xfile)
        parent_suite = tree.getroot().find('suite')

        folders = {}
        # populate folders with Robot Suites
        get_suites(parent_suite, folders)
        # get metadata
        metadata = get_metadata(parent_suite)
        build = 'no build metadata'
        if "OneView Version" in metadata:
            build = metadata["OneView Version"]

        # retrieve tests and add them to folders
        get_tests(parent_suite, folders)

        # get the Rally user
        try:
            tester = get('User', query='(UserName = "%s")' % (args.username), instance=True)
        except RallyRESTAPIError, details:
            errout('ERROR: %s \n' % details)
            sys.exit(4)

        # Create all the Test Folders, and record _ref
        p_ref = ptf.ref  # first time through, this is the folder passed in args
        for folder in sorted(sorted(folders), key=len):
            if "-" in folder:
                i = folder.rfind("-")
                p = folder[:i]
                p_ref = folders[p]['_ref']
            if '_ref' not in folders[folder]:
                f = get_or_create_folder(folders[folder]['name'], p_ref)
                folders[folder]['_ref'] = f._ref
                folders[folder]['p_ref'] = p_ref
                folders[folder]['FormattedID'] = f.FormattedID

        # Create test cases in their parent folder
        for tf in folders.itervalues():
            for test in tf['tests']:
                name = scrub(test.name)

                try:
                    tc = get('TestCase', query='((Name = "%s") AND (TestFolder.FormattedID = %s))' %
                                               (name, tf['FormattedID']), instance=True)
                except RallyRESTAPIError, details:
                    errout('ERROR: %s \n' % details)
                    sys.exit(4)

                if not tc or hasattr(tc, 'resultCount'):
                    if name == "":
                        continue
                    log.info("Creating Test Case: {0}".format(name))

                    tc_data = {"Workspace": wksp.ref,
                               "Name": name,
                               "Description": test.doc,
                               "Owner": tester.ref,
                               "Test Folder": tf['_ref'],
                               "Type": args.type,
                               "Method": "Automated"
                               }
                    if args.workproduct and wp:
                        tc_data['WorkProduct'] = wp.ref
                    if args.hardware:
                        tc_data['Hardware Platform'] = args.hardware
                    try:
                        tc = create('TestCase', tc_data)
                    except RallyRESTAPIError, details:
                        errout('ERROR: %s \n' % details)
                        sys.exit(4)

                if args.testset:
                    tc_in_ts = False

                    try:
                        tstc = get('TestSet', query="FormattedID = %s" % args.testset, instance=True, fetch="TestCases")
                        tclist = list(tstc.TestCases)
                        if len(tclist) > 0:
                            for i in tclist:
                                if i.ref == tc.ref:
                                    tc_in_ts = True
                                    log.info("Test Case: {0} already exists in Test Set: {1}".format(name, ts.Name))
                                    break
                    except RallyRESTAPIError, details:
                        errout('ERROR: %s \n' % details)
                        sys.exit(4)

                    if not tc_in_ts:
                        tclist = [{'_ref': x.ref} for x in tclist]
                        log.info("Adding Test Case: {0} to Test Set: {1}".format(name, ts.Name))
                        tsoid = ts.oid
                        tclist.append({"_ref": tc.ref})
                        ts_data = {"ObjectID": tsoid, "TestCases": tclist}

                        try:
                            tsu = update('TestSet', ts_data)
                        except RallyRESTAPIError, details:
                            errout('ERROR: %s \n' % details)
                            sys.exit(4)

                # test case results
                if not args.skipresults:
                    try:
                        if args.testset:
                            tcr = get('TestCaseResult',  # allow the same test result to be part of more than 1 test set
                                      query='((((TestCase.FormattedID = %s) AND (Build = "%s")) AND (Date = %s)) AND \
                                      (TestSet = %s))' %
                                            (tc.FormattedID, build, datetime.isoformat(test.starttime), ts.ref))
                            msg = "Test Case Result already exists for '%s' build:%s & date:%s & test set:%s.  Skipping." % \
                                  (name, build, test.date, ts.Name)
                        else:
                            tcr = get('TestCaseResult',
                                      query='(((TestCase.FormattedID = %s) AND (Build = "%s")) AND (Date = %s))' %
                                            (tc.FormattedID, build, datetime.isoformat(test.starttime)))
                            msg = "Test Case Result already exists for '%s' build:%s & date:%s.  Skipping." % \
                                  (test.name, build, test.date)

                    except RallyRESTAPIError, details:
                        errout('ERROR: %s \n' % details)
                        sys.exit(4)
                    if tcr.resultCount > 0:
                        log.warn(msg)
                        continue
                    verdict = "Pass" if test.status == "PASS" else "Fail"
                    tcr_data = {"Workspace": wksp.ref,
                                "TestCase": tc.ref,
                                "Build": build,
                                "Date": datetime.isoformat(test.starttime),
                                "Duration": format(test.duration, '.2f'),
                                "Notes": test.text,
                                "Verdict": verdict,
                                "Tester": tester.ref,
                                }

                    if args.testset:
                        tcr_data['TestSet'] = ts.ref
                    try:
                        tcr = create('TestCaseResult', tcr_data)
                    except RallyRESTAPIError, details:
                        errout('ERROR: %s \n' % details)
                        sys.exit(4)

                    log.info("Created  TestCaseResult OID: %s  TestCase: %s  Build: %s  Date: %s  Verdict: %s" %
                             (tcr.oid, tc.FormattedID, tcr.Build, tcr.Date, tcr.Verdict))

    log.info("Done.")


if __name__ == '__main__':
    main()
