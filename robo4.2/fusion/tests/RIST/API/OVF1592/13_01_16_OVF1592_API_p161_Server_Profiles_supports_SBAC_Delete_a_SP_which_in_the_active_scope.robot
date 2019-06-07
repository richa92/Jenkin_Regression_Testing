*** Settings ***
Documentation        Server Profiles supports SBAC Delete a SP which in the active scope
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

Suite Setup          Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Suite Teardown       Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles supports SBAC Delete a SP which in the active scope
    [Documentation]  OVF1592 API p161 Server Profiles supports SBAC Delete a SP which in the active scope

    Log    Deleing sp5   console=True
    ${resp}=     Remove Server Profile    ${create_server_profile}
    Wait For Task2  ${resp}  timeout=600

    Log   Check SP5 information   console=True
    ${sp_uri_result}=    Get Server Profile URI    ${create_server_profile["name"]}
    Should Be Equal  '${sp_uri_result}'   '/rest/server_profile_uri_${create_server_profile["name"]}_not_found'

