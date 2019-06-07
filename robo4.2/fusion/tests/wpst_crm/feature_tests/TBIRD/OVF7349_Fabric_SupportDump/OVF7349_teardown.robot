*** Settings ***
Documentation    OVF7349 tear down

Variables        ./data_OVF7349.py

Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FC_Nitro_OVF3323/DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py


*** Test Cases ***
Teardown
	Set Log Level    TRACE
	Log    [TEARDOWN]
	Fusion Api Login Appliance    ${appliance_ip}    ${admin_credentials}
	Power off ALL Servers    PressAndHold
	Remove All Server Profiles
	Remove All Server Profile Templates
	Remove ALL LS
	Remove ALL LSGs
    Remove All LEs
	Remove ALL Enclosure Groups
	Remove ALL LIGs
	Remove ALL Ethernet Networks
	Remove ALL FC Networks
	Remove ALL FCoE Networks
	Remove ALL Network Sets

	Remove OneView Config From CFM    ${oneview_config['host']}    ${cfm_ip}    ${cfm_credentials}
	Remove All Fabrics
	Remove ALL Users
