""" RoboGalaxy Test Dashboard

Modified from original robot script

Usage:  pushdata2sql.py input-xml  jenkins_build_tag    Jenkins_job_url     PushTag[optional]

This script reads robot output xml file, extracts test results and pushes data to SQL Server

Examples:
  Python C:\Scripts\PUSHDATA2SQL.py  C:\scripts\CAT-1-DryRun--Hardware_92_CANMIC-Update_Output.xml       jenkins-CAT-1-DryRun--Hardware_92_CANMIC-Update_2014-07-11_22-30-15  http://16.84.101.158:8080/job/CAT-1-DryRun--DCS/97/   PushTag


"""

import sys
import os
import csv
import pyodbc


from robot.result import ExecutionResult
from robot import utils


def process_suite(suite, items, level=0):
    if 'suite' in items:
        process_item(suite, level, 'Suite')
    if 'keyword' in items:
        for kw in suite.keywords:
            process_keyword(kw, level + 1)
    for subsuite in suite.suites:
        process_suite(subsuite, items, level + 1)
    for test in suite.tests:
        process_test(test, items, level + 1)


def process_test(test, items, level):
    if 'test' in items:
        process_item(test, level, 'Test', 'suite' not in items)
    if 'keyword' in items:
        for kw in test.keywords:
            process_keyword(kw, level + 1)


def process_keyword(kw, level):
    if kw is None:
        return
    process_item(kw, level, kw.type.capitalize())
    for subkw in kw.keywords:
        process_keyword(subkw, level + 1)


def process_item(item, level, item_type, long_name=False):
    testtag = "NA"
    indent = '' if level == 0 else ('|  ' * (level - 1) + '|- ')
    name = (item.longname if long_name else item.name).encode('UTF-8')
    elapsed = utils.elapsed_time_to_string(item.elapsedtime)
    item_type = indent + item_type
    if item_type == "|- Test":
        testtag = ", ".join(item.tags._tags) if item.tags._tags else ""
    item_name = name
    item_status = item.status
    item_starttime = item.starttime
    item_endtime = item.endtime
    item_elapsed = elapsed
    item_elapsesecs = str(item.elapsedtime / 1000.0)
    try:
        querystring = "insert into testsuites values \
            ('" + item_type + "','" + item_name + "','" + item_status + "','" + item_starttime + "','" + item_endtime + "','" + item_elapsed + "'," + item_elapsesecs + ",'" + buildtag + "','" + testtag + "')"
        print querystring
        cur.execute(querystring)
        con.commit()
    except Exception as e:
        print e
        pass


def push_testrun_to_sql(buildtag, jenkinsurl):
    testsuite = str(suite.longname)
    starttime = str(suite.starttime)
    endtime = str(suite.endtime)
    message = str(suite.full_message)
    passes = str(suite.statistics.all.passed)
    failures = str(suite.statistics.all.failed)
    querystring = "insert into testrun values \
        ('" + testsuite + "','" + starttime + "','" + endtime + "','" + message + "'," + passes + "," + failures + ",'" + buildtag + "','" + jenkinsurl + "','" + "',''" + ")"
    print querystring
    cur.execute(querystring)
    con.commit()


def push_testdetails_to_sql(inxml, buildtag):
    result = ExecutionResult(inxml)
    stats = result.statistics
    test_details = result.suite.tests._items
    testsuite = stats.suite.stat._name
    for test in test_details:
        testcase_name = test.name
        tags = ", ".join(test.tags._tags) if test.tags._tags else ""
        test_passed = str(test.passed)
        querystring = "insert into testrundetails values \
        ('" + buildtag + "','" + testsuite + "','" + testcase_name + "','" + tags + "','" + test_passed + "')"
        print querystring
        cur.execute(querystring)
        con.commit()

if __name__ == '__main__':

    try:
        con = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=;DATABASE=;UID=sa;PWD=')
        cur = con.cursor()

        if not (4 <= len(sys.argv)) or sys.argv[1] in ('--help', '-h'):
            print __doc__
            sys.exit(1)

        inxml = sys.argv[1]
        buildtag = sys.argv[2]
        jenkinsurl = sys.argv[3]

        items = 'suite-test-keyword'
        suite = ExecutionResult(inxml).suite
        process_suite(suite, items.lower())
        push_testrun_to_sql(buildtag, jenkinsurl)

        if (len(sys.argv) > 4 and sys.argv[4] == "PushTag"):
            push_testdetails_to_sql(inxml, buildtag)

        con.close()

    except Exception as e:
        print "Caught %s" % e
