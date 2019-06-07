*** Settings ***
Documentation        Scopes supports SBAC Update a Scope's scope which is the active scope to a scope resource
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
Scopes supports SBAC Update a Scope's scope which is the active scope to a scope resource
    [Documentation]  OVF1592 API p132 Scopes supports SBAC Update a Scope's scope which is the active scope to a scope resource

    Log  Add scope1 to scope2
    ${resp}=   Patch Resources Scopes   Scope:${Scope_List[4]}  ${Patch_add_Scope3}
    Wait For Task2   ${resp}
    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  Scope:${Scope_List[4]}   ${True}
