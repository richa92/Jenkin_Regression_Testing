*** Settings ***
Documentation        SBAC Update a Scope's scope which is the active scope to delete an active scope
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
SBAC Update a Scope's scope which is the active scope to delete an active scope
    [Documentation]  OVF1592 API n118 Scopes supports SBAC Update a Scope's scope which is the active scope to delete an active scope
    Set Log Level   TRACE
    Log  Delete test from scope2
    ${uri}=  Get Scope URI By Name   ${Scope_List[1]}
    ${uri_list}=  create list   ${uri}
    ${resps}=   Edit Scope   name=${Scope_List[4]}  removeresources=${uri_list}
    Log    ${errorMessages}    console=True
    Wait For Task2   ${resps}   timeout=60    PASS=Error  errorMessage=${NOT_AUTHORIZED_SCOPE}    VERBOSE=True

