*** Settings ***
Resource    					cho_resource_pre-requisites.txt
Suite Setup                     Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
Suite Teardown                  Fusion Api Logout Appliance

*** Test Cases ***
Add Licenses
	[Tags]    SETUP		LICENSES
    [Documentation]		Add Licenses to OneView
    Set Log Level	TRACE
	${licenses} =	Get Variable Value	${licenses}
	Run Keyword If	${licenses} is not ${null}  	Add Licenses from variable  ${licenses}  ${VERIFY}
	
Add Users
	[Tags]    SETUP		USERS
    [Documentation]		Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    Set Log Level	TRACE
	${users} =	Get Variable Value	${users}
	Add Users from variable  ${users}

Add San Manager
	[Tags]    SETUP		SAN-MANAGER
    [Documentation]		Add SAN Manager to OneView
	${responses}=  Add Non Existing San Managers  ${san_managers}
	Run Keyword for List  ${responses}  Wait For Task2
	Verify Resources for List  ${expected_san_managers}

Add Ethernet Networks
	[Tags]    SETUP		ETHERNET-NW
    [Documentation]		Add Ethernet Networks to OneView
    Set Log Level	TRACE
	Run Keyword If	${ethernet_networks} is not ${null}  	Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FCOE networks
	[Tags]	SETUP	FCOE-NW
	[Documentation]		Add FCOE Networks to OneView
	Set Log Level	TRACE
	Run keyword If	${fcoe_networks} is not ${null}		Add FCoE Networks from variable async	${fcoe_networks}  ${VERIFY}  ${expected_fcoe_networks}
	
Add Network Sets
	[Tags]    SETUP		NW-SETS
    [Documentation]		Add Network Sets to OneView
    Run Keyword If	${networksets} is not ${null}  	Add Networks Sets from variable async  ${networksets}  ${VERIFY}  ${expected_networksets}

Add Storage Systems and Verify
	[Tags]    SETUP		S-SYS
	[Documentation]		Add Storage Systems to OneView
	Set Log Level	TRACE
	${responses}=  Add Non Existing Storage Systems  ${storage_systems}
	Run Keyword for List  ${responses}  Wait For Task2
	${edit_responses}=  Edit Storage Systems  ${storage_systems}
	Run Keyword for List    ${edit_responses}  Wait For Task2
	Verify Resources for List  ${expected_storage_systems}

Add LIG
	[Tags]    SETUP		LIG
    [Documentation]		Add LIG to OneView
	Run Keyword If	${ligs} is not ${null}  	Add LIG from list  ${ligs}

Add EG
	[Tags]    SETUP		EG
    [Documentation]		Add Enclosure Group to OneView
	Run Keyword If	${encgroups_add} is not ${null}  	Add Enclosure Group from variable sync    ${encgroups_add}  ${VERIFY}  ${expected_encgroups_add}

Add LE
	[Tags]    SETUP		LE
    [Documentation]		Add LE to OneView
	Run Keyword If	${logical_enclosures} is not ${null}  	Add Logical Enclosure from variable	  ${logical_enclosures}
	Verify Resources for List  ${expected_logical_enclosures}