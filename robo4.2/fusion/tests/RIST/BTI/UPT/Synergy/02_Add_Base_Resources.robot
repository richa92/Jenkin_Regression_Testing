*** Settings ***
Documentation           Add Licenses, Users, Remote Support, SAN Managers, Networks, LIG, EG and Enclosure.
Resource                resource.txt
Suite Setup             Suite Setup
Suite Teardown          Suite Teardown

*** Test Cases ***
Synergy UPT Add Base Resources Create Appliance Selfsigned Certificate
    [Documentation]  Create appliance self-signed cert
    Create Appliance Selfsigned Cert

Synergy UPT Add Base Resources Add Licenses
    [Documentation]     Add Licenses
    ${licenses} =   Get Variable Value  ${licenses}
    ${responses} =  Run Keyword If    ${licenses} is not ${null}    Add Licenses from variable    ${licenses}
    Run Keyword If   ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resources for List  ${licenses}

Synergy UPT Add Base Resources Enable Remote Support
    [Documentation]    Enable remote support
    First Time Remote Support Registration

Synergy UPT Add Base Resources Check Enclosures Remote Support Status
    [Documentation]   Enclosure Remote Support Status
    Log  \nEnable Enclosure Remote Support Task Initiated
    :FOR  ${enclosure}  IN  @{enclosures_attributes}
    \   ${resp} =  Wait Until Keyword Succeeds  5 m  60 s  Get Task By Param  param=?filter="'name'='Enable Remote Support' AND associatedResource.resourceName='${enclosure['name']}'
    \   Wait for task2  ${resp}  timeout=300  interval=10
    Get Enclosure and verify remote support   ${enclosures_attributes}

Synergy UPT Add Base Resources Add Users
    [Documentation]  Add users
    ${responses} =  Run Keyword If  ${users} is not ${null}     Add Users from variable  ${users}
    Run Keyword If   ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resources for List  ${expected_users}   status=REGEX:OK|Warning

Synergy UPT Add Base Resources Add San Manager
    [Documentation]  Add SAN Manager
    Add San Managers Async  ${san_managers}
    Verify Resources for List  ${expected_san_managers}   status=REGEX:OK|Warning
    :FOR  ${fc_san_attributes}  IN  @{fc_sans_attributes}
     \   Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  FCSan:${fc_san_attributes['name']}  state  Discovered

Synergy UPT Add Base Resources Add Ethernet Networks
    [Documentation]  Add Ethernet Networks
    ${responses} =  Run Keyword If  ${ethernet_networks} is not ${null}    Add Ethernet Networks from variable async  ${ethernet_networks}
    Run Keyword If   ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

Synergy UPT Add Base Resources Add FC Networks
    [Documentation]  Creates FC Networks
    ${responses} =  Run Keyword If  ${fc_networks} is not ${null}    Add Non Existing FC Networks    ${fc_networks}
    Run Keyword If   ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

Synergy UPT Add Base Resources Add LIG
    [Documentation]  Add LIG
    ${responses} =  Run Keyword If   ${ligs} is not ${null}  Add LIG   ${ligs}
    Run Keyword If   ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

Synergy UPT Add Base Resources Add SAS LIG
    [Documentation]    Add SAS LIG
    ${responses} =  Run Keyword If   ${sas_ligs} is not ${null}  Add SAS LIG from list   ${sas_ligs}
    Run Keyword If   ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

Synergy UPT Add Base Resources Add EG
    [Documentation]  Add Enclosure Group
    ${responses} =  Run Keyword If  ${enclosure_groups} is not ${null}   Add Enclosure Group from variable sync    ${enclosure_groups}
    Run Keyword If   ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

Synergy UPT Add Base Resources Add Logical Enclosure
    [Documentation]  Add Logical Enclosure
    ${responses} =  Run Keyword If  ${logical_enclosures} is not ${null}   Add Logical Enclosure from lists Async    ${logical_enclosures}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2    ${responses}

Synergy UPT Add Base Resources Verify Base Resources
    [Documentation]  Verify base resources
    Verify Base Resources
    ${crit_ports} =  Get All Interconnects Ports Status
    Run keyword if  ${crit_ports}!=0  Log  There are ports in Critical Status.  WARN