"""
 A mechanism to lookup an expected message so that the message doesn't need to be hard coded and
 also allows for message sharing

 This is used by Wait For Task2

 Messages that contain a ${variable}, must have those variables passed to WFT2
 For example:  Wait For Task2    ${resp}    errorMessage=ethernet_exists    VERBOSE=${True}    name=Net777

 Regexp is supported but '\' must be doubly escaped as in "\\\\w*\\\\d{3}" to match Net777
   errorMessages = {'ethernet_exists': 'A network with the name \\\\w*\\\\d{3} already exists.'}

"""

errorMessages = {
    'ethernet_exists': 'A network with the name ${name} already exists.',
    'Unsupported_DE_patch': 'Unsupported drive enclosure patch operation.',
    'Invalid_SAS': 'Invalid SAS Interconnect Power configuration operation.',
    'Invalid_profile_initiator_name': 'The iSCSI initiator name is not valid. It either has invalid characters or is too long.',
    'Invalid_boot_initiator_name': 'The boot initiator name is invalid. It either has invalid characters or is too long.',
    'Invalid_secondary_boot': 'Secondary boot connection is not valid.',
    'Invalid_secondary_boot_connection': 'There is a \\\\"Secondary\\\\" boot connection without a matching \\\\"Primary\\\\" boot connection of the same function type.',  # F963
    'Multiple_primary_boot': 'Primary boot on connection \\\\d* is not valid',
    'Multiple_secondary_boot': 'Secondary boot on connection \\\\d* is not valid',
    'ProfileAlreadyExistsInServer': 'A profile is already assigned to the server hardware {/rest/server-hardware/*}.',
    'Invalid_flexNIC': 'An invalid FlexNIC is selected for connection \\\\d*. When using the Ethernet function type, PXE or iSCSI boot can only be enabled on FlexNIC "a" of a port.',  # F791
    'Invalid_iSCSI_and_BIOS_boot_mode': 'The server hardware does not support connections using an Ethernet function type with iSCSI boot parameters in legacy BIOS boot mode.',
    'Invalid_ethernet_with_iSCSI_boot': 'The server hardware does not support connections with an Ethernet function type and iSCSI boot parameters.',  # F963
    'Connection_initiator_name_non_unique': 'All bootable connections using an Ethernet function type and iSCSI boot parameters must share the same initiator name.',
    'No_iSCSI_boot_for_PXE_boot_order': 'Bootable iSCSI connections are not allowed with bootable PXE connections when the boot order is set to \\"PXE\\" in UEFI boot mode\\.',
    'Profile_network_set_ethernet': 'Network sets are not supported with the Ethernet function type when iSCSI parameters are enabled.',
    'Profile_network_set_iscsi': 'Network sets are not supported with the iSCSI function type when iSCSI parameters are enabled.',
    'DFRM_INSUFFICIENT_DRIVE_COUNT': "The local storage configuration for the Mezz 1 SAS controller requires 1 drives more than the maximum number of physical drives that this controller can manage \\\\{256\\\\}.",
    'DirectFabricJbodInvalidNumMinSizeGb': 'The minimum physical drive size for the SAS logical JBOD \\"\\\\w*, bay \\\\d{1,2}\\" is not valid.',
    'UNSUPPORTED_RAID_LEVEL_660': "The requested RAID level \\\\(RAID22\\\\) is not supported by the server hardware type: SY 660 Gen9 \\\\d.",
    'MORE_THAN_ONE_BOOTABLE_LOGICAL_DRIVE': 'The local storage settings are invalid because more than one bootable logical drive was specified.',
    'Invalid_flexNIC_for_iSCSI_function': 'The requested function type is not supported on connection \\\\d.',  # F791
    'Profile_network_set_iSCSI': 'Network sets are not supported with the iSCSI function type when iSCSI parameters are enabled.',  # F791
    'Chap_Name_too_long': 'The Chap name \\\\w* is invalid. This could be due to invalid characters, or due to the name not fitting within the permitted length of 1-223 characters.',
    'MutualChap_Name_too_long': 'The MutualChap name \\\\w* is invalid. This could be due to invalid characters, or due to the name not fitting within the permitted length of 1-223 characters.',
    'Invalid_Chap_Secret': 'The Chap secret related to connection \\\\d* is invalid due to invalid characters or length. For text \\\\(ASCII\\\\) secrets, 12-16 characters are required. For hex secrets, it must fit the format of "0x" followed by 24-32 hex digits.',
    'Invalid_MutualChap_Secret': 'The MutualChap secret related to connection \\\\d* is invalid due to invalid characters or length. For text \\\\(ASCII\\\\) secrets, 12-16 characters are required. For hex secrets, it must fit the format of "0x" followed by 24-32 hex digits.',
    'SW_iSCSI_Invalid_Chap_Secret': 'The Chap secret related to connection \\\\d* is invalid due to invalid characters or length. 12-16 ASCII characters are required for SW iSCSI with CHAP authentication',
    'SW_iSCSI_Invalid_MutualChap_Secret': 'The MutualChap secret related to connection \\\\d* is invalid due to invalid characters or length. 12-16 ASCII characters are required for SW iSCSI with CHAP authentication',
    'Invaid_initiator_vlan_id_for_tagged_untagged_network': 'The boot VLAN ID can only be specified for tunneled networks\\.',  # F791
    'FINAL_ATTRIBUTE_CHANGED': 'MAC Addresses Setting attribute cannot be changed.',
    'UNKNOWN_SERVER_TYPE': "Unable to determine the server hardware type '/bad_sht_uri'.",
    'INVALID_ENCLOSURE_GROUP': 'Unable to determine the enclosure group {/rest/EnclosureGroup_\\\\\w*_not_found}.',
    'AUTHORIZATION': 'Authorization error: User not authorized for this operation.',
    'Hardware_iSCSI_Invaid_initiator_vlan_id_for_tunnel_network': 'The boot VLAN id, when specified, must be between 1 and 4095 for tunnel networks.',  # F346
    'Software_iSCSI_Invaid_initiator_vlan_id_for_tunnel_network': 'A boot VLAN ID cannot be specified for Ethernet connections containing iSCSI parameters.',  # F791
    'IscsiDuplicateInitiatorIpAddress': 'The iSCSI initiator IP address "\\\\d*.\\\\d*.\\\\d*.\\\\d*" is being used by multiple connections in this profile.',  # F791
    'Boot_initiator_subnet_required': 'The boot initiator subnet mask must be specified.',
    'BootVlanIdNotOptional': 'The boot VLAN id can only be specified for tunneled networks.',
    'ISCSI_BOOT_VLAN_ID_NOT_SUPPORTED': 'An boot VLAN ID cannot be specified for iSCSI Ethernet connections using tunneled networks.',
    'Referenced_by_server_profile': 'A server profile template cannot be deleted while it is being referenced by server profiles',
    'Insufficient_Power': 'The power operation request did not succeed.',
    'User_Exists': 'The user name of the user already exists: ${name}.',
    'LIG_Exists': 'Another logical interconnect group with that name already exists: ${name}',
    'Invalid_functionType': 'The requested function type is not supported on connection 1.',
    'Boot_VLAN_Id_Only_Tunnel': 'The boot VLAN ID can only be specified for tunneled networks\\.',  # F648
    'Invalidate_LUN_MLPT_VSA': 'Unable to validate LUN values. Since the storage system is configured for Multiple LUNs Per Target \\\\(MLPT\\\\), the LUN value must be in the range 1\\.\\.255 to attach the volume',  # F313/F1247
    'LUN_not_unique_MLPT_VSA': 'Unable to validate LUN values. The LUN value must be unique to attach the volume',  # F313/F1247
    'Unsupported_DataProtectionLevel_VSA': 'Unable to create or update the volume because the given data protection level is not supported by the storage system.',  # F313/F1247
    'No_port_configuration': 'No storage system port configuration is valid for the request to attach',  # F313/F1247
    'Invalid_LUN_SLPT_VSA': 'Unable to validate LUN values. Since the storage system is configured with Single LUN Per Target \\\\(SLPT\\\\), the LUN value must be zero to attach volume ',  # F313/F1247
    'Mixed_paths_VSA': 'Unable to use a mix of enabled and disabled paths on the specified storage system',  # F313/F1247
    'Bootable_volume_nonbootable_connection': 'Volume [\\\\w\\\\W]* is marked bootable, but the volume is not configured with an enabled storage path using a bootable connection',  # F313/F1247
    'SP_Bootable_connection_nonbootable_volume': 'A bootable volume attachment is not specified for the iSCSI connection \\\\d*.',  # F313
    'SPT_Bootable_connection_nonbootable_volume': 'Connection \\\\d* is configured to boot from a managed volume, but no managed volume is selected for boot.',  # F1247
    'More_than_one_boot_volume': 'More than one volume attachment is set to \'Primary\' boot priority. Only one attachment can be marked as \'Primary\'\.',  # F963
    'Only_private_boot_volume': 'Volume .* is not private\\. Only private volumes can be selected as bootable\\.',  # F963
    'Storage_path_disabled_not_exist': "Volume {\\\"name\\\":\\\".*\\\", \\\"uri\\\":\\\"/rest/storage-volumes/[A-F0-9]{8}(-[A-F0-9]{4}){3}-[A-F0-9]{12}\\\"} is specified as bootable, but the volume is not configured with an enabled storage path using a bootable connection\.",  # F963
    'Already_attached_to_different_host': 'because it is already attached to a different host',  # F963
    'Multiple_bootable_volumes': 'Two or more volume attachments are specified as bootable\\.',  # F313/F1247
    'SP_attach_private_presented_volume': 'The volume \\{.*\\} is configured as a private volume in OneView, but it is presented to at least one other host on the storage system.',  # F313
    'SPT_attach_exist_private_volume': 'The attachment to existing private volume \\{.*\\} is not allowed.',  # F1247
    'Invalid_dhcp_server_profile_with_ip_address': 'The iSCSI initiator IP for connection \\\\d is being assigned via DHCP and cannot be added or modified',  # F1249
    'Invalid_dhcp_server_profile_template_with_subnetmask_or_gateway': 'The subnet mask and gateway attributes are not allowed for iSCSI connections using DHCP.',  # F1249
    'SPT_non_unique_ATAI': 'The associatedTemplateAttachmentId attribute "\\\\d*" is not unique within the context of the profile template ".*"',  # F1247(OVF1071)
    'SPT_invalid_ATAI': 'The associatedTemplateAttachmentId attribute for attachment \\\\d* in server profile template ".*" cannot be explicitly set to -1.',  # F1247/OVF1071
    'SPT_edit_existing_ATAI': 'Cannot change the attribute "associatedTemplateAttachmentId" for existing volume attachments in a profile template.',  # F1247/OVF1071
    'SP_ATAI_mismatch_storage_pool': 'A volume attachment and associated template attachment must use the same storage pool.',  # F1247/OVF1071
    'CONFIGURE_AMBIENT_TEMP_MODE_POWERON_WARNING': 'The ambient temperature mode setting has been applied to this logical enclosure.  However, the following server hardware was powered on, and must be power cycled to activate the new ambient temperature mode setting.*',
    'Encountered issues re-applying the configuration on enclosures': 'Encountered issues re-applying the configuration on enclosures*',
    'Server_Not_off_Profile_Edit': 'The profile operation did not succeed because server hardware .* is powered on',
    'Shareable_volume_not_supported': 'The attachment to pending volume \\\\".*\\\\" has invalid value for volumeShareable attribute.',  # F1321
    'Invalid_iSCSI_target_data_managed_volume': 'Target iSCSI volume data in the iSCSI boot connection \\\\d is not valid when using a managed volume.',  # F1321
    'Managed_Volume_No_Bootable_Connections': 'Volume .* with attachment ID \\\\d is specified as bootable, but the volume attachment is not configured with an enabled storage path that uses a connection specified to boot from a managed volume\\.',  # F1321, F963, OVF1086
    'iSCSI_initiator_IP_required': 'The IP address source must be specified.',  # 1231
    'Legacy_Bios_Not_Supported_for_SW_iSCSI': 'Connection \\\\d on network \\{\\\\"name\\\\":\\\\".*\\\\", \\\\"uri\\\\":\\\\".*\\\\"\\} is invalid. The server hardware does not support connections using an Ethernet function type with iSCSI boot parameters in legacy BIOS boot mode.',
    'INVALID_PROFILE_BOOT_URL': 'The value specified for managing BIOS settings is not valid or not supported\\.\\\\\\nInvalid value specified for one or more BIOS settings: \\\\\\n\\\\\\"Boot from URL \\\\d\\\\\\" is not within the valid length range \\\\(0-254\\\\) or it contains invalid characters that do not match the regular expression ',  # OVF706
    'INVALID_TEMPLATE_BOOT_URL': 'Invalid value specified for one or more BIOS settings: \\\\\\n\\\\\\"Boot from URL \\\\d\\\\\\" is not within the valid length range \\\\(0-254\\\\) or it contains invalid characters that do not match the regular expression ',  # OVF706
    'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6': 'The PXE boot policy \\\\(IPv4ThenIPv6\\\\) is not valid\\.',  # OVF1308
    'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4': 'The PXE boot policy \\\\(IPv6ThenIPv4\\\\) is not valid\\.',  # OVF1308
    'Invalid_lunType_SLPT_VSA': 'The attachment .* is set to \\\\"Manual\\\\" for Lun type on a single LUN per target \\\\(SLPT\\\\) storage system',
    'DE_Maintenance_Power': 'Unable to power (off|on) the Drive Enclosure. The Drive Enclosure is in maintenance state due to an ongoing support dump or firmware update operation.',  # OVS6667
    'DE_Maintenance_Refresh': 'Unable to refresh the Drive Enclosure. The Drive Enclosure is in maintenance state due to an ongoing support dump or firmware update operation.',  # OVS6667
    'DE_Maintenance_Reset': 'Unable to reset the Drive Enclosure. The Drive Enclosure is in maintenance state due to an ongoing support dump or firmware update operation.',  # OVS6667
    'SASIC_Maintenance': 'Unable to update the interconnect. The interconnect is in maintenance state due to an ongoing support dump or firmware update operation.',  # OVS6667
    'SASIC_Maintenance_Terse': 'The interconnect is in a maintenance state due to a firmware update or support dump operation.',  # OVS6667
    'Unable_Reapply': 'Unable to reapply the configuration.',
    'Unable_Reserve_JBOD': 'Unable to reserve the SAS logical JBOD named \\"${name}\\".',
    'Unable_Release_JBOD': 'Unable to release the SAS logical JBOD named \\"${name}\\".',
    'Unable_Update_From_Group': 'Unable to update from group.* firmware update operation.',
    'match_any_string': '\w*',
    'MULTIPLE_REPOSITORY_NOT_SUPPORTED_ERROR': 'Adding multiple external repository is currently not supported.',
    'EXTERNAL_FW_BUNDLE_DELETE_NOT_SUPPORTED_ERROR': 'This firmware bundle can not be removed as it exists only in the external repository external.',
    'INVALID_VOLUME_NAME': "Unable to set the property 'name' because the value does not meet the requirements set by the volume template.",  # OVF959
    'INVALID_VOLUME_DESCRIPTION': "Unable to set the property 'description' because the value does not meet the requirements set by the volume template.",  # OVF959
    'INVALID_VOLUME_SIZE': "Invalid or missing capacity specified for volume\\. Volume .*\\.",  # OVF959
    'VOLUME_SIZE_TOO_LARGE': 'Unable to create or update the volume because the specified capacity exceeds the required free capacity necessary to provision the volume for the given storage system.',  # OVF959
    'VOLUME_DATA_PROTECTION_LEVEL_LOCKED': "Unable to set the field 'dataProtectionLevel' because it is locked by the template.",  # OVF959
    'INVALID_VOLUME_DATA_PROTECTION_LEVEL': "Unable to set the property 'dataProtectionLevel' because the value does not meet the requirements set by the volume template\\. Volume .*\\.",  # OVF959,OVF961
    'INVALID_VOLUME_SHARABLE': "Unable to set the property 'isShareable' because the value does not meet the requirements set by the volume template\\. Volume .*\\.",  # OVF959,OVF961
    'VOLUME_SHARABLE_MUST_BE_TRUE_OR_FALSE': "The value specified for the boolean field 'isShareable' must be 'true' or 'false'.",  # OVF959
    'VOLUME_ISSHAREABLE_MUST_BE_FALSE': 'Volume .* attachment ID \\\\d requires the "isShareable" attribute to be "false" when creating a new volume from a server profile\\.',  # OVF959
    'UNABLE_TO_CREATE_VOLUME': 'Unable to create or update the volume\\. Volume .*\\.',  # OVF959
    'VOLUME_PROVISIONING_TYPE_LOCKED': "Unable to set the field 'provisioningType' because it is locked by the template.",  # OVF959
    'INVALID_VOLUME_PROVISIONING_TYPE': "The provisioning type provided is invalid\\. Volume .*\\.",  # OVF959
    'INVALID_VOLUME_STORAGE_POOL': "The required property 'storagePool' with value '.*' contains incorrect syntax.",  # OVF959
    'MISSING_VOLUME_TEMPLATEURI': 'The volume attachment with id \\\\d is missing one or more required fields: \\\\[volume\\.templateUri\\\\]\\.',  # OVF959
    'MISSING_VOLUMEURI_FIELD': 'The volume attachment with id \\\\d is missing one or more required fields: \\\\[volumeUri\\\\]\\.',  # OVF959
    'UNEXPECTED_ERROR': 'An unexpected error occurred',
    'iSCSI_Ethernet_on_same_Virtual_Function': 'Function type is iSCSI for port \\\\w* \\\\(\\\\w*\\\\) \\\\d:\\\\d-b and is Ethernet for port \\\\w* \\\\(\\\\w*\\\\) \\\\d:\\\\d-b\\. The connection request is not valid\\.',  # 648
    'NULL_VOLUME_NAME': 'Unable to create a volume with a null or empty name\\\\. Volume \\\\"null\\\\" with attachment ID \\\\d\\\\.',  # OVF959
    'INVALID_RESOURCE': 'Unable to access {"name":"resource", "uri":".*"}.  It might have been deleted.',  # OVF5
    'INVALID_SCOPE': 'Unable to access {"name":"scope", "uri":".*"}.  It might have been deleted.',  # OVF5
    'NOT_AUTHORIZED_ERROR': 'This user session is not authorized to perform the action.',  # OVF5
    'CREATION_NOT_AUTHORIZED_ERROR': 'Resource creation in the specified scope is not authorized. The scope does not match the user session permissions or does not exist.',  # OVF5
    'ASSOCIATION_FORBIDDEN_BY_SCOPE': 'This user session is not authorized to associate .* with this resource.',  # OVF5
    'Invalid_Public_Key_Length': 'Key length of the certificate is not valid.Resource : .*',  # OVF688_OVS6749
    'VSA_not_attached_to_network': 'No storage system port configuration is valid for the request to attach',  # OVF1072
    'PATCH_not_supported': 'PATCH operation replace on path /sanstorage/regenerateChapSecrets is not supported in xApi version \\\\d+.',  # OVF1537
    'Cannot_regenerate_CHAP_unless_server_powered_off': 'Cannot regenerate CHAP secrets unless the server hardware is powered off.',  # OVF1537
    'INVALID_NETWORK_ON_STORAGE_PATH': 'Attachment with id \\\\d has a storage path referencing connection \\\\d, but its storage system \\\\{\\\\"name\\\\":\\\\\".*\\\\", \\\\\"uri\\\\\":\\\\\".*\\\\"\\\\} is not attached to \\\\{\\\\"name\\\\":\\\\".*\\\\", \\\\"uri\\\\":\\\\"\\\\/rest\\\\/.*\\\\/.*\\\\"\\\\}\\.',  # OVF961
    'SecureBoot_unsupported_SHT': 'Secure boot cannot be managed by HPE OneView on the specified server hardware type.',  # OVF2161
    'SecureBoot_invalid_value': 'The secure boot value \\\\(enabled\\\\) is not valid\\\\.',  # OVF2161
    'SecureBoot_unsupported_boot_mode': 'Secure boot can only be managed in UEFI optimized boot mode.',  # OVF2161
    'ADD_POWER_DEVICE_WITH_WRONG_PWD': 'The supplied user name and/or password is not valid for the specified iPDU.',    # OVF358
    'LDA_IOBYPASS_UNSUPPORTED': 'Logical drive accelerator cannot be set to IO Bypass because it is only supported on SSD drives.',  # OVF899
    'Invalid_Cert_Alias_Name': 'Invalid alias name format',  # OVF688_OVS5874
    'Invalid_X509_Cert': 'Certificate is malformed',  # OVF688_OVS5874
    'Expired_Cert': 'One or more certificates have expired.*',  # OVF688_OVS5874
    'Delete_Cert_Error': 'Unable to delete the input certificate. No matching certificate found for the specified alias',  # OVF2422_OVS13134
    'Not_Effective_Cert': 'The certificate is not valid yet based on the current time on the appliance',  # OVF688_OVS5874
    'CA_Signed_Leaf_Not_Import': 'Unable to trust the incoming certificate.',  # OVF688_OVS5874
    'Same_Cert_Can_Not_Import': 'Unable to import the certificate. \\\s The alias ${ALIASNAME} is already associated with another certificate.',  # OVF688_OVS5874
    'MISSING_REQUIRED_FIELD_VOLUME': 'One or more required fields are missing\\. Volume .*\\.',  # OVF961
    'Cert_Revoked_Error': 'The certificate is revoked.',  # OVF2422_OVS11000
    'CRM_PORTS_EXCEED_MAX_PER_UPLINKSET': 'The uplink set .* contains more than 16 ports.',
    'CRM_INVALID_UPLINK_SET_PORT': 'Invalid uplink set: Port: .* for interconnect-type: .* is not an uplink port.',
    'CRM_INVALID_UPLINK_PORT_FOR_I3S': 'Uplink ports X1 and X2 are dedicated for Image Streamer uplink sets on the Virtual Connect SE 100Gb F8 Module.',
    'CRM_INVALID_INTERNAL_OS_DEPLOYMENT_PORT': 'Port .* is not a supported port for Image Streamer uplink set.',
    'CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS': 'An uplink set may not contain both split and un-split uplink ports.',
    'CRM_DELETE_NOT_ALLOWED_FOR_ASSOCIATED_PVLAN_NETWORK': 'Network\\\(s\\\) .*${name}.* cannot be removed from the uplink set because they are part of a private VLAN domain configuration in the network set.',  # OVF3500
    'CRM_PRIMARY_NETWORK_INVALID_FOR_CONNECTION': 'An internal error occurred and has been logged at approximately .* is a primary network, cannot be used to create connections.',
    'CRM_MAX_NUMBER_OF_PVLAN_DOMAINS_EXCEEDED': 'The number of private VLAN domains exceeds the maximum supported limit of 256.',
    'UnsupportedPrivateVlanNetworkSetMissingIsolated': 'Connection 1 references a network set .*${ns}.* that includes a primary network .*${primary_nw}.* but does not have corresponding secondary network .*${secondary_nw}.* in the network set.',
    'Import_Certificate': 'Certificate for the supplied proxy server is not imported to the appliance.',  # OVS5158
    'NOT_AUTHORIZED_SCOPE': 'Not authorized to manage scope assignments for .*',  # OVF1592
    'RESOURCE_NOT_SCOPABLE_ERROR': 'Cannot update scope assignments for .*',  # OVF1592
    'STORAGE_POOL_DOES_NOT_MATCH_TEMPLATE': 'The storage pool specified for the volume is not associated with the storage system specified in the volume template\\. Volume .*\\.',  # OVF959, OVF961
    'Valid_Certificate_Chain': 'Given certificate chain is either invalid \\\\(or\\\\) import of certificate chain is not allowed.',  # OVF2422_OVS11000
    'INVALID_NONVC_PORTID_EMPTY': 'Port must be specified for connection .* with network .*\\.',  # OVF518
    'INVALID_NONVC_PORTID_NONE': 'Connection \\".*\\" must have a defined portId and cannot be set to \\"None\\" for unmanaged connections\\.',  # OVF518
    'INVALID_NONVC_PORTID_AUTO': 'Connection \\".*\\" must have a defined portId and cannot be set to \\"Auto\\" for unmanaged connections\\.',  # OVF518
    'INVALID_NONVC_MAPPED_PORT': 'The network .* for the connection on physical port .* is not available on logical interconnect group .*\\.',  # OVF518
    'INVALID_NONVC_DIRECT_ATTACH': 'Connection \\".*\\" references networkUri \\".*\\" with fabricType \\"DirectAttach\\"\\. Direct attach networks are not supported by Fibre Channel interconnects\\.',  # OVF518
    'INVALID_NONVC_PORT_TYPE': 'Connection .* cannot be automatically assigned to a port because network .* is not assigned to a Virtual Connect interconnect, and/or the server hardware does not include an adapter that can access network .*\\.',  # OVF518
    'INVALID_NONVC_BOOT_ATTRIBUTES': 'Unmanaged connections do not support boot attributes\\.',  # OVF518
    'INVALID_NONVC_REQUESTED_BANDWIDTH': 'The requested bandwidth cannot be specified for unmanaged connection .*\\.',  # OVF518
    'UNABLE_TO_VERIFY_CERTIFICATE': 'Unable to verify the server certificate.',    # OVF354
    'CA_cert_Not_Import': 'Unable to trust the incoming certificate.',   # OVF354
    'Cert.SSL_CERTIFICATE_MISSING_DELETE_ERROR': 'Unable to delete the input certificate. No matching certificate found for the specified alias.',   # OVF354
    'SERVER_ALREADY_LICENSED_ILO': 'License already installed.',  # OVS28827
    'SERVER_ALREADY_LICENSED_NONE_AVAILABLE': 'No available \\"HPE OneView Advanced\\" licenses.',  # OVS28827
    'SERVER_ALREADY_LICENSED_PERMANENT': 'Server already licensed.',  # OVS28827
    'Certificate_Already_Exists': 'Import Certificate task already exists for same certificate.',  # OVF2422_OVS20734
    'Invalid_Cert_Alias_Name_FIPS_CNSA_SERVER': 'Invalid alias name format. Resource : .*',  # OVF2422_20734
    'Invalid_Cert_Alias_Name_FIPS_CNSA_CA': 'Invalid alias name format.',  # OVF2422_20734
    'Invalid_Public_Key_Length_FIPS_CNSA': 'Key length of the certificate is not valid.',  # OVF2422_OVS20734
    'SDBOOT_Invalid_settings': 'The value specified for managing boot settings is not valid or not supported.',    # OVS27399: OVTC36893
    'Invalid_Boot_Value': 'The boot order list contains invalid or duplicate values or does not conform to the boot order specification.',  # OVS27399: OVTC36894
    'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME': 'The value \\".*\\" is not permitted for argument \\"userName\\".',  # OVF2972 iLO config local users
    'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING': 'Argument \\".*\\" is not recognized for setting type \\"LocalAccounts\\".',  # OVF2972 iLO config local users
    'ILO_CONFIG_LOCAL_ACCOUNT_EXCEED_MAX': 'Argument \\"localAccounts\\" exceeds maximum bound of 8.',  # OVF2972 iLO config local users
    'ILO_CONFIG_UNSUPPORTED_SHT': 'Configuring the iLO settings via profile is not supported for server model \\"ProLiant BL460c G7\\".',  # OVF2972 iLO config local users
    'DuplicateBootVolumePriority': 'More than one volume attachment is set to \\"Primary\\" boot priority\\. Only one attachment can be set to \\"Primary\\"\\.',
    'ShareablePendingVolumeAttachmentNotSupported': 'The attachment to pending volume \".*\" has invalid value for \"isShareable\" attribute.',
    'ILO_PASSWORD_TO_SHORT': 'Argument \\\\"password\\\\" is below minimum bound of 8 for iLO setting \\\\"Manage administrator account\\\\".',
    'ILO_PASSWORD_TO_LONG': 'Argument \\"password\\" exceeds maximum bound of 39 for iLO setting \\"Manage administrator account\\".',
    'DFRM_SAS_LOGICAL_JBOD_UNABLE_TO_DELETE_ZONE': "Unable to delete SAS logical JBOD from the SAS logical interconnect {0}.",
    'CRM_NO_CERTIFICATE_SIGNING_REQUEST_IN_PROGRESS': 'Unable to retrieve the HTTPS certificate data. There is no certificate signing request in progress',
    'CRM_DUPLICATE_CERTIFICATE_SIGNING_REQUEST': 'A certificate signing request has already been initiated. Only one CSR per interconnect is allowed.',
    'CRM_MISSING_REQUIRED_FIELD_FOR_HTTPS_CERTIFICATES': 'The certificate signing request is missing the following required fields: .*.',
    'CRM_DEFAULT_INTERNAL_SERVER_EXCEPTION': 'Internal error',
    'UNRECOGNIZED_JSON_FIELD': 'Unrecognized JSON field.',  # OVF959, OVF961 for negative tests
    'PhysicalFunctionTypeCannotChange': 'Function type has changed for the connection with id \\\\d*. The connection request is not valid.',
    'CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY': 'The interconnect in bay \\\\d+ has exceeded the maximum number of allowed FC networks.',
    'CRM_MAX_FC_NETWORKS_EXCEEDED': 'The number of FC networks has exceeded the maximum limit of 30.',
    'CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH': 'Fibre Channel uplink set template ports are spanning multiple interconnects.',
    'CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK': 'The uplink set can only contain a maximum of 1 Fibre Channel network.',
    'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE': 'The port specified is not Fibre Channel or uplink capable',
    'CRM_PORTS_IN_DIFFERENT_SWITCH': 'Fibre Channel uplink set, ".*", ports are spanning multiple interconnects',
    'CRM_PORT_ALREADY_ASSIGNED': 'Port\\\\(s\\\\) Q.* are being used by another uplink set.',
    'CRM_PORT_NUMBER_UNKNOWN_FORMAT': 'The portNumber is of an unknown format.',
    'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT': 'Desired port speed is invalid for uplink. Valid values are 8/16/32Gb for Virtual Connect SE 100Gb F32 Module.',
    'SERVER_ALREADY_ADDED': 'The server hardware has already been added as .*.',
    'CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED': 'The network set operation failed because the maximum number of networks (4000) has been exceeded.',
    'CRM_LS_DELETE_PROFILE_CONNECTIONS_ASSOCIATED': 'The logical switch cannot be deleted while profiles are assigned to ports within this logical switch.',
    'FABRIC_DELETE_SWITCH_ASSOCIATED_WITH_LS': 'The fabric cannot be removed while there are logical switches.* associated with this fabric.',
    'DUPLICATE_PORT_CONNECTION': 'Connection ID \\\\d is requesting to use port .*, but it is already in use by another connection.',
    'DFRM_SAS_LOGICAL_JBOD_UNABLE_TO_DELETE_SP_EXISTS': 'Unable to delete logical JBOD. It is assigned to server profile *.',  # OVF900
    'InvalidWwpn': 'The user-defined WWPN \\\\(.*\\\\) is not valid.',  # OVF520
    'DuplicateWwpnForAssignedProfiles': 'The WWPN specified for connection \\\\d+ is used by another assigned server profile. All WWPNs specified for assigned server profiles must be unique.',  # OVF520
}
