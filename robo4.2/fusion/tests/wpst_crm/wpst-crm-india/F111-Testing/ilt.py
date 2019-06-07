
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from robot.libraries.BuiltIn import time
from robot.libraries.BuiltIn import re
from FusionLibrary.ui.servers import enclosures
from FusionLibrary.ui.servers.enclosures_elements import FusionEnclosuresPage
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.base_page import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.general import activity
from FusionLibrary.ui.networking.logicalinterconnects_elements import FusionLogicalInterconnectsPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType, FusionUIConst
from FusionLibrary.ui.business_logic.servers.enclosures import (C7000AddEnclosures,
                                                                C7000RemoveEnclosures,
                                                                C7000CommonOperationEnclosures,
                                                                C7000EditEnclosures,
                                                                C7000EnclosuresReapplyConfiguration,
                                                                C7000RefreshEnclosures,
                                                                C7000VerifyEnclosures,
                                                                TBirdVerifyEnclosures,
                                                                TBirdCommonOperationEnclosures,
                                                                TBirdEnclosuresInterconnectLinkTopology,
                                                                VerifyEnclosures,
                                                                EditScopeForEnclosures)
from FusionLibrary.ui.business_logic.networking.interconnects import CommonOperationInterconnects, VerifyInterconnects, InterconnectLinkPorts
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import C7000VerifyLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups import CommonOperationLogicalInterconnectGroups
from FusionLibrary.ui.business_logic.servers.enclosuregroups import C7000CommonOperationEnclosureGroups
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware, VerifyHardware
from collections import defaultdict

ROBOT_LIBRARY_VERSION = '0.1'


class ilt(object):

    def enclosure_tbird_validate_interconnect_link_topology(self, *enc_obj):
        """ Checks the blades & CIM slots in Enclosures overview
        Example:
        | `Fusion UI Verify Tbird Validate Interconnect Link Topology| @{enclosure list} |

        """
        return tbird_validate_interconnect_link_topology(enc_obj)


