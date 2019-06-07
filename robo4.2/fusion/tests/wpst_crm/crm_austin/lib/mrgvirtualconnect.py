#!/usr/local/bin/python
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
import logging
import time

from RoboGalaxyLibrary.utilitylib import logging as logger

from tests.wpst_crm.crm_austin.lib.mrgvcimplementation import VirtualConnectEnc, VirtualConnectSim
from oamodule import InterconnectsBase
from vcutils import Timer


libLogger = "api-logger"
# This class represents the Virtual Connect Module
# and provides implementation independent interface


class VirtualConnect():
    timer = 0
    simulator = 'False'

    def __init__(self, vc_credentials, oa_credentials):
        self._log = logging.getLogger(libLogger)
        # Disable support for VC simulator for now
        self._sim = vc_credentials.get('sim')
        if self._sim is None:
            self._sim = 'False'
        self._vc_credentials = vc_credentials
        self._oa_credentials = oa_credentials
        self._msg = ''
        self._timer = Timer()
        self._logger = logger
        # VirtualConnect.simulator = self._sim
        try:
            if self._sim == 'True':
                # VirtualConnect.timer = vc_credentials['timer']
                self._vc = VirtualConnectSim(vc_credentials)
            else:
                vc_credentials['ipAddress'] = vc_credentials['vcmIpAddress']
                vc_credentials['username'] = vc_credentials['vcmUsername']
                vc_credentials['password'] = vc_credentials['vcmPassword']
                self._logger._log_to_console_and_log_file("Connecting to VC {0}".format(vc_credentials['ipAddress']))
                self._vc = VirtualConnectEnc(vc_credentials)
        except Exception as e:
            self._msg = "Unable to create Virtual Connect Implementation"
            self._log.error(self._msg)
            raise Exception(self._msg, e)

    @classmethod
    def sleep(cls):
        if cls.simulator:
            time.sleep(float(cls.timer))

    def get_config_vc(self):
        fileName = 'config.txt'
        self._vc.get_config(fileName)

    def show_interconnect_module(self, bayNumber):
        return self._vc.show_interconnect(bayNumber)

    def config_virtual_connect(self, config, import_domain, verbose, doubleDense):
        self._logger._log_to_console_and_log_file("Configuring VC please wait...")
        try:
            if self._sim == 'True':
                self._logger._log_to_console_and_log_file("Configuring VC Simulator, please wait...")
                self._vc.config_vc(config, self._oa_credentials)
            else:
                self._logger._log_to_console_and_log_file("Configuring VC Real, please wait...")
                self._vc.config_vc(config, self._oa_credentials, import_domain, verbose, doubleDense)
        except Exception as e:
            msg = "Unable to configure VC"
            self._log.error(msg)
            raise Exception(msg, e)
        self._logger._log_to_console_and_log_file("Configuring VC complete")
        # VirtualConnect.sleep()

    def clear_vc_mode(self, credentials):
        credentials['ipAddress'] = credentials['oaIpAddress']
        credentials['username'] = credentials['oaUsername']
        credentials['password'] = credentials['oaPassword']
        self._logger._log_to_console_and_log_file("Clearing VC Mode from OA {0}  ".format(credentials['ipAddress']))
        self.interconnect = InterconnectsBase(credentials['username'], credentials['ipAddress'], credentials['password'])
        self.interconnectList = self.interconnect.getList()

        if self.interconnectList:
            self._vc.close()
#            for interconnect in self.interconnectList:
            for index in range(1, 2):
                self.interconnect.clearInterconnectMode()
                self.interconnect.clearInterconnectMode()
                # self.interconnect.restartInterconnect(interconnect['bay'])
                # self.interconnect.efuseInterconnect(interconnect['bay'], 'OFF')
                # self.interconnect.efuseInterconnect(interconnect['bay'], 'ON')
        self._logger._log_to_console_and_log_file("VC Mode clear complete.")

    def reset_virtual_connect(self, credentials):
        credentials['ipAddress'] = credentials['oaIpAddress']
        credentials['username'] = credentials['oaUsername']
        credentials['password'] = credentials['oaPassword']
        self._logger._log_to_console_and_log_file("Resetting VC modules from OA {0}  ".format(credentials['ipAddress']))
        self.interconnect = InterconnectsBase(credentials['username'], credentials['ipAddress'], credentials['password'])
        self.interconnectList = self.interconnect.getList()

        if self.interconnectList:
            self._vc.close()
#            for interconnect in self.interconnectList:
            for index in range(1, 3):
                self.interconnect.reset_io(index)
                # self.interconnect.efuseInterconnect(index, 'OFF')
                # self.interconnect.efuseInterconnect(index, 'ON')
                # self.interconnect.restartInterconnect(interconnect['bay'])
                # self.interconnect.efuseInterconnect(interconnect['bay'], 'OFF')
                # self.interconnect.efuseInterconnect(interconnect['bay'], 'ON')
        self._logger._log_to_console_and_log_file("Reset of VC modules complete.")

    def restart_interconnect_module(self, credentials, bay):
        credentials['ipAddress'] = credentials['oaIpAddress']
        credentials['username'] = credentials['oaUsername']
        credentials['password'] = credentials['oaPassword']
        self._logger._log_to_console_and_log_file("Restarting interconnect {0} from OA {1}  ".format(bay, credentials['ipAddress']))
        self.interconnect = InterconnectsBase(credentials['username'], credentials['ipAddress'], credentials['password'])

        self.interconnect.restartInterconnect(bay)
        self._logger._log_to_console_and_log_file("Restart interconnect {1} from OA {1} complete.".format(bay, credentials['ipAddress']))

    def remove_virtual_connect(self, credentials, bay):
        if bay != 1:
            self.interconnect = InterconnectsBase(credentials['username'], credentials['ipAddress'], credentials['password'])
            interconnectList = self.interconnect.getList()
            self.interconnect.efuseInterconnect(bay, 'OFF')

    def insert_virtual_connect(self, credentials, bay):
        self.interconnect = InterconnectsBase(credentials['username'], credentials['ipAddress'], credentials['password'])
        interconnectList = self.interconnect.getList()
        self.interconnect.efuseInterconnect(bay, 'OFF')

    def delete_domain(self, waitTime=120):
        self._logger._log_to_console_and_log_file("Deleting VC Domain please wait...")
        self._vc.delete_domain(waitTime)
        self._logger._log_to_console_and_log_file("VC Domain delete complete...")
        self._vc.close()
