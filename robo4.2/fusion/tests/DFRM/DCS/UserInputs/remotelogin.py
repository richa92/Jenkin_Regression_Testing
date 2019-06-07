#!/usr/bin/python


import re
import os
import sys
import paramiko
from robot.api import logger


class SSHUtils:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.ssh_obj = None
        self.sftp_obj = None

    def generate_local_rsa(self):
        #local_cmd = LocalCMDUtils()
        if not os.path.isfile(os.path.expanduser(os.path.join("~", ".ssh", "id_rsa"))):
            ret = os.system("ssh-keygen -t rsa -f `realpath ~/.ssh/id_rsa` -N ''")
            if ret != 0:
                logger.error("There is an error generating ssh rsa keys.")
                exit(-1)

    def setup_passwordless_ssh(self):
        import pexpect
        child = pexpect.spawn('ssh-copy-id %s@%s' %(self.user, self.host))
        try:
            index = child.expect(['(yes/no)', 'password:', pexpect.EOF])
            if index == 0:
                child.sendline("yes")
                if child.expect(['password:', pexpect.EOF]) == 0:
                    child.sendline(self.password)
                    if child.expect(['password:', pexpect.EOF]) == 0:
                        logger.error("Inside index=0. Wrong password provided for host %s" % self.host)
                        exit(-1)
            elif index == 1:
                child.sendline(self.password)
                if child.expect(['password:', pexpect.EOF]) == 0:
                    logger.error("Inside index=0. Wrong password provided for host %s" % self.host)
                    exit(-1)
            elif index == 2:
                if re.search("All keys were skipped because they already exist on the remote system",
                             child.before) is not None:
                    logger.info("Passwordless ssh already setup for host %s" % self.host)
                else:
                    logger.error("Inside index=1. There is some error using ssh-copy-id for host %s" % self.host)
                    exit(-1)
            else:
                logger.error("There is some error using ssh-copy-id for host %s" % self.host)
                exit(-1)
        except:
            e = sys.exc_info()[0]
            logger.error("Failed passwordless ssh setup (%s)" % e)

    def ssh_connect(self):
        if self.ssh_obj is None:
            self.ssh_obj = paramiko.SSHClient()
            self.ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                self.ssh_obj.connect(self.host, username=self.user , password=self.password)
            except (paramiko.ssh_exception.AuthenticationException,
                    paramiko.ssh_exception.SSHException):
                self.generate_local_rsa()
                self.setup_passwordless_ssh()
                try:
                    self.ssh_obj.connect(self.host, username=self.user)
                except:
                    e = sys.exc_info()[0]
                    logger.error("Failed ssh connect (%s)" % e)
            except:
                e = sys.exc_info()[0]
                logger.error("Failed ssh connect (%s)" % e)

    def remote_ssh(self, command):
        self.ssh_connect()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh_obj.exec_command(command)
        exit_status = ssh_stdout.channel.recv_exit_status()
        if ssh_stderr.read() or exit_status != 0:
            logger.error("Error in running command %s" % command)
            return 1
        return 0

    def remote_ssh_output(self, command):
        self.ssh_connect()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh_obj.exec_command(command)
        exit_status = ssh_stdout.channel.recv_exit_status()
        if ssh_stderr.read() or exit_status != 0:
            logger.error("Error in running command %s" % command)
            return None
        return ssh_stdout.read()

    def remote_get_sftp(self, local_path, remote_path):
        self.ssh_connect()
        if self.sftp_obj is None:
            self.sftp_obj = self.ssh_obj.open_sftp()
        try:
            self.sftp_obj.get(local_path, remote_path)
        except Exception as e:
            logger.error("Error in sftp.get (%s)" % e)

    def remote_put_sftp(self, local_path, remote_path):
        self.ssh_connect()
        if self.sftp_obj is None:
            self.sftp_obj = self.ssh_obj.open_sftp()
        try:
            self.sftp_obj.put(local_path, remote_path)
        except Exception as e:
            logger.error("Error in sftp.put (%s)" % e)

    def __del__(self):
        if self.sftp_obj is not None:
            self.sftp_obj.close()
        if self.ssh_obj is not None:
            self.ssh_obj.close()
