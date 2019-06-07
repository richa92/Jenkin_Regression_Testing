'''

Run Robot Test and Push Result To Sharepoint

'''
# from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    # testName = "F117 - Tbird FC DirectAttach Feature Test"
    testName = "F118 - Tbird FC FabricAttach Feature Test"
    # testPath = r'F117_teardown.robot'
    testPath = r'F118_feature_tests.robot'
    # testPath = r'F117_feature_tests.robot'
    # testPath = r'F117_feature_max_us_tests.robot'
    # dataPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\TBIRD\FC_POTASH'

    suite = TestSuiteBuilder().build(testPath)

    # result = suite.filter(excluded_tags=['speedChange'])
    # result = suite.filter(included_tags=['Login', 'InsertAsidePotash'])
    # result = suite.filter(included_tags=['setup'])
    # result = suite.filter(included_tags=['Login', 'ServerEnd2End'])
    # result = suite.filter(included_tags=['Login', 'LIUFGRemovePortAfterPowerOnB'])
    # result = suite.filter(included_tags=['Login', 'DisEnaAUplink', 'DisEnaBUplink'])
    # result = suite.filter(included_tags=['Login', 'ExceedMaxLiUSB', 'portStatusReason'])
    # result = suite.filter(included_tags=['Login', 'LiUSNegative'])

    IP = '15.245.131.72'
    VM = None
    result = suite.run(variable=['APPLIANCE_IP:%s' % IP,
                                 'VM:%s' % VM],
                       variablefile='data_F118_BA51_ha.py',
                       # variablefile='data_F118_BA51_ab.py',
                       critical='smoke',
                       output='output.xml',
                       exitonerror=True,
                       exitonfailure=True,
                       skipteardownonexit=True
                       )
    ResultWriter('output.xml').write_results()

if __name__ == '__main__':
    main()
