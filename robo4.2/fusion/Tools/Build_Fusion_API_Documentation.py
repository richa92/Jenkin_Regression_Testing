"""

Builds the FusionLibrary and Resource\api keyword documentation

First arg is where to create documentation folder.  Required
Second arg (any value) enable "dry run".  Only prints what would have been done.  Optional
Third arg (any value) enable "just_one_file".  Only process 1 Resource file.  A Dev thing.  Optional

"""

import os
import re
import glob
import subprocess
import sys
import datetime

just_one_file = False
src = "https://raw.github.hpe.com/ron-soto/RG_Branch_Shared_Tools/master/Build_Fusion_API_Doc"
raw = "?raw-true"
front_page = "OneViewRoboGalaxyLibrary.html"

cfm_html = "Plexxi_CFM_Keywords.html"
cfm_src = "Lib/site-packages/RoboGalaxyLibrary/keywords"
cfm_lib = "plexxi.PlexxiLibraryKeywords"


def sort_by_keyword(kw):
    matchObj = re.search("html>(\w.*)</a", kw)
    if (not matchObj):
        print "kw: %s did not match" % kw
        return "ZZZZZZZZ"
    # print matchObj.group(1)
    return matchObj.group(1)


def build_api():

    # used to provide spacing between keyword hyper link and additional info
    # in the index file
    spaces = "&nbsp;" * 4

    # Sorted list of Resource\api keywords
    index_hrefs = []

    if not dry_run:
        main_page = os.path.join(doc_dir, front_page)
        if os.path.exists(main_page):
            os.remove(main_page)
        main = open(main_page, "w")
        main.write("<h1>OneView RoboGalaxy Fusion Library</h1> </br>\n")
        main.write("<html>\n")
        main.write("<div>\n")
        main.write('<img src="%s/library.png%s" width=80 height=40>\n' % (src, raw))
        main.write('<a href=./FusionLibrary.html>Sorted Fusion Library Keywords (aka "Low Level Keywords")</a><br/><br/>\n')
        main.write('<img src="%s/library.png%s" width=80 height=40>\n' % (src, raw))
        main.write('<a href=./Fusion_Resources_Index.html>Sorted Resources Keywords (aka "High Level Keywords")</a><br/><br/>\n')
        main.write('<img src="%s/library.png%s" width=80 height=40>\n' % (src, raw))
        main.write('<a href=./%s>Sorted Plexxi CFM Keywords</a><br/><br/>\n' % cfm_html)
        main.write('<h2>High Level Keywords by Resource/Category</h2>\n')

    for path, dirs, files in os.walk(api_dir):
        # if dirs is empty, then we are done as we actually processed all the
        # file using glob below
        if (len(dirs) == 0):
            print "\nDone with api Resources.\n"
            break
        for dir in sorted(dirs):
            print "\n%s" % dir
            libdocpath = os.path.join(doc_dir, dir)
            if (not os.path.isdir(libdocpath)):
                print "%s: Mkdir %s" % (mode, libdocpath)
                if (not dry_run):
                    os.mkdir(libdocpath)

            main.write('<br/><img src="%s/folder.jpg%s" width=20 height=20>\n' % (src, raw))
            main.write('<a href=%s>%s/%s</a><br/>\n' % (dir, path, dir))

            # print "%s/%s" % (api_dir, dir)
            files = glob.glob("%s/%s/*.txt" % (path, dir))

            for file in files:
                # Capture the keyword names in this file
                process = subprocess.Popen(
                    ["python", "-m", "robot.libdoc", "%s" % file, "list"], stdout=subprocess.PIPE)
                (keywords, err) = process.communicate()
                process_status = process.wait()
                # build an html href line for the keywords and append to list
                keywords = keywords.split('\n')
                for keyword in keywords:
                    if (keyword != ''):
                        kw_path = file.replace('\\.', '').replace('\\', '/')
                        kw_html = kw_path.replace(
                            'Resources/api/',
                            '').replace(
                            'txt',
                            'html')
                        index_hrefs.append(
                            '<a href=%s>%s</a>%s(%s)</a><br/>' %
                            (kw_html, keyword.strip(), spaces, kw_path))

                # create name of the doc file for this resource item
                libdocfile = file.replace(
                    "txt",
                    "html").replace(
                    "./Resources/api",
                    doc_dir)
                # libdocfile = libdocfile.replace("\\", "/")

                main.write('%s<img src="%s/file.png%s" width=20 height=20>\n' % (spaces, src, raw))
                main.write('<a href=%s>%s</a><br/>\n' % (kw_html, kw_path.split('/')[-1]))

                # build the documentation for this resource item
                print "%s: python -m robot.libdoc %s %s" % (mode, file, libdocfile)
                if (not dry_run):
                    os.system(
                        "python -m robot.libdoc %s %s" %
                        (file, libdocfile))

                if just_one_file:
                    break

            if just_one_file:
                break

    # create the index_file file
    # index_file will contain an alphabetised list of the keywords in
    # Resources\api
    if (dry_run):
        print "Since dry_run, here are the first 5 entries in the index."
        print "\n".join(index_hrefs[0:5])
    else:
        index_file = os.path.join(doc_dir, "Fusion_Resources_Index.html")
        index_hrefs.sort(key=sort_by_keyword)
        index = open(index_file, "w")
        index.write(
            "<h1> Fusion Resource API Keywords (%d keywords)</h1> </br>\n" %
            len(index_hrefs))
        index.write("<html>\n")
        index.write("<div>\n")
        index.write("\n".join(index_hrefs))
        index.write("\n</div>\n")
        index.write("</html>\n")
        index.close()

        now = datetime.datetime.now()
        print ("Adding Created timestamp %d/%d/%d  %d:%d:%d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
        main.write("\n<br/>Created %d/%d/%d  %d:%d:%d<br/>\n" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
        main.write("\n</div>\n")
        main.write("</html>\n")
        main.close()
    print


def build_fusionlibrary():
    # Now FusionLibrary keywords (python, "low" level keywords)
    print "\nBuild FusionLibrary keyword doc."
    libdocfile = os.path.join(doc_dir, "FusionLibrary.html")
    print "%s: python -m robot.libdoc ./FusionLibrary %s" % (mode, libdocfile)
    if (not dry_run):
        os.system("python -m robot.libdoc ./FusionLibrary %s" % libdocfile)
    print


def build_plexxi_cfm_library():
    cwd = os.getcwd()
    print "Currently at: %s" % cwd

    cfm_path = os.path.join(cwd, cfm_src)
    print "cfm_path: %s" % cfm_path
    print "cd to : %s" % cfm_path
    os.chdir(cfm_path)

    cfm_doc_html = os.path.join(cwd, doc_dir)
    cfm_doc_html = os.path.join(cfm_doc_html, cfm_html)
    print "%s: python -m robot.llibdoc %s %s" % (mode, cfm_lib, cfm_doc_html)

    if (not dry_run):
        os.system("python -m robot.libdoc %s %s" % (cfm_lib, cfm_doc_html))

    os.chdir(cwd)
    cwd = os.getcwd()
    print "Currently at: %s" % cwd


if __name__ == "__main__":
    dirlist = os.listdir('.')
    print
    if ("FusionLibrary" not in dirlist) and ("Resources" not in dirlist):
        print "Expected to execute from same level as FusionLibrary and Resources.\n"
        sys.exit(1)

    arg_count = len(sys.argv)

    if (arg_count > 2):
        dry_run = True
        mode = "dry run"
    else:
        dry_run = False
        mode = "Executing"

    if (arg_count < 2):
        print "You must pass in path to location where library is to be created."
        sys.exit(1)
    else:
        doc_dir = sys.argv[1]
        if (not os.path.isdir(doc_dir)):
            try:
                # since os.mkdirs() not exist must grunt through it.
                paths = doc_dir.replace("\\", "/").split('/')
                if (paths[0] == "."):  # relative path
                    dirpath = "./"
                else:
                    dirpath = "/"
                paths = paths[1:]
                for path in paths:
                    dirpath += path
                    if (os.path.isdir(dirpath)):
                        dirpath += "/"
                        continue
                    if (dry_run):
                        print "Would mkdir %s" % dirpath
                    else:
                        print "mkdir %s" % dirpath
                        os.mkdir(dirpath)
                    dirpath += "/"
            except Exception:
                print "Unable to make directory %s" % doc_dir
                sys.exit(1)

    api_dir = "./Resources/api"

    if (arg_count > 3):
        just_one_file = True

    build_api()

    build_fusionlibrary()

#    build_plexxi_cfm_library()
