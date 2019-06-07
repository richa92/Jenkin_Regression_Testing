#!/usr/local/bin/python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko
import logging
import sys
import tempfile
import os
import re
import time
import string
from os import write
libLogger = "api-logger"
from robot.libraries.BuiltIn import BuiltIn


class OAOperations:

    def efuse_device(self, ip, uname, pw, dev, bay, state):
        log = logging.getLogger(libLogger)

        try:
            log.debug('Enter diag mode on %s' % (ip))
            command = '++diag--'
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = ip
            port = 22
            client.connect(hostname, port=port, username=uname, password=pw)

            # open channel to the OA
            chan = client.invoke_shell()
            time.sleep(10)
            chan.send(command + '\n')
            resp = chan.recv(999)
            print resp

            log.debug('Send efuse %s to interconnect %s' % (state, bay))
            command = string.Template('efuse $dev $bay $state')
            command = command.substitute(dev=dev, bay=bay, state=state)
            time.sleep(10)
            chan.send(command + '\n')
            resp = chan.recv(999)
            print resp

            # exit  diag mode
            time.sleep(10)
            chan.send('q\n')
            resp = chan.recv(999)
            print resp

        except Exception as e:
            msg = "Exception occured while attempting to send ssh command %s" \
                % (command)
            raise Exception(msg, e)
        finally:
            client.close()

        return

    def forceFailOver(self, ip, uname, pw):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with Prefix OA-ForceFailover")
            (fd, fname) = tempfile.mkstemp(prefix="OA-ForceFailover.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'FORCE TAKEOVER'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (uname, ip, pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            hostname = ip
            port = 22
            client.connect(hostname, port=port, username=uname, password=pw)

            stdin, stdout, stderr = client.exec_command(command)

            write(fd, stdout.read())
        except Exception as e:
            msg = "Exception occured while attempting to send ssh command %s" \
                % (command)
            raise Exception(msg, e)
        finally:
            client.close()

        try:
            log.debug('Opening file %s' % (fname))
            fd = open(fname)
        except Exception as e:
            msg = "Failed to open file %s" % (fname)
            raise Exception(msg, e)

        failoverList = []
        for line in fd:
            # JRT print line
            failoverList.append(line)

        return failoverList

    def validate_Tx_Rx_Rates_statistics(self, bay_no, output):
        list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == bay_no]
        bytesTX = list_val[0]['fcStatistics']['extendedStatistics']['numBytesTx']
        bytesRX = list_val[0]['fcStatistics']['extendedStatistics']['numBytesRx']
        framesTX = list_val[0]['fcStatistics']['extendedStatistics']['numFramesTx']
        framesRX = list_val[0]['fcStatistics']['extendedStatistics']['numFramesRx']
        return (bytesTX, bytesRX, framesTX, framesRX)

    def disable_enable_interconnect_ports(self, uri, output, port_no, enable_flag):

        temp_dict = {}
        list_keys = ['associatedUplinkSetUri', 'interconnectName', 'portType', 'portId', 'portHealthStatus', 'capability', 'configPortTypes', 'enabled', 'portName', 'portStatus', 'type']
        for i in output['ports']:
            if i['portName'] == port_no:
                for key in list_keys:
                    temp_dict[key] = i[key]
        temp_dict['enabled'] = enable_flag
        fz = BuiltIn().get_library_instance('FusionLibrary')
        output = fz.fusion_api_edit_interconnect_ports([temp_dict], uri)
        print output
        return output

    def Ochange_interconnect_ports_status(self, body, uri):

        param = '/update-ports'
        fz = BuiltIn().get_library_instance('FusionLibrary')
        # ss = fz.fusion_api_get_interconnect()
        ss = fz.fusion_api_edit_interconnect_ports(body, uri)
        return ss
