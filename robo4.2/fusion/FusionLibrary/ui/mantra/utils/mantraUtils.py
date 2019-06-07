# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.
"""
    Mantra Utils
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.utils.constants import mantraConstants
from FusionLibrary.ui.mantra.utils.constants import DCSConstants
import subprocess
import requests
import re


def checkElements(elements_list):
    """
        checkEelements receive a list of elements (ID locator, Message)
        e.g.
        mantraUtils.checkElements([[locator1,"Message"],[locator2,"Message"]])
        The Message is used to be displayed in the console and log.
        You can send a list of elements to be verified.
    """
    failure = False
    for elements in elements_list:
        # locator is in the position [0] and message in the position [1]
        if ui_lib.wait_for_element_visible(elements[0], timeout=20):
            logger._log_to_console_and_log_file("- " + elements[1] + " element was correctly displayed")
        else:
            logger._log_to_console_and_log_file("- " + elements[1] + " element was NOT displayed")
            failure = True
    # In case of failure, return true
    if failure:
        return True
    else:
        return False


def checkElementsText(elements_list):
    """
        The same idea of checkElements but here, passing an additional argument TEXT
        e.g.
        mantraUtils.checkElementsText([[locator1,"Message","Text1"],[locator2,"Message","Text2"]])
    """
    failure = False
    for elements in elements_list:
        # locator is in the position [0],  message in the position [1] and the text in the position [2]
        if ui_lib.wait_for_element_text(elements[0], elements[2], timeout=20):
            logger._log_to_console_and_log_file("- " + elements[1] + " element was correctly displayed")
        else:
            logger._log_to_console_and_log_file("- " + elements[1] + " element was NOT displayed")
            failure = True
    # In case of failure, return true
    if failure:
        return True
    else:
        return False


def add_DCS_Blade(address, encSettings):
    """
        Add a blade on BAY 5 thru DCS REST API
    """

    address = [address]

    for ipaddr in address:
        # Set Proxy
        logger._log_to_console_and_log_file(" Setting Proxy...")
        subprocess.call("set " + str(mantraConstants.HTTP_PROXY), shell=True)
        subprocess.call("set " + str(mantraConstants.HTTPS_PROXY), shell=True)
        # Get Instances
        logger._log_to_console_and_log_file("- Get DCS Instances...")
        urlGetInstance = "http://" + str(ipaddr.appliance_ip[8:]) + ":9990/dcs/rest/schematic/instances"
        response = requests.get(urlGetInstance, stream=True)
        # Copying JSON to a tempfile
        with open("instances.txt", "w") as tempfile:
            tempfile.write(str(response.json()))
        # Reading tempfile (searching for BL* and getting the ID)
        with open("instances.txt", 'r') as tempfile:
            for line in tempfile:
                fileInMemory = re.search("(BL.*.-)", line)
                if fileInMemory:
                    bladeID = fileInMemory.group(1)
                    logger._log_to_console_and_log_file("- Blade Model: " + str(bladeID[:10]))
                    logger._log_to_console_and_log_file("- Blade ID: " + str(bladeID[11:15]))
        # Mounting addBlade POST URI (getting the Enclosure Entity from constants.py)
        logger._log_to_console_and_log_file("- Mounting Add Blade URI...")
        addBladeURI = "http://" + str(ipaddr.appliance_ip[8:]) + ":9990/dcs/rest/schematic/instances/" + str(encSettings.id) + "?action=addblade&bladeId=" + str(bladeID[11:15]) + "&bayNum=" + str(encSettings.expansionBayNumber)
        logger._log_to_console_and_log_file("- Add Blade URI: " + addBladeURI)
        # Adding Blade
        logger._log_to_console_and_log_file("- Adding Blade on DCS...")
        response = requests.post(addBladeURI, stream=True)
        logger._log_to_console_and_log_file("- ADD Blade RESPONSE: " + str(response))
        # Validating the HTTP response
        if str(response) == "<Response [200]>":
            logger._log_to_console_and_log_file("- ADD Blade was correctly executed by DCS")
        else:
            ui_lib.fail_test("- An error was reported by DCS. Please, check your DCS status", captureScreenshot=False)
        # Removing tempfile
        subprocess.call("del instances.txt", shell=True)


def DCS_change_fan_status(ipaddr, bay_number, enclosure_id, status):
    """
        Change an enclosure's fan status in DCS. Works for C7000 only.
    """

    logger._log_to_console("\n- Setting status " + status + " to Fanbay number " + bay_number)
    if status not in DCSConstants.FAN_OP_STATUS_LIST:
        ui_lib.fail_test("\nInvalid status [%s] for enclosure's fan. Valid values are: %s" % (status, DCSConstants.FAN_OP_STATUS_LIST), False)

    # mount URL based on the informed enclosure id
    url_dcs_instance = "http://" + str(ipaddr[8:]) + DCSConstants.DCS_PORT + DCSConstants.DCS_REST_INSTANCES + "/" + enclosure_id

    # create the URI to change the fan status
    changeFanURI = url_dcs_instance + "?action=changeFanStatus&bayNum=" + bay_number + "&operationalStatus=" + status
    logger._log_to_console("\t- URI: " + changeFanURI)
    response = requests.post(changeFanURI, stream=True)

    if (response.status_code == DCSConstants.HTTP_STATUS_CODE_OK):
        logger._log_to_console_and_log_file("\t- Fan status changed successfully.")
    else:
        ui_lib.fail_test("\tChange fan status failed: " + response.content, False)
