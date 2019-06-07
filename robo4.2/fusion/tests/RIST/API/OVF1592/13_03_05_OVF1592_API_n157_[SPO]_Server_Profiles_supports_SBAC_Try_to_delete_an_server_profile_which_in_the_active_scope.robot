*** Settings ***
Documentation        Server Profiles supports SBAC Try to delete an server profile which in the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Run Keywords  Login Appliance    ${APPLIANCE_IP}  ${credentials["spa_credentials"]}
...                  AND          Clear Environment After Test   ${create_server_profile}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles supports SBAC Try to delete an server profile which in the active scope
    [Documentation]  OVF1592 API n157 [Server Profile Operator] Server Profiles supports SBAC Try to delete an server profile which in the active scope
    Log    Deleing sp5   console=True
    ${resp}=     Remove Server Profile    ${create_server_profile}
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
