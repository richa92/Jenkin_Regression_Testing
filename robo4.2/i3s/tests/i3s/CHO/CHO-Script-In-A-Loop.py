import os
import time

i = 1

while i <= 100:
    print '\n\n\n'
    print '+-' * 90
    print '\n'
    print ('\t\t\t\t\t\t\t\t\t  ITERATION NUMBER: ' + str(i))
    print '\n'
    print '+-' * 90
    print '\n\n\n'

    os.system(
        'pybot  -d C:\CHO\OV-4.00.11-I3S-4.00.07 --timestampoutputs -o OV-4.00.11-I3S-4.00.07.xml -l none -r none CHO-Tests.txt')

    i = i + 1
print ('Ran script 100 times')
