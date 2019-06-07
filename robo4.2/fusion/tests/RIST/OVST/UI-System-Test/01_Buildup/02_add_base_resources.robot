*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Add Users
    [Tags]    SETUP  USERS  TBIRD  C7000
    [Documentation]  Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    ${users} =       Get Variable Value  ${users}
    ${responses}=    Add Users from variable  ${users}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}
    Verify Users     ${expected_users}

Add San Manager
    [Tags]  SETUP    SM  TBIRD  C7000
    [Documentation]  Add SAN Manager to OneView
    ${responses}=    Add San Managers Async  ${san_managers}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}  timeout=120  interval=5
    Verify Resources for List  ${expected_san_managers}

Add Ethernet Networks
    [Tags]  SETUP    E-NW  TBIRD  C7000
    [Documentation]  Add Ethernet Networks to OneView
    Run Keyword If   ${ethernet_networks} is not ${null}  Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FC networks
    [Tags]  SETUP    FC-NW  TBIRD  C7000
    [Documentation]  Add FC Networks to OneView
    ${responses} =   Run Keyword If  ${fc_networks} is not ${null}  Add Non Existing FC Networks  ${fc_networks}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}
    Verify Resources for List  ${expected_fc_networks}

Add Network Sets
    [Tags]  SETUP    NW-SETS  TBIRD  C7000
    [Documentation]  Add Network Sets to OneView
    Run Keyword If   ${networksets} is not ${null}  Add Networks Sets from variable async  ${networksets}  ${VERIFY}  ${expected_networksets}

Add LIG
    [Tags]  SETUP    LIG  TBIRD  C7000
    [Documentation]  Add LIG to OneView
    Run Keyword If   ${ligs} is not ${null}  Add LIG  ${ligs}
    Verify Resources for List  ${expected_lig}

Add SAS LIG
    [Tags]  SETUP    SAS  TBIRD
    [Documentation]  Add SAS LIG to OneView
    ${responses} =   Run Keyword If  ${sas_lig} is not ${null}  Add SAS LIG from variable async  ${sas_lig}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2   ${responses}
    Verify Resources for List  ${expected_sas_lig}

Add EG
    [Tags]  SETUP    EG  TBIRD  C7000
    [Documentation]  Add Enclosure Group to OneView
    Run Keyword If   ${encgroups_add} is not ${null}  Add Enclosure Group from variable sync  ${encgroups_add}  ${VERIFY}  ${expected_encgroups_add}

Add Rack Server
    [Tags]    SETUP  RACK-SVR  C7000
    [Documentation]  Add Rack Server to OneView
    Run Keyword If   ${rackservers} is not ${null}  Add Server Hardware Async  ${rackservers}  ${VERIFY}  ${expected_rackservers}
