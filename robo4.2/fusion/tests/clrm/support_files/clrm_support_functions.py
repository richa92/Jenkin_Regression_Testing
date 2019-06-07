"""
This File contains common support functions used form CLRM Operations
"""
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
import time


class clrm_support_functions(object):
    """
    This class contains common fucntions used as part CLRM Operations
    """

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def append_name_to_dvswitch(self, virtual_switch_layout, postfix):
        """
        Appends postfix to the portgroup names and switch names
        Usage : Append Name to dvswitch| virtual_switch_layout | postfix
        """
        for vs in virtual_switch_layout:
            vs['name'] = vs['name'] + "_" + postfix
            for vsp in vs['virtualSwitchPortGroups']:
                vsp['name'] = vsp['name'] + "_" + postfix
        return virtual_switch_layout

    def convert_dictionary_to_tuplelist(self, input_dict, output_list):
        """ This function is to convert the input dictionary
            It will return a list of tuples with (key, value) pair
        Usage: convert_dictionary_to_tuplelist(self, input_dict, output_list)
        """
        if isinstance(input_dict, dict):
            for key, value in input_dict.items():
                if key == 'password' or key == "serverPassword" or key == "addHostRequests" or key == "inUse":
                    continue
                elif isinstance(value, dict):
                    clrm_support_functions.convert_dictionary_to_tuplelist(self, value, output_list)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            clrm_support_functions.convert_dictionary_to_tuplelist(self, item, output_list)
                        else:
                            if not isinstance(item, str):
                                item = str(item)
                            if item == "False" or item == "True":
                                item = item.lower()
                            output_list.append((key, item))
                else:
                    if not isinstance(value, str):
                        value = str(value)
                    if value == "False" or value == "True":
                        value = value.lower()
                    output_list.append((key, value))

    def validate_deployment_manager(self, dep_mgr):
        """
        Validates Deployment manager
        """
        request_list = []
        response_list = []
        count = 0
        param = '?"filter=name==%s"' % dep_mgr["name"]
        result = self.fusionlib.fusion_api_get_deployment_manager(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] != 0:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Failed to perform get on a deployment manager")
            logger._warn("Response : %s " % result)
            return False

        dep_mgr_copy = dep_mgr
        headers = ["Status Code", "Cache-Control", "Connection", "Content-Encoding", "Content-Type", "Date", "Server", "connection",
                   "Transfer-Encoding", "Vary", "Via", "content-length", "content-location", "via", "vary", "server",
                   "-content-encoding", "etag", "eTag", "modified", "cache-control", "date", "content-type", "transfer-encoding", "reason"]
        for value in headers:
            if value in dep_mgr_copy:
                del dep_mgr_copy[value]
        clrm_support_functions.convert_dictionary_to_tuplelist(self, dep_mgr_copy, request_list)
        clrm_support_functions.convert_dictionary_to_tuplelist(self, result, response_list)
        mismatch_list = []
        for item in request_list:
            if item not in response_list:
                mismatch_list.append(item)
                count += 1
        if count > 0:
            logger._warn("Validation failed for following %s items" % count)
            logger._warn("%s" % str(mismatch_list))
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

    def validate_hypervisor_manager(self, vcenter):
        """
        Validates Hypervisor manager Settings
        """
        request_list = []
        response_list = []
        count = 0
        param = '?"filter=name==%s"' % vcenter["name"]
        result = self.fusionlib.fusion_api_get_hypervisor_manager(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] != 0:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Failed to perform get on a hypervisor manager")
            logger._warn("Response : %s " % result)
            return False

        vcenter_dict1 = vcenter
        headers = ["Status Code", "Cache-Control", "Connection", "Content-Encoding", "Content-Type", "Date", "Server", "connection",
                   "Transfer-Encoding", "Vary", "Via", "content-length", "content-location", "via", "vary", "server",
                   "-content-encoding", "etag", "eTag", "modified", "cache-control", "date", "content-type", "transfer-encoding", "reason"]
        for value in headers:
            if value in vcenter_dict1:
                del vcenter_dict1[value]
        clrm_support_functions.convert_dictionary_to_tuplelist(self, vcenter_dict1, request_list)
        clrm_support_functions.convert_dictionary_to_tuplelist(self, result, response_list)
        mismatch_list = []
        for item in request_list:
            if item not in response_list:
                mismatch_list.append(item)
                count += 1
        if count > 0:
            logger._warn("Validation failed for following %s items" % count)
            logger._warn("%s" % str(mismatch_list))
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

    def HCP_create_validation(self, cluster_dict):
        """
        Validates Hypervisor Cluster profile creation with sent payload and created cluster profile
        """
        time.sleep(30)
        param = '?filter=name==%s' % cluster_dict["name"]
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] != 0:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Failed to perform get on a cluster")
            logger._warn("Response : %s " % result)
            return False
        count = 0
        mismatch_list = []

        if cluster_dict["addHostRequests"] is not None:
            hosts = cluster_dict["addHostRequests"]
            if len(hosts) != len(result["members"][0]["hypervisorHostProfileUris"]):
                count = count + 1
                mismatch_list.append(("hypervisorHostProfileUris", result["members"][0]["hypervisorHostProfileUris"]))
                logger._log_to_console_and_log_file("Add host request and hypervisorHostProfileUris are mismatching")

        mismatch_list, status1, validation_failed_count = clrm_support_functions.__validate_cluster(self, result, cluster_dict, mismatch_list)
        if not status1:
            logger._log_to_console_and_log_file("Validation failed for hypervisor cluster of HCP: %s" % cluster_dict["name"])
        count = count + validation_failed_count
        request_list = []
        clrm_support_functions.convert_dictionary_to_tuplelist(self, cluster_dict, request_list)
        response_list = []
        clrm_support_functions.convert_dictionary_to_tuplelist(self, result, response_list)
        for item in request_list:
            if item not in response_list:
                mismatch_list.append(item)
                count += 1
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            logger._warn("%s" % str(mismatch_list))
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful for HCP Create")
        return True

    def HCP_update_validation(self, cluster, res_data_copy, get_cp_res_data, deleted_hhps, name_flag):
        """
        Validates Hypervisor Cluster profile update with sent payload and updated cluster profile
        """
        time.sleep(30)
        if deleted_hhps is None:
            deleted_hhps = 0
        if res_data_copy["sharedStorageVolumes"] is None:
            del res_data_copy["sharedStorageVolumes"]
        if name_flag:
            param = '?filter=name==%s' % cluster["new_name"]
            result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        else:
            param = '?filter=name==%s' % cluster["name"]
            result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)

        count = 0
        request_list = []
        for key, value in res_data_copy.items():
            if key == "compliance":
                for key1 in value.keys():
                    if key1 == "state":
                        del res_data_copy[key][key1]
                        continue
            if key == "status":
                del res_data_copy[key]
                continue
            if key == "modified":
                if value is not None:
                    del res_data_copy[key]
                    continue
            if key == "eTag":
                if value is not None:
                    del res_data_copy[key]
                    continue

        mismatch_list = []
        existing_hhps = 0
        if get_cp_res_data["hypervisorHostProfileUris"] is not None:
            existing_hhps = len(get_cp_res_data["hypervisorHostProfileUris"])

        hhpUri_count = 0

        # This code is to validate hypervisor host profile uris
        hhpUri_count += existing_hhps
        if res_data_copy["addHostRequests"]:
            hhpUri_count += len(res_data_copy["addHostRequests"])
        hhpUri_count = hhpUri_count - deleted_hhps

        if result["members"][0]["hypervisorHostProfileUris"] is not None:
            if len(result["members"][0]["hypervisorHostProfileUris"]) != hhpUri_count:
                count += 1
                mismatch_list.append(("hypervisorHostProfileUris", result["members"][0]["hypervisorHostProfileUris"]))
                logger._log_to_console_and_log_file("Add host request and hypervisorHostProfileUris are mismatching")
        if result["members"][0]["hypervisorHostProfileUris"] is None:
            if hhpUri_count != 0:
                count += 1
                mismatch_list.append(("hypervisorHostProfileUris", result["members"][0]["hypervisorHostProfileUris"]))
                logger._log_to_console_and_log_file("Add host request and hypervisorHostProfileUris are mismatching")
        del res_data_copy["hypervisorHostProfileUris"], res_data_copy["addHostRequests"]

        clrm_support_functions.convert_dictionary_to_tuplelist(self, res_data_copy, request_list)
        response_list = []
        clrm_support_functions.convert_dictionary_to_tuplelist(self, result, response_list)
        for item in request_list:
            if item not in response_list:
                mismatch_list.append(item)
                count += 1
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            logger._warn("%s" % str(mismatch_list))
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful for HCP update")
        return True

    def HHP_update_validation(self, res_data_copy, cluster_name, hhp_uri):
        """
        Validates Hypervisor Host profile update with sent payload and updated Host profile
        """
        time.sleep(30)
        param = '?filter=name==%s' % cluster_name
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] == 1:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Failed to perform get on a cluster")
            logger._warn("Response : %s " % result)
            return False
        response = {}
        for uri in result["members"][0]["hypervisorHostProfileUris"]:
            if hhp_uri == uri:
                response = self.fusionlib.fusion_api_get_resource(uri)
                if 'uri' not in response or response["status_code"] not in (200, "OK", "Active", "Warning") or response["state"] not in ("Active", "Warning"):
                    return False
        if "hypervisorHostUri" in response:
            time.sleep(10)
            output = self.fusionlib.fusion_api_get_resource(response["hypervisorHostUri"])
            if 'uri' not in output or output["status_code"] not in (200, "OK", "Active", "Warning") or output["state"] not in ("Active", "Warning", "Configured"):
                return False
        count = 0
        for key, value in res_data_copy.items():
            if key in ("created", "modified", "eTag", "reDeployHost") and value is not None:
                del res_data_copy[key]
                continue
            if key == "powerState":
                if value is None:
                    del res_data_copy[key]
                    continue
                if value == output["powerState"]:
                    del res_data_copy[key]
                    continue
                elif value == "On" and output["powerState"] == "InMaintenance":
                    del res_data_copy[key]
                    continue
                elif value == "ExitMaintenance" and output["powerState"] == "On":
                    del res_data_copy[key]
                    continue
                else:
                    logger._log_to_console_and_log_file("Validation failed for powerState update")
                    count += 1
                    del res_data_copy[key]
                    continue
        request_list = []
        clrm_support_functions.convert_dictionary_to_tuplelist(self, res_data_copy, request_list)
        response_list = []
        clrm_support_functions.convert_dictionary_to_tuplelist(self, response, response_list)
        for item in request_list:
            if item not in response_list:
                logger._log_to_console_and_log_file("Validation failed for %s" % str(item))
                count += 1
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

    def __validate_cluster(self, result, cluster_dict, mismatch_list):
        """ This function is to validate hypervisor cluster with cluster profile body"""
        url = result["members"][0]["hypervisorClusterUri"]
        response = {}
        new_count = 0
        response = self.fusionlib.fusion_api_get_resource(url)
        logger._log_to_console_and_log_file("GET on Hypervisor Cluster %s" % response)
        if not response["name"] == cluster_dict["name"]:
            new_count += 1
            mismatch_list.append(("name", cluster_dict["name"]))
        if not response["hypervisorManagerUri"] == cluster_dict["hypervisorManagerUri"]:
            new_count += 1
            mismatch_list.append(("hypervisorManagerUri", cluster_dict["hypervisorManagerUri"]))
        if "hypervisorClusterSettings" in cluster_dict and cluster_dict["hypervisorClusterSettings"] is not None:
            if "drsEnabled" in cluster_dict["hypervisorClusterSettings"]:
                if not str(response["hypervisorClusterConfig"]["drsEnabled"]).lower() == str(cluster_dict["hypervisorClusterSettings"]["drsEnabled"]).lower():
                    new_count += 1
                    mismatch_list.append(("drsEnabled", cluster_dict["hypervisorClusterSettings"]["drsEnabled"]))
            if "haEnabled" in cluster_dict["hypervisorClusterSettings"]:
                if not str(response["hypervisorClusterConfig"]["haEnabled"]).lower() == str(cluster_dict["hypervisorClusterSettings"]["haEnabled"]).lower():
                    new_count += 1
                    mismatch_list.append(("haEnabled", cluster_dict["hypervisorClusterSettings"]["haEnabled"]))
        if new_count:
            return mismatch_list, False, new_count
        return mismatch_list, True, new_count

    def validate_get_hypervisor_host_profile(self, host):
        """ Validates the response of get call on hypervisor host profile
            Usage: _validate_get_hypervisor_host_profile(fusion_client, host)
        """
        url = host["hypervisorClusterProfileUri"]
        mismatch_list = []
        count = 0
        if host["type"] != "HypervisorHostProfile":
            count += 1
            mismatch_list.append(host["type"])
        response = self.fusionlib.fusion_api_get_resource(url)
        if 'uri' not in response or response['status'] not in (200, 'OK', 'Warning') or response["state"] not in ("Active", "Warning"):
            return False
        stat = clrm_support_functions._validate_ip_pool(self, response, host)
        if not stat:
            return False
        if host["hypervisorClusterProfileUri"] != response["uri"]:
            count += 1
            mismatch_list.append(host["hypervisorClusterProfileUri"])
        counter = 0
        for host_profile_uri in response["hypervisorHostProfileUris"]:
            if host["uri"] != host_profile_uri:
                counter += 1
        if counter == len(response["hypervisorHostProfileUris"]):
            count += 1
            mismatch_list.append(host["uri"])
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

    def _validate_get_hypervisor_clusters(self, hyp_cluster):
        """ Validates the response of get call on hypervisor clusters
        Usage:_validate_get_hypervisor_clusters(fusion_client, hyp_cluster)
        """
        mismatch_list = []
        count = 0
        if hyp_cluster["type"] != "HypervisorCluster":
            count += 1
            mismatch_list.append(hyp_cluster["type"])
        param = '?filter=name==%s' % hyp_cluster["name"]
        resp = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if hyp_cluster["hypervisorClusterProfileUri"] != resp['members'][0]['uri']:
            count += 1
            mismatch_list.append(hyp_cluster["hypervisorClusterProfileUri"])
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

    def _validate_ip_pool(self, cluster, host_profile):
        """Validates the IP address of the hypervisor host profile
           Usage: _validate_ip_pool(fusion_client, cluster, host_profile)
        """
        list1 = list2 = list3 = []
        start_ip = None
        end_ip = None
        if host_profile["ipSettings"]:
            for key, value in host_profile["ipSettings"].items():
                if key == "ip":
                    host_profile_ip = value
        else:
            logger._warn("IP-pool values does not exist")
            return False
        if cluster["ipPools"]:
            for value in cluster["ipPools"]:
                for key1, value1 in value.items():
                    if key1 == "rangeUris":
                        resp = self.fusionlib.fusion_api_get_resource(value1[0])
                        logger._log_to_console_and_log_file(resp)
                        if 'uri' not in resp:
                            return False
                        else:
                            start_ip = resp["startAddress"]
                            end_ip = resp["endAddress"]
            for value in host_profile_ip.split("."):
                list1.append(value)
            if start_ip:
                for value in start_ip.split("."):
                    list2.append(value)
            if end_ip:
                for value in end_ip.split("."):
                    list3.append(value)
            for i in range(0, 4, 1):
                if not list2[i] <= list1[i] <= list3[i]:
                    return False
        return True

    def validate_get_hypervisor_host(self, host):
        """ Validates the response of get call on hypervisor hosts
            Usage: _validate_get_hypervisor_host(fusion_client, host)
        """
        mismatch_list = []
        count = 0
        if host["type"] != "HypervisorHost":
            count += 1
            mismatch_list.append(host["type"])
        if host["hypervisorClusterUri"] is None:
            logger._log_to_console_and_log_file("Hypervisor Cluster Uri is null")
            return False
        response = self.fusionlib.fusion_api_get_resource(host["hypervisorClusterUri"])
        if host["hypervisorClusterUri"] != response["uri"]:
            count += 1
            mismatch_list.append(host["hypervisorClusterUri"])
        counter = 0
        for host_uri in response["hypervisorHostUris"]:
            if host["uri"] != host_uri:
                counter += 1
        if counter == len(response["hypervisorHostUris"]):
            count += 1
            mismatch_list.append(host["uri"])
        if count > 0:
            logger._warn("Validation failed for %s items" % count)
            return False
        else:
            logger._log_to_console_and_log_file("Validation is successful")
        return True

