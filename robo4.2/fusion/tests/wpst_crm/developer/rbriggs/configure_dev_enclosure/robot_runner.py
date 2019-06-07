# from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    # testName = "Configure Dev Enclosure"
    testpath = r'quick_test.robot'
    # testPath = r'C:\rg-fusion\fusion\tests\wpst_crm\developer\rbriggs\configure_dev_enclosure\demo.txt'
    # testPath = r'C:\rg-fusion\fusion\tests\wpst_crm\feature_tests\biggs\biggs.txt'

    suite = TestSuiteBuilder().build(testpath)

    suite.filter(included_tags='hpip')
    # result = suite.filter(included_tags='one')
    # result = suite.filter(included_tags='ENCLOSURE GROUPS')
    # result = suite.filter(included_tags=['LIGS', 'ENCLOSURE GROUPS'])

    result = suite.run(variable=['APPLIANCE_IP:10.178.14.1'],
                       critical='smoke',
                       output='output.xml')
    # Report and xUnit files can be generated based on the  result object.
    ResultWriter(result).write_results(report='report.html', log='log.html')
    # Generating log files requires processing the earlier generated output XML.
    ResultWriter('output.xml').write_results()

    stats = result.suite.statistics
    print ('Total failed %d' % stats.all.failed)
    print ('Total passed %d' % stats.all.passed)
    print ('Total tests %d' % stats.all.total)


if __name__ == '__main__':
    main()
