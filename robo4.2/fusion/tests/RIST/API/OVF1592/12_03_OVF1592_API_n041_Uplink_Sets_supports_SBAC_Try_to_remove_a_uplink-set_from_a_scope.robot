*** Settings ***
Documentation        Network Sets supports SBAC Create new Network Set which is in the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
supports SBAC Try to remove a uplink-set from a scope
    Log  Can not Remove uplinksets from scope
    ${resps}=   Patch Resources Scopes   US:${uplink_name}  ${Patch_remove_Scope0}
    Wait For Task2   ${resps}   timeout=240   PASS=Error  errorMessage=${RESOURCE_NOT_SCOPABLE_ERROR}    VERBOSE=True
