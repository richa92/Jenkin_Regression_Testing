import os
import httplib
import httplib2
import sys
import json
import datetime
import time
import logging
import subprocess
import threading
import RoboGalaxyLibrary
import FusionLibrary
from RoboGalaxyLibrary import iLOKeywords
from robot.libraries.BuiltIn import BuiltIn
import data_variables_hellfire_ovst

app_name = "OS_deployment_"


def deploy_os(host_ilo):
    ilo_obj = iLOKeywords()
    iLOKeywords.ilo_connect(ilo_obj, host_ilo['ilo_ip'], host_ilo['username'], host_ilo['password'])
    iLOKeywords.ilo_set_host_power(ilo_obj, host_power=True)
    iLOKeywords.ilo_insert_virtual_media(ilo_obj, host_ilo['device'], host_ilo['image_url'])
    iLOKeywords.ilo_set_virtual_media_status(ilo_obj)
    iLOKeywords.ilo_set_one_time_boot(ilo_obj, host_ilo['device'])
    iLOKeywords.ilo_cold_boot_server(ilo_obj)
    time.sleep(900)


class OsDeploymentThread(threading.Thread):
    def __init__(self, name, *args):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args

    def run(self):
        hostilo = self.args
        hostilolist = list(hostilo)
        for i in hostilolist:
            deploy_os(i)


def deploy():
    host_ilos = []
    input_host_ilos = BuiltIn().get_variable_value("${ilo_ips}")
    for i in input_host_ilos:
        host_ilos.append(i)
    app_count = len(host_ilos)
    i = 0
    for ilo in host_ilos:
        i += 1
        tn = 'thread_' + str(i)
        an = app_name + tn
        tn = OsDeploymentThread(an, ilo)
        tn.start()
