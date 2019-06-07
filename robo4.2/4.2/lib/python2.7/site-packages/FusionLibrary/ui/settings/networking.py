# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Edit Networking Page
"""
import time
from datetime import datetime
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from FusionLibrary.ui.business_logic.settings.networking import EditNetworking
from FusionLibrary.ui.business_logic.settings.networking import VerifyNetworking
from RoboGalaxyLibrary.utilitylib import logging as logger


def edit_C7000_networking(networking_obj):
    """  Edit C7000 networking """

    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    EditNetworking.click_networking()
    EditNetworking.select_action_edit()
    EditNetworking.wait_edit_networking_dialog_shown()
    logger.info("Editing networking")
    EditNetworking.input_appliance_host_name(networking_obj.hostname)

    if networking_obj.ipv4assignment.lower().strip() == "manual":
        EditNetworking.choose_ipv4_address_assignment("manual")
        EditNetworking.input_ipv4_address(networking_obj.ipv4address)
        EditNetworking.input_ipv4_subnet_mask_or_cidr(networking_obj.ipv4mask)
        EditNetworking.input_ipv4_gateway_address(networking_obj.ipv4gateway)

    else:
        EditNetworking.choose_ipv4_address_assignment("dhcp")

    EditNetworking.input_preferred_dns_server(networking_obj.preferreddns)
    EditNetworking.input_alternate_dns_server(networking_obj.alternatedns)

    if networking_obj.ipv6assignment.lower().strip() == "manual":
        EditNetworking.choose_ipv6_address_assignment("manual")
        EditNetworking.input_ipv6_address(networking_obj.ipv6address)
        EditNetworking.input_ipv6_subnet_mask_or_cidr(networking_obj.ipv6mask)
        EditNetworking.input_ipv6_gateway_address(networking_obj.ipv6gateway)

    elif networking_obj.ipv6assignment.lower().strip() == "unassign":
        EditNetworking.choose_ipv6_address_assignment("unassign")

    else:
        EditNetworking.choose_ipv6_address_assignment("dhcpv6")

    EditNetworking.click_networking_edit_ok()
    EditNetworking.wait_applying_network_settings_progress_bar_shown()
    EditNetworking.wait_applying_network_settings_progress_bar_disappear()
    EditNetworking.click_settings()
    EditNetworking.wait_networking_panel_disappear()
    return True


def verify_C7000_networking(networking_obj):
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    EditNetworking.click_networking()
    VerifyNetworking.wait_host_name_shown(networking_obj.hostname, timeout=10)
    time.sleep(5)
    VerifyNetworking.verify_host_name(networking_obj.hostname)

    if networking_obj.ipv4assignment.lower().strip() == "manual":
        VerifyNetworking.verify_ipv4_assignment(networking_obj.ipv4assignment)
        VerifyNetworking.verify_ipv4_address(networking_obj.ipv4address)
        VerifyNetworking.verify_ipv4_subnet_mask_or_cidr(networking_obj.ipv4mask)
        VerifyNetworking.verify_ipv4_gateway_address(networking_obj.ipv4gateway)
    elif networking_obj.ipv4assignment.lower().strip() == "dhcp":
        VerifyNetworking.verify_ipv4_assignment(networking_obj.ipv4assignment)
        VerifyNetworking.verify_ipv4_subnet_mask_or_cidr(networking_obj.ipv4mask)
        VerifyNetworking.verify_ipv4_gateway_address(networking_obj.ipv4gateway)

    VerifyNetworking.verify_ipv6_assignment("not set")
    # if networking_obj.ipv6assignment.lower().strip() == "unassign":
    #     VerifyNetworking.verify_ipv6_assignment("not set")
    #     VerifyNetworking.verify_ipv6_address("not set")
    #     VerifyNetworking.verify_ipv6_subnet_mask_or_cidr("not set")
    #     VerifyNetworking.verify_ipv6_gateway_address("not set")
    # elif networking_obj.ipv6assignment.lower().strip() == "dhcpv6":
    #     VerifyNetworking.verify_ipv6_assignment(networking_obj.ipv6assignment)
    #     VerifyNetworking.verify_ipv6_subnet_mask_or_cidr(networking_obj.ipv6mask)
    #     VerifyNetworking.verify_ipv6_gateway_address(networking_obj.ipv6gateway)
    # else:
    #     VerifyNetworking.verify_ipv6_assignment(networking_obj.ipv6assignment)
    #     VerifyNetworking.verify_ipv6_address(networking_obj.ipv6address)
    #     VerifyNetworking.verify_ipv6_subnet_mask_or_cidr(networking_obj.ipv6mask)
    #     VerifyNetworking.verify_ipv6_gateway_address(networking_obj.ipv6gateway)
    VerifyNetworking.verify_preferred_dns_server(networking_obj.preferreddns)
    VerifyNetworking.verify_alternate_dns_server(networking_obj.alternatedns)
    EditNetworking.click_settings()
    EditNetworking.wait_networking_panel_disappear()
    return True


def get_appliance_hostname_and_ip_address():
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    start = datetime.now()
    timeout = 10  # 10 seconds to get hostname & ip address
    while (datetime.now() - start).total_seconds() < timeout:
        hostname = EditNetworking.get_appliance_host_name()
        if hostname.strip() == '':
            time.sleep(1)
            continue
        else:
            break
    else:
        hostname = ''

    start = datetime.now()
    while (datetime.now() - start).total_seconds() < timeout:
        ip_address = EditNetworking.get_appliance_ip_address()
        if ip_address.strip() == '':
            time.sleep(1)
            continue
        else:
            break
    else:
        ip_address = ''

    return str(hostname), str(ip_address)
