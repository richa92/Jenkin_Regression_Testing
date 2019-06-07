*** Settings ***
Documentation        Scopes supports SBAC Update a Scope which in the inactive scope
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
Scopes supports SBAC Update a Scope which in the inactive scope
    [Documentation]  OVF1592 API n121 Scopes supports SBAC Update a Scope which in the inactive scope

    Log  Edit scope4 change some value
    ${resps}=   Edit Scope   name=${Scope_List[5]}   new_name=${new_scope_name3}
    Wait For Task2   ${resps}   timeout=60    PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
