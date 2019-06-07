from os import system, path
from sys import exit
from threading import Thread
from time import sleep
from argparse import ArgumentParser
from getpass import getpass
import tarfile
import paramiko
import urllib
import os
import shutil
import time
from pyVim import connect
from pyVmomi import vim
import requests


def get_ovf_descriptor(ovf_path):
    """
    Read in the OVF descriptor.
    """
    if path.exists(ovf_path):
        with open(ovf_path, 'r') as f:
            try:
                ovfd = f.read()
                f.close()
                return ovfd
            except:
                print "Could not read file: %s" % ovf_path
                exit(1)


def extract_ova(svmcloc):
    '''
    extract ova file
    '''
    svmcfile = urllib.URLopener()
    download_location = "C:/hpe-svmc.ova"
    remaining_download_tries = 15
    while remaining_download_tries > 0:
        try:
            svmcfile.retrieve(svmcloc, download_location)
            print "successfully downloaded svmc ova "
            time.sleep(1)
        except:
            print("error downloading svmc ova on trial no: " + str(16 - remaining_download_tries))
            remaining_download_tries = remaining_download_tries - 1
            continue
        else:
            break
    try:
        extracted_ovfpath = "C:/hpe-svmc-extracted"
        if os.path.exists("C://hpe-svmc-extracted"):
            shutil.rmtree(extracted_ovfpath)
        if (svmcloc.endswith(".ova")):
            tar = tarfile.open(download_location)
            tar.extractall(path=extracted_ovfpath)
            tar.close()
        else:
            print "Not an .ova file: %s " % svmcloc
    except Exception as e:
        print "Exception %s in extract_ova() with the filename %s", e, svmcloc
        raise e
    return extracted_ovfpath


def get_files_from_dir(dir, filetype):

    files = []
    try:
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)) and file.endswith(filetype):
                file = os.path.realpath(os.path.join(dir, file))
                files.append(file)
    except Exception as e:
        print "Exception %s in get_files_from_dir() with the directory name %s and filetype %s", e, dir, filetype
        raise e
    return files


def get_obj_in_list(obj_name, obj_list):
    """
    Gets an object out of a list (obj_list) whos name matches obj_name.
    """
    for o in obj_list:
        if o.name == obj_name:
            return o
    print ("Unable to find object by the name of %s in list:\n%s" %
           (o.name, map(lambda o: o.name, obj_list)))
    exit(1)


def get_objects(si, datacenter, datastore, cluster):
    """
    Return a dict containing the necessary objects for deployment.
    """
    # Get datacenter object.
    datacenter_list = si.content.rootFolder.childEntity
    if datacenter:
        datacenter_obj = get_obj_in_list(datacenter, datacenter_list)
    else:
        datacenter_obj = datacenter_list[0]

    # Get datastore object.
    datastore_list = datacenter_obj.datastoreFolder.childEntity
    if datastore:
        datastore_obj = get_obj_in_list(datastore, datastore_list)
    elif len(datastore_list) > 0:
        datastore_obj = datastore_list[0]
    else:
        print "No datastores found in DC (%s)." % datacenter_obj.name

    # Get cluster object.
    cluster_list = datacenter_obj.hostFolder.childEntity
    if cluster:
        cluster_obj = get_obj_in_list(cluster, cluster_list)
    elif len(cluster_list) > 0:
        cluster_obj = cluster_list[0]
    else:
        print "No clusters found in DC (%s)." % datacenter_obj.name

    # Generate resource pool.
    resource_pool_obj = cluster_obj.resourcePool

    return {"datacenter": datacenter_obj,
            "datastore": datastore_obj,
            "resource pool": resource_pool_obj}


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


def keep_lease_alive(lease):
    """
    Keeps the lease alive while POSTing the VMDK.
    """
    while(True):
        sleep(5)
        try:
            # Choosing arbitrary percentage to keep the lease alive.
            lease.HttpNfcLeaseProgress(50)
            if (lease.state == vim.HttpNfcLease.State.done):
                return
        except:
            return


def execute_command_for_svmc(svmc_ip, svmc_root_user, svmc_root_pw):
    ssh = paramiko.client.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(svmc_ip, username=svmc_root_user, password=svmc_root_pw, timeout=30.0)
    command = "pm_roles_permission -o -y Admin -a hpinvent"
    output = ssh.exec_command(command)
    time.sleep(5)


def deploy_svmc(svmc_name, vc_ip, vc_user, vc_password, vc_port, datacenter_svmc, datastore_svmc, cluster_svmc, svmc_net_details, svmcloc, svmc_root_user, svmc_root_pw):
    ovf_path = extract_ova(svmcloc)
    ovf_file = get_files_from_dir(ovf_path, ".ovf")[0]
    vmdk_path = get_files_from_dir(ovf_path, ".vmdk")
    ovfd = get_ovf_descriptor(ovf_file)
    try:
        si = connect.Connect(vc_ip, vc_port, vc_user, vc_password)
        content = si.RetrieveContent()
    except:
        print "Unable to connect to %s" % vc_ip
        exit(1)
    objs = get_objects(si, datacenter_svmc, datastore_svmc, cluster_svmc)
    propertydict = {"eth0_:_ipaddress": svmc_net_details[0][0],
                    "eth0_:_subnet_mask": svmc_net_details[0][1],
                    "eth0_:_default_gateway": svmc_net_details[0][2],
                    "eth0_:_dns_servers": svmc_net_details[0][3][0]
                    }
    manager = si.content.ovfManager
    spec_params = vim.OvfManager.CreateImportSpecParams()
    ovfPropertyMappings = []
    for key, value in propertydict.items():
        param = vim.KeyValue()
        param.key = key
        param.value = value
        ovfPropertyMappings.append(param)
    spec_params.propertyMapping = ovfPropertyMappings
    spec_params.ipAllocationPolicy = 'fixedPolicy'
    spec_params.ipProtocol = 'static'
    import_spec = manager.CreateImportSpec(ovfd, objs["resource pool"], objs["datastore"], spec_params)
    import_spec.importSpec.configSpec.name = svmc_name
    lease = objs["resource pool"].ImportVApp(import_spec.importSpec,
                                             objs["datacenter"].vmFolder)
    while(True):
        if (lease.state == vim.HttpNfcLease.State.ready):
            keepalive_thread = Thread(target=keep_lease_alive, args=(lease,))
            keepalive_thread.start()
            curl_loc = "C:/curl-7.53.1-win64-mingw/bin/curl.exe"
            i = 0
            for vmdk in vmdk_path:
                url = lease.info.deviceUrl[0].url.replace('*', vc_ip)
                curl_cmd = (curl_loc + " --globoff" + " -Ss -X POST --insecure -T %s -H 'Content-Type:application/x-vnd.vmware-streamVmdk' %s" % (vmdk, url))
                system(curl_cmd)
                i = i + 1
            lease.HttpNfcLeaseComplete()
            keepalive_thread.join()
            vm_obj = get_obj(content, [vim.VirtualMachine], svmc_name)
            tasks = vm_obj.PowerOn()
            time.sleep(300)
            # execute_command_for_svmc(svmc_net_details[0][0], svmc_root_user, svmc_root_pw)
            connect.Disconnect(si)
            return 0
        elif (lease.state == vim.HttpNfcLease.State.error):
            print "Lease error: " + lease.state.error
            exit(1)
    connect.Disconnect(si)
