*** Settings ***
Documentation        Scopes supports SBAC Update a Scope which is the active scope
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
Scopes supports SBAC Update a Scope which is the active scope
    [Documentation]  OVF1592 API p131 Scopes supports SBAC Update a Scope which is the active scope

    Log  Edit scope5 change some value
    ${resp}=   Edit Scope   name=${new_scope_name}   new_name=${new_scope_name_update}
    Wait For Task2   ${resp}
