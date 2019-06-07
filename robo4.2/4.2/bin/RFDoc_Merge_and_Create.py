import os
import sys
import re
import argparse
import time
from selenium import webdriver
try:
    from robot.libdoc import libdoc
except ImportError:
    print "Please install robot library python bindings properly"
    sys.exit(1)

BASE_ROBOT_PATH = "C:\\Python27\\Lib\\site-packages\\"
ROBOT_PATH_SUFFIX = "robot\\libdoc.py"
LIBDOC_PATH = ""
KW_HEADER = "*** Keywords ***\n"
OPEN_BRACE = 0

USAGE = """
******************************************************************************
                RFDOC Merge and Create XML and HTML
******************************************************************************

Description
******************************************************************************
The Tool is used to merge Multiple Resource files from a base folder specified
into a single Resource file text and then generate HTML and XML files with the
same using libdoc.py.


Usage
******************************************************************************

After running the batch file provided user needs to give input for the
following.
1. A valid base path from where the tool can search for resource files
2. A valid file name for single resource file, HTML and XML files to be created.
   Dont give extension as the same name will be taken for all three file extension
   to be created.
3. Respond "Yes" or "No" for providing excluding directories
    > If "Yes", then provide all the relative path of directories that need to be
      excluded from the base path. Provide the directories by delimiting each by
      comma separator.

    > If "No" the execution will be continued without any exclusion.
4. Enter the version of the RFDoc to be created
Note: External keyword is a keyword that is used for writing Testcases and
      Internal Keywords are those keywords used by the External keywords
      inside resource file

Syntax
*******
      External keyword in the resource file should be as follows,

Keyword
    [Documentation]     {External} Description.....
    ...                 Description  contd.....


Example:
******************************************************************************

Enter the RFDoc File name: C:\RoboGalaxy\Aadhi_RG\Resources

Enter the RFDoc File name: Aadhi_RG

Enter the version of the RFDoc: 2.5

DO you want to exclude any path in base path provided? [Yes or No]: Yes

Please Enter relative paths to be excluded from the base path given, separated by
comma [,]: abc, abc/def, xyz


Output: Aadhi_RG.html, Aadhi_RG.xml, Aadhi_RG.txt

******************************************************************************

"""
print USAGE
"""
SEARCH_PATH = raw_input("Enter the Resource files path: ")
if not os.path.exists(SEARCH_PATH):
    print "\nThe Path entered is not valid or does not exist. Please enter a single valid base path for searching the resource files.\n"
    sys.exit(1)
FILENAME = raw_input("\nEnter the RFDoc File name without extension: ")

while 1:
    KEYWORD = raw_input("\nCreate RFDoc with only 'External Keywords'? [Yes Or No] : ")
    if KEYWORD.lower() not in ['yes', 'y', 'n', 'no']:
        print "\nPlease enter any of the following as answer. 'yes', 'y', 'n', 'no'\n"
    else:
        break

VERSION = raw_input("\nEnter the Version of the RFDoc: ")

while 1:
    EXCLUDE = raw_input("\nDO you want to exclude any path in base path provided? [Yes or No]: ")
    if EXCLUDE.lower() not in ['yes', 'y', 'n', 'no']:
        print "\nPlease enter any of the following as answer. 'yes', 'y', 'n', 'no'\n"
    else:
        break
try:
    if EXCLUDE.lower() == 'yes' or EXCLUDE.lower() == 'y':
        EXCLUDE_PATH = raw_input("\nPlease Enter relative paths to be excluded from the base path given, separated by comma [,] : ")
        EXCLUDE_PATH = [os.path.join(SEARCH_PATH, each_path.strip()) for each_path in EXCLUDE_PATH.split(',') if (os.path.exists(os.path.join(SEARCH_PATH,each_path )))]
        print EXCLUDE_PATH
except OSError, err:
    print "\nOne of the path given in comma separated list does not exist. Make sure you have given proper relative path from actual search path given.\n"
    sys.exit(1)
"""
VERSION = EXCLUDE_PATH = EXCLUDE = FILENAME = PY_SEARCH_PATH = TEXT_SEARCH_PATH = XML_PATH = HTML_PATH = LIB_PATH = ""
SERVER_URL = "http://127.0.0.1:8000"


def discover_robot_library():
    global LIBDOC_PATH
    robot_lib_pattern = "robotframework-.*-.*.egg"
    python_files = os.listdir(BASE_ROBOT_PATH)
    for each in python_files:
        if re.match(robot_lib_pattern, each):
            robot_framework = re.match(robot_lib_pattern, each).group()
            break

    if robot_framework:
        LIBDOC_PATH = os.path.join(
            BASE_ROBOT_PATH, robot_framework, ROBOT_PATH_SUFFIX)
        if not os.path.exists(LIBDOC_PATH):
            raise Exception("Robot path is empty or does not exist")
    else:
        raise Exception("Robot path not discovered")


