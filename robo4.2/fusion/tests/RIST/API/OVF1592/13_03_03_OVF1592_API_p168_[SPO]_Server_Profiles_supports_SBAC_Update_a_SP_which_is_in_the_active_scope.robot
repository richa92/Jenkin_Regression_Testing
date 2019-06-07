*** Settings ***
Documentation        Server Profiles supports SBAC Update a SP which is in the active scope
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

Test Setup           Run Keywords  Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
...                  AND          Prepare Environment For Test
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles supports SBAC Update a SP which is in the active scope
    [Documentation]  OVF1592 API p164 [Server Profile Administrator] Server Profiles supports SBAC Update a SP which is in the active scope

    Log   Edit sp1 name to sp7   console=True
    Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
    ${resp}=  Edit Server Profile  ${Edit_server_profile}  newname=${new_sp_name3}
    Wait For Task2   ${resp}  timeout=600
    Log   Check sp7 information   console=True
    ${sp_uri_result}=    Get Server Profile URI      ${new_sp_name3}
    Should Not Be Equal     '${sp_uri_result}'   '/rest/server_profile_uri_${new_sp_name3}_not_found'
    ${sp_uri_result}=    Get Server Profile URI      ${Edit_server_profile['name']}
    Should Be Equal        '${sp_uri_result}'   '/rest/server_profile_uri_${Edit_server_profile['name']}_not_found'

    Log  Edit sp7 name back to sp1    console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile2}  newname=${sp_list[1]}
    Wait For Task2   ${resp}  timeout=600

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Prepare Environment For Test
    Log    Create new server profiles sp5    console=True
    ${status}  ${resp}=  Run Keyword And Ignore Error    Add Server Profile  ${create_server_profile}
    Run Keyword If  '${status}'=='PASS'    Wait For Task2   ${resp}  timeout=600
