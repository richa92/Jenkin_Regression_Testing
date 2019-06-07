*** Settings ***
Documentation        Scopes supports SBAC Delete a Scope which in the active scope
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

Test Setup           Login Appliance   ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Scopes supports SBAC Delete a Scope which in the active scope
    [Documentation]  OVF1592 API p135 Scopes supports SBAC Delete a Scope which in the active scope

    Log  Delete scope5 which in active scope
    ${resps}=   Remove Scope By Name   ${new_scope_name_update}
    Wait For Task2   ${resps}