#!/usr/local/bin/python
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
import logging
import warnings
from time import sleep
# there are some annoying warning with paramiko so we import the warnings
# module and ignore them
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
import paramiko

libLogger = "api-logger"
from RoboGalaxyLibrary.utilitylib import logging as logger

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.


class Interface ():

    def __init__(self, credentials):
        self.msg = ''
        self.log = logging.getLogger(libLogger)
        self.credentials = credentials
        self._port = 22
        try:
            self.connect()
        except Exception as e:
            self.msg = "Exception %s while trying to connect" % e
            self.log.error(self.msg)
            raise Exception(self.msg, e)

    def __del__(self):
        self.disconnect()

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.WarningPolicy())
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.credentials['ipAddress'], port=self._port, username=self.credentials[
                                'username'], password=self.credentials['password'])
        except Exception:
            self._connected = False
        else:
            self._connected = True
        return self._connected

    def send_command_wait(self, command):
        return self.send_command(command, True)

    def send_command_no_wait(self, command):
        return self.send_command(command, False)

    def send_command(self, command, verbose, waitTime=0):
        noWait=False
        try:
            self.msg = 'Sending command %s' % command
            if verbose:
                logger._log_to_console_and_log_file(self.msg)
            else:
                self.log.debug(self.msg)
            stdin, stdout, stderr = self.client.exec_command(command)
            output = ''
            stdin.flush()
            error = stderr.read()
            if len(error) > 0:
                self.msg = "Command failed with %s" % error
                if verbose:
                    logger._log_to_console_and_log_file(self.msg)
                else:
                    self.log.error(self.msg)
                raise RuntimeError(self.msg)
            else:
                output = stdout.read()
                if len(output) > 0:
                    self.msg = 'Output from %s: %s' % (command, output)
                    if verbose:
                        logger._log_to_console_and_log_file(self.msg)
                    else:
                        self.log.debug(self.msg)
                    if (('Unable to communicate with the Virtual Connect Manager' in output and 'delete domain' not in command)
                        or ('Virtual Connect Manager not found at this IP address' in output)):
                            logger._log_to_console_and_log_file("WARN: CIC Managed. Unable to establish connection to VCM.")
                            raise RuntimeError(self.msg)
                    if 'ERROR' in output:
                        if 'Enclosure already exists in the domain' in output:
                            logger._log_to_console_and_log_file("WARN: It appears that the enclosure you are trying to import already exists in the domain. This command is ignored and test will continue.")
                            noWait=True
                        elif 'Enclosure not imported, No enclosures currently exist in the domain' in output and 'delete domain' in command:
                            logger._log_to_console_and_log_file("WARN: It appears that you are trying to delete a domain that does not exist. This command is ignored and test will continue.")
                            noWait=True
                        elif 'Enclosure not imported, No enclosures currently exist in the domain' in output and 'poweroff server' in command:
                            logger._log_to_console_and_log_file("WARN: It appears that you are trying to poweroff server when domain does not exist. This command is ignored and test will continue.")
                        else:
                            raise RuntimeError(self.msg)

        except Exception as e:
            raise Exception(e)
        if 'delete domain' in command and noWait is False:
            logger._log_to_console_and_log_file("DEBUG: Delete domain successful. Sleeping %s seconds now..." % waitTime)
            sleep(waitTime)
        return output

    def copy_file(self, sfileName, dfileName):
        try:
            sFile = open(sfileName)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.credentials['ipAddress'], username=self.credentials[
                        'username'], password=self.credentials['password'])
            self.sftp = ssh.open_sftp()
            self.sftp.putfo(sFile, dfileName)
            sFile.close()
            self.sftp.close()
        except Exception as e:
            self.msg = "Exception %s while trying to ftp file " % e
            raise Exception(self.msg, e)

    def reconnect(self):
        return self.connect()

    def disconnect(self):
        self.client.close()
        self._connected = False
