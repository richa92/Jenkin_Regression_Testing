*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_806_me_data.py
Variables         ./environment_data.py

*** Variables ***
${fusion_api_resource}    C:/Users/komerao/OVF1134/fusion/Resources/api/fusion_api_resource.txt
${X-API-VERSION}    800
${fusion_ip}        15.212.167.184
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${profileTemplate}    ovf806_spt
${serverProfile}      ovf806_sp


*** Keywords ***
Get OSD Settings Attributes
    [Documentation]    Capture OS Deployment settings from profile response body
    [Arguments]    ${prof}
    ${osd_attributes}=    Create Dictionary
    ${sp_body} =    Get Server Profile    ${prof}
    ${osdp_uri} =    Get From Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri
    ${osdp_resp}=    Get Resource by URI    ${osdp_uri}
    ${osdp}=    Get From Dictionary    ${osdp_resp}    name
    ${osVol}=    Get OS Volume From Server Profile    ${prof}
    ${attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    Set To Dictionary    ${osd_attributes}    osVolume=${osVol}    osdp=${osdp}    ca_attributes=${attrib_values}
    [Return]    ${osd_attributes}

Compare OSD Setting Dictionaries
    [Documentation]    compare dictionaries of osd settings
    [Arguments]    ${dict1}    ${dict2}
    ${keys} =    Get Dictionary Keys    ${dict1}
    :For    ${key}    IN    @{keys}
    \    Run Keyword If    '${key}'=='DomainName'    Should Be Equal As Strings    ${dict1['${key}']}    ${dict2['${key}']}
    \    ...    ELSE IF    '${key}'=='Hostname'    Should Be Equal As Strings    ${dict1['${key}']}    ${dict2['${key}']}
    \    ...    ELSE IF    '${key}'=='SSH'    Lists Should Be Equal    ${dict1['${key}']}    ${dict2['${key}']}
    \    ...    ELSE    Return From Keyword    False
    [Return]    True

OVF806 Test Setup
    [Documentation]    Suite teardown include delete profile and spt
    [Arguments]    ${spt}=${profileTemplate}    ${sp}=${serverProfile}

    Remove SPT And Server Profiles by SPT    ${spt}
    Delete Server Profile    ${sp}
