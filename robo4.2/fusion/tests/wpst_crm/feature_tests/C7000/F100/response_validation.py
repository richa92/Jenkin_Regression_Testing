
codes = {'connection-templates-CRM_DEFAULT_INVALID_ARGUMENT': {'errorCode': 'CRM_DEFAULT_INVALID_ARGUMENT', 'status_code': 400, 'message': 'Updating connection-template: Invalid bandwidth: Maximum bandwidth exceeds 20 GBits/s', 'recommendedActions': None},
         'fcoe-networks-CRM_CHANGING_VLAN_ID': {'errorCode': 'CRM_CHANGING_VLAN_ID', 'status_code': 400, 'message': 'VLAN ID can NOT be changed.', 'recommendedActions': None},
         'CRM_VALUE_OUT_OF_RANGE': {'errorCode': 'CRM_VALUE_OUT_OF_RANGE', 'status_code': 400, 'message': 'Value is out of range.', 'recommendedActions': None},
         'CRM_MISSING_VLAN_ID_IN_NETWORK': {'errorCode': 'CRM_MISSING_VLAN_ID_IN_NETWORK', 'status_code': 400, 'message': None, 'recommendedActions': None},
         'CRM_DUPLICATE_NETWORK_NAME': {'errorCode': 'CRM_DUPLICATE_NETWORK_NAME', 'status_code': 400, 'message': None, 'recommendedActions': None},
         'network-sets-CRM_INVALID_NETWORK_URI': {'errorCode': 'CRM_INVALID_NETWORK_URI', 'status_code': 400, 'message': 'the type of the network URI passed is not valid. This call requires ethernet-networks URI. Please provide a valid ethernet-networks URI.', 'recommendedActions': None},
         'CRM_MAX_FCOE_NETWORKS_REACHED': {'errorCode': 'CRM_MAX_FCOE_NETWORKS_REACHED', 'status_code': 400, 'message': 'FCoE network * cannot be created because the maximum number of FCoE networks (256) exists.', 'recommendedActions': None},
         }


