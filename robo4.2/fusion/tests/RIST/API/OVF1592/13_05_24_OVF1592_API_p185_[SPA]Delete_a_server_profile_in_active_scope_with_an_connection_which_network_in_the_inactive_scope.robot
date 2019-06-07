*** Settings ***
Documentation        Server Profiles supports SBAC Delete a SP which in the inactive scope
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

Test Setup           Run Keywords    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
...                  AND    Prepare Environment for Test
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Delete a server profile in active scope with an connection which network in the inactive scope
    [Documentation]  OVF1592 API p185_[SPA]Delete a server profile in active scope with an connection which network in the inactive scope
    Log    Deleing new SP: sp5   console=True
    Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    ${resp}=     Remove Server Profile    ${create_sp_network3}
    Wait For Task2   ${resp}   timeout=600

    Log   Check SP5 information   console=True
    ${sp_Uri_Result}=    Get Server Profile URI     ${create_sp_network3["name"]}
    Should Be Equal  '${sp_uri_result}'   '/rest/server_profile_uri_${create_sp_network3["name"]}_not_found'

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Prepare Environment For Test
    ${resp}=  Add Server Profile  ${create_sp_network3}
    Wait For Task2   ${resp}   timeout=600
