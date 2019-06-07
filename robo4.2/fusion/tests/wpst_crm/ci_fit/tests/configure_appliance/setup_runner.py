'''



'''
# from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    # testName = "Configure Dev Enclosure"
    testPath = r'C:\rg-fusion\fusion\tests\wpst_crm\ci_fit\tests\configure_appliance\setup.txt'
    dataPath = r'C:\rg-fusion\fusion\tests\wpst_crm\developer\rbriggs\configure_dev_enclosure\efit_data_variables.py'

    suite = TestSuiteBuilder().build(testPath)
    result = suite.run(variable=['DATA:..\\..\\..\\feature_tests\\F113\\data_variables.py',
                                 'VM:ov-russell-tot',
                                 'VMSETUP:no',
                                 'FTS:no',
                                 'CONFIGURE:yes'],
                       critical='smoke',
                       output='output.xml')
    # Report and xUnit files can be generated based on the  result object.
    ResultWriter(result).write_results(report='report.html', log=None)
    # Generating log files requires processing the earlier generated output XML.
    ResultWriter('output.xml').write_results()

    stats = result.suite.statistics
    print ('Total failed %d' % stats.all.failed)
    print ('Total passed %d' % stats.all.passed)
    print ('Total tests %d' % stats.all.total)

#   command = "sharepoint.exe " + " " + testName  + " " +  str(stats.all.total) + " " + str(stats.all.passed) + " " + str(stats.all.failed)
#   runner.run_cmd(command)

if __name__ == '__main__':
    main()
