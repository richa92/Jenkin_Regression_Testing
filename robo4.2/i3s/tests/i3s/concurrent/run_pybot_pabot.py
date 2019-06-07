#!/usr/bin/python
import os
import time
import sys
total_args_passed = len(sys.argv)
count = 1
if (total_args_passed == 1):
        print("Total number of arguments passed : %d" % total_args_passed)
        print("Please pass the required arguments to execute tests")
        exit()
else:
        while ( count < total_args_passed):
                os.system(sys.argv[count])
                count = count+1
        time.sleep(5)

print ("Test execution completed")
