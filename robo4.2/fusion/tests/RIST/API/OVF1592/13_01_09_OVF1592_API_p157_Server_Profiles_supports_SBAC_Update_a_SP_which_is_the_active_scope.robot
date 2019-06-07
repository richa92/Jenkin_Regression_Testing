*** Settings ***
Documentation        Server Profiles supports SBAC Update a SP which is the active scope
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Test Setup           Login Appliance    ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles supports SBAC Update a SP which is the active scope
    [Documentation]  OVF1592 API p157 Server Profiles supports SBAC Update a SP which is the active scope
    Log   Edit sp2 name to sp7   console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile}  newname=${new_sp_name3}
    Wait For Task2   ${resp}  timeout=600
    Log   Check sp7 information   console=True
    ${sp_uri_result}=    Get Server Profile URI      ${new_sp_name3}
    Should Not Be Equal     '${sp_uri_result}'   '/rest/server_profile_uri_${new_sp_name3}_not_found'
    ${sp_uri_result}=    Get Server Profile URI      ${Edit_server_profile['name']}
    Should Be Equal        '${sp_uri_result}'   '/rest/server_profile_uri_${Edit_server_profile['name']}_not_found'

    Log  Edit sp7 name back to sp2    console=True
    ${resps}=  Edit Server Profile  ${Edit_server_profile2}  newname=${sp_list[1]}
    Wait For Task2   ${resps}  timeout=600
