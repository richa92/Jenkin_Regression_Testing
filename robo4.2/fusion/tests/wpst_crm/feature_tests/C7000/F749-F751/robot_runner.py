'''


'''
#from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    testName = ""
    testPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\c7000\F749-F751\feature_test_F749-F751.txt'
    #dataPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\F748-49\common_variables.py'

    suite = TestSuiteBuilder().build(testPath)

    #result = suite.filter(excluded_tags=['FTS', 'TSS'])
    #result = suite.filter(included_tags=['7', '8', '40'])
    #result = suite.filter(included_tags=['15', '16', '17', '18'])
    #result = suite.filter(included_tags='5')
    #result = suite.filter(included_tags='ENCLOSURE GROUPS')
    #result = suite.filter(included_tags=['FTS', 'TSS'])
    IP = None
    #IP = '15.199.229.190'
    VM = 'HPOneView-SSH_3.00.00_244361p78'
    result = suite.run(variable=['APPLIANCE_IP:%s' % IP,
                                 'VM:%s' % VM],
                       critical='smoke',
                       output='output.xml',
                       exitonerror=True,
                       exitonfailure=True,
                       skipteardownonexit=True)
    # Report and xUnit files can be generated based on the  result object.
    #ResultWriter(result).write_results(report='report.html', log='log.html')
    # Generating log files requires processing the earlier generated output XML.
    ResultWriter('output.xml').write_results()

    stats = result.suite.statistics
    print ('Total failed %d' % stats.all.failed)
    print ('Total passed %d' % stats.all.passed)
    print ('Total tests %d' % stats.all.total)

if __name__ == '__main__':
    main()

