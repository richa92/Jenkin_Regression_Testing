*** Settings ***
Documentation        Server Profiles supports SBAC Try to create a new server profile
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
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles supports SBAC Try to create a new server profile
    [Documentation]  OVF1592 API n154 [Server Profile Operator] Server Profiles supports SBAC Try to create a new server profile

    Log    Create new server profiles sp5    console=True
    ${resp}=  Add Server Profile  profile=${create_server_profile}  status_code=403
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
