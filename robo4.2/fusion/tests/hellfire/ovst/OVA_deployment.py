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
import atexit
import argparse
from pyVmomi import vim, vmodl
from pyVim import connect
from pyVim.connect import Disconnect, SmartConnect
import paramiko


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
LOG = logging.getLogger("AutoDeploy")
# Parameters ######################################
IP_Proto = "static"       # dhcp or static
vc_ip = "10.10.0.62"
vc_username = "Administrator@vsphere.local"
vc_password = "Hellfire!234"
vc_port = 443
datastore = "QA-JS1-DataStore-1"
host_ip = "10.10.0.36"
app_name = "OneViewHellfireOvst"
http_proxy = "web-proxy.houston.hpecorp.net:8080"
datacenter = "JumpStation-DC"
####################################################
# Debug Logging
####################################################
# debug_log = True
debug_log_resources = ['\t<logger name="com.hp.ci.mgmt.clrm" level="TRACE" />\n']
root_user = "root"
root_password = "hpvse1"
####################################################
# Static Appliance IP Parameters
####################################################
app_ipaddr = "10.10.4.181"
netmask = "255.255.192.0"
gateway = "10.10.0.1"
hostname = "autoapp.hpe.com"

####################################################


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


def deploy_appliance(appname, ovaloc, ovf_network, network, waitForIp=True):
    if vc_username.find('@') != -1:
        user = vc_username
        res = user.split('@')
        username = res[1] + '%5c' + res[0]
    else:
        username = vc_username
    ovftool_loc = "c:/progra~1/vmware/vmware~2/ovftool.exe"
    if 'http' in ovaloc:
        if waitForIp is True:
            cmd = ovftool_loc + ' --noSSLVerify -ds=\"%s\" --powerOn --X:waitForIp -n=%s -dm=thin  --net:\"%s\"=\"%s\"  %s vi://%s:%s@%s/%s/host/%s' % (datastore, appname, ovf_network, network, ovaloc, username, vc_password, vc_ip, datacenter, host_ip)
        else:
            cmd = ovftool_loc + ' --noSSLVerify -ds=\"%s\" --powerOn -n=%s -dm=thin  --net:\"%s\"=\"%s\"  %s vi://%s:%s@%s/%s/host/%s' % (datastore, appname, ovf_network, network, ovaloc, username, vc_password, vc_ip, datacenter, host_ip)
    else:
        cmd = ovftool_loc + ' --noSSLVerify -ds=\"%s\"  --powerOn --X:waitForIp -n=%s  %s vi://%s:%s@%s/%s/host/%s' % (datastore, appname, ovaloc, username, vc_password, vc_ip, datacenter, host_ip)
    LOG.info("Deploying Appliance %s on host %s in Vcenter %s", appname, host_ip, vc_ip)
    print "cmd is: ", cmd
    deploy = os.system(cmd)


def connect_to_host_and_get_vm(host, user, pswd, vm_name):
    """
     Connect to vcenter and Get the vm associated with a given text name
    """
    app_vm = None
    server_con = connect_host(host, user, pswd)
    app_vm = server_con.get_vm_by_name(vm_name)
    return app_vm


def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj


def wait_for_task(task):
    """
    Waits for vSphere task
    """
    task_done = False
    while not task_done:
        if task.info.state == 'success':
            return task.info.state
        if task.info.state == 'error':
            raise AssertionError("Failed to complete task, error = %s" % task.info.error)


