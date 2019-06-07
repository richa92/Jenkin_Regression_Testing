#!/usr/local/bin/python
# #############################################################################
# OneView Component Logging Level Adjuster
# logLevels.py
# Author: Russell N. Briggs 09/01/2013
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
# >
import argparse
import json
import pprint
import requests
import string
# import pdb
from requests.auth import AuthBase


class CicAuth(AuthBase):

    def __init__(self, sessionid):
        self.sessionid = sessionid

    def __call__(self, r):
        r.headers['auth'] = self.sessionid

        return r


class LoginSession(object):

    def __init__(self, ip, uname, pw):
        self.ip = ip
        self.uname = uname
        self.pw = pw

    def post(self):

        # pdb.set_trace()
        data = {'userName': self.uname, 'password': self.pw}
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json', 'X-API-Version': 3}
        sessionUrl = string.Template("https://$ip/rest/login-sessions")
        sessionUrl = sessionUrl.substitute(ip=self.ip)

        try:
            resp = requests.post(sessionUrl, data=json.dumps(data), headers=headers, verify=False)
        except Exception as x:
            msg = "Exception occured while attempting to authenticate user\
                  '%s', password '%s', at IP '%s'" % (self.uname, self.pw, self.ip)
            raise Exception(msg, e)

        if resp.status_code != 200:
            msg = "Status %d received from a login-sessions POST for user '%s', password '%s', at IP '%s', %s " % (resp.status_code, self.uname, self.pw, self.ip, resp.text)
            raise Exception(msg)
        else:
            return resp.json()


class ExecRequest(object):

    def __init__(self, ip, sessionId):
        self.ip = ip
        self.sessionId = CicAuth(sessionId)

    def get_logger_levels(self):
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json', 'X-API-Version': 3}
        sessionUrl = string.Template("https://$ip/logs/rest/debug")
        sessionUrl = sessionUrl.substitute(ip=self.ip)

        try:
            resp = requests.get(sessionUrl, auth=self.sessionId, headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to execute the request '%s'" \
                % (reqBody)
            raise Exception(msg, e)

        if resp.status_code != 200:
            msg = "Status %d received from execute request %s : headers = %s body = %s text = %s" \
                % (resp.status_code, sessionUrl, headers, reqBody, resp.text)
            raise Exception(msg)
        else:
            pprint.pprint(resp.json(), width=200)

    def set_logger_level(self, reqBody):
        data = reqBody
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json', 'X-API-Version': 3}
        sessionUrl = string.Template("https://$ip/logs/rest/debug")
        sessionUrl = sessionUrl.substitute(ip=self.ip)

        try:
            r = requests.post(sessionUrl, auth=self.sessionId, data=json.dumps(data), headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to execute the request '%s'" \
                % (reqBody)
            raise Exception(msg, e)

        if r.status_code != 200:
            msg = "Status %d received from execute request %s : headers = %s body = %s text = %s" \
                % (r.status_code, sessionUrl, headers, reqBody, resp.text)
            raise Exception(msg)
        else:
            print r

    def delete_logger_level(self, reqBody):
        data = reqBody
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json', 'X-API-Version': 3}
        sessionUrl = string.Template("https://$ip/logs/rest/debug")
        sessionUrl = sessionUrl.substitute(ip=self.ip)

        try:
            r = requests.delete(sessionUrl, auth=self.sessionId, data=json.dumps(data), headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to execute the request '%s'" \
                % (reqBody)
            raise Exception(msg, e)

        if r.status_code != 200:
            msg = "Status %d received from execute request %s : headers = %s body = %s text = %s" \
                % (r.status_code, sessionUrl, headers, reqBody, resp.text)
            raise Exception(msg)
        else:
            print r


def getCmdLineParam():
    parser = argparse.ArgumentParser(description="logLevels.py is used to configure the component logging levels on a Fusion appliance using ReST calls.")
    parser_parent = argparse.ArgumentParser(add_help=False)
    parser_parent.add_argument("-u", "--user", "--u", dest="user", help="The OneView user.  Defaults to Administrator", default="Administrator")
    parser_parent.add_argument("-p", "--password", "--p", dest="password", help="The OneView user's password.", required=True)
    parser_parent.add_argument("-a", "--a", "--appliance", dest="appliance", help="The IP or DNS name of the OneView appliance", required=True)
    subparsers = parser.add_subparsers(title='subcommands')
    # DELETE
    parser_set = subparsers.add_parser('delete', parents=[parser_parent], help="This subcommand is used to delete a logger.")
    parser_set.add_argument("-lo", "--lo" "--logger", dest="logger", help="The logger to delete or change", required=True)
    parser_set.add_argument("-le", "--le" "--level", dest="level", help="The logger level",
                            choices=['INFO', 'ERROR', 'DEBUG', 'WARN', 'OFF'], required=True)
    parser_set.set_defaults(func=delete)
    # SET
    parser_set = subparsers.add_parser('set', parents=[parser_parent], help="This subcommand is used to add or update logger levels.")
    parser_set.add_argument("-lo", "--lo" "--logger", dest="logger", help="The logger to add or change", required=True)
    parser_set.add_argument("-le", "--le" "--level", dest="level", help="The desired logger level",
                            choices=['INFO', 'ERROR', 'DEBUG', 'WARN', 'OFF'], required=True)
    parser_set.set_defaults(func=set)
    # LIST
    parser_list = subparsers.add_parser('list', parents=[parser_parent], help="This subcommand is used to list the logging levels.")
    parser_list.set_defaults(func=list)

    args = parser.parse_args()
    args.func(args)


def login(args):
    try:
        curSession = LoginSession(ip=args.appliance, uname=args.user, pw=args.password)
        response = curSession.post()
        authToken = response['sessionID']
        return authToken

    except Exception as e:
        msg = "An unhandled exception occurred."
        raise Exception(msg, e)


def delete(args):
    try:
        authToken = login(args=args)
        requestBase = ExecRequest(ip=args.appliance, sessionId=authToken)
        data = {'level': args.level, 'scope': 'COMPONENT', 'loggerName': args.logger}
        requestBase.delete_logger_level(reqBody=data)

    except Exception as e:
        msg = "An unhandled exception occurred."
        raise Exception(msg, e)


def set(args):
    try:
        authToken = login(args=args)
        requestBase = ExecRequest(ip=args.appliance, sessionId=authToken)
        data = {'level': args.level, 'scope': 'COMPONENT', 'loggerName': args.logger}
        requestBase.set_logger_level(reqBody=data)

    except Exception as e:
        msg = "An unhandled exception occurred."
        raise Exception(msg, e)


def list(args):
    try:
        authToken = login(args=args)
        requestBase = ExecRequest(ip=args.appliance, sessionId=authToken)
        requestBase.get_logger_levels()

    except Exception as e:
        msg = "An unhandled exception occurred."
        raise Exception(msg, e)


def main():
    getCmdLineParam()

if __name__ == "__main__":
    main()
