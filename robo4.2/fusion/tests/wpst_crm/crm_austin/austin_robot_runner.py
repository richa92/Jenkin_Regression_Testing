'''
Run Robot Test

'''
from RoboGalaxyLibrary.utilitylib import exec_process as runner
from robot.api import TestSuiteBuilder
from robot.api import ResultWriter

import os

vc_test_dir = "\\Common\\"
# vc_test_files = ["example-existingLIG1.txt"]
vc_test_files = ["dryrun.txt"]
# vc_test_files = ["temp1.txt"]

# the main function


def main():
    cwd = os.getcwd()
    runner_path = os.getcwd()
    vc_test_path = cwd + vc_test_dir
    os.chdir(vc_test_path)
    # os.chdir(vc_test_path)
    cwd = os.getcwd()
    for vc_test_file in vc_test_files:
        print 'dir is ' + cwd
        suite = TestSuiteBuilder().build(vc_test_path + vc_test_file)
        # suite.filter(included_tags='ACTIVE')
        result = suite.run(critical='smoke', output=runner_path +
                           '/output.xml')
        ResultWriter(result).write_results(report=runner_path +
                                           '/report.html', log=None)
        ResultWriter(runner_path + '/output.xml').write_results()

        stats = result.suite.statistics
        print ('Total failed %d' % stats.all.failed)
        print ('Total passed %d' % stats.all.passed)
        print ('Total tests %d' % stats.all.total)

if __name__ == '__main__':
    main()
