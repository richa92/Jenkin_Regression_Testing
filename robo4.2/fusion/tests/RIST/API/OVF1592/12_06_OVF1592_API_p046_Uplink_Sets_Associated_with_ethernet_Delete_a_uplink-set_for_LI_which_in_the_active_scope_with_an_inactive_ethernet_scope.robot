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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Test Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet_Delete a uplink-set for LI which in the active scope with an ethernet which in the inactive scope
    Log    \nAdd eth3 to uplinkset    console=True
    ${resps}=   Add Uplinkset from variable Async    ${add_Uplinksets2}
    Wait For Task2   ${resps}   timeout=240

    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    Log    \nRemive uplinkset ${add_Uplinksets2["name"]}    console=True
    ${resp}=   Remove Uplinkset By Name    ${add_Uplinksets2["name"]}
    Wait For Task2    ${resp}  timeout=240
