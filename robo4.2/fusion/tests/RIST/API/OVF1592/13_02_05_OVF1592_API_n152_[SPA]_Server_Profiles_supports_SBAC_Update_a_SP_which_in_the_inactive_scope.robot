*** Settings ***
Documentation        Server Profiles supports SBAC Update a SP which in the inactive scope
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
[SPA] - Server Profiles supports SBAC Update a SP which in the inactive scope
    [Documentation]  OVF1592 API n152 [Server Profile Administrator] Server Profiles supports SBAC Update a SP which in the inactive scope

    Log   Can not edit sp4   console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile3}
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
