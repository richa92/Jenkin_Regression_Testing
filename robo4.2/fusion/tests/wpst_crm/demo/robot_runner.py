'''

Run Robot Test and Push Result To Sharepoint

'''
# from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    testName = "Bobby's Test"
    testPath = r'C:\Users\Administrator\git\robogalaxy\tests\demo\wpst_crm\logical_interconnect_groups.txt'

    suite = TestSuiteBuilder().build(testPath)
    result = suite.run(critical='smoke', output='output.xml')
    # Report and xUnit files can be generated based on the  result object.
    ResultWriter(result).write_results(report='repot.html', log=None)
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
