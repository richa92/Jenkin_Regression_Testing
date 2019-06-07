*** Settings ***
Documentation        Scopes supports SBAC Update a Scope's scope which is the active scope
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
Scopes supports SBAC Update a Scope's scope which is the active scope
    [Documentation]  OVF1592 API n119 Scopes supports SBAC Update a Scope's scope which is the active scope
    Log  Add scope3 to scope2
    ${resps}=   Patch Resources Scopes   Scope:${Scope_List[4]}  ${Patch_add_Scope5}
    Wait For Task2   ${resps}   timeout=60    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

    Validate Resource Assigned/Unassigned To Scope    ${Scope_List[5]}  Scope:${Scope_List[4]}   ${False}
