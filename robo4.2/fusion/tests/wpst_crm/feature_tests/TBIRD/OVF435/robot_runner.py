'''

Run Robot Test and Push Result To Sharepoint

'''
#from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    testName = "OVF435 - Tbird OVF435 Feature Test"
    testPath = r'ovf435-feature-tests.robot'
    #dataPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\TBIRD\F105\data_variables.py'

    suite = TestSuiteBuilder().build(testPath)

    #result = suite.filter(excluded_tags=['FTS', 'TSS'])
    #result = suite.filter(included_tags=['12', '13', '15'])
    result = suite.filter(included_tags='38')
    #result = suite.filter(included_tags=['FTS', 'TSS', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
    #result = suite.filter(included_tags=['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])

    IP = '16.125.70.221'
    VM = None
    result = suite.run(variable=['APPLIANCE_IP:%s' % IP,
                                 'VM:%s' % VM],
                       variablefile='data_variables.py',
                       critical='smoke',
                       output='output.xml',
                       exitonerror=True,
                       exitonfailure=True,
                       skipteardownonexit=True
                       )
    ResultWriter('output.xml').write_results()

if __name__ == '__main__':
    main()

