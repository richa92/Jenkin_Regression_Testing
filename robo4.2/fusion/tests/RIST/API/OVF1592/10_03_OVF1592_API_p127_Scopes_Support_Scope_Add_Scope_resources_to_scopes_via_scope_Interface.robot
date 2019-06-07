*** Settings ***
Documentation        Scopes Support Scope Add Scope resources to scopes via scope Interface
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Scopes Support Scope Add Scope resources to scopes via scope Interface
    [Documentation]  OVF1592 API p127 Scopes Support Scope Add Scope resources to scopes via scope Interface

    Log  Delete Production of scope5
    ${uri}=  Get Scope URI By Name   ${new_scope_name}
    ${uri_list}=  create list   ${uri}
    ${resps}=   Edit Scope   ${Scope_List[0]}  addresources=${uri_list}
    Wait For Task2   ${resps}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  Scope:${new_scope_name}   ${TRUE}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  Scope:${new_scope_name}   ${TRUE}