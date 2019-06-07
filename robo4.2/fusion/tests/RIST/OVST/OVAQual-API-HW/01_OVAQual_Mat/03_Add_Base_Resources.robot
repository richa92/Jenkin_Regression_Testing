*** Settings ***
Documentation    Add Base Resources to OneView
Resource                ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Add Users
    [Tags]      SETUP       USERS
    [Documentation]     Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    ${users} =  Get Variable Value  ${users}
    Run Keyword If  ${users} is not ${null}     Add Users from variable async  ${users}    ${VERIFY}  ${expected_users}

Download SPP
    [Tags]  DOWNLOAD
    [Documentation]        Download SPP bundle from HTTP server
    Download Latest File From Web Folder   ${WEB_URL}    ${WEB_USERNAME}   ${WEB_PASSWORD}

Add Firmware Bundle
    [Tags]    SETUP      FW-BUNDLE
    [Documentation]        Upload SPP bundle to OneView
    ${status}    ${message}    Run Keyword And Ignore Error    OperatingSystem.File Should Exist    ${SPP_LOCAL_FILE}
    Run Keyword If    '${status}'=='FAIL'
    ...    Log    SPP File is not download from HTTP Url.Pick up latest SPP file from local path    WARN  console=True
    Create Folder If Not Exists    ${SPP_LOCALPATH}
    ${file}=  Run Keyword If   '${status}'=='FAIL'   Get File From Local Path   ${SPP_LOCALPATH}
    ${filestatus}    ${filemsg}    Run Keyword And Ignore Error    OperatingSystem.File Should Exist    ${file}
    ${SPP_FILE}=  Set Variable If   '${filestatus}' == 'FAIL'   ${SPP_LOCAL_FILE}   ${file}
    Log   SPP to be Installed:${SPP_FILE}    console=True
    Run Keyword If   '${SPP_FILE}' != '${None}'   Upload Firmware Bundle Async    ${SPP_FILE}   ${VERIFY}
    ...      ELSE    Log    No SPP Bundle available in local path to upload    WARN    console=True

Add San Manager
    [Tags]      SETUP      SM
    [Documentation]     Add SAN Manager to OneView
    Run Keyword If  ${san_managers} is not ${null}     Add San Managers Async    ${san_managers}    ${VERIFY}  ${expected_san_managers}

Add Ethernet Networks
    [Tags]      SETUP       E-NW
    [Documentation]     Add Ethernet Networks to OneView
    Run Keyword If  ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FC networks
    [Tags]    SETUP      FC-NW
    [Documentation]        Add FC Networks to OneView
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}    ${VERIFY}    ${expected_fc_networks}

Add iSCSI Networks
    [Tags]      SETUP       ISCSI-NW
    [Documentation]     Add iSCSI Networks to OneView
    Run Keyword If  ${iscsi_networks} is not ${null}     Add Ethernet Networks from variable async  ${iscsi_networks}  ${VERIFY}  ${expected_iscsi_networks}

Add Network Sets
    [Tags]      SETUP       NW-SETS
    [Documentation]     Add Network Sets to OneView
    Run Keyword If  ${networksets} is not ${null}   Add Networks Sets from variable async  ${networksets}  ${VERIFY}  ${expected_networksets}

Add LIG
    [Tags]      SETUP       LIG
    [Documentation]     Add LIG to OneView
    Run Keyword If    ${ligs} is not ${null}   Add LIG async   ${ligs}  ${VERIFY}  ${expected_lig}

Add EG
    [Tags]      SETUP       EG
    [Documentation]     Add Enclosure Group to OneView
    Run Keyword If  ${encgroups_add} is not ${null}     Add Enclosure Group from variable async    ${encgroups_add}  ${VERIFY}  ${expected_encgroups_add}
    Wait Until Keyword Succeeds    ${TIMEOUT}    ${POLLING_INTERVAL}    EnclosureGroup Status Should Be    ${encgroups_add}    OK

Add Rack Server
    [Tags]  SETUP    R-SVR
    [Documentation]  Add Rack Server to OneView
    Run Keyword If  ${rackservers} is not ${null}     Add Server hardware from variable async   ${rackservers}  ${VERIFY}  ${expected_rackservers}
    Power off ALL servers    47
    Verify Resources for List   ${expected_rackservers}
