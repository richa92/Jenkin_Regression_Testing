*** Settings ***
Documentation                 Add  Base Resources to OneView
Resource                        resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Add Users
    [Documentation]        Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    [Tags]    SETUP        USERS
    Run Keyword If  ${users} is not ${null}     Add Users from variable async  ${users}    ${VERIFY}  expected_users=${expected_users}

Add San Manager
    [Documentation]     Add SAN Manager to OneView
    [Tags]      SETUP       SM
    Run Keyword If  ${san_managers} is not ${null}     Add San Managers Async    ${san_managers}    ${VERIFY}  expected_san_managers=${expected_san_managers}

Add Ethernet Networks
    [Documentation]        Add Ethernet Networks to OneView
    [Tags]    SETUP        E-NW
    Run Keyword If    ${ethernet_networks} is not ${null}      Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  expected_networks=${expected_ethernet_networks}

Add FC networks
    [Documentation]        Add FC Networks to OneView
    [Tags]    SETUP      FC-NW
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}  ${VERIFY}    expected_networks=${expected_fc_networks}

Add Network Sets
    [Documentation]        Add Network Sets to OneView
    [Tags]    SETUP        NW-SETS
    Run Keyword If    ${networksets} is not ${null}      Add Networks Sets from variable async  ${networksets}  ${VERIFY}  expected_network_sets=${expected_networksets}

Add LIG
    [Documentation]        Add LIG to OneView
    [Tags]    SETUP        LIG
    Run Keyword If    ${ligs} is not ${null}   Add LIG async   ${ligs}  ${VERIFY}  expected_lig=${expected_lig}

Add SAS LIG
    [Documentation]       Add SAS LIG to OneView
    [Tags]   SETUP        SAS
    Run Keyword If  ${sas_lig} is not ${null}    Add SAS LIG from variable async    ${sas_lig}    ${VERIFY}    expected_sas_lig=${expected_sas_lig}

Add EG
    [Documentation]        Add Enclosure Group to OneView
    [Tags]    SETUP        EG
    Run Keyword If    ${encgroups_add} is not ${null}      Add Enclosure Group from variable async    ${encgroups_add}  ${VERIFY}  expected_result=${expected_encgroups_add}