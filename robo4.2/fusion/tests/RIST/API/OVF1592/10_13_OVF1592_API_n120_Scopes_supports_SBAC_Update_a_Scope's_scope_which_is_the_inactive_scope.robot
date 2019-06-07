*** Settings ***
Documentation        Scopes supports SBAC_Update a Scope's scope which is the inactive scope
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
Scopes supports SBAC_Update a Scope's scope which is the inactive scope
    [Documentation]  OVF1592 API n120 Scopes supports SBAC_Update a Scope's scope which is the inactive scope

    Log  Can not Edit scope4 change some scope
    ${resps}=   Patch Resources Scopes   Scope:${Scope_List[5]}  ${Patch_add_Scope3}
    Wait For Task2   ${resps}   timeout=60    PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
