"""
wrapper.py

Wrapper functions
"""
import paramiko
import socket
import sys


class wrapper(object):

    def __init__(self):
        self.sock = None
        self.cmd_channel = None
        self.session = None

    def cifit_open_connection(self, host, port=22):
        res = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE)
        family, socktype, proto, canonname, sockaddr = res[0]
        if '.' in host:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        else:
            self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        self.sock.connect((sockaddr))

    def cifit_login(self, username, password):
        self.session = paramiko.Transport(self.sock)
        self.session.start_client()
        self.session.auth_password(username, password)
        self.cmd_channel = self.session.open_session()

    def cifit_execute_command(self, command):
        self.cmd_channel.exec_command(command)
        data = self.cmd_channel.recv(4096)
        stdoutData = data
        while stdoutData:
            sys.stdout.write(stdoutData)
            stdoutData = self.cmd_channel.recv(4096)
        return data

    def cifit_close_connection(self):
        self.cmd_channel.close()
        self.session.close()
        self.sock.close()
