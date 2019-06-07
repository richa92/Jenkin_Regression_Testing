#!/usr/local/bin/python
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
# from resources import resources
import logging
import sys
from time import sleep

from RoboGalaxyLibrary.utilitylib import logging as logger

from vcutils import switch, Timer, Timeout
from mrgvcinterface import Interface


libLogger = "api-logger"

# This is the VirtualConnect Simulator Class


class VirtualConnectSim():

    def __init__(self, credentials):
        self._log = logging.getLogger(libLogger)
        self._credentials = credentials
        self._root_credentials = {}
        self._root_credentials['ipAddress'] = credentials['vcmIpAddress']
        self._root_credentials['username'] = credentials['sshUsername']
        self._root_credentials['password'] = credentials['sshPassword']
        self._interface = Interface(self._root_credentials)

        self._dev_dir = '/usr/local/vcm/bin'
        self._data_dir = '/data/home/vcm'

        self._vcmd_grep_com = 'ps -ef | grep vcmd | grep -v grep'
        self._vcmd_pgrep_com = 'pgrep vcmd'
        self._copy_vc_sim_file()
        self._logger = logger

    def send_command(self, command):
        self._command = command
        self._interface.send_command(self._command)

    def _start_vc_sim(self):

        command = self._dev_dir + '/startVcSim.sh &'
        self._interface.send_command_no_wait(command)

    def _stop_vc_sim(self):

        command = self._dev_dir + '/stopVcSim.sh &'
        self._interface.send_command_no_wait(command)

    def delete_domain(self):

        self._stop_vc_sim()
        command = 'rm -Rf /tmp/*'
        self._interface.send_command_no_wait(command)
        self._start_vc_sim()
        sleep(2)

    def _copy_vc_sim_file(self):

        destFileName = self._dev_dir + '/startVcSim.sh'
        self._interface.copy_file('startVcSim.sh', destFileName)
        command = 'chmod +x '
        self._interface.send_command_no_wait(command + destFileName)
        destFileName = self._dev_dir + '/stopVcSim.sh'
        self._interface.copy_file('stopVcSim.sh', destFileName)
        self._interface.send_command_no_wait(command + destFileName)

    def _remove_vc_sim_files(self):

        destFileName = self._dev_dir + '/env.var'
        command = 'rm ' + destFileName
        self.interface.send_command_no_wait(command)
        destFileName = self._dev_dir + '/startVcSim.sh'
        command = 'rm ' + destFileName
        self._interface.send_command_no_wait(command)

    def _config_vc_sim(self, config):

        with open(config, 'r') as f:
            data = f.read()
        f.close
        line = data.split('\n')
        for filename in line:
            if filename.find('base') != -1:
                baseFile = filename
            if filename.find('profiles') != -1:
                profilesFile = filename

        library = 'export LD_LIBRARY_PATH=/usr/local/vcm/lib:/usr/local/vcmsupport/lib;'
        vcli_login = 'export vcli_username=Administrator; export vcli_password=Administrator;'
        vcli = self._dev_dir + '/vcli '
        find_enclosure = 'find enclosure local pw=pw ip=1.1.1.1 un=un'
        import_enclosure = 'import enclosure enc0'
        import_base = 'import base na file=' + baseFile
        import_profile = 'import profiles na file=' + profilesFile
        vcli_command = library + vcli_login + vcli

        command = vcli_command + find_enclosure
        self._interface.send_command_no_wait(command)
        sleep(1)
        command = vcli_command + import_enclosure
        self._interface.send_command_no_wait(command)
        sleep(1)
        command = vcli_command + import_base
        self._interface.send_command_no_wait(command + '>/dev/null 2>&1')
        sleep(1)
        command = vcli_command + import_profile
        self._interface.send_command_no_wait(command + '>/dev/null 2>&1')
        sleep(10)
        print('breakpoint')

    def config_vc(self, config, oa_credentials):

        self.delete_domain()
        self._config_vc_sim(config)
        print('Breakpoint')

    def close(self):
        self._interface.__delete__()

    def reconnect(self):
        if self._interface is None:
            self.interface = Interface(self._credentials)

# This is the Virtual Connect Enclosure Class


class VirtualConnectEnc():

    def __init__(self, credentials):
        self._log = logging.getLogger(libLogger)
        self._credentials = credentials
        self._interface = Interface(credentials)
        self._timer = Timer()
        self._command = ''
        self._temp_config_file = 'temp-config.txt'
        self._logger = logger

    def send_command(self, command):
        self._command = command
        self._interface.send_command(self._command, True)

    def _config_vc_enc(self, config, oa_credentials, import_domain, verbose, doubleDense):
        configFile = config
        self._logger._log_to_console('Configuring Virtual Connect please wait ')
        if import_domain is True:
            if doubleDense is True:
                self._command = 'import enclosure username=' + oa_credentials['oaUsername'] + ' password=' + oa_credentials['oaPassword'] + ' DoubleDense=true' + '\n'
            else:
                self._command = 'import enclosure username=' + oa_credentials['oaUsername'] + ' password=' + oa_credentials['oaPassword'] + '\n'
            self._interface.send_command(self._command, verbose)
        if config is not None:
            fo = open(configFile, "r+")
            for line in fo:
                command = line.split(' ')
                for case in switch(command[0]):
                    if case('add'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('assign'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('unassign'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('copy'):
                        pass
                    if case('delete'):
                        pass
                    if case('exit'):
                        pass
                    if case('help'):
                        pass
                    if case('import'):
                        pass
                    if case('load'):
                        pass
                    if case('poweroff'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('poweron'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('reboot'):
                        pass
                    if case('remove'):
                        pass
                    if case('reset'):
                        pass
                    if case('restore'):
                        pass
                    if case('save'):
                        pass
                    if case('set'):
                        self._interface.send_command(line, verbose)
                        continue
                    if case('show'):
                        pass
                    if case('start'):
                        pass
                    if case('stop'):
                        self._interface.send_command(line, verbose)
                        sys.stdout.write('.')
                        break
                    if case():
                        pass  # default
            fo.close()
    print("")

    def config_vc(self, config, oa_credentials, import_domain, verbose, doubleDense):
        self._config_vc_enc(config, oa_credentials, import_domain, verbose, doubleDense)

    def delete_domain(self, waitTime=120):
        self._interface.send_command('poweroff server * -force', False)
        self._interface.send_command('delete domain -quiet', False, waitTime)
        timer = Timer('delete domain', 3600)
        timer.start()
        self._interface.disconnect()
        while True:
            sleep(60)
            try:
                timer.elapse()
                self._logger._log_to_console_and_log_file("Attempting to reconnect...")
                if self.reconnect():
                    break
            except Timeout as e:
                self._msg = "Timeout"
                self._log.error(self._msg)
                raise Exception(self._msg, e)
            timer.stop()

    def get_config(self, fileName):
        output = self._interface.send_command('show config', True)
        lines = output.split('\n')
        fo = open(fileName, "wb+")
        for line in lines:
            fo.write(line + '\n')
        fo.close()

    def show_interconnect(self, bayNumber):
        icmCmd = 'show interconnect ' + bayNumber + '\n'
        output = self._interface.send_command(icmCmd, True)
        lines = output.split('\n')
        return lines

    def close(self):
        self._interface.disconnect()

    def reconnect(self):
        if self._interface is None:
            self._interface = Interface(self._credentials)
            return self._interface.connect()
        else:
            return self._interface.reconnect()
