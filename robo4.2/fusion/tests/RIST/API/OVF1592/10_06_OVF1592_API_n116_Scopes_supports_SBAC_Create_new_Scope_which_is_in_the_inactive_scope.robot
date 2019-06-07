*** Settings ***
Documentation        Scopes supports SBAC Create new Scope which is in the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Scopes supports SBAC Create new Scope which is in the inactive scope
    [Documentation]  OVF1592 API n116 Scopes supports SBAC Create new Scope which is in the inactive scope
    Log  Can not Create scope7 with scope Stage
    ${resp}=   Create Scope   ${create_scope3}
    Wait For Task2   ${resp}   timeout=60    PASS=Error  errorMessage=${CREATION_NOT_AUTHORIZED_ERROR}    VERBOSE=True

