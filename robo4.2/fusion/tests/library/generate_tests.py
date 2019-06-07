"""
This file walks the FusionLibrary and Resources keywords and creates a unified test suite
which can be used to do a dryrun execution of all keywords.
"""
import os
import robot.parsing.settings
from robot.parsing import ResourceFile
from robot.libdocpkg.robotbuilder import LibraryDocBuilder

KEYWORD_TEST_FILE = 'keyword_tests.robot'
MAIN_RESOURCE_FILE = 'Resources/api/fusion_api_resource.txt'
HEADER = """
*** Settings ***
Library     FusionLibrary
Resource    Resources/api/fusion_api_resource.txt

*** Test Cases ***

"""


def create_robot_tests(fout):
    """
    Create tests for all robot based keywords
    """
    processed = {}   # dict to avoid circular imports

    def get_all_keywords(resource):
        """
        Helper function to recursively get keywords from resource files
        """
        keywords = []
        resource.populate()
        for res in [i for i in resource.imports.data if isinstance(i, robot.parsing.settings.Resource)]:
            keyword_file = os.path.abspath('{}/{}'.format(res.directory, res.name))
            if keyword_file not in processed:
                res_obj = ResourceFile(keyword_file)
                processed[keyword_file] = res_obj
                keywords += get_all_keywords(res_obj)
        for keyword in resource.keywords:
            print(keyword.name)
            keywords.append(tuple((keyword.source, keyword.name, keyword.args.value if keyword.args.value else [])))
        return keywords

    fusion_api_resource = ResourceFile(MAIN_RESOURCE_FILE)
    for keyword in get_all_keywords(fusion_api_resource):
        fout.write('Test {}\n'.format(keyword[1]))
        fout.write('    [Documentation]    {}\n'.format(keyword[0]))
        fout.write('    {} '.format(keyword[1]))
        for arg in keyword[2]:
            if '=' in arg:
                fout.write('    {}    '.format(arg.split('=')[-1]))
            else:
                if arg.startswith('&'):
                    fout.write('    testk=testv    ')
                else:
                    fout.write('    test    ')
        fout.write('\n\n')


def create_python_tests(fout):
    """
    Walk the python keywords and create tests
    """
    for keyword in LibraryDocBuilder().build('FusionLibrary').keywords:
        print(keyword.name)
        fout.write('Test {}\n'.format(keyword.name))
        fout.write('    [Documentation]    {}\n'.format(keyword.name))
        fout.write('    {} '.format(keyword.name))
        for arg in keyword.args:
            if '=' in arg:
                fout.write('    {}    '.format(arg.split('=')[-1]))
            else:
                if arg.startswith('&'):
                    fout.write('    testk=testv    ')
                else:
                    fout.write('    test    ')
        fout.write('\n\n')

# open the keyword test file and write keyword tests to it
with open(KEYWORD_TEST_FILE, 'w+') as output_file:
    output_file.write(HEADER)
    create_python_tests(output_file)
    create_robot_tests(output_file)
