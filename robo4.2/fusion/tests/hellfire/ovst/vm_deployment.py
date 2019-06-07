from pysphere import VIServer
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

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
LOG = logging.getLogger("AutoDeployVMs")


# Parameters ######################################
app_count = 10
vc_ip = "10.10.0.62"
vc_username = "Administrator@vsphere.local"
vc_password = "Hellfire!234"
datastore = "VOLUME_VSA20"
host_ip = "hellfirecluster123"
app_name = "Hellfire_OVST_VM"
network = "mgmtVMNetwork"
network_name = "mgmt"
ovaloc = "http://10.10.0.130/OVST_OV/OVST_VM_OVA/RedHatCPULoad.ova"
http_proxy = "web-proxy.houston.hpecorp.net:8080"
datacenter = "DCV"


def connect_host(host, user, pswd):
    server = VIServer()
    try:
        server.connect(host, user, pswd)
        LOG.info("Connected to %s %s", server.get_server_type(), host)
        return server
    except:
        print "unable to connect to host: " + host + " error message: "


def get_appliance_IP(appliance_name):
    try:
        server_con = connect_host(vc_ip, vc_username, vc_password)
        vm = server_con.get_vm_by_name(appliance_name)
        if vm:
            ip = vm.get_property('ip_address', from_cache=False)
            return ip, True
    except:
            print "VM %s not found" % appliance_name


def deploy_appliance(appname):
    if vc_username.find('@') != -1:
        user = vc_username
        res = user.split('@')
        username = res[1] + '%5c' + res[0]
    else:
        username = vc_username
    ovftool_loc = "c:/progra~1/vmware/vmware~2/ovftool.exe"
    if 'http' in ovaloc:
        cmd = ovftool_loc + ' --noSSLVerify --proxy=%s -ds=\"%s\" --powerOn -n=%s -dm=thin  --net:\"%s\"=\"%s\"  %s vi://%s:%s@%s/%s/host/%s' % (http_proxy, datastore, appname, network, network_name, ovaloc, username, vc_password, vc_ip, datacenter, host_ip)
    else:
        cmd = ovftool_loc + ' --noSSLVerify -ds=\"%s\"  --powerOn -n=%s  %s vi://%s:%s@%s/%s/host/%s' % (datastore, appname, ovaloc, username, vc_password, vc_ip, datacenter, host_ip)
    LOG.info("Deploying Appliance %s on host %s in Vcenter %s", appname, host_ip, vc_ip)
    print "cmd is: ", cmd
    deploy = os.system(cmd)


def execute_automation_script(ipaddr, script_cmd):
    LOG.info("Executing Automation test script...")
    newcmd = script_cmd % (ipaddr)
    os.system(newcmd)


def invoke_process(appname):
    deploy_appliance(appname)


class myThread(threading.Thread):
    def __init__(self, appname):
        threading.Thread.__init__(self)
        self.name = appname

    def run(self):
        print "Starting " + self.name
        invoke_process(self.name)
        print "Exiting " + self.name


def main():
    LOG.info("Invoking Main method")
    LOG.info("Spawning %s deployment threads", app_count)
    for i in xrange(app_count):
        tn = 'thread_' + str(i + 1)
        print tn
        an = app_name + "_" + str(i + 1)
        tn = myThread(an)
        tn.start()
