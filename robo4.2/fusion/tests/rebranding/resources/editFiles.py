import sys
import fileinput
import os

XMLFILE = os.getcwd() + "\\..\\data\\test_data.xml"
print "Now reading " + XMLFILE

# Edit XML file to replace the address and browser
for line in fileinput.input(XMLFILE, inplace=True):
    if "appliance_ip" and "browser" in line:
        line = line.replace(line, '\t\t' + '<env seleniumSpeed="0.1" appliance_ip="https://' + sys.argv[1] + '" browser="' + sys.argv[3] + '" />' + '\n')
    sys.stdout.write(line)
print "XML file was updated with the specified appliance password: " + sys.argv[1]
print "XML file was updated with the specified browser: " + sys.argv[3]

# Edit XML file to replace the password
for line in fileinput.input(XMLFILE, inplace=True):
    if "password" in line:
        line = line.replace(line, '\t\t' + '<user name="Administrator" password="' + sys.argv[2] + '" />' + '\n')
    sys.stdout.write(line)
print "XML file was updated with the specified appliance password: " + sys.argv[2]