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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles supports SBAC Delete a SP which in the inactive scope
    Log    Deleing sp4   console=True
    ${resp}=     Remove Server Profile    ${Edit_server_profile3}
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

    Log   Check SP5 information   console=True
    ${sp_Uri_Result}=    Get Server Profile URI     ${sp_list[3]}
    Should Not Be Equal  '${sp_uri_result}'   '/rest/server_profile_uri_${sp_list[3]}_not_found'
