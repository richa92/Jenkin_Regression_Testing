import subprocess
import unittest
import time
import sys
import commands
import os
import datetime


print("---------------------------- Setup LI  test--------------------\n ")
# time.sleep(900)
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")
date = time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
date = "\\" + date
directory = log + date + "\Setup_single_Lis"

Hill_sanity1 = os.system("pybot -L TRACE Pre-req-test.robot")
if not os.path.exists(directory):

    os.makedirs(directory)
time.sleep(2)

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)

if Hill_sanity1 != 0:

    print("call from python failed for LI_Ui FW update...\n")


time.sleep(10)


print("---------------------------- LI UI FW Test F1212  test--------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\LI_Fulltests"

Hill_sanity1 = os.system("pybot -L TRACE LI_Full_F1212_tests.robot")
if not os.path.exists(directory):
    os.makedirs(directory)
time.sleep(2)

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)

if Hill_sanity1 != 0:

    print("call from python failed for LI_Ui FW update...\n")


time.sleep(10)

print("----------------------------  LE test--------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\LE_tests"


if not os.path.exists(directory):
    os.makedirs(directory)


Sanity_1 = os.system("pybot -L TRACE LE_F1212_Full_tests.robot")


time.sleep(2)
#Cisco_fexvalidatelogs = 'log_fex_validate_'+ str(sticktime)+'.html'
#Cisco_fexvalidatereport = 'report_fex_validate_'+ str(sticktime)+'.html'
#os.system("copy log.html logs\%s" % (Cisco_fexvalidatelogs))
#os.system("copy report.html logs\%s" % (Cisco_fexvalidatereport))

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)


if Sanity_1 != 0:
    print("call from python failed for LE FW tests...\n")


time.sleep(10)

print("----------------------------  LE Additional tests--------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\LE_additional_tests"


if not os.path.exists(directory):

    os.makedirs(directory)


Sanity_1 = os.system("pybot -L TRACE LE_F1212_additional_test.robot")


time.sleep(2)
# Cisco_fexvalidatelogs = 'log_fex_validate_'+ str(sticktime)+'.html'
# Cisco_fexvalidatereport = 'report_fex_validate_'+ str(sticktime)+'.html'
# os.system("copy log.html logs\%s" % (Cisco_fexvalidatelogs))
# os.system("copy report.html logs\%s" % (Cisco_fexvalidatereport))

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)


if Sanity_1 != 0:
    print("call from python failed for FW additional tests...\n")


time.sleep(10)


print("----------------------------  Additional tests--------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\LI_additional_tests"


if not os.path.exists(directory):

    os.makedirs(directory)


Sanity_1 = os.system("pybot -L TRACE LI_F1212_full_additional.robot")


time.sleep(2)
# Cisco_fexvalidatelogs = 'log_fex_validate_'+ str(sticktime)+'.html'
# Cisco_fexvalidatereport = 'report_fex_validate_'+ str(sticktime)+'.html'
# os.system("copy log.html logs\%s" % (Cisco_fexvalidatelogs))
# os.system("copy report.html logs\%s" % (Cisco_fexvalidatereport))

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)


if Sanity_1 != 0:
    print("call from python failed for FW additional tests...\n")


time.sleep(10)


print("----------------------------  Setup Multiple LIs --------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\Multiple_Lis_setup"


if not os.path.exists(directory):
    os.makedirs(directory)


Sanity_1 = os.system("pybot -L TRACE Multiple_LIs_setup.robot")


time.sleep(2)

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)


if Sanity_1 != 0:
    print("call from python failed for firmwareValidation1...\n")


time.sleep(10)


print("----------------------------  Multiple LIs Firmware update --------------------\n ")
sticktime = datetime.datetime.now()
sticktime = sticktime.strftime("%Y-%m-%d-%H-%M")

# date=time.strftime("%d-%m-%Y-%H-%M-%S")
log = "logs"
# date="\\"+date
directory = log + date + "\Multiple_Lis_setup"


if not os.path.exists(directory):
    os.makedirs(directory)


Sanity_1 = os.system("pybot -L TRACE MLIs_F1212_FW_Update.robot")


time.sleep(2)

os.system("copy log.html " + directory)

os.system("copy report.html " + directory)


if Sanity_1 != 0:
    print("call from python failed for FW Validation1...\n")


time.sleep(10)