def extract_all_keyword_code(filename):
    kw_full_code = []
    kw_code = ""
    kw_start_pattern = "^\w"
    kw_code_pattern = "^[\t ]+[A-Za-z\$\.\\@#\[].*"
    with open(filename, 'r') as fp:
        for each_line in fp:
            if not re.search("[A-Za-z]", each_line):
                continue
            if each_line.startswith("Resource") or each_line.startswith("Variables") or each_line.startswith("Library"):
                continue
            else:
                if re.search(kw_start_pattern, each_line):
                    if kw_code:
                        kw_full_code.append(kw_code)
                        kw_code = ""
                    kw_start = True
                    kw_code = each_line
                elif re.search(kw_code_pattern, each_line):
                    kw_start = False
                    kw_code = kw_code + each_line
        kw_full_code.append(kw_code)
    return kw_full_code


def filter_external_keywords(kw_data):
    data = []
    ext_kw_pattern = "\[Documentation]\s+\{External\}"
    for each_kw in kw_data:
        if re.search(ext_kw_pattern, each_kw):
            data.append(each_kw)
    return data


def create_txt_with_py_keywords(filename):
    """
    Create text file with keywords from python source file
    :param filename:
    """
    """
    Create text file with keywords from python source file
    :param filename:
    :return data:
    """
    global OPEN_BRACE
    kw_full_code = []
    cline = ""
    kw_code = ""
    line = ""
    tmp_str = ""
    kw_start_pattern = "def "
    kw_code_pattern = "^[\t ]+[A-Za-z\$\.\\@#\[].*"

    array = []
    with open(filename, 'r') as fp:
        for each_line in fp:
            each_line = each_line.replace(
                "'''", '"""')  # Fix for incorrect comment quotes(''') in the .py file
            # print each_line
            # To read the arguments spread across multiple lines
            if len(each_line) > 1:
                if each_line.lstrip(' ').startswith("def") and each_line[-2] == '(' or OPEN_BRACE == 1:
                    each_line = each_line.lstrip(' ')
                    # print each_line
                    if not each_line[0] == '#':
                        tmp_str = tmp_str + each_line.rstrip('\n')
                    OPEN_BRACE = 1
                    if each_line[-2] == ':' and each_line[-3] == ')':
                        array.append(tmp_str)
                        OPEN_BRACE = 0
                else:
                    array.append(each_line)

    for index in range(len(array)):
        if not re.search("[A-Za-z]", array[index]):
            continue
        if array[index].startswith("import") or array[index].startswith("class") or array[index].__contains__("__init__")\
                or array[index].__contains__("__del__") or array[index].__contains__("main"):
            continue
        else:
            # Read the function name and arguments
            if re.search(kw_start_pattern, array[index]):
                kw_code = array[index].lstrip()[4:]
                # print kw_code
                # Read arguments
                if re.search(r"\((.+)\)", kw_code, re.M | re.I):
                    key = kw_code.split('(')[0].replace('_', ' ')
                    line = key + "\t\t[Arguments]\t"
                    arg_list = (
                        re.search(r"\((.+)\)", kw_code, re.M | re.I)).group(1).split(',')
                    for i in range(len(arg_list)):
                        # tmp = "$".join(arg_list[i])
                        line = line + "\t\t$" + \
                            "{" + arg_list[i].split('=', 1)[0] + "}"
                else:  # Read the function without arguments
                    line = kw_code.split('(')[0].replace('_', ' ')

                # print line
                # Read comments between """ quotes
                if '"""' not in array[index + 1]:
                    # print array[index+1]
                    continue
                elif re.search(r'"""$', array[index + 1]):
                    comment = re.findall(r'"""([^"]*)', array[index + 1])
                    cline = comment[0]
                    if cline == '\n':
                        for i in range(index + 2, len(array)):
                            if re.search(r'"""$', array[i]):
                                index += i
                                break
                            if array[i].__contains__("Example:") or array[i].__contains__("Examples:"):
                                cline = cline + \
                                    "\n\t...\t\t\n\t...\t\t" + array[i]
                            elif array[i].__contains__(" | "):
                                cline = cline + "\n\t...\t\t" + array[i]
                            else:
                                cline = cline.rstrip(
                                    '\n') + array[i].rstrip('\n')
                    # print cline
                else:
                    comment = re.findall(r'"""([^\n]*)', array[index + 1])
                    cline = comment[0]
                    if cline:
                        for i in range(index + 2, len(array)):
                            if re.search(r'"""$', array[i]):
                                index += i
                                break
                            if array[i].__contains__("Example:") or array[i].__contains__("Examples:"):
                                cline = cline + \
                                    "\n\t...\t\t\n\t...\t\t" + array[i]
                            elif array[i].__contains__(" | "):
                                cline = cline + "\n\t...\t\t" + array[i]
                            else:
                                cline = cline.rstrip(
                                    '\n') + array[i].rstrip('\n')
                    # print "--------------",cline
            if line:
                kw_full_code.append(line + "\n\n")
                if cline != '\n':
                    # Fix to avoid removal of '\' by 'libdoc' library
                    cline = cline.replace("\\", "\\\\")
                    kw_full_code.append(
                        "\t[Documentation]\t\t" + cline + "\n\n")
                kw_code = ""
                line = ""
                cline = "\n"

    # return kw_full_code
    full_data = ''.join(kw_full_code)
    with open("tmp.txt", 'a+') as fp:
        # fp.write(KW_HEADER)
        fp.write(full_data)

