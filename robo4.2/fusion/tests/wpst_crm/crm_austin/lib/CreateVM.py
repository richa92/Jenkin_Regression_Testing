#!/usr/bin/python
# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.

from pysphere import VIServer
from pysphere import MORTypes
from pysphere.resources import VimService_services as VI
from pysphere.vi_task import VITask
from pysphere.vi_property import VIProperty
import random
import datetime
import sys
import os
import re
import time


# Custom settings.
server_name = "vc-vcenter-03.usa.hp.com"
user_name = "wpstuser"
password = "HPvse123"
guest_user = "root"
guest_password = "hpvse1"
cluster_name = "WPST-OneView-LRVCb"
install_script = "/usr/local/bin/yum-austin"
install_script_log = "/tmp/yum-austin.log"
datastore_list = [
                  "WPST-Cluster-DS01",
                  "WPST-Cluster-DS02",
                  "WPST-Cluster-DS03",
                  "WPST-Cluster-DS04"
                  ]
max_vm_age_in_hours = 2
max_stale_vm_replacement_builds = 2
max_passbuild_history =10
vm = None
building_string = "[Installing]"


def log(str):
    print str
    sys.stdout.flush()


def build_vm(server, resourcepool, name_prefix):
    ip_field = "(unknown)"
    # vm_name = name_prefix + building_string + " " + time_string + " " + ip_field + " #" + build_number
    vm_name = name_prefix + building_string+ ip_field + " "+ time_string + "#" + build_number
    log("Deploying VM %s from template %s..." % (vm_name, template_name))
    template = server.get_vm_by_name(template_name)
    log("template=%s" % template)
    ds_list = server.get_datastores()
    log("dlist=%s" % ds_list)
    ds_list = server.get_datastores().items()
    random.shuffle(datastore_list)
    log("datastore_list=%s" % datastore_list)
#    for datastore in datastore_list:
#        for ds in ds_list:
#            if ds[1] == datastore:
#                ds_ref = ds[0]
#                break
#        datastore_props = VIProperty(server, ds_ref)
#        #log("Space available on datastore %s: %d" % (datastore, datastore_props.summary.freeSpace/1024**3))
#        if datastore_props.summary.freeSpace/1024**3 > 170:
#            log("Selected datastore: %s" % datastore)
#            break
#        else:
#            log("Not enough space on datastore %s" % datastore)
#            continue
#    else:
#        raise Exception("Available free space on all datastores is less than 170Gb, aborting VM creation. Delete unused VMs and try again.")

    # Retry VM creation if host reports vSphere HA support error
    for i in range (0, 3):
        try:
            log("Cloning VM from template...")
