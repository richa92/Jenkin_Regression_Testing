*** Settings ***
Documentation        Uplink Sets Associated with ethernet_Update a uplink-set for LI which in the active scope with delete an ethernet which in the inactive scope
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
Test Teardown        Clear Environment for 12_15
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet_Update a uplink-set for LI which in the active scope with delete an ethernet which in the inactive scope
    Log    \nEdit the uplinkset to delete an inactive network eth4    console=True
    ${resp}=    Edit uplinkset    ${update_Uplinksets["name"]}    ${update_Uplinksets}    ${LI1}
    Wait For Task2   ${resp}    timeout=240

*** Keywords ***
Clear Environment for 12_15
    [Documentation]  Clear Environment for 12_15
    Login Appliance    ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    Log    \nRemive uplinkset ${update_Uplinksets["name"]}    console=True
    ${resp}=   Remove Uplinkset By Name    ${update_Uplinksets["name"]}
    Wait For Task2    ${resp}  timeout=240
