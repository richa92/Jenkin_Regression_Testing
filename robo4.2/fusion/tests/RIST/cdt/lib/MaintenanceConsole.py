from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.api.deco import keyword

import sys
import os
import time
import paramiko


def block_no_keyword_warn():
    # this provides a keyword so RoboGalaxy doesn't issue a warning
    # stating "No Keyword found"
    # this is a no-op keyword
    pass


class MaintenanceConsole(object):

    def __init__(self):
        self.username = ""
        self.userpw = ""
        self.node = ""
        self.client = None
        self.session = None

    @keyword(name="execute maintenance login")
    def execute_maintenance_login(self, hostname, timeout=15):
        self.node = hostname
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        logger._log_to_console_and_log_file("Hostname is {0}".format(self.node))
        connect_args = {}
        connect_args['hostname'] = self.node
        connect_args['username'] = "maintenance"
        connect_args['password'] = ""
        connect_args['allow_agent'] = False
        connect_args['look_for_keys'] = False
        connect_args['timeout'] = timeout
        logger._log_to_console_and_log_file("connect args {!s}"
                                            .format(connect_args))
        self.client.connect(**connect_args)
        self.open_session()

    def open_session(self, timeout=45):
        self.session = (self.client.get_transport()).open_session()
        self.session.setblocking(0)  # Set to non-blocking mode
        self.session.get_pty()
        self.session.invoke_shell()

    @keyword(name="execute_user_login")
    def execute_user_login(self, username="Administrator", userpw="hpvse123"):
        self.username = username
        self.userpw = userpw
        self.send_response("{!s}\t".format(username))
        self.send_response("{!s}\t".format(userpw))
        self.send_response("\n")

    @keyword(name="send response")
    def send_response(self, cmdstr):
        # execute command
        logger._log("{!s}\n  Command: {!s} \n{!s}\n".format(
            ("=" * 40), cmdstr, ("=" * 40)))

        self.session.send(cmdstr)

    @keyword(name="read data")
    def read_data(self, timeout=45):
        s = ''
        t_end = time.time() + timeout
        while time.time() < t_end:
            if self.session.recv_ready():
                break
            time.sleep(1)
        if time.time() >= t_end:  # we timed out, process never exited
            logger._log_to_console_and_log_file(
                "Command did not complete within timeout.")
            retcode = -1
        else:
            s = self.session.recv(4096)
        return s

    @keyword(name="login exit")
    def login_exit(self, timeout=15):
        logger._log("\n{!s} END {!s}\n".format(("=" * 20), ("=" * 20)))
        self.client.close()
