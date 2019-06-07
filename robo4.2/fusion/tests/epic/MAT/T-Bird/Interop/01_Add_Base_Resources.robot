*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for Refresh and Verify Enclosure, Add License, San Manager, User, Networks, Network Sets, Storage System, LIG, EG and upload SPP Tests.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Test Cases ***

Rename All Enclosures
    [Tags]    RENAME
    [Documentation]        Rename Enclosure
    Set Log Level    TRACE
    ${responses}=  Edit Enclosure from List    ${encl_update}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=500
    Verify Resources for List  ${expected_enclosure}

#Verify Enclosure
#    [Tags]      VERIFY
#    [Documentation]  Verify Servers, Interconnects of Monitored Enclosure
#    Verify Resources for List     ${encs_monitor}
#    Verify Resources for List     ${server_monitor}
#    Verify Resources for List     ${interconnects_monitor}
#    Verify Resources for List     ${sasinterconnects_monitor}

Add License
    [Tags]      ADDLICENSE      SETUP
    [Documentation]        Add Licenses to OneView
    Run Keyword If  ${licenses} is not ${null}    Add Licenses from variable    ${licenses}     ${VERIFY}

Add San Manager Async
    [Tags]    ADD-SM
    [Documentation]     Add SAN Manager to OneView
    Run Keyword If  ${san_managers} is not ${null}    Add San Managers Async  ${san_managers}  ${VERIFY}  ${expected_san_managers}

Add User Async
    [Tags]    ADD-USER       SETUP
    [Documentation]  Add users to OneView (roles - Infrastructure administrator, Server administrator, Network administrator, Read only and Storage administrator)
    Run Keyword If  ${users} is not ${null}  Add Users from variable async    ${users}  ${VERIFY}  ${expected_users}

#SPP Upload
#    [Tags]    ADDSPP        SETUP
#    [Documentation]  Add SPP bundle to OneView
#    Upload SPP to Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${spp_details['path']}

Add Ethernet Networks Async
    [Tags]    ADD-ETH    SETUP
    [Documentation]        Add Ethernet Networks to OneView
    Run Keyword If  '${PREV TEST STATUS}'=='FAIL'     Pause Execution    message=Add San Manager Async failed. Press OK to continue.
    Run Keyword If  ${ethernet_networks} is not ${null}    Add Ethernet Networks from variable async    ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FC Networks Async
    [Tags]    ADD-FC      SETUP
    [Documentation]        Add Ethernet Networks to OneView
    ${responses}=  Add Non Existing FC Networks  ${fc_networks}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_fc_networks}

Add FCOE Networks
    [Tags]    ADD-FCOE   SETUP
    [Documentation]        Add FCOE Networks to OneView
    Run Keyword If  ${fcoe_networks} is not ${null}    Add FCoE Networks from variable async    ${fcoe_networks}    ${VERIFY}   ${expected_fcoe_networks}

Add Network Sets Async
    [Tags]    ADD-NS     SETUP
    [Documentation]        Add Network Sets to OneView
    Run Keyword If  ${network_sets} is not ${null}    Add Networks Sets from variable async    ${network_sets}  ${VERIFY}  ${expected_network_sets}

ADD LIGs
    [Tags]    ADDLIG        SETUP
    [Documentation]        Add LIG and SASLIG to OneView
    Run Keyword If  ${ligs} is not ${null}  Add LIG  ${ligs}
    Verify Resources for List  ${expected_lig}
    Run Keyword If  ${sas_ligs} is not ${null}          Add SAS LIG from variable async        ${sas_ligs}
    Verify Resources for List  ${expected_sas_lig}

ADD EG
    [Tags]    ADDEG     SETUP
    [Documentation]        Add Enclosure Group to OneView
    Run Keyword If  ${enc_groups} is not ${null}    Add Enclosure Group from variable sync    ${enc_groups}
