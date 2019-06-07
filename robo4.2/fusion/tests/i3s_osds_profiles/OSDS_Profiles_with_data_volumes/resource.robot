*** Settings ***
Library           FusionLibrary
Library           i3SLibrary
Library           String
Resource          ../Resources/api/resource.robot
Variables         ./data_variable.py
Variables         ./environment_data.py
Resource          ${fusion_api_resource}
Library           json
Library           copy

*** Variables ***
${fusion_ip}    10.1.1.122
${force} =      False
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
@{resourcesList}   ethernets    egs     servers    osdps    volumes
${fusion_api_resource}       ../../../../fusion/Resources/api/fusion_api_resource.txt

*** Keywords ***
Login To Appliance And Verify Prerequisites and Add Storage Volumes
    [Documentation]    Login to appliance and verify whether applaince meets Prerequisites and add Storage Volumes
    [Arguments]     ${fusion_ip}    ${admin_credentials}     ${vol}

    I3S Suite Setup    ${fusion_ip}    ${admin_credentials}
    Add Storage Volumes Async   ${vol}
    :FOR    ${resourceName}    IN    @{resourcesList}
    \    ${blnVerifyPreReqs} =    Run Keyword If    '${resourceName}' == 'ethernets'    Get Ethernet Networks Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'egs'    Get Enclosure Groups Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'servers'    Get Servers Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'osdps'    Get OS deployment Plans Passed in Variable File
	\       ...                          ELSE IF    '${resourceName}' == 'volumes'    Get OS Storage Volumes Passed in Variable File
    \    Return From Keyword If    ${blnVerifyPreReqs}!=True    One or more '${resourceName}' are not exist in appliance

    [Return]    ${blnVerifyPreReqs}


