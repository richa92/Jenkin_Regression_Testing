# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
'''

Run Robot Test and Push Result To Sharepoint

'''
# from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter


# the main function
def main():
    testName = "Mantra Tests"
    testPath = r'C:\robogalaxy\fusion\tests\mantra\ui\Sample.txt'

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


if __name__ == '__main__':
    main()