def vm_customization(appname, vc_ip, vc_port, vc_username, vc_password, net_details, isDHCP=None):
        service_instance = connect.Connect(vc_ip, vc_port, vc_username, vc_password)
        content = service_instance.RetrieveContent()
        lst = []
        vm = get_obj(content, [vim.VirtualMachine], appname)
        if vm.runtime.powerState != 'poweredOff':
            raise AssertionError("WARNING:: Power off your VM before reconfigure Vm Name= %s" % appname)
        globalip = vim.vm.customization.GlobalIPSettings()
        customspec = vim.vm.customization.Specification()
        for net in net_details:
            adaptermap = vim.vm.customization.AdapterMapping()
            adaptermap.adapter = vim.vm.customization.IPSettings()
            if not isDHCP:
                """Static IP Configuration"""
                adaptermap.adapter.ip = vim.vm.customization.FixedIp()
                adaptermap.adapter.ip.ipAddress = net[0]
                adaptermap.adapter.subnetMask = net[1]
                adaptermap.adapter.gateway = net[2]
                globalip.dnsServerList = net[3][0]
            else:
                """DHCP Configuration"""
                adaptermap.adapter.ip = vim.vm.customization.DhcpIpGenerator()
            adaptermap.adapter.dnsDomain = net[4]
            lst.append(adaptermap)
        ident = vim.vm.customization.LinuxPrep(domain=net_details[0][4], hostName=vim.vm.customization.FixedName(name=appname))
        customspec.identity = ident
        customspec.nicSettingMap = lst
        customspec.globalIPSettings = globalip
        task = vm.Customize(spec=customspec)
        return wait_for_task(task)


def create_network_file():
    file_eth0 = open("ifcfg-eth0", 'w')
    file_eth0.write("DEVICE='eth0'\nONBOOT='yes'\nUSERCTL='no'\nBOOTPROTO='static'\nDEFROUTE='yes'\nPEERDNS='no'\nRABBIT_LISTENING='false'\nPOSTGRES_LISTENING='false'\nPEER_IPADDR='127.0.0.1'\nIPV6INIT='no'\nNAME='" + app_name + "'\nSTATIC_HOSTNAME='" + hostname + "'\nIPADDR='" + app_ipaddr + "'\nNETMASK='" + netmask + "'\nGATEWAY='" + gateway + "'")
    file_eth0.close()
    time.sleep(5)


def add_debug_logging(app_ip):
    transport = paramiko.Transport((app_ip, 22))
    transport.connect(username=root_user, password=root_password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    with sftp.open('/ci/etc/cilogback.xml') as fin, sftp.open('/ci/etc/cilogback_copy.xml', 'w') as fout:
        for line in fin:
            fout.write(line)
    with sftp.open('/ci/etc/cilogback_copy.xml') as fin, sftp.open('/ci/etc/cilogback.xml', 'w') as fout:
        for line in fin:
            if '</configuration>' in line:
                fout.write(debug_log_resources[0])
            fout.write(line)
    sftp.remove('/ci/etc/cilogback_copy.xml')


def ov_deploy_process(appname, ovaloc, ovf_network, network, ov_waitforip, net_details, debug_log):
    deploy_appliance(appname, ovaloc, ovf_network, network, ov_waitforip)
    if IP_Proto == "static":
        global app_ipaddr
        LOG.info("Entering Static IP Configuration ...")
        time.sleep(30)
        server_con = connect_host(vc_ip, vc_username, vc_password)
        app_vm = server_con.get_vm_by_name(appname)
#        LOG.info("Logging into the Appliance and updating network config file...")
#        time.sleep(5)
#        app_vm.login_in_guest("root", "hpvse1")
#        time.sleep(5)
#        create_network_file()
#        time.sleep(5)
#        app_vm.send_file("ifcfg-eth0", "/etc/sysconfig/network-scripts/ifcfg-eth0", overwrite=True)
#        time.sleep(5)
#        LOG.info("Power cycle the Appliance...")
        app_vm.power_off()
        time.sleep(10)
        vm_customization(appname, vc_ip, vc_port, vc_username, vc_password, net_details)
        app_vm.power_on()
        LOG.info("Appliance Powered ON...")
        LOG.info("Waiting for Appliance to start...")
        time.sleep(800)
        if debug_log is True:
            add_debug_logging(app_ipaddr)

    elif IP_Proto == 'dhcp':
        LOG.info("Entering DHCP IP Configuration ... ")
        LOG.info("Waiting for Appliance to start...")
        time.sleep(800)
        app_ipaddr = get_appliance_IP(appname)
        LOG.info("IP Addr of the appliance: %s", app_ipaddr)
        if debug_log is True:
            add_debug_logging(app_ipaddr)
