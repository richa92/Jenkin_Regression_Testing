""" PushTestplan2SQL

Walk the testsuite folder and dump data to SQL

Usage:  pushtestplan2sql.py Path_To_TestSuite_folder


"""
import sys
import pyodbc
from robot.parsing.model import TestData


class TestPlan(object):

    def __init__(self, path):
        self.suite = TestData(parent=None, source=path)
        self.parents = self.suite.name
        self.debug = True

    def walk_testplan(self, suite):
        for test in suite.testcase_table:
            tags = " ".join(test.tags.value) if test.tags.value else " "
            querystring = "insert into testplan values \
                ('" + self.parents + "','" + suite.parent.name + "','" + suite.name + "','" + test.name + "','" + tags + "')"
            if self.debug:
                print self.parents + "=child=" + suite.parent.name + "=suite=" + suite.name + "=TestName=" + test.name + "=Tags= " + tags
                print querystring
            cur.execute(querystring)
            con.commit()
        for child_suite in suite.children:
            self.walk_testplan(child_suite)

    def truncate_table(self):
        print "Truncating testplan table.\n"
        cur.execute("truncate table testplan")
        con.commit()


if __name__ == "__main__":
    try:
        print len(sys.argv)
        if not (2 <= len(sys.argv)) or sys.argv[1] in ('--help', '-h'):
            print __doc__
            sys.exit(1)

        con = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=;DATABASE=;UID=sa;PWD=')
        cur = con.cursor()

        testplan = TestPlan(sys.argv[1])
        testplan.truncate_table()
        testplan.walk_testplan(testplan.suite)
        con.close()

    except Exception as e:
        print "Caught %s" % e
