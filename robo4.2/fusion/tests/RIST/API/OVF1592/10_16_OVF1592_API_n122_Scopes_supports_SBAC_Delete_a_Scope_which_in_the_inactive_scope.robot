*** Settings ***
Documentation        Scopes supports SBAC Delete a Scope which in the inactive scope
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
Scopes supports SBAC Delete a Scope which in the inactive scope
    [Documentation]  OVF1592 API n122 Scopes supports SBAC Delete a Scope which in the inactive scope

    Log  Can not delete scope4 which in inactice scope
    ${uri} =    Get Scope URI By Name    ${Scope_List[5]}
    ${resps} =    Fusion Api Delete Scope    uri=${uri}
    Wait For Task2   ${resps}   timeout=60    PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