def tbird_validate_interconnect_link_topology(enc_obj):
    """ Make sure the populated  cxp topology is expected,
        and that its properties are displayed appropriately.
        Arguments:
            Enc obj: displayed on the OneView UI (one-based)

    """
    error = 0
    encl_no = {}

    for enclosure in enc_obj:
        logger.info("Validate cxp topology for enclosure %s" % enclosure.name)
        if not enclosures.select_enclosure(enclosure.name):
            continue

        # interconnect link topology
        FusionUIBase.select_view_by_name('Interconnect Link Topology')
        expected_msg = " "
        expected_msg_for_oneencl = ""
        # get enclosure list
        encl_list = []
        encl_list = TBirdEnclosuresInterconnectLinkTopology.get_enclosure_list_from_interconnect_link_topology(15)
        logger.info(encl_list)
        no_of_encl = len(encl_list)
        logger.info("Interconnect link topology validation is for %s Enclosures" % (no_of_encl))

        error_string = " "
        port = 1
        d = {}

        no_cl_supp = 0
        if no_of_encl > 1:
            (error, d, encl_no, encl_numbering_list, power_state, data, member_list) = enclosures._get_validate_enclosure_numbering(encl_list)
            if (len(encl_numbering_list) > 0 and encl_numbering_list[0] != " "):
                encl_1 = encl_numbering_list[0]
            if (len(encl_numbering_list) > 1 and encl_numbering_list[1] != " "):
                encl_2 = encl_numbering_list[1]
            if (len(encl_numbering_list) > 2 and encl_numbering_list[2] != " "):
                encl_3 = encl_numbering_list[2]
            if (len(encl_numbering_list) > 3 and encl_numbering_list[3] != " "):
                encl_4 = encl_numbering_list[3]
            if (len(encl_numbering_list) > 4 and encl_numbering_list[4] != " "):
                encl_5 = encl_numbering_list[4]
            for loop in range(0, no_of_encl):
                if not (encl_numbering_list[loop] == encl_list[loop]):
                    logger.warn("Enclosure numbering  list displayed on UI is not matching with the validation")
                    error_string = "Enclosure Numbering displayed on UI is not matching with the validation" + "\t"
        else:
            (expected_msg_for_oneencl, power_state) = _get_no_of_cl_single_encl(enclosure.name)
            encl_no[str(enclosure.name)] = 1
            encl_list = []
            encl_list.append(enclosure.name)

            if len(expected_msg) > 0:
                no_cl_supp = 1

        count = 1
        bay_no = {}
        connected_encl = {}
        alert = {}
        encl_dct = defaultdict(int)
        alert_msgs = []
        bay_numbering = 0
        wrong_ic = 0
        wrong_b_bay = 0
        for encl_name in encl_list:
            logger.info(encl_name)
            encl_ic_bay_port_list = []

            encl_ic_bay_port_list = TBirdEnclosuresInterconnectLinkTopology.get_interconnect_cxp_bay_from_interconnect_link_topology(count, 15, False)

            for bay_data in encl_ic_bay_port_list:

                bay_data = bay_data.split("\n")

                if not (count in encl_dct):
                    encl_dct[count] = 0

                if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                    logger.info("fabric a side")
                    encl_dct[count] = 1
                    aside_bay = bay_data[0]

                    if (any(FusionUIConst.CONST_CL10 in data for data in bay_data)):
                        a_bay_ic = bay_data[3]
                        a_bay_no = bay_data[2]
                elif (aside_bay == "1"):
                    if (bay_data[0] == "4"):

                        if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) and (encl_no[encl_name] != 2):
                            wrong_ic = 1
                        logger.info("fabric b side")
                        encl_dct[count] += 1
                    elif (any(FusionUIConst.CONST_CL10 in data for data in bay_data)):
                        wrong_bay_set = aside_bay
                        wrong_b_bay = 1

                elif(aside_bay == "2"):

                    if(bay_data[0] == "5"):
                        if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) and (encl_no[encl_name] != 2):
                            wrong_ic = 1
                        logger.info("fabric b side")
                        encl_dct[count] += 1
                    elif (any(FusionUIConst.CONST_CL10 in data for data in bay_data)):
                        wrong_bay_set = aside_bay
                        wrong_b_bay = 1

                elif(aside_bay == "3"):

                    if(bay_data[0] == "6"):
                        if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) and (encl_no[encl_name] != 2):
                            wrong_ic = 1
                        logger.info("fabric b side")
                        encl_dct[count] += 1
                    elif (any(FusionUIConst.CONST_CL10 in data for data in bay_data)):
                        wrong_bay_set = aside_bay
                        wrong_b_bay = 1

            if (encl_dct[count] == 1):
                bay_no[count] = bay_data[0]

            count += 1
        for i in range(1, no_of_encl):
            if (encl_dct[i] > encl_dct[i + 1]):
                bay_numbering = encl_dct[i + 1]
                logger.info("bay no if %s" % bay_numbering)
            else:
                bay_numbering = encl_dct[i]
                logger.info("bay no else %s" % bay_numbering)
        count = 1

        for encl_name in encl_list:
            port_sts = 0
            alert_msgs = []
            connected_encl_alert_msgs = []
            encl_ic_bay_port_list = []
            power_stat = None
            power_bit = 0
            encl_status = C7000VerifyEnclosures.verify_enclosure_status_ok(encl_name, 10, False)
            logger.info("enclosure status is %s" % encl_status)
            encl_ic_bay_port_list = TBirdEnclosuresInterconnectLinkTopology.get_interconnect_cxp_bay_from_interconnect_link_topology(count, 15, False)
            logger.info("encl bay info before connected info %s " % encl_ic_bay_port_list)

            for bay_data in encl_ic_bay_port_list:

                bay_data = bay_data.split("\n")
                logger.info("bay info before connected info %s " % bay_data)

                if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                    if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) or any("FusionUIConst.CONST_HAFNIUM_POTASSIUM" in loop for loop in bay_data):
                        power_stat = power_state["encl_{}_bay_{}".format(encl_name, bay_data[0])]
                        aside_bay = bay_data[0]
                        key = encl_no.get(encl_name)
                        if (key):
                            logger.info("\n-------------------")
                            logger.info("encl %s  is %s \n" % (encl_no[str(encl_name)], encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[4]))
                            logger.info("\n-------------------")
                        else:
                            logger.info("\n-------------------")
                            logger.info("encl is %s \n" % (encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[4]))
                            logger.info("\n-------------------")
                        first = True
                        for port in range(1, 5):
                            connected_port = " "
                            connected_ic = " "
                            frame_error_msg = 0
                            connected_webelement = " "
                            logger.info("port is %d" % port)
                            port_status = TBirdEnclosuresInterconnectLinkTopology.get_cxpport_status_interonnect_link_topology(count, bay_data[0], port)

                            if (port_status == "ok"):
                                logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                                port_sts += 1

                                (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                            elif (port_status == "disabled"):

                                if (power_state == "Off"):
                                    power_bit = 1
                                    (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                if (no_of_encl > 4):
                                    error += 1
                                    logger._warn("The Interconnect port L%s status is %s" % (port, port_status))
                                else:
                                    logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                            elif (port_status == "error"):
                                logger.info("The Interconnect port C%s status is %s" % (port, port_status))
                                (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                if first:
                                    connector_info = _get_connector_information(bay_data[0], bay_data[3], enclosure.name)
                                    first = False
                                if (connected_ic is None) and (connector_info["port{}_connectedto".format(port)] != ""):
                                    connected_ic = connector_info["port{}_connectedto".format(port)]
                                    connected_port = connector_info["port{}_connectedport".format(port)]
                                    logger.info(connected_ic)
                                    logger.info(connected_port)
                                if (connected_ic is None) and (bay_numbering == 0 or bay_numbering == 2):

                                    alert["encl_{!s}_alert_b_port".format(encl_name)] = 0
                                    for encls in encl_list:
                                        for bay in range(1, 7):
                                            for prt in range(1, 5):

                                                if("encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt) in d):
                                                    if(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[3] and (d["encl_{!s}_k_bay{}_port{}_connectedport".format(encls, bay, prt)] == "L1")):
                                                        logger.info(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)])
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L" + str(port) + "to " + encls + ", interconnect " + str(bay) + ", port  L" + repr(prt) + " is improperly connected. Learn more"
                                                        break
                                    logger.info(connector_info["port{}_connectorinfo".format(port)])
                                    if (connector_info["port{}_connectorinfo".format(port)] != "noconnector"):

                                        expected_msg = "Invalid interconnect link topology cabling. Cable from " + bay_data[3] + ", port L" + str(port) + " is either disconnected or connected to an outside management ring."
                                    else:
                                        if port is 1:
                                            logger.info(" in encl 2 %s" % frame_error_msg)
                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."
                                        elif port is 2:
                                            if (k >= 3):
                                                expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_3 + ", interconnect " + bay_data[0] + " is missing."
                                        elif port is 3:
                                            if (no_of_encl == 3):
                                                expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L2 of " + encl_3 + ", interconnect " + bay_data[0] + " is missing."
                                            if (no_of_encl >= 4):
                                                expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_4 + ", interconnect " + bay_data[0] + " is missing."
                                        else:
                                            if (no_of_encl <= 3):
                                                expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L4 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."
                                            if (no_of_encl >= 4):
                                                expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_5 + ", interconnect " + bay_data[0] + " is missing."

                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                elif(connected_ic is None and bay_numbering == 1):
                                    logger.info(connector_info["port{}_connectorinfo".format(port)])
                                    if (connector_info["port{}_connectorinfo".format(port)] != "noconnector"):

                                        expected_msg = "Invalid interconnect link topology cabling. Cable from " + bay_data[3] + ", port L" + str(port) + " is either disconnected or connected to an outside management ring."
                                    else:
                                        if port is 1:

                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_2 + ", interconnect bay " + bay_data[0]
                                        elif port is 2:
                                            if (no_of_encl >= 3):
                                                expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_3 + ", interconnect bay " + bay_data[0]
                                        elif port is 3:
                                            if (no_of_encl == 3):
                                                expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_3 + ", interconnect bay " + bay_data[0]
                                            if (no_of_encl >= 4):
                                                expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_4 + ", interconnect bay " + bay_data[0]
                                        else:
                                            if (no_of_encl <= 3):
                                                expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_2 + ", interconnect bay " + bay_data[0]
                                            if (no_of_encl >= 4):
                                                expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_5 + ", interconnect bay " + bay_data[0]

                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                elif not (connected_ic is None or connected_ic == " "):
                                    power_state = enclosures.get_powerstate_information(bay_data[0], connected_ic, enclosure.name)
                                    if (power_state == "Off"):
                                        expected_msg = "Invalid interconnect link topology. Port L" + str(port) + " of interconnect " + bay_data[3] + " is connected to interconnect " + connected_ic + " which is powered off."
                                        alert_msgs.append(expected_msg)
                                        logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                            if not (connected_ic is None or connected_ic == " "):
                                logger.info("connected interconnect is %s" % connected_ic)

                                (valid_bit, framed_msg, expected_msg) = _validate_a_fabric_ports(no_of_encl, bay_data, port, connected_port, connected_ic, encl_numbering_list)
                                if valid_bit:
                                    logger.info("The Interconnect port L%s is connected as expected" % port)
                                    logger.info("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))
                                else:
                                    error += 1
                                    alert["encl_{!s}_bay{}_port{}_ic".format(encl_name, bay_data[0], port)] = connected_ic
                                    alert["encl_{!s}_bay{}_port{}".format(encl_name, bay_data[0], port)] = connected_port
                                    alert["encl_{!s}_bay{}_port{}_msg".format(encl_name, bay_data[0], port)] = framed_msg
                                    alert_msgs.append(expected_msg)
                                    connected_encl_alert_msgs.append(framed_msg)
                                    logger.info("Expected Alert message is: %s" % expected_msg)
                    elif any(FusionUIConst.CONST_CL10 in data for data in bay_data):

                        aside_bay = bay_data[0]
                        key = encl_no.get(encl_name)
                        if (key):
                            logger.info("\n-------------------")
                            logger.info("encl %s  is %s \n" % (encl_no[str(encl_name)], encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[3]))
                            logger.info("\n-------------------")
                        else:
                            logger.info("\n-------------------")
                            logger.info("encl is %s \n" % (encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[3]))
                            logger.info("\n-------------------")

                        for port in range(1, 2):
                            logger.info("port is %d" % port)
                            port_status = TBirdEnclosuresInterconnectLinkTopology.get_cxpport_status_interonnect_link_topology(count, bay_data[0], port)
                            logger.info(port_status)
                            if (port_status == "ok"):
                                logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                                port_sts += 1

                            elif (port_status == "disabled"):
                                # power_state = enclosures.get_powerstate_information(bay_data[0], bay_data[2], enclosure.name)
                                if (power_state["encl_{}_bay_{}".format(encl_name, bay_data[0])] == "Off"):
                                    power_bit = 1
                                    (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                if (no_of_encl > 4):
                                    error += 1
                                    logger._warn("The Interconnect port L%s status is %s" % (port, port_status))
                                else:
                                    logger.info("The Interconnect port L%s status is %s" % (port, port_status))

                            elif (port_status == "error"):
                                logger.info("The Interconnect port C%s status is %s" % (port, port_status))
                                connector_info = _get_connector_information(bay_data[0], bay_data[2], enclosure.name)
                                # if (connected_ic is None) and (connector_info["port{}_connectedto".format(port)] != ""):
                                if (connector_info["port{}_connectedto".format(port)] != ""):
                                    connected_ic = connector_info["port{}_connectedto".format(port)]
                                    connected_port = connector_info["port{}_connectedport".format(port)]
                                    logger.info(connected_ic)
                                    logger.info(connected_port)
                                if (not (connected_ic is None or connected_ic == " ")and (encl_no[encl_name] == 1)):

                                    expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[2] + ", port L" + str(port) + " to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))

                                elif (bay_numbering == 0 or bay_numbering == 2):

                                    alert["encl_{!s}_alert_b_port".format(encl_name)] = 0
                                    for encls in encl_list:
                                        for bay in range(1, 7):
                                            for prt in range(1, 5):

                                                if("encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt) in d or "encl_{!s}_cl_bay{}_port{}_connected_ic".format(encls, bay, prt) in d):
                                                    if(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[2] and (d["encl_{!s}_k_bay{}_port{}_connectedport".format(encls, bay, prt)] == "L1")):
                                                        logger.info(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)])
                                                        logger.info("came here")
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[2] + ", port L" + str(port) + "to " + encls + ", interconnect " + str(bay) + ", port  L" + str(prt) + " is improperly connected. Learn more"
                                                        break
                                                elif("encl_{!s}_cl_bay{}_port{}_connected_ic".format(encls, bay, prt) in d):
                                                    if(d["encl_{!s}_cl_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[2] and (d["encl_{!s}_k_bay{}_port{}_connectedport".format(encls, bay, prt)] == "L1")):
                                                        logger.info(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)])
                                                        logger.info("came here")
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[2] + ", port L" + str(port) + "to " + encls + ", interconnect " + str(bay) + ", port  L" + str(prt) + " is improperly connected. Learn more"
                                                        break
                                                if ((connector_info["port{}_connectorinfo".format(port)] != "noconnector") and (connected_ic is None)):
                                                        # logger.info("came here too")
                                                    expected_msg = "Invalid interconnect link topology cabling. Cable from " + bay_data[2] + ", port L" + str(port) + " is either disconnected or connected to an outside management ring."
                                                elif not (connected_ic is None or connected_ic == " "):

                                                    if (power_state["encl_{}_bay_{}".format(connected_ic.split(",")[0], connected_ic.split(" ")[2])] == "Off"):
                                                        expected_msg = "Invalid interconnect link topology. Port L" + str(port) + " of interconnect " + bay_data[2] + " is connected to interconnect " + connected_ic + " which is powered off."

                                                else:

                                                    if (encl_no[encl_name] == 2):

                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."

                                                    elif (encl_no[encl_name] == 3):
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L2 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."

                                                    elif (encl_no[encl_name] == 4):
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L3 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."
                                                    elif (encl_no[encl_name] == 5):

                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L4 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."
                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))

                elif(bay_data[0] == "4" or bay_data[0] == "5" or bay_data[0] == "6"):
                    if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) or any("FusionUIConst.CONST_HAFNIUM_POTASSIUM" in loop for loop in bay_data):
                        power_stat = power_state["encl_{}_bay_{}".format(encl_name, bay_data[0])]
                        bside_bay = bay_data[0]
                        key = encl_no.get(encl_name)
                        if (key):
                            logger.info("\n-------------------")
                            logger.info("encl %s  is %s \n" % (encl_no[str(encl_name)], encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[4]))
                            logger.info("\n-------------------")
                        else:
                            logger.info("\n-------------------")
                            logger.info("encl is %s \n" % (encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[4]))
                            logger.info("\n-------------------")
                        first = True
                        for port in range(1, 5):
                            connected_port = " "
                            connected_ic = " "
                            frame_error_msg = 0
                            connected_webelement = " "
                            logger.info("port is %d" % port)
                            port_status = TBirdEnclosuresInterconnectLinkTopology.get_cxpport_status_interonnect_link_topology(count, bay_data[0], port)

                            if (port_status == "ok"):
                                logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                                port_sts += 1

                                (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)

                            elif (port_status == "disabled"):

                                if (power_state == "Off"):
                                    power_bit = 1
                                    (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                if (no_of_encl > 4):
                                    error += 1
                                    logger._warn("The Interconnect port L%s status is %s" % (port, port_status))
                                else:
                                    logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                            elif (port_status == "error"):
                                logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                                (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                logger.info("connected ic in k is %s" % connected_ic)
                                if first:
                                    connector_info = _get_connector_information(bay_data[0], bay_data[3], enclosure.name)
                                    first = False
                                if (connected_ic is None) and (connector_info["port{}_connectedto".format(port)] != ""):
                                    connected_ic = connector_info["port{}_connectedto".format(port)]
                                    connected_port = connector_info["port{}_connectedport".format(port)]

                                if (encl_no[str(encl_name)] != 2):

                                    expected_msg = "Invalid interconnect link topology. The interconnect " + bay_data[3] + " is invalid and makes port L" + str(port) + " critical."
                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                elif (connected_ic is None) and (bay_numbering == 0 or bay_numbering == 2):

                                    alert["encl_{!s}_alert_b_port".format(encl_name)] = 0
                                    for encls in encl_list:
                                        for bay in range(1, 7):
                                            for prt in range(1, 5):

                                                if("encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt) in d):
                                                    if(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[3] and (d["encl_{!s}_k_bay{}_port{}_connectedport".format(encls, bay, prt)] == "L1")):
                                                        logger.info(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)])
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L" + str(port) + "to " + encls + ", interconnect " + str(bay) + ", port  L" + str(prt) + " is improperly connected. Learn more"
                                                        break
                                                if (connector_info["port{}_connectorinfo".format(port)] != "noconnector") and ():
                                                    expected_msg = "Invalid interconnect link topology cabling. Cable from " + bay_data[3] + ", port L" + str(port) + " is either disconnected or connected to an outside management ring."

                                                else:
                                                    if port is 1:

                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."
                                                    elif port is 2:
                                                        if (no_of_encl >= 3):
                                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_3 + ", interconnect " + bay_data[0] + " is missing."
                                                    elif port is 3:
                                                        if (no_of_encl == 3):
                                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L2 of " + encl_3 + ", interconnect " + bay_data[0] + " is missing."
                                                        if (no_of_encl >= 4):
                                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_4 + ", interconnect " + bay_data[0] + " is missing."
                                                    else:
                                                        if (no_of_encl <= 3):
                                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L4 of " + encl_1 + ", interconnect " + bay_data[0] + " is missing."
                                                        if (no_of_encl >= 4):
                                                            expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_5 + ", interconnect " + bay_data[0] + " is missing."
                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                elif(connected_ic is None) and (bay_numbering == 1):
                                    if port is 1:

                                        expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_1 + ", interconnect bay " + bay_data[0]
                                    elif port is 2:
                                        if (no_of_encl >= 3):
                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_3 + ", interconnect bay " + bay_data[0]
                                    elif port is 3:
                                        if (no_of_encl == 3):
                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_3 + ", interconnect bay " + bay_data[0]
                                        if (no_of_encl >= 4):
                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_4 + ", interconnect bay " + bay_data[0]
                                    else:
                                        if (no_of_encl <= 3):
                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_1 + ", interconnect bay " + bay_data[0]
                                        if (no_of_encl >= 4):
                                            expected_msg = "Invalid interconnect link topology. Interconnect is missing from enclosure " + encl_5 + ", interconnect bay " + bay_data[0]

                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                elif not (connected_ic is None or connected_ic == " "):
                                    power_state = enclosures.get_powerstate_information(bay_data[0], connected_ic, enclosure.name)
                                    if (power_state == "Off"):
                                        expected_msg = "Invalid interconnect link topology. Port L" + str(port) + " of interconnect " + bay_data[3] + " is connected to interconnect " + connected_ic + " which is powered off."
                                        alert_msgs.append(expected_msg)
                                        logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                            if not (connected_ic is None or connected_ic == " "):
                                (valid_bit, framed_msg, expected_msg) = _validate_b_fabric_ports(no_of_encl, bay_data, port, connected_port, connected_ic, encl_numbering_list)
                                if valid_bit:
                                    logger.info("The Interconnect port L%s is connected as expected" % port)
                                    logger.info("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))
                                else:
                                    error += 1
                                    alert["encl_{!s}_bay{}_port{}_ic".format(encl_name, bay_data[0], port)] = connected_ic
                                    alert["encl_{!s}_bay{}_port{}".format(encl_name, bay_data[0], port)] = connected_port
                                    alert["encl_{!s}_bay{}_port{}_msg".format(encl_name, bay_data[0], port)] = framed_msg
                                    alert_msgs.append(expected_msg)
                                    connected_encl_alert_msgs.append(framed_msg)
                                    logger.info("Expected Alert message is: %s" % expected_msg)
                    elif any(FusionUIConst.CONST_CL10 in data for data in bay_data):

                        bside_bay = bay_data[0]
                        key = encl_no.get(encl_name)
                        if (key):
                            logger.info("\n-------------------")
                            logger.info("encl %s  is %s \n" % (encl_no[str(encl_name)], encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[3]))
                            logger.info("\n-------------------")
                        else:
                            logger.info("\n-------------------")
                            logger.info("encl is %s \n" % (encl_name))
                            logger.info("Interconnect bay %s - %s" % (bay_data[0], bay_data[3]))
                            logger.info("\n-------------------")
                        for port in range(1, 2):
                            logger.info("port is %d" % port)
                            port_status = TBirdEnclosuresInterconnectLinkTopology.get_cxpport_status_interonnect_link_topology(count, bay_data[0], port)
                            logger.info(port_status)
                            if (port_status == "ok"):
                                logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                                port_sts += 1

                            elif (port_status == "disabled"):
                                # power_state = enclosures.get_powerstate_information(bay_data[0], bay_data[2], enclosure.name)
                                if (power_state["encl_{}_bay_{}".format(encl_name, bay_data[0])] == "Off"):
                                    power_bit = 1
                                    (connected_port, connected_ic) = enclosures._get_connectedport_information(count, bay_data[0], power_state, port)
                                if (no_of_encl > 4):
                                    error += 1
                                    logger._warn("The Interconnect port L%s status is %s" % (port, port_status))
                                else:
                                    logger.info("The Interconnect port L%s status is %s" % (port, port_status))
                            elif (port_status == "error"):
                                logger.info("The Interconnect port C%s status is %s" % (port, port_status))
                                connector_info = _get_connector_information(bay_data[0], bay_data[2], enclosure.name)
                                if (connector_info["port{}_connectedto".format(port)] != ""):
                                    connected_ic = connector_info["port{}_connectedto".format(port)]
                                    connected_port = connector_info["port{}_connectedport".format(port)]
                                if (not (connected_ic is None or connected_ic == " ")and (encl_no[encl_name] == 1)):

                                    expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[2] + ", port L" + str(port) + " to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))

                                elif (bay_numbering == 0 or bay_numbering == 2):
                                    logger.info("in cl")
                                    logger.info(connected_ic)
                                    logger.info(connected_port)
                                    alert["encl_{!s}_alert_b_port".format(encl_name)] = 0
                                    for encls in encl_list:
                                        for bay in range(1, 7):
                                            for prt in range(1, 5):

                                                if("encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt) in d or "encl_{!s}_cl_bay{}_port{}_connected_ic".format(encls, bay, prt) in d):
                                                    if(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[2] or d["encl_{!s}_cl_bay{}_port{}_connected_ic".format(encls, bay, prt)] == bay_data[2]and (d["encl_{!s}_k_bay{}_port{}_connectedport".format(encls, bay, prt)] == "L1")):
                                                        logger.info(d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encls, bay, prt)])
                                                        logger.info("came here")
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[2] + ", port L" + str(port) + " to " + encls + ", interconnect " + str(bay) + ", port  L" + str(prt) + " is improperly connected. Learn more"
                                                        break
                                                if ((connector_info["port{}_connectorinfo".format(port)] != "noconnector") and (connected_ic is None)):

                                                    expected_msg = "Invalid interconnect link topology cabling. Cable from " + bay_data[2] + ", port L" + str(port) + " is either disconnected or connected to an outside management ring."
                                                    break
                                                elif not (connected_ic is None or connected_ic == " "):

                                                    if (power_state["encl_{}_bay_{}".format(connected_ic.split(",")[0], connected_ic.split(" ")[2])] == "Off"):
                                                        expected_msg = "Invalid interconnect link topology. Port L" + str(port) + " of interconnect " + bay_data[2] + " is connected to interconnect " + connected_ic + " which is powered off."
                                                        alert_msgs.append(expected_msg)
                                                        logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
                                                else:

                                                    if (encl_no[encl_name] == 2):

                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L1 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."

                                                    elif (encl_no[encl_name] == 3):
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L2 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."

                                                    elif (encl_no[encl_name] == 4):
                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L3 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."
                                                    elif (encl_no[encl_name] == 5):

                                                        expected_msg = "Invalid interconnect link topology cabling. Cable connecting port L" + str(port) + " of " + encl_name + ", interconnect " + bay_data[0] + " to port L4 of " + encl_2 + ", interconnect " + bay_data[0] + " is missing."

                                    alert_msgs.append(expected_msg)
                                    logger.info("Expected Alert message  for port %s : is: %s" % (port, expected_msg))
            status = False
            alert_ms = TBirdEnclosuresInterconnectLinkTopology.get_alert_text(5, False)
            # alert_state = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_ALERT_STATE, 10)
            if ((encl_status is False) and ("Invalid interconnect link topology" in alert_ms)):
                if (wrong_ic == 1):
                    expected_msg = "Invalid interconnect link topology. Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module at Side B is not in first or second enclosure."
                    logger.info("Expected Alert is: %s" % expected_msg)
                    alert_msgs.append(expected_msg)
                elif (wrong_b_bay == 1):
                    expected_msg = "Invalid interconnect link topology. Virtual Connect SE 40Gb F8 Module for Synergy not present at A-side of bay set " + wrong_bay_set + " in enclosure"
                    logger.info("Expected Alert is: %s" % expected_msg)
                    alert_msgs.append(expected_msg)
                elif (no_cl_supp == 1):

                    logger.info("Expected Alert is: %s" % expected_msg_for_oneencl)
                    alert_msgs.append(expected_msg_for_oneencl)
                elif (_frame_alert_message_if_encl_status_error(encl_name, encl_no, no_of_encl, port_sts, "cl10") or encl_dct[count] == 1):
                    logger.info("came here framing msg")
                    expected_msg = "Invalid interconnect link topology"
                    logger.info("Expected Alert is: %s" % expected_msg)
                    alert_msgs.append(expected_msg)
                elif(power_bit == 1):
                    logger.info("came here ")
                    expected_msg = "Invalid interconnect link topology"
                    logger.info("Expected Alert is: %s" % expected_msg)
                    alert_msgs.append(expected_msg)

            if len(alert_msgs) > 0:
                status = capture_alerts(encl_name, count, alert_msgs)

            if (count != no_of_encl and status):
                enclosures.select_enclosure(enclosure.name)
                FusionUIBase.select_view_by_name('Interconnect Link Topology')

            count += 1

    if (error > 0):
        raise AssertionError("Topology validation failed in Enclosure Page")
    else:
        return True


def _get_connector_information(bay_num, interconnect, enclosure, timeout=10):
    from FusionLibrary.ui.networking import interconnects
    connector_info = {}
    linked_ports = []
    unlinked_ports = []
    total_no_of_ports = []
    order_of_ports = []
    port_count = 0
    TBirdEnclosuresInterconnectLinkTopology.click_cxpport_cxp_interconnect(bay_num, interconnect)
    FusionUIBase.select_view_by_name('Interconnect Link Ports')
    if VerifyInterconnects.verify_interconnect_link_ports_label(15, False):
        port_table_information = InterconnectLinkPorts.get_port_table_information(5, False)
        linked_ports, unlinked_ports, order_of_ports = interconnects._get_linked_unlinked_ports_information(port_table_information, order_of_ports, port_count)
        total_no_of_ports = len(linked_ports) + len(unlinked_ports)
        port_count = -1

        for item in order_of_ports:
            port_count = port_count + 1
            port = int(item)
            port_status = InterconnectLinkPorts.get_cxpport_status_from_interconnect_link_ports(port, 5, False)
            cxpport_data = InterconnectLinkPorts.get_port_information_from_interconnect_link_ports(port, 5, False)
            logger.info("port %s status in IC page is %s" % (port, port_status))
            logger.info("Click on the port to capture the connector information \n")
            cxpport_connector_info = InterconnectLinkPorts.get_cxpport_connector_information_from_interconnect_link_ports(port, 5, False)
            CommonOperationInterconnects.refresh_current_page(timeout, False)
            cxpport_data = cxpport_data.split("\n")
            connectedic = cxpport_data[2].split(',')

            length1 = len(cxpport_data)
            i = 1
            if ("No connector" in cxpport_connector_info):
                connector_info["port{}_connectorinfo".format(port)] = "noconnector"
                connector_info["port{}_connectedto".format(port)] = ""
                connector_info["port{}_connectedport".format(port)] = ""
                logger.info("connector info %s" % connector_info["port{}_connectorinfo".format(port)])
            else:
                connector_info["port{}_connectorinfo".format(port)] = "connector present"
                if not ("none" in cxpport_data[2]):

                    connector_info["port{}_connectedto".format(port)] = connectedic[0] + "," + connectedic[1]
                    connector_info["port{}_connectedport".format(port)] = connectedic[2]
                else:
                    connector_info["port{}_connectedto".format(port)] = None
                    connector_info["port{}_connectedport".format(port)] = None
                    logger.info(connector_info["port{}_connectedto".format(port)])
            logger.info(connector_info["port{}_connectorinfo".format(port)])
        enclosures.select_enclosure(enclosure)
        FusionUIBase.select_view_by_name('Interconnect Link Topology')
        return connector_info


def capture_alerts(enclname, encl_count, alert_msgs, timeout=5):
    encl_cxp_status = TBirdEnclosuresInterconnectLinkTopology.get_enclosure_status_in_interconnectlinktopology(enclname, encl_count, 10, False)

    activity_state = "Locked"
    alerts_msgs_ov = []
    logger.info("Enclosure Status is %s" % encl_cxp_status)
    if (encl_cxp_status == "error"):
        TBirdEnclosuresInterconnectLinkTopology.click_cxpenclosure(enclname, encl_count, timeout)

        encl_status = C7000VerifyEnclosures.verify_enclosure_status_ok(enclname, 5, False)
        if (encl_status is False):
            logger.info("%s Enclosure status is %s" % (enclname, encl_cxp_status))
        else:
            logger.info("Enclosure status is different on main page than CXP topology ")
        logger.info("capturing the alerts")
        # Navigate to Activity Page
        FusionUIBase.select_view_by_name('Activity')
        # Filter Active Alerts
        TBirdEnclosuresInterconnectLinkTopology.click_filter_all_states(timeout, False)
        TBirdEnclosuresInterconnectLinkTopology.click_filter_activity_state(activity_state, timeout, False)
        CommonOperationInterconnects.refresh_current_page(timeout, False)
        # Display the error count

        error_count = TBirdEnclosuresInterconnectLinkTopology.get_error_count_in_invalid_interonnect_link_topology(5, False)
        import re
        error_count = re.sub(r'\s', '', error_count)

        if (error_count == "1"):
            no_of_alerts = 1
        else:
            no_of_alerts = int(error_count)
        # Display the Active alerts on Console
        k = 1

        for k in range(1, no_of_alerts + 1):

            if k <= no_of_alerts:

                if not TBirdEnclosuresInterconnectLinkTopology.click_alert_label_collapser(k, timeout, False):
                    break

                alert_msg = TBirdEnclosuresInterconnectLinkTopology.get_activity_text(k, 15, False)

                resolution_msg = TBirdEnclosuresInterconnectLinkTopology.get_resolution_text(k + 1, 15, False)
                TBirdEnclosuresInterconnectLinkTopology.click_event_details_collapser(k + 1, 15, False)
                event_msg = CommonOperationInterconnects.get_event_text(k + 1, 15, False)
                logger.info("---------------------------------------\n")
                logger.info("%d. Alert: %s \n" % (k, alert_msg))
                logger.info("%s \n" % resolution_msg)
                logger.info("%s \n" % event_msg)
                logger.info("---------------------------------------\n")
                TBirdEnclosuresInterconnectLinkTopology.click_event_details_collapser(k + 1, 5, False)
                TBirdEnclosuresInterconnectLinkTopology.click_alert_label_collapser(k, 5, False)

                alerts_msgs_ov.append(alert_msg)
        # Compare expected and OV alerts
        k = 1

        for alert in alert_msgs:
            count = 0
            for k in alerts_msgs_ov:

                if (alert in k):
                    logger.info("Expected and Actual Alert message is proper")
                    count += 1
                else:
                    pass
        if (count == 0) or (len(alert_msgs) != len(alerts_msgs_ov)):
            logger.warn("Verify the alerts, expected and actual alert count is not matching !! or Expected alerts are not present in Activity")

        FusionUIBase.select_view_by_name('Overview')
        return True

    else:
        return False


def _frame_alert_message_if_encl_status_error(encl_name, encl_no, encl_len, port_sts, ic_kind):
    msg_bit = False
    logger.info(ic_kind)
    if (ic_kind == "cl10"):
        if (encl_len == 5):
            if (encl_no[encl_name] == 1 and port_sts == 5):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 5):
                msg_bit = True
            elif (encl_no[encl_name] >= 3 and port_sts == 2):
                msg_bit = True
        elif(encl_len == 4):
            if (encl_no[encl_name] == 1 and port_sts == 4):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 4):
                msg_bit = True
            elif (encl_no[encl_name] >= 3 and port_sts == 2):
                msg_bit = True
        elif(encl_len == 3):
            if (encl_no[encl_name] == 1 and port_sts == 3):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 3):
                msg_bit = True
            elif (encl_no[encl_name] >= 3 and port_sts == 2):
                msg_bit = True
        elif(encl_len == 2):
            if (encl_no[encl_name] == 1 and port_sts == 2):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 2):
                msg_bit = True

    if (ic_kind == "cl20"):
        if(encl_len == 3):
            if (encl_no[encl_name] == 1 and port_sts == 6):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 6):
                msg_bit = True
            elif (encl_no[encl_name] == 3 and port_sts == 4):
                msg_bit = True
        elif(encl_len == 2):
            if (encl_no[encl_name] == 1 and port_sts == 4):
                msg_bit = True
            elif (encl_no[encl_name] == 2 and port_sts == 4):
                msg_bit = True
    return msg_bit


