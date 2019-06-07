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


class InterconnectsBase(object):

    def __init__(self, uname, ip, pw):
        self.uname = uname
        self.ip = ip
        self.pw = pw

    def getList(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug('Creating temp file with prefix OA-interconnect')
            (fd, fname) = tempfile.mkstemp(prefix="OA-interconnect.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'show interconnect list'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        # NOTE: If the OA team changes their command output then this will break.
        # It's not suppossed to change though
        pattern = '  [1-8]'
        Interconnects = []
        for line in fd:
            matches = re.search(pattern, line)
            if matches:
                lineAttrDict = dict()
                lineAttr = line.split()
                if lineAttr[1] == '[Absent]':
                    continue
                else:
                    if lineAttr[1] == 'Fibre':
                        lineAttrDict['bay'] = lineAttr[0]
                        lineAttrDict['type'] = lineAttr[1]
                        lineAttrDict['manufacturer'] = lineAttr[3]
                        lineAttrDict['power'] = lineAttr[4]
                        lineAttrDict['health'] = lineAttr[5]
                        lineAttrDict['uid'] = lineAttr[6]
                        lineAttrDict['ip'] = lineAttr[7]
                        Interconnects.append(lineAttrDict)
                    else:
                        lineAttrDict['bay'] = lineAttr[0]
                        lineAttrDict['type'] = lineAttr[1]
                        lineAttrDict['manufacturer'] = lineAttr[2]
                        lineAttrDict['power'] = lineAttr[3]
                        lineAttrDict['health'] = lineAttr[4]
                        lineAttrDict['uid'] = lineAttr[5]
                        lineAttrDict['ip'] = lineAttr[6]
                        Interconnects.append(lineAttrDict)
            else:
                continue
        fd.close()

        return Interconnects

    def restartInterconnect(self, bay):
        log = logging.getLogger(libLogger)

        try:
            log.debug('Restarting interconnect %s' % (bay))
            command = string.Template("restart interconnect $bay")
            command = command.substitute(bay=bay)
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

            stdin, stdout, stderr = client.exec_command(command)
        except Exception as e:
            msg = "Exception occured while attempting to send ssh command %s" \
                % (command)
            raise Exception(msg, e)
        finally:
            client.close()

        return

    def clearInterconnectMode(self):
        log = logging.getLogger(libLogger)

        try:
            command = 'clear vc mode'
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

            # open channel to the OA
            chan = client.invoke_shell()
            time.sleep(10)
            chan.send(command + '\n')
            resp = chan.recv(999)
            print resp

        except Exception as e:
            msg = "Exception occured while attempting to send ssh command %s" \
                % (command)
            raise Exception(msg, e)
        finally:
            client.close()

        return

    def efuseInterconnect(self, bay, state):
        log = logging.getLogger(libLogger)

        try:
            log.debug('Enter diag mode on %s' % (self.ip))
            command = '++diag--'
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

            # open channel to the OA
            chan = client.invoke_shell()
            time.sleep(10)
            chan.send(command + '\n')
            resp = chan.recv(999)
            print resp

            log.debug('Send efuse %s to interconnect %s' % (state, bay))
            command = string.Template('efuse SWM $bay $state')
            command = command.substitute(bay=bay, state=state)
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

    def reset_io(self, bay):
        log = logging.getLogger(libLogger)

        try:
            log.debug('Enter diag mode on %s' % (self.ip))
            command = '++diag--'
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

            # open channel to the OA
            chan = client.invoke_shell()
            time.sleep(10)
            chan.send(command + '\n')
            resp = chan.recv(999)
            print resp

            log.debug('Send reset_io to interconnect %s' % bay)
            command = string.Template('reset_io $bay')
            command = command.substitute(bay=bay)
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

    def execute_diag_cmd(self, cmd, maxRetry=1, interval=1):
        log = logging.getLogger(libLogger)
        log.debug('Entering diag mode on %s' % (self.ip))
        command = '++diag--'
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        hostname = self.ip
        port = 22
 
        for x in range(maxRetry):
            try:
                client.connect(hostname, port=port, username=self.uname, password=self.pw)

                # open channel to the OA
                chan = client.invoke_shell()
                time.sleep(10)
                chan.send(command + '\n')
                resp = chan.recv(999)
                #print resp

                log.debug('Sending command to diag cli: %s' % cmd)
                command = string.Template('$cmd')
                command = command.substitute(cmd=cmd)
                time.sleep(10)
                chan.send(command + '\n')
                resp = chan.recv(999)
                print resp

                # exit  diag mode
                time.sleep(10)
                chan.send('q\n')
                resp = chan.recv(999)
                #print resp
                return True

            except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
                msg = "Exception occured while attempting to send ssh command %s" \
                    % (command)
                print msg
                print e
                sleep(interval)
            finally:
                client.close()

        return   False


class OaBase(object):

    def __init__(self, uname, ip, pw):
        self.uname = uname
        self.ip = ip
        self.pw = pw

    def getInfo(self):
        oaVer = '1.0'
        log = logging.getLogger(libLogger)

        try:
            log.debug('Creating temp file with prefix OA-info')
            (fd, fname) = tempfile.mkstemp(prefix="OA-info.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'show oa info'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        # NOTE: If the OA team changes their command output then this will break.
        # It's not suppossed to change though
        pattern = 'Firmware Ver.'
        Interconnects = []
        for line in fd:
            matches = re.search(pattern, line)
            if matches:
                lineAttr = line.split(':')
                oAver = lineAttr[1]
                oAver = oAver.rstrip('\n')
                oAver = oAver.lstrip()

            else:
                continue
        fd.close()

        return oAver


class OaStatus(object):

    def __init__(self, uname, ip, pw, bay):
        self.uname = uname
        self.ip = ip
        self.pw = pw
        self.bay = bay

    def getRole(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with prefix OA-status")
            (fd, fname) = tempfile.mkstemp(prefix="OA-status.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'show oa status %s' % (self.bay)
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        # NOTE: If the OA team changes their command output then this will break.
        # It's not suppossed to change though
        pattern = 'Role'
        roles = []
        for line in fd:
            matches = re.search(pattern, line)
            if matches:
                lineAttr = line.split(':')
                oArole = lineAttr[1]
                oArole = oArole.rstrip('\n')
                oArole = oArole.lstrip()
                roles.append(oArole)
            else:
                continue
        fd.close()
        return oArole


class OaFailover(object):

    def __init__(self, uname, ip, pw):
        self.uname = uname
        self.ip = ip
        self.pw = pw

    def getActiveOaIP(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with prefix OA-activeOaIP")
            (fd, fname) = tempfile.mkstemp(prefix="OA-activeOaIP.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'show oa network active'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        pattern = 'IPv4 Address'
        # JRT lineList = []
        for line in fd:
            matches = re.search(pattern, line)
            if matches:
                lineAttr = line.split(':')
                oaIP = lineAttr[1]
                # strip newline and leading space from IP
                oaIP = oaIP.rstrip('\n')
                oaIP = oaIP.lstrip()
            else:
                continue
            # JRT lineList.append(line)
            return oaIP

    # Force failover method for OA in Active state
    def forceFailOver(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with prefix OA-ForceFailover")
            (fd, fname) = tempfile.mkstemp(prefix="OA-ForceFailover.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'FORCE TAKEOVER'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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


class ActiveOA(object):

    def __init__(self, uname, ip, pw):
        self.uname = uname
        self.ip = ip
        self.pw = pw

    def getActiveOA(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with prefix OA-active")
            (fd, fname) = tempfile.mkstemp(prefix="OA-active.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = 'show oa network'
            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        activeOaList = []
        for line in fd:
            print line
            activeOaList.append(line)

        return activeOaList


class OASupportDump(object):

    def __init__(self, uname, ip, pw, ftpURL):
        self.uname = uname
        self.ip = ip
        self.pw = pw
        self.ftpURL = ftpURL

    def getOASupportDump(self):
        log = logging.getLogger(libLogger)

        try:
            log.debug("Creating temp file with prefix OA-Support-Dump")
            (fd, fname) = tempfile.mkstemp(prefix="OA-Support-Dump.")
        except Exception as e:
            msg = "Exception occured while attempting to create a temp file"
            raise Exception(msg, e)

        try:
            command = string.Template("upload supportdump ftp://$ftpURL")
            command = command.substitute(ftpURL=self.ftpURL)

            log.debug('Sending ssh command: %s, %s, %s, %s' % (self.uname, self.ip, self.pw, command))

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            hostname = self.ip
            port = 22
            client.connect(hostname, port=port, username=self.uname, password=self.pw)

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

        oaSupportDumpStatus = "Successful"
        return oaSupportDumpStatus
