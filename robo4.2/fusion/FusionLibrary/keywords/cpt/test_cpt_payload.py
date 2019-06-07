#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Unit test cases for CPT Payload Generator
"""
from mock import patch
from payload_generator import CptPayloadGenerator
from unittest import TestCase
from copy import deepcopy


# Inputs for the tests
ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://192.168.124.10/iso/esxi/65.iso",
          "deployment_network": "CPT_NET",
          "ilo_user": "Administrator",
          "ilo_pass": "admin123"}

RHEL74 = {"os_name": "RHEL74x64",
          "os_repo": "http://192.168.124.10/iso/rhel/74",
          "system_password": "hpvse123",
          "deployment_network": "CPT_NET",
          "network_driver": "http://192.168.124.10/drivers/network/",
          "storage_driver": "http://192.168.124.10/drivers/storage",
          "ilo_user": "Administrator",
          "ilo_pass": "admin123"}

CPT = {"host": "192.168.124.20", "user": "root", "password": "hpvse123"}
SERVER_URL = "/rest/server-profiles/a4caf4a4-01a7-441b-8964-c57a1e38b0f9"

# Mock outputs
SERVER_PROFILE = {"serialNumber": "VIRTUALNUMBER001",
                  "type": "ServerProfileV8",
                  "name": "Server Profile 1",
                  "bootMode": None,
                  "connectionSettings": {
                      "connections": [{"mac": "aa:bb:cc:dd:ee",
                                       "id": "3",
                                       "networkUri":
                                           "/rest/ethernet-networks/NET_1",
                                       "boot": {"priority": "NotBootable"}}]},
                  "serverHardwareUri": "/rest/server-hardware/Bay02",
                  "status": "OK"}

SERVER_PROFILE1 = deepcopy(SERVER_PROFILE)
sp = SERVER_PROFILE1['connectionSettings']['connections']
sp.append({"mac": "aa:bb:cc:dd:ef",
           "id": "2",
           "networkUri": "/rest/ethernet-networks/NET_3",
           "boot": {"priority": "NotBootable"}})

SERVER_PROFILE2 = deepcopy(SERVER_PROFILE)
sp = SERVER_PROFILE2['connectionSettings']['connections']
sp.append({"mac": "aa:bb:cc:dd:ef",
           "id": "2",
           "networkUri": "/rest/fcoe-networks/NET_3",
           "boot": {"priority": "Primary"}})

SERVER_PROFILE3 = deepcopy(SERVER_PROFILE2)
sp = SERVER_PROFILE3['connectionSettings']['connections']
sp.append({"mac": "aa:bb:cc:dd:ff",
           "id": "1",
           "networkUri": "/rest/fcoe-networks/NET_3",
           "boot": {"priority": "Secondary"}})

ILO_DICT = {"ip": "192.168.124.20",
            "user": "Administrator",
            "password": "hpvse123"}

NET_PROFILE = {"count": 1,
               "members": [{"uri": "/rest/ethernet-networks/NET_1"}]}


class TestCptPayload(TestCase):
    """
    Test cases for validating input generator for OS Deployment
    """

    @patch('payload_generator.CptPayloadGenerator._get_ilo_dict')
    @patch('payload_generator.CptPayloadGenerator._get_network_uri')
    @patch('payload_generator.CptPayloadGenerator._set_server_profile')
    def test_input_for_single_server_deployment(self, mock_sp, mock_net,
                                                mock_ilo):
        """
        Test the result of the keyword
        :param mock_sp: Handle to mock method _set_server_profile
        :param mock_net: Handle to mock method _get_network_uri
        :param mock_ilo: Handle to mock method _get_ilo_dict
        :return:
        """
        mock_sp.return_value = None
        mock_net.return_value = '/rest/ethernet-networks/NET_1'
        mock_ilo.return_value = ILO_DICT

        # Begin test logic
        t = CptPayloadGenerator()
        t.server = SERVER_PROFILE
        r = t.generate_payload(SERVER_URL, ESXi65)

        self.assertEqual(r['host']['name'], "VIRTUALNUMBER001")
        self.assertEqual(r['os_name'], "ESXi65x64")
        self.assertEqual(r['boot_mode'], "Legacy")
        self.assertEqual(r['network']['mac'], 'aa:bb:cc:dd:ee')
        self.assertEqual(r['ilo']['password'], "hpvse123")

    @patch('payload_generator.CptPayloadGenerator._get_ilo_dict')
    @patch('payload_generator.CptPayloadGenerator._get_network_uri')
    @patch('payload_generator.CptPayloadGenerator._set_server_profile')
    def test_input_for_unordered_network(self, mock_sp, mock_net, mock_ilo):
        """
        Test the result of the keyword
        :param mock_sp: Handle to mock method _set_server_profile
        :param mock_net: Handle to mock method _get_network_uri
        :param mock_ilo: Handle to mock method _get_ilo_dict
        :return:
        """
        mock_sp.return_value = None
        mock_net.return_value = '/rest/ethernet-networks/NET_1'
        mock_ilo.return_value = ILO_DICT

        # Begin test logic
        t = CptPayloadGenerator()
        t.server = SERVER_PROFILE1
        r = t.generate_payload(SERVER_URL, ESXi65)

        self.assertEqual(r['network']['pos'], 2)

    @patch('payload_generator.CptPayloadGenerator._get_ilo_dict')
    @patch('payload_generator.CptPayloadGenerator._get_network_uri')
    @patch('payload_generator.CptPayloadGenerator._set_server_profile')
    def test_input_for_network_driver(self, mock_sp, mock_net, mock_ilo):
        """
        Test the result of the keyword
        :param mock_sp: Handle to mock method _set_server_profile
        :param mock_net: Handle to mock method _get_network_uri
        :param mock_ilo: Handle to mock method _get_ilo_dict
        :return:
        """
        mock_sp.return_value = None
        mock_net.return_value = '/rest/ethernet-networks/NET_1'
        mock_ilo.return_value = ILO_DICT

        # Begin test logic
        t = CptPayloadGenerator()
        t.server = SERVER_PROFILE1
        r = t.generate_payload(SERVER_URL, RHEL74)

        self.assertEqual(r['network']['drivers'],
                         "http://192.168.124.10/drivers/network/")

    @patch('payload_generator.CptPayloadGenerator._get_ilo_dict')
    @patch('payload_generator.CptPayloadGenerator._get_network_uri')
    @patch('payload_generator.CptPayloadGenerator._set_server_profile')
    def test_input_for_fcoe(self, mock_sp, mock_net, mock_ilo):
        """
        Test the result of the keyword
        :param mock_sp: Handle to mock method _set_server_profile
        :param mock_net: Handle to mock method _get_network_uri
        :param mock_ilo: Handle to mock method _get_ilo_dict
        :return:
        """
        mock_sp.return_value = None
        mock_net.return_value = '/rest/ethernet-networks/NET_1'
        mock_ilo.return_value = ILO_DICT

        # Begin test logic
        t = CptPayloadGenerator()
        t.server = SERVER_PROFILE2
        r = t.generate_payload(SERVER_URL, RHEL74)

        self.assertEqual(r['storage']['fcoe']['enabled'], True)

    @patch('payload_generator.CptPayloadGenerator._get_ilo_dict')
    @patch('payload_generator.CptPayloadGenerator._get_network_uri')
    @patch('payload_generator.CptPayloadGenerator._set_server_profile')
    def test_input_for_multipaths(self, mock_sp, mock_net, mock_ilo):
        """
        Test the result of the keyword
        :param mock_sp: Handle to mock method _set_server_profile
        :param mock_net: Handle to mock method _get_network_uri
        :param mock_ilo: Handle to mock method _get_ilo_dict
        :return:
        """
        mock_sp.return_value = None
        mock_net.return_value = '/rest/ethernet-networks/NET_1'
        mock_ilo.return_value = ILO_DICT

        # Begin test logic
        t = CptPayloadGenerator()
        t.server = SERVER_PROFILE3
        r = t.generate_payload(SERVER_URL, RHEL74)

        self.assertEqual(r['storage']['fcoe']['enabled'], True)
        self.assertEqual(r['storage']['fcoe']['mac2'], "aa:bb:cc:dd:ff")
        self.assertEqual(r['storage']['multipath'], True)
        self.assertEqual(r['network']['pos'], 3)