'''
    <textString name="anotherUplinkSet">
        <version number="*" value="Another UplinkSet is using one of the ports."/>
    </textString>

    <textString name="ADDRESS_FORMAT_VMAC-errorCode">
        <version number="*" value="ADDRESS_FORMAT_VMAC"/>
    </textString>

    <textString name="ADDRESS_FORMAT_VSN-errorCode">
        <version number="*" value="ADDRESS_FORMAT_VSN"/>
    </textString>

    <textString name="ADDRESS_FORMAT_VWWN-errorCode">
        <version number="*" value="ADDRESS_FORMAT_VWWN"/>
    </textString>

    <textString name="AUTHORIZATION-errorCode">
        <version number="*" value="AUTHORIZATION"/>
    </textString>

    <textString name="AUTHN_LOCAL_LOGIN_DISABLED-errorCode">
        <version number="*" value="AUTHN_LOCAL_LOGIN_DISABLED"/>
    </textString>

    <textString name="AUTHN_LOCAL_LOGIN_DISABLED-message">
        <version number="*" value="Local user authentication was disabled by the appliance security administrator."/>
    </textString>

    <textString name="AUTHN_AUTH_DIR_FAIL-errorCode">
        <version number="*" value="AUTHN_AUTH_DIR_FAIL"/>
    </textString>

    <textString name="AUTHN_UNABLE_AUTH-errorCode">
        <version number="*" value="AUTHN_UNABLE_AUTH"/>
    </textString>

    <textString name="AUTHN_LOGOUT_FAILED-errorCode">
        <version number="*" value="AUTHN_LOGOUT_FAILED"/>
    </textString>

    <textString name="BIOS_SETTING_FAILED_ERROR-errorCode">
        <version number="*" value="BIOS_SETTING_FAILED_ERROR"/>
    </textString>

    <textString name="BW_TOTAL_LINKRATE_OVERFLOW_ERROR-errorCode">
        <version number="*" value="BW_TOTAL_LINKRATE_OVERFLOW_ERROR"/>
    </textString>

    <textString name="BW_TOTAL_LINKRATE_OVERFLOW_ERROR-message">
        <version number="*" value="Total requested bandwidth of \d+ Gb/s from connections \[\d+, \d+, \d+, \d+\] exceeds physical link capacity of \d+ Gb/s." type="regex"/>
    </textString>

    <textString name="BW_TOTAL_LINKRATE_OVERFLOW_ERROR-recommendedActions">
        <version number="*" value="Edit the requested bandwidth on these connections and try again."/>
    </textString>

    <textString name="BW_NETWORKMAXBW_OVERFLOW_ERROR-errorCode">
        <version number="*" value="BW_NETWORKMAXBW_OVERFLOW_ERROR"/>
    </textString>

    <textString name="BW_NETWORKMAXBW_OVERFLOW_ERROR-message">
        <version number="*" value="Requested bandwidth \(\d+ Gb/s\) exceeds the maximum bandwidth \(\d+ Gb/s\) configured on the network for connection \d+." type="regex"/>
    </textString>

    <textString name="BW_NETWORKMAXBW_OVERFLOW_ERROR-recommendedActions">
        <version number="*" value="Verify parameters and try again."/>
    </textString>

    <textString name="CRM_BW_EXCEEDS_20GB-errorCode">
        <version number="*" value="CRM_DEFAULT_INVALID_ARGUMENT"/>
    </textString>

    <textString name="CRM_BW_EXCEEDS_20GB-message">
        <version number="*" value="Updating connection-template: Invalid bandwidth: Maximum bandwidth exceeds 20 GBits/s"/>
    </textString>

    <textString name="CRM_MAX_FCOE_NETWORKS_REACHED-errorCode">
        <version number="*" value="CRM_MAX_FCOE_NETWORKS_REACHED"/>
    </textString>

    <textString name="CRM_MAX_FCOE_NETWORKS_REACHED-message">
        <version number="*" value="FCoE network \w cannot be created because the maximum number of FCoE networks (256) exists." type="regex"/>
    </textString>

    <textString name="CRM_DUPLICATE_NETWORK_NAME-errorCode">
        <version number="*" value="CRM_DUPLICATE_NETWORK_NAME"/>
    </textString>

    <textString name="CRM_ID_NOT_UUID-errorCode">
        <version number="*" value="CRM_ID_NOT_UUID"/>
    </textString>

    <textString name="CRM_NETWORK_SET_CONSTRAINT_A_VIOLATION-errorCode">
        <version number="*" value="CRM_NETWORK_SET_CONSTRAINT_A_VIOLATION"/>
    </textString>

    <textString name="CRM_VALUE_OUT_OF_RANGE-message">
        <version number="*" value="Value is out of range."/>
    </textString>

    <textString name="CRM_VALUE_OUT_OF_RANGE-errorCode">
        <version number="*" value="CRM_VALUE_OUT_OF_RANGE"/>
    </textString>

    <textString name="FTS.DNS_CONFIG-errorCode">
        <version number="*" value=".*FTS.DNS_CONFIG" type="regex"/>
    </textString>

    <textString name="FTS.DNS_CONFIG-invalid_ddns_dns_message">
        <version number="*" value="OverrideDhcpDnsServers specified in conjunction with DNS configuration data."/>
    </textString>

    <textString name="FTS.DNS_CONFIG-invalid_domain_name_message">
        <version number="*" value="The specified domain name has an invalid format:.*." type="regex"/>
    </textString>

    <textString name="FTS.DNS_CONFIG-invalid_nameserver_message">
        <version number="*" value="The specified DNS server address has an invalid format:.*." type="regex"/>
    </textString>

    <textString name="FTS.DNS_CONFIG-v6_off_nameserver_message">
        <version number="*" value="The DNS server at .* cannot be used because its IP address family is not configured." type="regex"/>
    </textString>

    <textString name="DUPLICATED_PROFILE_NAME-errorCode">
        <version number="*" value="DUPLICATED_PROFILE_NAME"/>
    </textString>

    <textString name="DuplicateMultipleNetworksPerPortError-errorCode">
        <version number="*" value="DuplicateMultipleNetworksPerPortError"/>
    </textString>

    <textString name="DuplicateNetworksPerPortError-errorCode">
        <version number="*" value="DuplicateNetworksPerPortError"/>
    </textString>

    <textString name="DUPLICATE_BOOT_ORDER-errorCode">
        <version number="*" value="DUPLICATE_BOOT_ORDER"/>
    </textString>

    <textString name="DUPLICATE_PRIMARY_BOOT_CONNECTION-errorCode">
        <version number="*" value="DUPLICATE_PRIMARY_BOOT_CONNECTION"/>
    </textString>

    <textString name="DUPLICATED_PROFILE_NAME-errorCode">
        <version number="*" value="DUPLICATED_PROFILE_NAME"/>
    </textString>

    <textString name="DUPLICATE_SECONDARY_BOOT_CONNECTION-errorCode">
        <version number="*" value="DUPLICATE_SECONDARY_BOOT_CONNECTION"/>
    </textString>

    <textString name="ENCGRP_USEDNAME-errorCode">
        <version number="*" value="ENCGRP_USEDNAME"/>
    </textString>

    <textString name="FIRMWARE_DELETED-errorCode">
        <version number="*" value="FIRMWARE_DELETED"/>
    </textString>

    <textString name="EnclosureBayUnavailableForProfile-errorCode">
        <version number="*" value="EnclosureBayUnavailableForProfile"/>
    </textString>

    <textString name="ENC_RESOURCE_NOT_FOUND-errorCode">
        <version number="*" value="ENC_RESOURCE_NOT_FOUND"/>
    </textString>

    <textString name="FINAL_ATTRIBUTE_CHANGED-errorCode">
        <version number="*" value="FINAL_ATTRIBUTE_CHANGED"/>
    </textString>

    <textString name="FTS.APPLIANCE_SETUP-errorCode">
        <version number="*" value=".*FTS.APPLIANCE_SETUP" type="regex"/>
    </textString>

    <textString name="FTS.APPLIANCE_SETUP-message">
        <version number="*" value="Host name is required."/>
    </textString>

    <textString name="FTS.NET_CONFIG-errorCode">
        <version number="*" value=".*FTS.NET_CONFIG" type="regex"/>
    </textString>

    <textString name="FTS.NET_CONFIG-invalid_hostname_message">
        <version number="*" value="Host name has an invalid format."/>
    </textString>

    <textString name="FTS.NET_CONFIG-missing_ip_message">
        <version number="*" value="The appliance-1 IPv4 address is required for static configurations."/>
    </textString>

    <textString name="FTS.NET_CONFIG-invalid_ip_message">
        <version number="*" value="The appliance-1 IPv4 address has an invalid format:*." type="regex"/>
    </textString>

    <textString name="FTS.NET_CONFIG-invalid_gw_message">
        <version number="*" value="The IPv4 gateway address has an invalid format:*." type="regex"/>
    </textString>

    <textString name="FTS.NET_CONFIG-not_same_subnet_message">
        <version number="*" value="The appliance-1 IPv4 and IPv4 gateway addresses are not in the same subnet (.*)." type="regex"/>
    </textString>

    <textString name="FTS.NET_CONFIG-missing_subnet_message">
        <version number="*" value="The IPv4 subnet mask address is required for static configurations."/>
    </textString>

    <textString name="FTS.NET_CONFIG-invalid_subnet_message">
        <version number="*" value="The IPv4 subnet mask address has an invalid format:.*." type="regex"/>
    </textString>

    <textString name="GetNetworkError-errorCode">
        <version number="*" value="GetNetworkError"/>
    </textString>

    <textString name="INVALID_ADDR-errorCode">
        <version number="*" value="INVALID_ADDR"/>
    </textString>

    <textString name="INVALID_FW_CONFIG-errorCode">
        <version number="*" value="INVALID_FW_CONFIG"/>
    </textString>

    <textString name="INVALID_LICENSE_KEY-errorCode">
        <version number="*" value="INVALID_LICENSE_KEY"/>
    </textString>

    <textString name="INVALID_PARAMETER_SH_NOT_MATCH_SHT-errorCode">
        <version number="*" value="INVALID_PARAMETER_SH_NOT_MATCH_SHT"/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST-errorCode">
        <version number="*" value="INVALID_POWER_CONTROL_REQUEST"/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST-recommendedActions">
        <version number="*" value="Change the power control request specifying an operation and target power state appropriate to the present server power state."/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST_POWER_COLDBOOT_OFF-errorCode">
        <version number="*" value="INVALID_POWER_CONTROL_REQUEST_POWER_COLDBOOT_OFF"/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST_POWER_COLDBOOT_OFF-recommendedActions">
        <version number="*" value="Power the server on to boot the server."/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST_POWER_RESET_OFF-errorCode">
        <version number="*" value="INVALID_POWER_CONTROL_REQUEST_POWER_RESET_OFF"/>
    </textString>

    <textString name="INVALID_POWER_CONTROL_REQUEST_POWER_RESET_OFF-recommendedActions">
        <version number="*" value="Power the server on to reset the server."/>
    </textString>

    <textString name="INVALID_REQUESTED_BANDWIDTH-errorCode">
        <version number="*" value="INVALID_REQUESTED_BANDWIDTH"/>
    </textString>

    <textString name="INVALID_REQUESTED_BANDWIDTH-message">
        <version number="*" value="Bandwidth request is not valid \(\d+\.\d+ Gb/s\) for connection \d+." type="regex"/>
    </textString>

    <textString name="INVALID_REQUESTED_BANDWIDTH-recommendedActions">
        <version number="*" value="Verify that the bandwidth parameter is in the increments of \(\d+.\d+ Gb/s\). Specify a bandwidth value between the minimum \(\d+.\d+ Gb/s\) and the maximum \(\d+ Gb/s\) and try again." type="regex"/>
    </textString>

    <textString name="INVALID_SECONDARY_BOOT_CONNECTION-errorCode">
        <version number="*" value="INVALID_SECONDARY_BOOT_CONNECTION"/>
    </textString>

    <textString name="DUPLICATED_PROFILE_NAME-errorCode">
        <version number="*" value="DUPLICATED_PROFILE_NAME"/>
    </textString>

    <textString name="INVALID_PARAMETER_SH_NOT_MATCH_EG-errorCode">
        <version number="*" value="INVALID_PARAMETER_SH_NOT_MATCH_EG"/>
    </textString>

    <textString name="INVALID_PARAMETER_SH_NOT_MATCH_SHT-errorCode">
        <version number="*" value="INVALID_PARAMETER_SH_NOT_MATCH_SHT"/>
    </textString>

    <textString name="INVALID_PREFIX-errorCode">
        <version number="*" value="INVALID_PREFIX"/>
    </textString>

    <textString name="INVALID_FILTER-errorCode">
        <version number="*" value="INVALID_FILTER"/>
    </textString>

    <textString name="INVALID_OVERRIDDEN_SETTINGS-errorCode">
        <version number="*" value="INVALID_OVERRIDDEN_SETTINGS"/>
    </textString>

    <textString name="LICENSE_ALREADY_EXISTS-errorCode">
        <version number="*" value="LICENSE_ALREADY_EXISTS"/>
    </textString>

    <textString name="LOCALE_NOT_SUPPORTED-message">
        <version number="*" value="Appliance does not support the provided locale."/>
    </textString>

    <textString name="OVERLAPPING_POOLRANGE-errorCode">
        <version number="*" value="OVERLAPPING_POOLRANGE"/>
    </textString>

    <textString name="PORT_FUNCTION_NOT_SUPPORTED-errorCode">
        <version number="*" value="PORT_FUNCTION_NOT_SUPPORTED"/>
    </textString>

    <textString name="POWER_CONTROL_NOT_ALLOWED-errorCode">
        <version number="*" value="POWER_CONTROL_NOT_ALLOWED"/>
    </textString>

    <textString name="POWER_CONTROL_NOT_ALLOWED-recommendedActions">
        <version number="*" value="Try the operation later after the profile configuration has completed."/>
    </textString>

    <textString name="reapplyConfig">
        <version number="*" value="The reapply configuration .* completed on $name." type="regex"/>
    </textString>

    <textString name="SERVER_NOT_OFF-errorCode">
        <version number="*" value="SERVER_NOT_OFF"/>
    </textString>

    <textString name="ServerNotOffProfileEdit-errorCode">
        <version number="*" value="ServerNotOffProfileEdit"/>
    </textString>

    <textString name="SPP_ID_INVALID-errorCode">
        <version number="*" value="SPP_ID_INVALID"/>
    </textString>

    <textString name="UNABLE_TO_REMOVE_ACTIVEPROFILE-errorCode">
        <version number="*" value="UNABLE_TO_REMOVE_ACTIVEPROFILE"/>
    </textString>

    <textString name="UNABLE_TO_REMOVE_ACTIVEPROFILE-message">
        <version number="*" value=".* is hosting active server profiles." type="regex"/>
    </textString>

    <textString name="UNSUPPORTED_BIOS_SETTINGS-errorCode">
        <version number="*" value="UNSUPPORTED_BIOS_SETTINGS"/>
    </textString>

    <textString name="UNSUPPORTED_FWBASELINE-errorCode">
        <version number="*" value="UNSUPPORTED_FWBASELINE"/>
    </textString>

    <textString name="refreshStorageStatus">
        <version number="*" value="Updated storage system with serial number \w*\." type="regex"/>
    </textString>

    <textString name="diffDomain">
        <version number="*" value="Storage pool $name has moved to a different domain."/>
    </textString>

    <textString name="deletedPool">
        <version number="*" value="Storage pool is not present on the storage system."/>
    </textString>

    <textString name="unableRefreshPool">
        <version number="*" value="Unable to refresh storage pool."/>
    </textString>

    <textString name="unableCreateVolume">
        <version number="*" value="Unable to create volume $name."/>
    </textString>

    <textString name="unableUpdateVolume">
        <version number="*" value="Unable to update volume."/>
    </textString>

    <textString name="invalidMissing">
        <version number="*" value="Invalid or missing data in input."/>
    </textString>

    <textString name="criticalPool">
        <version number="*" value="The associated storage pool is in a critical state."/>
    </textString>

    <textString name="notFound">
        <version number="*" value="Not Found"/>
    </textString>

    <textString name="createdVolume">
        <version number="*" value="Created volume $name on storage system .* in pool \w*\." type="regex"/>
    </textString>

    <textString name="configureSanError">
        <version number="*" value="An error occurred while configuring SAN storage."/>
    </textString>

    <textString name="editProfileError">
        <version number="*" value="Unable to edit server profile: $name"/>
    </textString>

    <textString name="resourceNotFound">
        <version number="*" value="Resource not found."/>
    </textString>

    <textString name="invalidView">
        <version number="*" value="Invalid view parameter ($view)."/>
    </textString>

    <textString name="invalidMetric">
        <version number="*" value="Metric request specified unrecognized metric name ($fields) or unsupported sample interval (-)."/>
    </textString>

</data>

'''

# #######################################
default_variables = {'codes': codes
                     }


def get_variables():

    variables = default_variables
    return variables
