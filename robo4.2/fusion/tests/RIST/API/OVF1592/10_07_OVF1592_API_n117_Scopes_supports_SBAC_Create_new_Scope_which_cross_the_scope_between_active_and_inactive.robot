*** Settings ***
Documentation        Scopes supports SBAC Create new Scope which cross the scope between active and inactive
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
Scopes supports SBAC Create new Scope which cross the scope between active and inactive
    [Documentation]  OVF1592 API n117 Scopes supports SBAC Create new Scope which cross the scope between active and inactive

    Log  Can not Create scope7 with scope Stage
    ${resp}=   Create Scope   ${create_scope4}
    Wait For Task2   ${resp}   timeout=60    PASS=Error  errorMessage=${CREATION_NOT_AUTHORIZED_ERROR}    VERBOSE=True

