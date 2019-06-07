from robot.api import TestSuiteBuilder
from robot.api import ResultWriter

def main():

    testPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\C7000\F748-F750\feature_test_F748-F750.txt'
    suite = TestSuiteBuilder().build(testPath)

    result = suite.filter(included_tags=['6'])
    #result = suite.filter(included_tags='ENCLOSURE GROUPS')
    #result = suite.filter(included_tags=['FTS', 'TSS', '1'])
    #result = suite.filter(included_tags=['2', '3', '4', '5', '7', '9'])
    IP = None
    IP = '15.199.229.190'
    VM = 'HPOneView-SSH_3.00.00_244361'
    result = suite.run(variable=['APPLIANCE_IP:%s' % IP,
                                 'VM:%s' % VM],
                       critical='smoke',
                       output='output.xml',
                       exitonerror=True,
                       exitonfailure=True,
                       skipteardownonexit=True
                       )
    ResultWriter('output.xml').write_results()
    stats = result.suite.statistics
    print ('Total failed %d' % stats.all.failed)
    print ('Total passed %d' % stats.all.passed)
    print ('Total tests %d' % stats.all.total)

if __name__ == '__main__':
    main()

