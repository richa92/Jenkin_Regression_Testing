***Settings ***
Library           FusionLibrary
Library           i3SLibrary
Library           String
Resource          ../Resources/api/resource.robot
Variables         ./data_variables.py
Variables         ./environment_data.py
Variables         ./nw_as_mgmt.py
Variables         ./network_set_as_mgmt.py
Variables         ./negative_test_data.py

*** Variables ***
${fusion_ip}    10.1.1.122
${force} =      False

*** Keywords ***
Delete Connection By Name
    [Documentation]    Delete connection from connection list by name
    [Arguments]    ${connections}    ${conn_name}

    :FOR    ${conn}    In    @{connections}
    \    Run Keyword If    "${conn['name']}"=="${conn_name}"    Remove Values From List    ${connections}    ${conn}
    [Return]    ${connections}

Create SPT with multi-NIC management OSDP
    [Documentation]    Create SPT with multi-NIC management OSDP
    [Arguments]    ${spt}

    ${spt_body} =    copy.deepcopy    ${spt}
    ${spt_uri} =    Get Server Profile Template URI    ${spt_body['name']}
    Run Keyword If  '${spt_uri}'!= '/rest/server_profile_template_uri_${spt_body['name']}_not_found'
    ...    Remove SPT And Server Profiles by SPT    ${spt_body['name']}

    ${blnCreateSPT} =    Create I3S SPT    ${spt_body}
    Should Be Equal As Strings    "${blnCreateSPT}"    "True"    Fail    Failed to create SPT '${spt['name']}'

Create SP with multi-NIC management OSDP
    [Documentation]    Verifies whether server HW is free, if not removes the profile
    ...    assigned and creates SP with multi-NIC management OSDP
    [Arguments]    ${sp}

    ${sp_body} =    copy.deepcopy    ${sp}
    ${server_prof} =    Get Server Hardware Profile    ${sp_body['serverHardwareUri']}
    Run Keyword If    '${server_prof}'!='${null}'    Run Keywords
    ...    Power Off Profile Server    ${sp_body['serverHardwareUri']}    AND
    ...    Delete Server Profile    ${server_prof}

    ${blnCreateSP} =    Create I3S Server Profile    ${sp_body}
    Should Be Equal As Strings    "${blnCreateSP}"    "True"    Fail    Failed to create SP '${sp['name']}'

Create SP from SPT with multi-NIC management OSDP
    [Documentation]    Create SPT and SP from same SPT of multi-NIC management OSDP
    [Arguments]    ${spt}    ${sp_from_spt}

    ${spt_body} =    copy.deepcopy    ${spt}
    ${sp_body} =    copy.deepcopy    ${sp_from_spt}

    ${spt_name} =    Strip String    ${spt_body['name']}
    ${spt_uri} =    catenate    SEPARATOR=    SPT:    ${spt_name}
    Set To Dictionary    ${sp_body}    serverProfileTemplateUri=${spt_uri}

    # If SP is associated with SPT delete SP 1st and then SPT
    ${spt_uri} =    Get Server Profile Template URI    ${spt_body['name']}
    Run Keyword If  '${spt_uri}'!= '/rest/server_profile_template_uri_${spt_body['name']}_not_found'
    ...    Remove SPT And Server Profiles by SPT    ${spt_body['name']}

    ${blnCreateSPT} =    Create I3S SPT    ${spt_body}
    Should Be True    ${blnCreateSPT}    Failed to create SPT '${spt_body['name']}'

    # Delete if any profile is created on server HW
    ${server_prof} =    Get Server Hardware Profile    ${sp_body['serverHardwareUri']}
    Run Keyword If    '${server_prof}'!='${null}'    Run Keywords
    ...    Power Off Profile Server    ${sp_body['serverHardwareUri']}    AND
    ...    Delete Server Profile    ${server_prof}

    ${blnCreateSP} =    Create I3S SP from I3S SPT    ${sp_body}
    Should Be True    ${blnCreateSP}    Failed to create SP '${sp_body['name']}'
