'''
This module will start the server ping in LInux/Windows
for a number of times given in the calling function.
Example :
startthread    ${number}    ${server_ip}    ${name}    ${flag}
'''
import threading
import os
import time
from RoboGalaxyLibrary.data.test_data import DataObj
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib


def checkservicehealth(no, ip, name, flag):
    if flag == "Windows":
        print os.system("ping -n %s %s > %s" % (no, ip, name))
        time.sleep(2)
    elif flag == "Linux":
        print "Pinging in Linux"
        print os.system("ping -c %s %s > %s" % (no, ip, name))
        time.sleep(2)
    else:
        ui_lib.fail_test("Please provide valid flag value to ping")


def startthread(no, ip, name, flag):
    t1 = threading.Thread(name="checkservicehealth", target=checkservicehealth, args=(no, ip, name, flag))
    t1.start()

if __name__ == "__main__":
    startthread(no, ip, name, flag)