# def create_xml_with_py_keywords(py_script_list):
#   xml_header = """<?xml version="1.0" encoding="UTF-8"?>
# <keywordspec generated="%s" type="library" name="%s" format="ROBOT">
# <version>%s</version>
# <scope>global</scope>
# <namedargs>yes</namedargs>
# <doc>Documentation for test library.</doc>
    """ % (time.asctime(), FILENAME, VERSION)
    xml_footer = "</keywordspec>"
    libdoc_xml_command = "python %s -f xml -v %s %s %s"
    kw_code_pattern = "<kw.*>[\w\s<>/]+</kw>"
    main_xml_kws = []
    for each_script in py_script_list:
        xml_name = each_script.split('\\')[-1].split('.')[0] + '.xml'
        #print "DEBUG", "--", LIBDOC_PATH, "--", VERSION, "--", each_script, "--", xml_name, "DEBUGEND"
        print libdoc_xml_command % (LIBDOC_PATH, VERSION, each_script, xml_name)
        os.system(libdoc_xml_command % (LIBDOC_PATH, VERSION, each_script, xml_name))
        with open(xml_name) as xmlp:
            xml_data = xmlp.read()
            xml_kws = re.findall(kw_code_pattern, xml_data)
            main_xml_kws.extend(xml_kws)
        #os.remove(xml_name)

    with open("Aadhi_RG_PY.xml", 'w') as xmlwt:
        xmlwt.write(xml_header)
        for each in main_xml_kws:
            xmlwt.write(each)
        xmlwt.write(xml_footer)
    """


def parse_arguments():
    global VERSION, EXCLUDE_PATH, EXCLUDE, FILENAME, TEXT_SEARCH_PATH, PY_SEARCH_PATH, XML_PATH, HTML_PATH, LIB_PATH
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", dest="version", help="Enter the version of the RFDoc to be created")
    parser.add_argument("--exclude", nargs="*", dest="exclude",
                        help="Enter the directories that need to be excluded from searching")
    parser.add_argument("--filename", dest="filename",
                        help="Enter the name of the result file with which xml and html needs to be created")
    parser.add_argument("--textpath", dest="textpath",
                        help="Enter the base path where the txt files must be searched for")
    parser.add_argument("--pypath", dest="pypath",
                        help="Enter the base path where the python files must be searched for")
    parser.add_argument("--upload", action="store_true",
                        help="Specifies that the given rfdoc should be uploaded to server")
    parser.add_argument(
        "--user", dest="user", help="Enter the base path where the txt files must be searched for")
    parser.add_argument(
        "--pass", dest="pass", help="Enter the base path where the txt files must be searched for")
    args = parser.parse_args()
    if not args.textpath:
        # print "\n'--path' was not given as input"
        TEXT_SEARCH_PATH = raw_input("\nEnter the Resource files path: ")
    else:
        TEXT_SEARCH_PATH = args.textpath

    if not args.pypath:
        # print "\n'--path' was not given as input"
        PY_SEARCH_PATH = raw_input("\nEnter the Python Resource files path: ")
    else:
        PY_SEARCH_PATH = args.pypath

    if not args.filename:
        # print "\n'--filename' was not given as input"
        FILENAME = raw_input("\nEnter the RFDoc File name without extension: ")
    else:
        FILENAME = args.filename

    if not args.version:
        # print "\n'--version' was not given as input"
        VERSION = raw_input("\nEnter the Version of the RFDoc: ")
    else:
        VERSION = args.version

    if not args.exclude:
        EXCLUDE = 'no'

        EXCLUDE = raw_input(
            "\nDO you want to exclude any path in base path provided? [Yes or No]: ")
        while 1:
            if EXCLUDE.lower() not in ['yes', 'y', 'n', 'no']:
                print "\nPlease enter any of the following as answer. 'yes', 'y', 'n', 'no'\n"
            else:
                break
        try:
            if EXCLUDE.lower() == 'yes' or EXCLUDE.lower() == 'y':
                EXCLUDE_PATH = raw_input(
                    "\nPlease Enter relative paths to be excluded from the base path given, separated by comma [,] : ")
                EXCLUDE_PATH = [os.path.join(SEARCH_PATH, each_path.strip()) for each_path in EXCLUDE_PATH.split(
                    ',') if (os.path.exists(os.path.join(SEARCH_PATH, each_path)))]
                print EXCLUDE_PATH
        except OSError, err:
            print "\nOne of the path given in comma separated list does not exist. Make sure you have given proper relative path from actual search path given.\n"
            sys.exit(1)

    else:
        EXCLUDE_PATH = args.exclude
        EXCLUDE_PATH = [os.path.join(SEARCH_PATH, each_path.strip()) for each_path in EXCLUDE_PATH if (
            os.path.exists(os.path.join(SEARCH_PATH, each_path)))]
        EXCLUDE = 'yes'

    XML_PATH = '%s.xml' % FILENAME
    HTML_PATH = '%s.html' % FILENAME
    LIB_PATH = '%s.txt' % FILENAME
    return args


