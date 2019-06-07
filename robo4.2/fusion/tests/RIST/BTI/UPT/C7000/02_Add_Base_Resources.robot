*** Settings ***
Documentation           Add Licenses, Users, Remote Support, SAN Managers, Networks, LIG, EG and Enclosure.
Resource                resource.txt
Suite Setup             Suite Setup
Suite Teardown          Suite Teardown

*** Test Cases ***
C7000 UPT Add Base Resources Create Appliance Self-signed Server Certificate
    [Documentation]  Create self-signed server sertificate
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Create Appliance Selfsigned Cert

C7000 UPT Add Base Resources Add Licenses
    [Documentation]   Add Licenses
    ${licenses} =  Get Variable Value  ${licenses}
    ${responses} =  Run Keyword If  ${licenses} is not ${null}    Add Licenses from variable    ${licenses}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resource  ${licenses}

C7000 UPT Add Base Resources Enable Remote Support
    [Documentation]    Enable remote support
    First Time Remote Support Registration

C7000 UPT Add Base Resources Add Users
    [Documentation]  Add users
    ${responses} =  Run Keyword If  ${users} is not ${null}     Add Users from variable  ${users}
    Run Keyword If   ${responses} is not ${null}  Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resource  ${expected_users}  enabled=True

C7000 UPT Add Base Resources Add San Manager
     [Documentation]  Add SAN Manager
     Add San Managers Async  ${san_managers}
     Verify Resources for List  ${expected_san_managers}   status=REGEX:OK|Warning
     :FOR  ${fc_san_attributes}  IN  @{fc_sans_attributes}
     \   Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  FCSan:${fc_san_attributes['name']}  state  Discovered

C7000 UPT Add Base Resources Add Ethernet Networks
    [Documentation]  Add ethernet networks
    ${responses} =  Run Keyword If  ${ethernet_networks} is not ${null}  Add Ethernet Networks from variable async  ${ethernet_networks}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}

C7000 UPT Add Base Resources Add FC Networks
    [Documentation]  Add FC networks
    ${responses} =  Run Keyword If  ${fc_networks} is not ${null}   Add Non Existing FC Networks    ${fc_networks}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    :FOR  ${fc_san_attributes}  IN  @{fc_sans_attributes}
    \   Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  FCSan:${fc_san_attributes['name']}  state  Managed

C7000 UPT Add Base Resources Add LIGs
    [Documentation]  Add LIG
    ${responses} =  Run Keyword If   ${ligs} is not ${null}  Add LIG   ${ligs}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}

C7000 UPT Add Base Resources Add EGs
    [Documentation]  Add Enclosure Group
    ${responses} =  Run Keyword If  ${enclosure_groups} is not ${null}  Add Enclosure Group from variable sync   ${enclosure_groups}
    Run Keyword If   ${responses} is not ${null}  Run Keyword And Continue On Failure    Wait For Task2   ${responses}

C7000 UPT Add Base Resources Add Enclosures
    [Documentation]  Add Enclosures
    ${responses} =  Run Keyword If   ${enclosures} is not ${null}   Add Non-Existing Enclosures from variable Async   ${enclosures}
    ${reslength} =  get length   ${responses}
    Run Keyword If  '${reslength}' is not '${0}'  Run Keyword And Continue On Failure   Wait For Task2  ${responses}  timeout=1200   interval=10

C7000 UPT Add Base Resources Check Enclosures Remote Support Status
    [Documentation]  Enclosure Remote Support Status
    Log  \nEnable Enclosure Remote Support Task Initiated
    :FOR  ${enclosure}  IN  @{enclosures_attributes}
    \   ${resp} =  Wait Until Keyword Succeeds  5 m  60 s  Get Task By Param  param=?filter="'name'='Enable remote support' AND associatedResource.resourceName='${enclosure['name']}'
    \   Wait for task2  ${resp}  timeout=500  interval=10
    Get Enclosure and verify remote support   ${enclosures_attributes}

C7000 UPT Add Base Resources Verify Base Resources
    [Documentation]  Verify Base resources
    Verify Base Resources
    ${crit_ports} =  Get All Interconnects Ports Status
    Run keyword if  ${crit_ports}!=0  Log  There are ports in Critical Status.  WARN