*** Settings ***
Documentation        Scopes Support Scope Add Scope resources to scopes via Scope Interface
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
Scopes Support Scope Add Scope resources to scopes via Scope Interface
    [Documentation]  OVF1592 API p125 Scopes Support Scope Add Scope resources to scopes via Scope Interface
    Log    Set the patch body based on the location of scope1    console=True
    ${scopes}=    Get Assigned Scope URIs By Resource Name    Scope:${new_scope_name}
    ${scope}=    Get Scope URI By Name    ${Scope_List[0]}

    ${body}=    Set Variable If  '${scopes[0]}'=='${scope}'  ${Patch_remove_Scope0}  ${Patch_remove_Scope1}

    Log  Delete Production of scope5
    ${resps}=   Patch Resources Scopes   Scope:${new_scope_name}  ${body}
    Wait For Task2   ${resps}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  Scope:${new_scope_name}   ${False}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  Scope:${new_scope_name}   ${TRUE}