#            vm = template.clone(vm_name, datastore=ds_ref, resourcepool=resourcepool, folder=folder_name, power_on=True)
            vm = template.clone(vm_name, resourcepool=resourcepool, folder=folder_name, power_on=True)
            break
        except Exception, e:
            if str(e).startswith("[Task Error]: The host is reporting errors in its attempts to provide vSphere HA support", 0) or \
               str(e).startswith("[Task Error]: An error occurred while communicating with the remote host", 0):
                log("Unable to deploy VM due to host errors. Retrying...")
                continue
            else:
                raise e
                break
    else:
        raise Exception ("Exhausted all three attempts to deploy a VM.")

    vm = server.get_vm_by_name(vm_name)
    vm_status = vm.get_status()
    if vm_status == "POWERED ON" or vm_status == "POWERING ON":
        log("VM power state: %s" % vm_status)
    else:
        try:
            log("Powering on VM...")
            vm.power_on()
        except Exception, e:
            log("Failed to power on VM.")
            delete_vm(vm)
            raise e

    # Retry fetching VM IP in case of a failure
    for i in range(0, 2):
        try:
            log("Waiting up to 120 seconds for vmtools to be available...")
            vm.wait_for_tools(timeout=120)
        except Exception as e:
            "here1"
            delete_vm(vm)
            vm = None
            raise e
        log("Got vmtools.")
        pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        log("Waiting up to 120 seconds for VM to acquire an IP address...")
        start_time = time.time()
        while (time.time() < start_time + 120):
            ip = vm.get_property('ip_address', from_cache=False)
            if ip == None:
                time.sleep(2)
            else:
                break
        if not pattern.match(ip):
            log("Failed to fetch IPv4 address of newly created VM. Deleting VM...")
            delete_vm(vm)
            vm = None
            raise Exception("Failed to fetch IPv4 address of newly created VM. Aborted.")
        else:
            log("Got VM ip %s." % ip)
            break
    else:
        error_msg = "Failed to get IPv4 address of VM " + vm_name
        delete_vm(vm)
        raise Exception(error_msg)
    log("Got IP address: %s" % ip)
    vm_name = vm_name.replace(ip_field, "(" + ip + ")")
    log("Renaming VM to '%s'." % vm_name)
    vm.rename(vm_name)

    log("Logging in to guest OS...")
    vm.login_in_guest(guest_user, guest_password)

    log("Installing %s on VM..." % vm_munged_name_prefix)
    pid = None
    # TODO:  It is possible to copy this script from Jenkins to the VM, instead of relying on it already existing there.
    pid = vm.start_process(install_script, args=[version, oneview_build_number, ">", install_script_log, "2>&1"])
    log("Started %s... (PID %s)" % (install_script, pid))
    if pid is None:
        delete_vm(vm)
        raise Exception("Failed to invoke %s on VM" % install_script)

    # Wait for install_script to complete
    process_running = True
    while process_running:
        try:
            process_list = vm.list_processes()
        except Exception, e:
            if str(e).startswith("[InvalidStateFault]: The operation is not allowed in the current state", 0) or \
               str(e).startswith("[InvalidPowerStateFault]: The attempted operation cannot be performed in the current state", 0) or \
               str(e).startswith("[GuestOperationsUnavailableFault]: The guest operations agent could not be contacted", 0):
                log("Looks like VM is being migrated to a different host. Waiting 10 seconds before querying process list again...")
                time.sleep(10)
                continue
        for process in process_list:
            if process['pid'] == pid and process['exit_code'] == None:
                time.sleep(5)
                break
            elif process['pid'] == pid and process['exit_code'] != 0:
                error_msg = "Error running %s on VM. Exit code: %s" % (install_script, str(process['exit_code']))
                try:
                    yum_log = "install_script." + vm_munged_name_prefix + "." + build_number + ".log."
                    vm.get_file(install_script_log, yum_log, overwrite=True)
                    f = open(yum_log, 'r')
                    for line in f.readlines():
                        log(line)
                    f.close()
                except Exception, e:
                    pass
                delete_vm(vm)
                raise Exception(error_msg)
            elif process['pid'] == pid and process['exit_code'] == 0:
                process_running = False
                break
        if not process_running:
            break
        time.sleep(1)
    # log("Successfully installed %s%s." % (vm_name_prefix, version))
    log("Successfully installed %s." % vm_munged_name_prefix)
    #vm_name = vm_name.replace(building_string, "")
    vm_name = vm_name.replace(building_string, "[Installed]")
    log("Renaming VM to '%s'." % vm_name)
    vm.rename(vm_name)


def delete_vm(vm):
    vm_name = vm.get_property('name', from_cache=False)
    log("Preparing to delete VM %s..." % vm_name)
    vm_status = vm.get_status()
    log("VM status: %s" % vm_status)
    if vm_status == "POWERED OFF" or vm_status == "POWERING OFF":
        log("VM power state: %s" % vm_status)
    else:
        log("Powering off VM %s..." % vm_name)
        vm.power_off()

    log("Deleting VM %s..." % vm_name)
    request = VI.Destroy_TaskRequestMsg()
    _this = request.new__this(vm._mor)
    _this.set_attribute_type(vm._mor.get_attribute_type())
    request.set_element__this(_this)
    ret = server._proxy.Destroy_Task(request)._returnval

    # Wait for the delete task to finish
    task = VITask(ret, server)

    status = task.wait_for_state([task.STATE_SUCCESS, task.STATE_ERROR])
    if status == task.STATE_SUCCESS:
        log("VM successfully deleted from disk.")
    elif status == task.STATE_ERROR:
        error_msg = "Error while deleting VM: " + task.get_error_message()
        raise Exception(error_msg)


