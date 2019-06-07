*** Settings ***
Documentation        Uplink Sets supports SBAC Try to add uplink-set into a active scope
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

Test Setup           Login Appliance    ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets supports SBAC Try to add uplink-set into a active scope
    Log  Try to Add uplink-set into an active scope    console=True
    ${resps}=   Patch Resources Scopes   US:${uplink_name}  ${Patch_add_Scope0}
    Wait For Task2   ${resps}  timeout=240    PASS=Error  errorMessage=${RESOURCE_NOT_SCOPABLE_ERROR}    VERBOSE=True