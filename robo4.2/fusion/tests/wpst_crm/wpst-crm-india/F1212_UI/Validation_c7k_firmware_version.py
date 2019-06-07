import re
import time
import paramiko
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.utilitylib import logging

class Validation_c7k_firmware_version:

    def verify_c7k_ic_version(self, icbay, appip, appuname="Administrator", appasswd="Admin", dcs="no"):
        """   This   function   to connect to OA   and   then    get the desired interconnects firmware version
        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  #  SSH  Port to    establish  connection
        client.connect(appip, port, username=appuname, password=appasswd)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        if dcs == 'yes':
            cmd = "show interconnect info " + str(icbay)
            input, output, error = client.exec_command(cmd)
            data = output.read()
            logging._log_to_console_and_log_file("data is %s" % data)
            data = data.strip()
            m = re.search('Firmware Version: (.*)', data)
            if m:
                logging._log_to_console_and_log_file("match found !")
                logging._log_to_console_and_log_file("Value of firmware version: %s" % (m.group(1)))

                return m.group(1)
        else:
            cmd = "show interconnect info " + str(icbay)
            input, output, error = client.exec_command(cmd)
            data = output.read()
            logging._log_to_console_and_log_file("data is %s" % data)
            data = data.strip()
            m = re.search('Firmware Version: (.*)', data)
            if m:
                logging._log_to_console_and_log_file("Firmware version match found !")
                logging._log_to_console_and_log_file("Value of firmware version is : %s" % (m.group(1)))

                return m.group(1)
