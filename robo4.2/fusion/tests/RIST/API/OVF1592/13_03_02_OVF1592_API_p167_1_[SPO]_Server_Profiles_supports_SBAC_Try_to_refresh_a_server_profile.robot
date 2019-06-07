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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles supports SBAC Delete a SP which in the active scope
    [Documentation]  OVF1592 API p167 [Server Profile Administrator] Server Profiles supports SBAC Delete a SP which in the active scope

    Log     Refresh sp2    console=True
    ${resp}=   Patch Server Profile  ${Edit_server_profile}   path=/refreshState   value=RefreshPending
    Wait For Task2   ${resp}  timeout=600

    Log     Refresh sp4    console=True
    ${resp}=   Patch Server Profile  ${Edit_server_profile3}   path=/refreshState   value=RefreshPending
    Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
