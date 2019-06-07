from FusionLibrary.libs.cli.cli_base import remote_actions
from RoboGalaxyLibrary.utilitylib import logging
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import sys
import paramiko
import re


class EMCLIKeywords(object):

    def get_data_from_switch(self, switch_ip, commands, uname, pwd):
        ''' This function logs into the switch and runs the commands passed. Commands here is a list of commands.
            The output will be a list of the return value and return code after command execution in the same order
            that the commands were passed '''

        logging.info("\nConnecting to %s and run command %s" % (switch_ip, commands))
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22
        errorcodelist = []
        datalist = []
        logging.info("Password is %s" % pwd)
        client.connect(switch_ip, port=port, username=uname, password=pwd)
        i = 0
        for command in commands:
            print "executing command %s" % command
            input, output, error = client.exec_command(command)
            errorcodelist.insert(i, output.channel.recv_exit_status())
            datalist.insert(i, output.read())
            i = i + 1
        return (datalist, errorcodelist)

    def get_canmic_block(self, appip, port, appuname, apppassw, cmd):
        """
            This function reads CANMIC blocks from EM using EM IPV6
        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(appip, port, appuname, apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        logging.info("cmd %s" % cmd)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        d = data.split("\n")
        mdata = []

        for k in d:
            head, sep, tail = k.partition('|')
            head = head[10:].split(" ")
            mdata = mdata + head
        return filter(None, mdata)

    def get_connector_information_from_em(self, dcs, enclosurename, appip, username, password, emipv6, icbay, blk, power_state, prod_name, port_count):

        logging.info("Function to Get connector information from EM")

        # Capture the port connector information by logging into EM
        vendorOUI = ""
        partnumber = ""
        serialnumber = ""
        revision = ""
        connector_present = ""
        connectortype = ""
        connectorspeed = ""
        connectorvendor = ""
        cxpdata = ""
        ic_dict = {"Type": [], "Speed": [], "Vendor": [], "Vendor OUI": [],
                   "Part number": [], "Revision": [], "Serial number": []}
        if dcs.lower() == 'yes':
            # For DCS EM
            cmd = 'curl -ik --request POST https://%s/rest/v1/Managers/20%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (emipv6, icbay, blk)
        else:
            # Get XAUTH of EM to use with EM RIS request
            xauth_cmd = ['/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (enclosurename)]
            (datalst, errorcode) = self.get_data_from_switch(appip, xauth_cmd, username, password)
            strdata = ''.join(datalst)
            xauth = strdata.strip()
            cmd = 'curl --globoff -ki -x "" --request POST --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (xauth, emipv6, icbay, blk)

        port = 22
        mdata = self.get_canmic_block(appip, port, username, password, cmd)

        # check the presence of CXP connector
        if (power_state != "Off" and len(mdata) > 0):
            connector_present = mdata[0]
            connector_present = '{0:08b}'.format(int(mdata[0]))
            connector_present = connector_present[-1]

            if connector_present is "0":
                logging.info("C1 - Connector is present")
                # Get Vendor OUI
                i = 1
                while i < 4:
                    if mdata[i] != "" and mdata[i] != "20":
                        vendorOUI = vendorOUI + (mdata[i]).upper()
                        if (i < 3):
                            vendorOUI = vendorOUI + "-"

                    i = i + 1
                # Get Part number
                i = 4
                while i < 20:
                    if mdata[i] != "" and mdata[i] != "20":
                        partnumber = partnumber + chr(int(mdata[i], 16))
                    i = i + 1
                i = 20
                while i < 22:
                    revision = revision + chr(int(mdata[i], 16))
                    i = i + 1

                # get serial-number
                i = 22
                while i < 38:
                    if mdata[i] != "" and mdata[i] != "20":
                        serialnumber = serialnumber + chr(int(mdata[i], 16))
                    i = i + 1

                if(("Synergy 20Gb Interconnect Link Module" in prod_name) or ("Synergy 10Gb Interconnect Link Module" in prod_name)):

                    blk = 200 + port_count
                    connectortype = ""
                    connectorspeed = ""
                    connectorvendor = ""
                    if dcs.lower() == 'yes':
                                        # For DCS EM
                        cmd = 'curl -ik --request POST https://%s/rest/v1/Managers/20%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (emipv6, icbay, blk)
                    else:

                        cmd = 'curl --globoff -ki -x "" --request POST --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s -H "Content-Type: application/json" -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (xauth, emipv6, icbay, blk)

                    cxpdata = self.get_canmic_block(appip, port, username, password, cmd)
                elif ("Synergy 10/40Gb Pass-Thru Module" in prod_name):
                    cxpdata = mdata

                if len(cxpdata) > 0:
                    logging.info("---%s" % (cxpdata))

                    connectortype_temp = int(cxpdata[54], 16)
                    if connectortype_temp == 254:
                        connectortype = "ILP"
                    if connectortype_temp == 255:
                        connectortype = "Unknown"
                    if connectortype_temp == 64:
                        connectortype = "10GBASE-T"
                    if connectortype_temp == 43:
                        connectortype = "Active DAC"
                    if connectortype_temp == 42:
                        connectortype = "Passive DAC"

                    connectorspeed = str(12 * (int(cxpdata[53], 16)))
                    # Right now, OV is not using this paramter. OV always returns none for this.
                    if cxpdata[0] == '00':
                        connectorvendor = "none"
                    if cxpdata[0] == '43':
                        connectorvendor = "Cisco"
                    if cxpdata[0] == '4e':
                        connectorvendor = "HP Network"
                    if cxpdata[0] == '53':
                        connectorvendor = "HP Servers"
                    connectorvendor = "none"
                    ic_dict["Type"] = connectortype
                    ic_dict["Speed"] = connectorspeed
                    ic_dict["Vendor"] = connectorvendor

                logging.info(vendorOUI)
                logging.info(partnumber)
                logging.info(revision)
                logging.info(serialnumber)
                ic_dict["Vendor OUI"] = vendorOUI
                ic_dict["Part number"] = partnumber
                ic_dict["Revision"] = revision
                ic_dict["Serial number"] = serialnumber

            else:
                logging.info("No Connector in EM")
        else:
            logging.info("ICM power is off state, we will not be able to read Canmic Block")
        return (connector_present, ic_dict)