def get_vm_tuple_list(server, folder_filter, name_prefix):
    '''Returns a list of tuple(vm, timestamp) of VMs of the desired version.'''
    vm_tuple_list = []
    vm_path_list = server.get_registered_vms(advanced_filters=folder_filter)
    for vm_path in vm_path_list:
        vm = server.get_vm_by_path(vm_path)
        vm_name = vm.get_property('name', from_cache=False)
        if vm_name.startswith(name_prefix):
            vm_tuple = (vm, None)
            try:
                tokens = vm_name.split(' ')
                timestamp = tokens[1] + ' ' + tokens[2] + ' ' + tokens[3] + ' ' + tokens[4]
                #log("ts=%s" % timestamp)
                vm_tuple = (vm, datetime.datetime.strptime(timestamp, '%B %d %Y %H:%M:%S'))
                #vm_tuple = (vm, datetime.datetime.strptime(timestamp, '%Y%m%d %H:%M:%S'))
            except Exception, e:
                log("Could not determine timestamp of VM %s.  Skipping." % vm_name)
            vm_tuple_list.append(vm_tuple)
    return vm_tuple_list


def get_stale_vms(server, folder_filter, name_prefix):
    stale_tuple_list = []
    vm_tuple_list = get_vm_tuple_list(server, folder_filter, name_prefix)
    stale_time = datetime.datetime.now() - datetime.timedelta(hours=max_vm_age_in_hours)
    for vm,vm_timestamp in vm_tuple_list:
        if vm_timestamp is not None and vm_timestamp < stale_time:
            stale_tuple_list.append((vm,vm_timestamp))
    # Sort from oldest to newest.
    if stale_tuple_list:
        stale_tuple_list = [(vm,vm_timestamp) for vm,vm_timestamp in sorted(stale_tuple_list, key=lambda x: x[1])]
    for vm,ts in stale_tuple_list:
        log("Found stale VM: %s" % vm.get_property('name', from_cache=False))
    return stale_tuple_list


def get_num_vms_building(vm_tuple_list):
    num_vms_building = 0
    for vm,ts in vm_tuple_list:
        if building_string in vm.get_property('name', from_cache=False):
            num_vms_building += 1
    return num_vms_building


def delete_a_stale_vm(server, folder_filter, name_prefix):
    '''Deletes the oldest stale VM.'''
    stale_list = get_stale_vms(server, folder_filter, name_prefix)
    if stale_list:
        log("Deleting a stale VM.")
        delete_vm(stale_list[0][0])


# Main.
try:
    server = None
    num_args = len(sys.argv)
    for arg in sys.argv:
        log("arg=%s" % arg)
    log("num=%s" % num_args)
    if num_args != 8 and num_args != 11:
        log("Usage: python " + sys.argv[0] + " <VM-name-previx> <OneView-version-to-install> <vCenter-folder-name(case-sensitive)> <build-number> <build-id(date)> <max_vm_count> <vm_template_name> [Oneview_build_number] [Oneview_passbuild_Id] [PurgeOldVms]")
        exit(1)
    else:
        vm_name_prefix = str(sys.argv[1])
        version = str(sys.argv[2])
        folder_name = str(sys.argv[3])
        build_number = str(sys.argv[4])
        time_string = datetime.datetime.strptime(str(sys.argv[5]), '%Y-%m-%d_%H-%M-%S').strftime('%B %d %Y %H:%M:%S')
        max_vm_count = int(str(sys.argv[6]))
        template_name = str(sys.argv[7])

        if num_args == 11:
            oneview_build_number = str(sys.argv[8])
            oneview_passbuild_id = str(sys.argv[9])
            is_purge = str(sys.argv[10])
            vm_munged_name_prefix = vm_name_prefix + version + "_P" + oneview_passbuild_id + "_" + oneview_build_number
        else:
            oneview_build_number = ""
            vm_munged_name_prefix = vm_name_prefix + version

        log("Connecting to vCenter %s..." % server_name)
        server = VIServer()
        server.connect(server_name, user_name, password)

        # Get a reference to the folder in which VM needs to be created
        folders_list = server._get_managed_objects(MORTypes.Folder)
        for key in folders_list.keys():
            if folders_list[key] == folder_name:
                folder_mor = key
                break
        else:
            raise Exception("Folder not found")

