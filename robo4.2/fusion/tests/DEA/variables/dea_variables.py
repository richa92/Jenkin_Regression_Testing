""" All the variables defined within default_variables will automatically get loaded
    when a variables file is loaded from a Robot Resource file
    Variables should be named in all UPPERCASE or using CamelCase
    underscore or spaces can be used in variable named, for example Fan_Status
"""

default_variables = {
    # Altair Variables
    "ALTAIR_ADMIN_USERNAME": 'Administrator',
    "ALTAIR_DEFAULT_ADMIN_PASSWORD": 'Tbird123',
    "AlTAIR_ADMIN_PASSWORD": 'Tbird123',
    "ALTAIR_IP": '10.15.50.30',
    "ILO_TOOLS": '/tools/mpconfig.jar',
    "Operating_System": 'Linux 7 x86_64',
    "OS_Build_Plan": 'Smoke Windows 2012 R2 + SPP Smoke',

    # Smoke Test:: Altair server for 10.64 Network
    "ALTAIR_IP_1064": '10.64.0.40',

    # do not change this value
    "GIT_REPO_ROOT": "",
    "RESOURCE_ROOT": '/fusion/tests/DEA/resource',
    "VARIABLE_ROOT": '/fusion/tests/DEA/variables',
    "EM_RESOURCE_ROOT": '/mgmtfw/tests/thunderbird/resources',
    "EM_VARIABLES_ROOT": '/mgmtfw/tests/thunderbird/variables',
    "FUSION_FRU_ROOT": '/fusion/tests/dea/hal/fru_bin',

    # Fusion variables
    "APPLIANCE_IP": '10.16.24.254',
    "FUSION_USERNAME": 'Administrator',
    "FUSION_PASSWORD": 'Tbird123',
    "APPLIANCE_IPV6": 'fe80::9eb6:54ff:fe98:5150',
    "NTP_invalid_IP": 'fe80::250:56ff:fe11:1234',
    "FUSION_NIC": 'bond0',
    "FUSION_PROMPT": '#',
    "FUSION_TIMEOUT": 20,
    "Test_Flag": "Tbird",
    "Status_Code": 202,
    "SSH_HOST": '10.16.27.254',
    "SSH_USERNAME": 'root',
    "SSH_PASSWORD": 'hpvse1',
    "FUSION_ALERTTYPE_PREFIX": 'hpris',
    "Status_Code_200": 200,
    "Bandwidth_Mod_Value": 8000,
    "active_cim": '10.16.27.254',
    "standby_cim": None,
    # OA Variables
    "OA_IP": '10.15.19.254',
    "OA_USERNAME": 'Administrator',
    "OA_Password": 'PEtest123',
    "iLO_Admin_Password": 'Tbird123',

    # VC Variables
    "VC_IP": '10.15.4.40',
    "VC_USERNAME": 'Administrator',
    "VC_PASSWORD": 'HGKP8P6Q',

    # iLO Variables
    "ilo_ip": '10.16.96.96',
    "iLO_UserName": 'Administrator',
    "iLO_Password": 'Tbird123',
    "iLO_Adapter_Dir": 'NetworkAdapters',
    "iLO_Adapter_Slot": '1',
    "iLO_Adapter_Directory": 'NetworkAdapters',
    "iLO_Adapter_Position": '1',

    # Email Notify variables
    "Sender": 'deafusionqa@hpe.com',
    "Receiver": 'PE-TEST_Representatives@hpe.com',
    "Subject": '',
    "Content": '',
    "Server_Name": 'Condor',
    "CAT_Name": 'CAT1 SE: [OV 4.20]:',
    "SMTP_Server": 'smtp3.hpe.com',
    "AutoVM_IP": '\\10.15.53.34\\',
    # Device Model variables
    "ICM_Model_Carbon": 'Virtual Connect SE 16Gb FC Module for Synergy',
    "ICM_Model_Potash": 'Virtual Connect SE 40Gb F8 Module for Synergy',
    "ICM_Model_SuperShaw": 'HP VC FlexFabric-20/40 F8 Module',
    "ICM_Model_8Gb_FC_Module": 'HP VC 8Gb 24-Port FC Module',
    "ICM_Model_16Gb_FC_Module": 'HP VC 16Gb 24-Port FC Module',
    # Device Bay variables
    "bay": 2,
    "fan_bay1": 1,
    "fan_bay2": 2,
    "ICM_Bay": 3,
    "ICM_Bay2": 1,
    "ICM_Bay3": 2,
    "ICM_Bay4": 5,
    "ICM_Bay_Port": 'Q1',
    "ICM_Bay2_Port": 'Q1',
    "ICM_Bay3_Port": 'Q1.1',
    "ICM_Bay4_Port": 'Q1.1',
    "ICM_Bay_FC1": 1,
    "ICM_Bay_FC2": 4,
    "ICM_C7000_Bay1": 1,
    "ICM_C7000_Bay2": 2,
    "ICM_C7000_Bay3": 3,
    "ICM_C7000_Bay4": 4,
    "ICM_C7000_Bay5": 5,
    "ICM_C7000_Bay6": 6,
    "ps_bay": 1,
    "SAS_Bay1": 1,
    "SAS_Bay2": 4,
    "Server_Bay": 1,
    "EM_Bay": 1,
    "Adapter_Mezz_Slot": 3,

    "Bronco_UEFI_bay": 1,
    "Quiz_UEFI_bay": 2,
    "Ember_UEFI_bay": 3,
    "Quartz_UEFI_bay": 3,
    "Electron_UEFI_bay": 1,

    "Bronco_Legacy_bay": 8,
    "Quiz_Legacy_bay": 6,
    "Ember_Legacy_bay": 7,
    "Quartz_Legacy_bay": 7,
    "Electron_Legacy_bay": 8,
    "Adapter_Bay": 1,

    # profile varialbes
    "requestedBW": 5000,

    # 3PAR Storage variables
    "OS_Type": 'Windows 2012 / WS2012 R2',
    "volumeCapacity": '42949672960',
    "3PAR_IP": '10.15.30.30',
    "3PAR_Uname": '3paradm',
    "3PAR_Pwd": '3pardata',
    "3PAR_Name": 'DEA3parTesting',
    "3PAR_StorageURI": 'DEA3parTesting',
    "3PAR_poolName": 'FC_r1',
    "3PAR_Domain": 'DEA',
    "3PAR_SerialNumber": '1612973',
    "FCoE_WWPN": '20:21:00:02:AC:00:32:AD',
    "FCoE_WWPN2": '21:21:00:02:AC:00:32:AD',
    "FC_WWPN": '21:11:00:02:AC:00:32:AD',
    "FC_WWPN2": '20:11:00:02:AC:00:32:AD',
    "FC_WWPN3": '21:12:00:02:AC:00:32:AD',
    "FC_WWPN_NULL": '00:00:00:00:00:00:00:00',
    "3PAR_portName_FCoE": '0:2:1',
    "3PAR_portName_FC": '1:1:1',
    "3PAR_managed_portname_FCoE": '0:2:1',
    "3PAR_managed_portname_FC": '1:1:1',

    # Smoke Test: 3PAR Storage Volume to bay
    "3PAR_Vol_Bay7": "DEA_Bay7_Volume",
    "3PAR_Vol_Template_Name": "DEA_Volume_Template",

    # VSA iSCSI Storage variables
    "iSCSI_Boot_Target_IP": '10.15.1.150',
    "iSCSI_Boot_Target_IP_NULL": '10.15.1.155',
    "iSCSI_ipv4_1015": '10.15.1.200',
    "iSCSI_ipv4_2019": '10.202.32.11',

    # Mezz Model Variables
    "Bronco_Model": 'Synergy 3820C 10/20Gb CNA',
    "Ember_Model": 'Synergy 3520C 10/20Gb CNA',
    "Quiz_Model": 'Synergy 2820C 10Gb CNA',
    "Quartz_Model": 'Synergy 3830C 16G FC HBA',
    "Electron_Model": 'Synergy 3530C 16G HBA',

    # Server Model Variables
    "Blackbird_Model": 'Synergy 480 Gen9 Compute Module',
    "Redbird_Model": 'Synergy 660 Gen9 Compute Module',
    "Bigbird_Model": 'Synergy D3940 Storage Module',
    "Firebird_Model": 'Synergy 6x0 Gen9 Compute Module',
    "Firebird_2s_Model": 'Synergy 620 Gen9 Compute Module',
    "Firebird_4s_Model": 'Synergy 680 Gen9 Compute Module',
    "Server_Gen": 'Gen9',

    # Test Flag
    "Test_Tag": 'Bronco',
    "Adapter_Name": 'Breezy',

    # Wait variables
    "EM_SET_FACTORY_WAIT": 900,
    "EM_Failover_Wait": 300,
    "Server_Boot_Wait": 900,
    "Server_Boot_Wait_Legacy": 1200,

    # Request body variables
    # "Enclosures": 'CN754408RZ',
    "Enclosures": 'MXQ705086B',
    "Ethernet_Name": 'Test_Enet',
    "FC_Name": 'Test_FC',
    "FC_Name1": 'Test_FC1',
    "FC_Name2": 'Test_FC2',
    "FC_Name3": 'Test_FC_NULL',
    "FCOE_Name": 'Test_FCoE',
    "FCOE_Name2": 'Test_FCoE2',
    "FCOE_Name3": 'Test_FCoE_NULL',
    "LIG_Name": 'Lig-Tbird',
    "LIG_Name2": "Lig-Tbird2",
    "LIG_Name3": 'Lig-Tbird3',
    "LIG_Name4": "Lig-Tbird4",
    "LIG_Name_FC": 'Lig-TbirdFC',
    "LIG_Name_FC1": 'Lig-FC1',
    "LIG_Name_FC2": 'Lig-FC2',
    "SAS_Name1": 'SAS_LIG1',
    "SAS_Name2": 'SAS_LIG2',
    "Encl_Grp_Name": 'Encl_Grp',
    "Logical_Encl_Name": 'Logical_Encl',
    "ethernet_vlan_id": 1015,
    "FC_Type": 'FibreChannel',
    "minPSForRedundantPowerFeed": '2',
    "ServerHardware": 'MXQ645026W, bay 1',
    "port_assignment": 'Auto',
    "id_primary": 1,
    "id_secondary": 2,
    # Multi-Variables
    "Ethernet_Name1": 'VLAN1015',
    "Ethernet_Name2": 'VLAN85',
    "Ethernet_Name3": 'VLAN10',
    "Ethernet_Name4": 'VLAN27',
    "Ethernet_vlanID_1064": "1064",
    "NetworkSet_Name": 'NS01',
    "NetworkSet_Name2": 'NS02',
    "NetworkSet_Name3": 'NS03',
    # Smoke Test: Port's connection names
    "Eth_Port_Conn_Name": "Connection Bay Ethernet",
    "FCoE_Port_Conn_Name": "Connection Bay FCoE",
    "FC_Port_Conn_Name": "Connection Bay FC",

    # Smoke Test: enclosure use in Smoke Test Suite
    "Encl_Uri_Name": "MXQ706000W",
    # EM Switch Ports for Mgmt and CIManager
    "EM_switch_port_mgmt_bay1": 122,
    "EM_switch_port_mgmt_bay2": 222,
    "EM_switch_port_cim_bay1_port1": 113,
    "EM_switch_port_cim_bay1_port2": 114,
    "EM_switch_port_cim_bay2_port1": 213,
    "EM_switch_port_cim_bay2_port2": 214,
    "Stand_By_Cim_IP": '10.15.9.254',
    "CIM_developer_tar_path": 'impala.rsn.rdlabs.hpecorp.net/fusion_setup/setup_customized_fusion.tar',

    # alerts variable
    "El_Blade_UnsupportedDeviceFault": 'BladeUnsupportedDeviceFault',
    "El_FrontPanel_UnsupportedDeviceFault": 'FrontPanelUnsupportedDeviceFault',
    "El_Fan_UnsupportedDeviceFault": 'FanUnsupportedDeviceFault',
    "El_CIM_UnsupportedDeviceFault": 'CIManagerUnsupportedDeviceFault',
    "El_PS_UnsupportedDeviceFault": 'PowerSupplyUnsupportedDeviceFault',
    "El_Interconnect_UnsupportedDeviceFault": 'InterconnectUnsupportedDeviceFault',
    "EL_Em_FuseFault": 'EmFuseFault',
    "EL_Ring_NoStandby_MgmtPort": 'RingNoStandbyMgmtPort',
    "EL_Ring_NoStandby_MgmtPort_Cleared": 'RingNoStandbyMgmtPortCleared',
    "Front_Panel_Thermal_Read_Sensor": 'FrontPanelThermalReadSensor',
    "Front_Panel_Thermal_Read_Sensor_Cleared": 'FrontPanelThermalReadSensorCleared',
    "Em_DiskEncryptionFault": 'EmDiskEncryptionFault',
    "Em_DiskEncryptionFaultCleared": 'EmDiskEncryptionFaultCleared',
    "Em_TpmFwUpdateFault": 'EmTpmFwUpdateFault',
    "Em_TpmFwUpdateFaultCleared": 'EmTpmFwUpdateFaultCleared',

    # Enclosure Device Type Variables
    "FANDevice_EM": 'FAN',
    "PSDevice_EM": 'PS',
    "ICMDevice_EM": 'ICM',
    "BladeDevice_EM": 'SERVER',
    "FLMDevice_EM": 'FLM',
    "CIMDevice_EM": 'CIM',
    "Active_Node": "Active",
    "Standby_Node": "Standby",
    "Device_Wait_Time": '600',
    "interval": '5',
    "CIM_Device_Wait_Time": '1200',
    "CIM_Device_interval": '30',
    # SPP upload and firmware update
    "LE_Name": 'Logical_Encl',
    "SPP_FilePath": 'c:\\SPP\SPP2017100.2017_0810.43.iso',
    "FirmwareBaseline": '2017.10.0',
    "ForceInstallFirmware": 'False',
    "FirmwareUpdateOn": 'SharedInfrastructureAndServerProfiles',
    "LogicalInterconnectUpdateMode": 'Parallel',
    "UpdateFirmwareOnUnmanagedInterconnect": 'False',
    "NetworkType": ['ethernet-networkV4', 'fc-networkV4', 'fcoe-networkV4', 'iSCSI-networkV4'],
    "FirmwareUpdateIsNonDisruptive": 'False',
    "LocalControlFilePath": '/fusion/tests/DEA/Misc/localOVemRegistryFile.json',
    "MCTPDisabled_Alert": 'server-hardware.devices.adapter.discover',
    "MCTPEnabled_ALert": 'Trap.cpqNic3ConnectivityRestored',
    "OneView_Backup_Local_Path": 'C:\\Ov_Backup\\',
    "Server_Virtual_MACfault_AlertID": 'profilemgr.ServerHardware.ProfileAppliedServerDiffPersonality',
    # Resource Category Variables For Different OV Alerts
    "Enclosure_category": 'enclosures',
    "ICM_Category": 'interconnects',
    "Server_Category": 'server-hardware',
    "Drive_enclosure_Category": 'drive-enclosures',
    "SupportDump_Path": 'c:\\PETest_ovSupportDumps\\Regression_Runs',

    # PE-TEST  FLM  Alert Variables
    "EM_NTP_Time_sync": 'EmNTPTimeSync',
    "EM_NTP_Time_sync_Cleared": 'EmNTPTimeSyncCleared',
}


def get_variables(fusion_ip=None, switch=None):
    """ Variable files can have a special get_variables method that returns variables as a mapping.
    """
    variables = default_variables
    return variables
