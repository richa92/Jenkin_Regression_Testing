*** Settings ***
Documentation        Scopes Support Scope Remove Scope resources scopes via Scope Interface
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
Scopes Support Scope Remove Scope resources scopes via Scope Interface
    [Documentation]  OVF1592 API p126 Scopes Support Scope Remove Scope resources scopes via Scope Interface

    Log  Create scope5 with scope Test
    ${resp}=   Create Scope   ${create_scope1}
    Wait For Task2  ${resp}
    ${resps}=   Patch Resources Scopes   Scope:${new_scope_name}  ${Patch_add_Scope0}
    Wait For Task2   ${resps}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  Scope:${new_scope_name}   ${TRUE}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  Scope:${new_scope_name}  ${TRUE}