def upload_rfdoc():
    driver = webdriver.Firefox()
    driver.get(SERVER_URL)
    driver.find_element_by_link_text("upload").click()
    driver.find_element_by_id("id_file").click()
    driver.find_element_by_css_selector("input[type=\"file\"]").clear()
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(
        os.path.join(os.getcwd(), XML_PATH))
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()


def main():
    """Main Function"""
    print "\n******* Execution Starts ********"
    args = parse_arguments()
    print args
    mainstream = ''
    full_data_list = []
    # discover_robot_library()
    py_list = []
    if TEXT_SEARCH_PATH:
        for root, dirs, files in os.walk(TEXT_SEARCH_PATH, topdown=True):
            if EXCLUDE.lower() == 'yes' or EXCLUDE.lower() == 'y':
                dirs[:] = [each_dir for each_dir in dirs if os.path.join(
                    root, each_dir) not in EXCLUDE_PATH]
            for each in files:
                if each.endswith('.txt'):
                    print os.path.join(root, each)
                    data = extract_all_keyword_code(os.path.join(root, each))
                    full_data_list.extend(data)

    if PY_SEARCH_PATH:
        for root, dirs, files in os.walk(PY_SEARCH_PATH, topdown=True):
            if EXCLUDE.lower() == 'yes' or EXCLUDE.lower() == 'y':
                dirs[:] = [each_dir for each_dir in dirs if os.path.join(
                    root, each_dir) not in EXCLUDE_PATH]
            for each in files:
                if each.endswith('.py'):
                    print os.path.join(root, each)
                    # py_list.append(os.path.join(root, each))
                    create_txt_with_py_keywords(os.path.join(root, each))

        # create_xml_with_py_keywords(py_list) # old function to create
        # keywords from pyhton file
    """
    if KEYWORD.lower() == 'yes' or KEYWORD.lower() == 'y':
        full_data_list = filter_external_keywords(full_data_list)
    """
    full_data = ''.join(full_data_list)
    if not len(full_data) <= 0:
        with open(LIB_PATH, 'w') as fp:
            fp.write(KW_HEADER)
            fp.write(full_data)

    # Merger the keyword file generated from python code with original Keyword
    # file
    if os.path.isfile("tmp.txt") and os.path.isfile(LIB_PATH):
        f = open(LIB_PATH, 'a')
        with open("tmp.txt", 'r') as fp:
            for each_line in fp:
                f.write(each_line)
        os.remove("tmp.txt")
    elif os.path.isfile("tmp.txt"):
        f = open(LIB_PATH, 'w')
        f.write(KW_HEADER)
        with open("tmp.txt", 'r') as fp:
            for each_line in fp:
                f.write(each_line)
        os.remove("tmp.txt")

    if VERSION:
        # os.system(libdoc_xml_command % (LIBDOC_PATH, VERSION, LIB_PATH, XML_PATH))
        # os.system(libdoc_html_command % (LIBDOC_PATH, VERSION, LIB_PATH, HTML_PATH))
        libdoc(LIB_PATH, XML_PATH, version=VERSION)
        libdoc(LIB_PATH, HTML_PATH, version=VERSION)
    else:
        # os.system(libdoc_xml_command % (LIBDOC_PATH, LIB_PATH, XML_PATH))
        # os.system(libdoc_html_command % (LIBDOC_PATH, LIB_PATH, HTML_PATH))
        libdoc(LIB_PATH, XML_PATH)
        libdoc(LIB_PATH, HTML_PATH)

    if args.upload:
        upload_rfdoc()
if __name__ == "__main__":
    main()