# SWITCH_VALIDATIONS
    def validate_virtual_switch_config_policy(self, name):
        """ This function validates the virtual switch configuration policy
            Usage: validate_virtual_switch_config_policy(fusion_client, name)
        """
        flag = False
        param = '?filter=name==%s' % name
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] == 1:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Failed to perform get on a cluster")
            logger._warn("Response : %s " % result)
            return flag
        counter = 0
        for key, value in result["members"][0].items():
            if key == "hypervisorHostProfileTemplate":
                for key1, value1 in value.items():
                    if key1 == "virtualSwitches":
                        value1 = value1
                        break
        if not result["members"][0]["hypervisorHostProfileTemplate"]["virtualSwitchConfigPolicy"]["manageVirtualSwitches"]:
            if not value1:
                flag = True
        else:
            if not result["members"][0]["hypervisorHostProfileTemplate"]["virtualSwitchConfigPolicy"]["configurePortGroups"]:
                for each in value1:
                    for key2, value2 in each.items():
                        if key2 == "virtualSwitchPortGroups":
                            if value2:
                                status = clrm_support_functions._validate_virtual_port_purpose(self, value2)
                                if not status:
                                    counter += 1
                                else:
                                    flag = True
                            elif not value2:
                                flag = True
        if counter != 0:
            flag = False
        return flag

    def _validate_virtual_port_purpose(self, port_groups):
        """
        This function is to validate virtual_port_purpose
        Usage: _validate_virtual_port_purpose(port_groups)
        """
        flag = False
        for ports in port_groups:
            for key3, value3 in ports.items():
                if key3 == "virtualSwitchPorts":
                    for purpose in value3:
                        for key4, value4 in purpose.items():
                            if key4 == "virtualPortPurpose" and value4[0] == "Management":
                                flag = True
        return flag

    def _update_virtual_switches(self, req, networks):
        """
        This function is to modify switch layout of a cluster
        """
        switch_details = []
        for j in networks.split(","):
            for i in req:
                for k2, v2 in i.items():
                    if k2 == "name" and v2 == j:
                        switch_details.append(i)
                        break
        if switch_details:
            return True, switch_details
        return False, switch_details

    def validate_vSwitch_connections(self, cluster_obj):
        """
        This function is to validate server profile connections with cluster virtual switch connections
        Usage: validate_vSwitch_connections(self, cluster_obj)
        """
        ds_flag = False
        for cluster in cluster_obj:
            cluster_name = cluster["name"]
            ser_profile_template = cluster["profile_name"]
            switch_type = ""
            for key, settings in cluster["cluster_settings"].items():
                if key == "virtual_switch_type":
                    switch_type = settings
                if switch_type == "Distributed":
                    switch_usage = cluster["cluster_settings"]["distributed_switch_usage"]
                    switch_version = cluster["cluster_settings"]["distributed_switch_version"]
                    ds_flag = True
                if switch_type == "Standard":
                    switch_usage = ""
                    switch_version = ""
        profile_conn, status = clrm_support_functions._get_server_profile_template_connections(self, ser_profile_template)
        if not status:
            logger._log_to_console_and_log_file("Unable to get server profile information")
            return False
        logger._log_to_console_and_log_file("Networks in Server profile are: %s" % profile_conn)
        cluster_conn, status = clrm_support_functions._get_hypervisor_cluster_profile_switch_layout(self, cluster_name)
        if not status:
            logger._log_to_console_and_log_file("Unable to get cluster information")
            return False
        logger._log_to_console_and_log_file("Networks in Cluster are: %s" % cluster_conn)
        count = 0
        value = clrm_support_functions.__validate_switch_usage(self, cluster_conn, ds_flag, switch_usage, switch_version, count)
        count += value
        value1 = clrm_support_functions.__validate_clusterAndHostProfile_vs_spt_switch_connections(self, profile_conn, cluster_conn, count)
        count += value1
        # Commenting out multinic validations
        # value2 = __validate_cluster_multiNicVMotion(cluster_conn, count)
        # count += value2
        host_profile_uris, flag = clrm_support_functions._get_hypervisor_host_profile_uris(self, cluster_name)
        if not flag:
            logger._log_to_console_and_log_file("Failed to get hypervisor host profile uris, cannot perform vswitch validations for host profiles")
            return False
        for hpuri in host_profile_uris:
            host_connections = []
            hostprofile_data = self.fusionlib.fusion_api_get_resource(hpuri)
            host_connections, status = clrm_support_functions._get_switch_layout(self, hostprofile_data)
            if not status:
                logger._log_to_console_and_log_file("Failed to get the switch details of %s " % cluster)
                return host_connections, False
            host_value = clrm_support_functions.__validate_switch_usage(self, host_connections, ds_flag, switch_usage, switch_version, count)
            count += host_value
            host_value1 = clrm_support_functions.__validate_clusterAndHostProfile_vs_spt_switch_connections(self, profile_conn, host_connections, count)
            count += host_value1

        if count > 0:
            logger._log_to_console_and_log_file("validation failed for %s items" % count)
            return False
        logger._log_to_console_and_log_file("vSwitch validation is successful")
        return True

    def __validate_switch_usage(self, connections, ds_flag, switch_usage, switch_version, count):
        """ This subfuction is for validating switch usage details of cluster/host profiles"""
        if ds_flag:
            for conn in connections:
                for k, v in conn.items():
                    if k == "type":
                        if switch_usage == "AllNetworks":
                            if not v == "Distributed":
                                count += 1
                            else:
                                if conn["distributed_version"] != switch_version:
                                    count += 1
                        else:
                            if switch_usage == "GeneralNetworks":
                                if "purpose" in conn:
                                    if conn["purpose"] == "General" or not conn["purpose"]:
                                        if not v == "Distributed":
                                            count += 1
                                        else:
                                            if conn["distributed_version"] != switch_version:
                                                count += 1
                                    else:
                                        if not v == "Standard":
                                            count += 1
        else:
            for conn in connections:
                for k, v in conn.items():
                    if k == "type":
                        if not v == "Standard":
                            count += 1
        return count

    def _get_hypervisor_cluster_profile_switch_layout(self, cluster):
        """ This function is to get switch layout details of hypervisor cluster profile
            Usage: _get_hypervisor_cluster_profile_switch_layout(self, cluster)
        """
        networks = []
        param = '?filter=name==%s' % cluster
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] != 0:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Cluster %s not exists")
            logger._warn("Response : %s " % result)
            return networks, False
        for key, value in result["members"][0].items():
            if key == "hypervisorHostProfileTemplate":
                networks, status = clrm_support_functions._get_switch_layout(self, value)
                if not status:
                    logger._log_to_console_and_log_file("Failed to get the switch details of %s " % cluster)
                    return networks, False
        return networks, True

    def _get_hypervisor_host_profile_uris(self, cluster):
        """ This function is to get hypervisor host profile uris"""
        hostprofile_uris = []
        param = '?filter=name==%s' % cluster
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if 'uri' in result and result['status_code'] in (200, "OK", "Active", "Warning") and result['count'] != 0:
            logger._log_to_console_and_log_file("Response : %s " % result)
        else:
            logger._warn("Cluster %s not exists")
            logger._warn("Response : %s " % result)
            return hostprofile_uris, False
        host_profile_uris = result["members"][0]["hypervisorHostProfileUris"]
        if host_profile_uris:
            return host_profile_uris, True
        else:
            return host_profile_uris, False

    def _get_switch_layout(self, switch_info):
        """ This function is to fetch the switch layout of
        cluster/host profiles"""
        networks = []
        for key1, value1 in switch_info.items():
            if key1 == "virtualSwitches":
                for vswitch in value1:
                    network = {}
                    for key2, value2 in vswitch.items():
                        if key2 == "name":
                            network[key2] = value2
                        if key2 == "virtualSwitchType":
                            network["type"] = value2
                        if key2 == "version":
                            if key2:
                                network["distributed_version"] = value2
                        if key2 == "virtualSwitchUplinks":
                            if len(value2) > 1:
                                uplinks = clrm_support_functions.__get_virtualSwitchUplinks(self, value2)
                                network["uplinks_status"] = uplinks
                        if key2 == "virtualSwitchPortGroups":
                            subnet = clrm_support_functions.__get_virtualSwitchPortGroups(self, value2)
                            if len(subnet) > 1:
                                network["sub-networks"] = subnet
                            else:
                                for i in subnet:
                                    for key, value in i.items():
                                        if key == "uri":
                                            network[key] = value
                                        if key == "purpose":
                                            network[key] = value
                                        else:
                                            network["purpose"] = ""
                                        if key == "vlan":
                                            network[key] = value
                            networks.append(network)
        return networks, True

    def __get_virtualSwitchPortGroups(self, switches):
        """This function is to get virtual switches in hypervisor cluster profile
           Usage: __get_virtualSwitchPortGroups(self, switches)
        """
        sub_networks = []
        for vpgroup in switches:
            subnetwork_details = {}
            for key3, value3 in vpgroup.items():
                if key3 == "networkUris":
                    for i in value3:
                        subnetwork_details["uri"] = i
                if key3 == "name":
                    subnetwork_details["name"] = value3
                if key3 == "vlan":
                    subnetwork_details["vlan"] = value3
                if key3 == "virtualSwitchPorts":
                    if value3:
                        for k in value3:
                            for key, value in k.items():
                                if key == "virtualPortPurpose":
                                    for i in value:
                                        if i:
                                            subnetwork_details["purpose"] = i
            sub_networks.append(subnetwork_details)
        return sub_networks

    def __get_virtualSwitchUplinks(self, uplink):
        """This function is to get virtual switche uplinks in hypervisor cluster profile
            Usage:__get_virtualSwitchUplinks(self, plink)
        """
        uplink_list = []
        for link in uplink:
            uplink_dict = {}
            for k, v in link.items():
                if k == "active":
                    uplink_dict["active"] = v
                if k == "name":
                    uplink_dict["name"] = v
            uplink_list.append(uplink_dict)
        return uplink_list

    def _get_server_profile_template_connections(self, ser_profile_template):
        """ This function is to get switch layout of server profile
            Usage: _get_server_profile_switch_layout(self, cluster)
        """
        network_uri_list = []
        param = '?filter=name==%s' % ser_profile_template
        server_profile_template = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=param)
        for key, value in server_profile_template["members"][0].items():
            if key == "connections":
                for conn in value:
                    for key1 in conn.keys():
                        if key1 == "networkUri":
                            network_uri_list.append(conn["networkUri"])
        networks = []
        for uri in network_uri_list:
            result = self.fusionlib.fusion_api_get_resource(uri)
            temp = {}
            for key, value in result.items():
                if key == "name":
                    temp[key] = value
                if key == "vlanId":
                    temp[key] = value
                if key == "purpose":
                    if value:
                        temp[key] = value
                if key == "uri":
                    if "network-sets" in value:
                        netset_list = clrm_support_functions.__get_networks_from_network_sets(self, value)
                        temp["sub-networks"] = netset_list
                    else:
                        temp[key] = value
            networks.append(temp)
        return networks, True

    def __get_networks_from_network_sets(self, value):
        """
        This function is to get the virtual switches of networks in network sets
        Usage:
        """
        network_set_list = []
        result = self.fusionlib.fusion_api_get_resource(value)
        for k, v in result.items():
            if k == "networkUris":
                for i in v:
                    network_set_dict = {}
                    resp = self.fusionlib.fusion_api_get_resource(i)
                    for key, value in resp.items():
                        if key == "name":
                            network_set_dict[key] = value
                        if key == "vlanId":
                            network_set_dict[key] = value
                        if key == "purpose":
                            network_set_dict[key] = value
                        if key == "uri":
                            network_set_dict[key] = value
                    network_set_list.append(network_set_dict)
        return network_set_list

    def __validate_clusterAndHostProfile_vs_spt_switch_connections(self, profile_conn, cluster_conn, count):
        """This function is to validate switch layout in cluster against switch layout in spt
            Usage:__validate_cluster_and_spt_switch_connections(profile_conn, cluster_conn, count)
        """
        for ser in profile_conn:
            for conn in cluster_conn:
                for k1, v1 in ser.items():
                    if k1 == "name":
                        if v1 == conn[k1]:
                            if "purpose" in conn:
                                if not ser["purpose"] == conn["purpose"]:
                                    if ser["purpose"] == "General" and conn["purpose"] != "":
                                        count += 1
                            if "uri" in conn:
                                if not ser["uri"] == conn["uri"]:
                                    count += 1
                            if "vlan" in conn:
                                if int(conn["vlan"]) > 0:
                                    if not ser["vlanId"] == int(conn["vlan"]):
                                        count += 1
                            if "sub-networks" in conn and "sub-networks" in ser:
                                clrm_support_functions.__validate_clusterAndHostProfile_vs_spt_switch_connections(self, ser["sub-networks"], conn["sub-networks"], count)
                            elif "sub-networks" in conn and "sub-networks" not in ser:
                                clrm_support_functions.__validate_clusterAndHostProfile_vs_spt_switch_connections(self, [ser], conn["sub-networks"], count)
        return count

    @staticmethod
    def __validate_cluster_multiNicVMotion(cluster_conn, count):
        """This function will validate the multiNicVMotion in cluster
          Usage: __validate_cluster_multiNicVMotion(cluster_conn, count)
         """
        for conn1 in cluster_conn:
            if "uplinks_status" in conn1:
                list1 = []
                active_list = []
                standby_list = []
                for k in conn1["uplinks_status"]:
                    for key, value in k.items():
                        if key == "active":
                            if value:
                                active_list.append(k["name"])
                            else:
                                standby_list.append(k["name"])
                if "sub-networks" in conn1:
                    for conn2 in conn1["sub-networks"]:
                        if isinstance(conn2, dict):
                            for k1, v1 in conn2.items():
                                if k1 == "purpose":
                                    if v1 == "VMMigration":
                                        list1.append(v1)
                if list1:
                    if len(list1) == (len(active_list) + len(standby_list)):
                        if len(active_list) == 1:
                            logger._log_to_console_and_log_file("The %s network is active on port %s " % conn1["name"] % active_list)
                        else:
                            logger._log_to_console_and_log_file("multiNicVMotion validation failed")
                            count += 1
        return count

    @staticmethod
    def get_hypervisor_cluster_profile_by_name(fusion_client, cluster_name):
        """
        This is place holder function.
        Needs Implementation for this.
        """
        result, status = fusion_client.Get_Cluster_Profile(cluster_name)
        return result, status

    @staticmethod
    def validate_hypervisorClusterProfile_indexing(fusion_client, cluster_name):
        """
        This function is to validate the Hypervisor cluster profile indexing
        Usage: validate_hypervisorClusterProfile_indexing(fusion_client, cluster_name)
        """
        count = 0
        result, status = clrm_support_functions.get_hypervisor_cluster_profile_by_name(fusion_client, cluster_name)
        if not status:
            logger._log_to_console_and_log_file("Cluster %s does not exists" % cluster_name)
            return False
        HHP_Uris = []
        storage_volumes = []
        for k, v in result.items():
            if k == "hypervisorHostProfileTemplate":
                for k1, v1 in v.items():
                    if k1 == "serverProfileTemplateUri":
                        SP_uri = v1
            if k == "hypervisorClusterUri":
                Cluster_uri = v
            if k == "hypervisorHostProfileUris" and v is not None:
                for i in v:
                    HHP_Uris.append(i)
            if k == "uri":
                clusterProfile_uri = v
            if k == "status":
                cluster_status = v
            if k == "state":
                cluster_state = v
            if k == "sharedStorageVolumes" and v is not None:
                for i in v:
                    for k1, v1 in i.items():
                        if k1 == "storageVolumeUri":
                            storage_volume = v1
                    storage_volumes.append(storage_volume)
        default_hdrs = fusion_client.get_default_hdrs()
        status, xapi_version = fusion_client.get_xapi_version()
        if not status:
            logger._log_to_console_and_log_file("Could not get the X-API-Version")
            return False
        default_hdrs["X-API-Version"] = xapi_version
        fusion_client._http.set_headers(default_hdrs)

        cat_url = fusion_client.uri['index-by-category'] + "hypervisor-cluster-profiles"
        resp = fusion_client.get(cat_url)
        flag = False
        for key, value in resp.items():
            if key == "members":
                for i in value:
                    if i["uri"] == clusterProfile_uri:
                        flag = True
                        for key1, value1 in i.items():
                            if key1 == "state":
                                if value1 != cluster_state:
                                    logger._log_to_console_and_log_file("The state of Cluster profile is not compatible in category indexing")
                                    return False
                            if key1 == "status":
                                if value1 != cluster_status:
                                    logger._log_to_console_and_log_file("The status of Cluster profile is not compatible in category indexing")
                                    return False
                if not flag:
                    logger._log_to_console_and_log_file("The Cluster profile is not found in category indexing")
                    return False

        url = fusion_client.uri['index-by-associations'] + clusterProfile_uri
        response = fusion_client.get(url)
        for k, v in response.items():
            if k == "total":
                logger._log_to_console_and_log_file("Total number of assciations is %s" % v)
            if k == "members":
                for i in v:
                    for k1, v1 in i.items():
                        if k1 == "parentUri":
                            if not v1 == clusterProfile_uri:
                                logger._log_to_console_and_log_file("Cluster Profile Uri is not matching")
                                count += 1
                                return False
                        if k1 == "name":
                            if v1 == "HYPERVISOR_CLUSTER_PROFILE_TO_SERVER_PROFILE_TEMPLATE":
                                if not i["childUri"] == SP_uri:
                                    logger._log_to_console_and_log_file("Server Profile Uri is not matching")
                                    count += 1
                            if v1 == "HYPERVISOR_CLUSTER_PROFILE_TO_HYPERVISOR_CLUSTER":
                                if not i["childUri"] == Cluster_uri:
                                    logger._log_to_console_and_log_file("Cluster Uri is not matching")
                                    count += 1
                            if v1 == "HYPERVISOR_CLUSTER_PROFILE_TO_HYPERVISOR_HOST_PROFILE":
                                if not i["childUri"] in HHP_Uris:
                                    logger._log_to_console_and_log_file("Host Profile Uri is not matching")
                                    count += 1
                            if v1 == "HYPERVISOR_CLUSTER_PROFILE_TO_STORAGE_VOLUME":
                                if not i["childUri"] in storage_volumes:
                                    logger._log_to_console_and_log_file("Storage volume Uri is not matching")
                                    count += 1
        if count > 0:
            logger._log_to_console_and_log_file("validation failed for %s items in indexing by association" % count)
            return False
        logger._log_to_console_and_log_file("validation of indexing for Hypervisor Cluster Profile is successful")
        return True

    def get_all_server_hardwares_in_appliance(self):
        """ Gets the list of all server hardwares available in Oneview Appliance
            Usage: get_server_hardwares_in_appliance(fusion_client)
        """
        response = self.fusionlib.fusion_api_get_resource("/rest/enclosures")
        all_server_hardware_list = []
        for enc in response['members']:
            bays = clrm_support_functions._get_device_bays_in_enclosure(self, enc)
            all_server_hardware_list.append(bays)
        return all_server_hardware_list

    def _get_device_bays_in_enclosure(self, enclosure):
        """ Gets the list of all server hardwares available in an Enclosure
            Usage: _get_device_bays_in_enclosure(fusion_client, enclosure))
        """
        server_hardware_list_in_enclosure = []
        for bay in enclosure['deviceBays']:
            if bay['deviceUri'] is not None:
                bay_info = {}
                resp = self.fusionlib.fusion_api_get_resource(bay['deviceUri'])
                bay_info['category'] = resp['category']
                bay_info['state'] = resp['state']
                bay_info['uri'] = resp['uri']
                bay_info['name'] = resp['name']
                bay_info['serverHardwareTypeUri'] = resp['serverHardwareTypeUri']
                bay_info['powerState'] = resp['powerState']
                bay_info['locationUri'] = resp['locationUri']
                bay_info['status'] = resp['status']
                if bay_info['category'] == "server-hardware":
                    server_hardware_list_in_enclosure.append(bay_info)
        return server_hardware_list_in_enclosure

    def get_spts_in_appliance(self):
        """ Gets the list of all server profile templates available in Oneview Appliance
            Usage: get_spts_in_appliance(fusion_client)
        """
        response = self.fusionlib.fusion_api_get_resource("/rest/server-profile-templates")
        all_spt_list = []
        for spt in response['members']:
            spt_info = {}
            spt_info['name'] = spt['name']
            spt_info['serverHardwareTypeUri'] = spt['serverHardwareTypeUri']
            all_spt_list.append(spt_info)
        return all_spt_list

    def get_host_profiles_from_cluster_profile(self, cluster_name):
        """ Gets the list of names of server hardware associated with host profiles of a cluster profile
            Usage: get_host_profiles_from_cluster_profile(fusion_client, cluster_name)
        """
        server_hardware_in_host_profiles = []
        if cluster_name is None:
            return server_hardware_in_host_profiles
        param = '?filter=name==%s' % cluster_name
        result = self.fusionlib.fusion_api_get_hypervisor_cluster_profile(uri=None, api=None, headers=None, param=param)
        if result['count'] == 0:
            return server_hardware_in_host_profiles
        if len(result["members"][0]["hypervisorHostProfileUris"]) != 0:
            for hp in result["members"][0]["hypervisorHostProfileUris"]:
                response = self.fusionlib.fusion_api_get_resource(hp)
                response_sp = self.fusionlib.fusion_api_get_resource(response["serverProfileUri"])
                response_sh = self.fusionlib.fusion_api_get_resource(response_sp["serverHardwareUri"])
                server_hardware_name = response_sh["name"]
                server_hardware_in_host_profiles.append(server_hardware_name)
        return server_hardware_in_host_profiles

    def select_free_servers(self, spt_for_cluster, num_of_servers):
        """ Selects the list of free servers for cluster creation available in Oneview Appliance
            Usage: select_free_servers(fusion_client, spt_for_cluster, num_of_servers)
        """
        spt_hardware_type = None
        available_spts = clrm_support_functions.get_spts_in_appliance(self)
        for spt in available_spts:
            for k, v in spt.iteritems():
                if k == 'name' and v == spt_for_cluster:
                    spt_hardware_type = spt['serverHardwareTypeUri']
        hardware_list = []
        available_server_hardwares = clrm_support_functions.get_all_server_hardwares_in_appliance(self)
        for enc in available_server_hardwares:
            for ser in enc:
                for k, v in ser.iteritems():
                    if k == 'serverHardwareTypeUri' and v == spt_hardware_type:
                        if ser['state'] == 'NoProfileApplied' and ser['status'] == 'OK' and ser['powerState'] == 'Off':
                            hardware_list.append(ser['name'])
        return hardware_list[:num_of_servers]

    def select_assigned_servers_to_delete(self, num_of_profiles, cluster_name=None):
        """ Selects the list of servers to be removed from cluster
            Usage: select_assigned_servers_to_delete(fusion_client, num_of_profiles, cluster_name=None)
        """
        hostProfiles = clrm_support_functions.get_host_profiles_from_cluster_profile(self, cluster_name)
        if len(hostProfiles) >= num_of_profiles:
            return hostProfiles[:num_of_profiles]
        return hostProfiles
