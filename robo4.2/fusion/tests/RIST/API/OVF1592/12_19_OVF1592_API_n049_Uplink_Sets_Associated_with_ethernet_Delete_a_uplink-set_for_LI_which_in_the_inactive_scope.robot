*** Settings ***
Documentation        Uplink Sets Associated with ethernet Create a new uplink set  for LI which in the active scope with a ethernet which in another active scope
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
Test Teardown        Clear Environment after Completed All Uplink-sets tests
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet_Delete a uplink-set for LI which in the inactive scope
    Log    \nRemive uplinkset ${update_Uplinksets1["name"]}    console=True
    ${resp}=   Remove Uplinkset By Name    ${update_Uplinksets1["name"]}
    Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

*** Keywords ***
Clear Environment after Completed All Uplink-sets tests
    [Documentation]    Clear test environment after LI test completed
    Login Appliance    ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resp} =  Update Logical Interconnect from Group    ${li_update_dto}