#         folder_filter = {"parent": folder_mor}
        clusters_list = server.get_clusters()
        for cluster_key in clusters_list.keys():
            if clusters_list[cluster_key] == cluster_name:
                resourcepool = server.get_resource_pools(cluster_key).keys()[0]
# WPST
        folder_mor = [mor for mor, name in
                  server._get_managed_objects(MORTypes.Folder).items()
                  if name == folder_name][0]
        vms = server._get_managed_objects(MORTypes.VirtualMachine, from_mor=folder_mor).values()
        # delete old VMs
        if is_purge == 'True':
            for vmname in vms:
                if vm_munged_name_prefix not in vmname:
                    targetvm = server.get_vm_by_name(vmname)
                    delete_vm(targetvm)
        # create new VM
        matched_vms = [vmname for vmname in vms if vmname.startswith(vm_munged_name_prefix)]
        if len (matched_vms) <= max_vm_count:
            log("Building a new VM due to too few VMs.")
            build_vm(server,resourcepool, vm_munged_name_prefix)
        else:
            log("Exceed the maximum number of VMs (%s) defined, no more new VM to be built" % max_vm_count)

        # Get vm quality info.
#         vm_tuple_list = get_vm_tuple_list(server, folder_name, vm_munged_name_prefix)
#         vm_count = len(vm_tuple_list)
#         num_vms_building = get_num_vms_building(vm_tuple_list)
#         log("The number of VMs currently building is %s." % num_vms_building)
#         stale_vm_list = get_stale_vms(server, folder_name, vm_munged_name_prefix)
#         too_few_vms = vm_count < max_vm_count
#         too_many_vms = vm_count >= max_vm_count + max_stale_vm_replacement_builds
        #log("vm_count=%s, max_vm_count=%s(+%s)" % (vm_count, max_vm_count, max_stale_vm_replacement_builds))
        #log("stale_vm_list: %s" % str(stale_vm_list))
        #log("too_few_vms: %s" % too_few_vms)
        #log("too_many_vms: %s" % too_many_vms)

        # Decide what to do about creating/deleting VMs.
#         if too_few_vms or (not too_many_vms and num_vms_building < len(stale_vm_list) and stale_vm_list):
#             if too_few_vms:
#                 log("Building a new VM due to too few VMs.")
#                 build_vm(server,resourcepool, vm_munged_name_prefix)
#             else:
#                 log("Building a new VM due to stale VMs.")
#                 build_vm(server,resourcepool, vm_munged_name_prefix)
#                 if not too_few_vms:
#                     delete_a_stale_vm(server, folder_filter, vm_munged_name_prefix)
#         else:
#             # Log why we're not building a VM now."
#             if too_many_vms:
#                 reason = "too many VMs."
#             elif not stale_vm_list:
#                 reason = "no stale VMs."
#             elif num_vms_building > 0:
#                 reason = "new VM already installing."
#             else:
#                 reason = "being confused."
#             log("Not building a new VM now due to " + reason)

        # After building a new VM and deleting a stale one, there should never be
        # more than max_vm_count built VMs.  If so, delete a stale one.
#         new_vm_tuple_list = get_vm_tuple_list(server, folder_filter, vm_munged_name_prefix)
#         new_vm_count = len(new_vm_tuple_list)
#         if (new_vm_count - get_num_vms_building(new_vm_tuple_list)) > max_vm_count:
#             delete_a_stale_vm(server, folder_filter, vm_munged_name_prefix)


except Exception, e:
    import traceback
    stack = traceback.format_exc()
    log("The Exception: %s" % str(e))
    log("VM: %s" % vmname)
    log(stack)
    if building_string in vmname:
        log("Exception occurred, deleting failed VM.")
        targetvm = server.get_vm_by_name(vmname)
        delete_vm(targetvm)
#     elif vm:
#         log("Exception occurred, deleting failed VM.")
#         delete_vm(vm)
    else:
        log("Exception occurred, and no VM to delete.")
    exit(1)
finally:
    if server is not None:
        server.disconnect()
        log("Disconnecting to vCenter %s..." % server_name)
