*** Settings ***
Documentation        Scopes supports SBAC Update a Scope scope which is the active scope to delete a scope resource
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
Scopes supports SBAC Update a Scope scope which is the active scope to delete a scope resource
    [Documentation]  OVF1592 API p133 Scopes supports SBAC Update a Scope scope which is the active scope to delete a scope resource

    Log  Delete scope1 from scope2
    ${uri}=  Get Scope URI By Name   ${Scope_List[3]}
    ${uri_list}=  create list   ${uri}
    ${resps}=   Edit Scope   ${Scope_List[4]}  removeresources=${uri_list}
    Wait For Task2   ${resps}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[4]}  Scope:${Scope_List[3]}   ${False}