def _validate_a_fabric_ports(encl_len, bay_data, port, connected_port, connected_ic, encl_numbering_list):
    logger.info("in validate a side fabric ports")
    expected_msg = " "
    framed_message = " "
    valid_bit = 0
    if port is 1:
        logger.info(port)
        logger.info(connected_port + connected_ic)
        logger.info("L1" + encl_numbering_list[1] + ', ' + "interconnect " + bay_data[0])
        if (connected_port + connected_ic == "L1" + encl_numbering_list[1] + ', ' + "interconnect " + bay_data[0]):
            valid_bit = 1
        else:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L1 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L1 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))
            logger.warn(expected_msg)

    elif port is 2:
        if (encl_len == 2):
            valid_bit = 0
        elif (encl_len >= 3):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[2] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        if valid_bit == 0:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L2 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L2 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    elif port is 3:
        if (encl_len == 2):
            valid_bit = 0
        elif (encl_len == 3):
            if (connected_port + connected_ic == "L2" + encl_numbering_list[2] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        elif (encl_len >= 4):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[3] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        if valid_bit == 0:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L3 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L3 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    else:
        if (encl_len == 2):
            valid_bit = 0
        elif (encl_len == 3):
            if (connected_port + connected_ic == "L2" + encl_numbering_list[1] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        elif (encl_len == 4):
            valid_bit = 0
        elif (encl_len >= 5):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[4] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        if valid_bit == 0:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L4 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L4 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    return (valid_bit, framed_message, expected_msg)


def _validate_b_fabric_ports(encl_len, bay_data, port, connected_port, connected_ic, encl_numbering_list):
    logger.info("in validate b side fabric ports")
    expected_msg = " "
    framed_message = " "
    valid_bit = 0
    if port == 1:
        logger.info(connected_port + connected_ic)
        logger.info("L1" + encl_numbering_list[0] + ', ' + "interconnect " + bay_data[0])
        if (connected_port + connected_ic == "L1" + encl_numbering_list[0] + ', ' + "interconnect " + bay_data[0]):
            valid_bit = 1
        else:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L1 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L1 to " + connected_ic + ", port" + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    if port == 2:
        if (encl_len == 2):
            valid_bit = 0
        elif (encl_len >= 3):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[2] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        else:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L2 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L2 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    if port == 3:
        loger.info("inside b")
        if (encl_len == 2):
            valid_bit = 0
        elif (encl_len == 3):
            loger.info("inside 3")
            if (connected_port + connected_ic == "L2" + encl_numbering_list[2] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        elif (encl_len >= 4):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[3] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        if valid_bit == 0:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L3 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L3 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    if port == 4:
        if (encl_len == 2):
            if (connected_port + connected_ic == "L2" + encl_numbering_list[0] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        elif (encl_len == 3):
            if (connected_port + connected_ic == "L2" + encl_numbering_list[0] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        elif (encl_len == 4):
            valid_bit = 0
        elif (encl_len >= 5):
            if (connected_port + connected_ic == "L1" + encl_numbering_list[4] + ', ' + "interconnect " + bay_data[0]):
                valid_bit = 1
        else:
            connected_encl = connected_ic.split(",")[0]
            framed_message = "Invalid interconnect link topology cabling. Cable connecting " + connected_ic + ", port " + connected_port + " to " + bay_data[3] + ", port L4 is improperly connected. Learn more"
            expected_msg = "Invalid interconnect link topology cabling. Cable connecting " + bay_data[3] + ", port L4 to " + connected_ic + ", port " + connected_port.strip() + " is improperly connected. Learn more"
            logger._warn("The Interconnect port L%s is connected to port %s of %s" % (port, connected_port, connected_ic))

    return (valid_bit, framed_message, expected_msg)


def _get_no_of_cl_single_encl(encl):
    encl_ic_bay_port_list = []
    c2 = ''
    c1 = ''
    i = 0
    alert_msg = ''
    count = 1
    power_state = {}
    encl_ic_bay_port_list = TBirdEnclosuresInterconnectLinkTopology.get_interconnect_cxp_bay_from_interconnect_link_topology(count, 15, False)

    for bay_data in encl_ic_bay_port_list:
        bay_data = bay_data.split("\n")
        if any(FusionUIConst.CONST_CL10 in data for data in bay_data):
            if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                power_state["encl_{}_bay_{}".format(encl, bay_data[0])] = enclosures.get_powerstate_information(bay_data[0], bay_data[2], encl)
                logger.info("power state of icm %s is %s" % (bay_data[2], power_state["encl_{}_bay_{}".format(encl, bay_data[0])]))

                if i == 0:
                    c1 = bay_data[3] + " in " + bay_data[2]
            elif(bay_data[0] == "4" or bay_data[0] == "5" or bay_data[0] == "6"):
                power_state["encl_{}_bay_{}".format(encl, bay_data[0])] = enclosures.get_powerstate_information(bay_data[0], bay_data[2], encl)
                logger.info("power state of icm %s is %s" % (bay_data[2], power_state["encl_{}_bay_{}".format(encl, bay_data[0])]))
                if i > 0:
                    c1 = ', ' + bay_data[3] + " in " + bay_data[2]
            c2 = c2 + c1
            i = i + 1
    alert_msg = 'Invalid interconnect link topology. ' + c2 + ' are not supported in a single enclosure topology.'
    logger.info(alert_msg)
    return (alert_msg, power_state)
