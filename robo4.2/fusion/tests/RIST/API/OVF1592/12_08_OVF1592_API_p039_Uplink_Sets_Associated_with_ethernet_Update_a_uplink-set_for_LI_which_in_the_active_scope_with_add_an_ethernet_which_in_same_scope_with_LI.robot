*** Settings ***
Documentation        Uplink Sets Associated with ethernet Create a new uplink-set for LI which in the active scope with a ethernet which in the inactive scope
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
Uplink Sets Associated with ethernet Update a uplink-set for LI which in the active scope with add an ethernet which in same scope with LI
    Log   \nAdd a uplinkset without "portConfigInfos" & network
    ${resps}=   Add Uplinkset from variable Async    ${add_Uplinksets}
    Wait For Task2   ${resps}    timeout=240

    Log    \nEdit the uplinkset to add an active network eth2    console=True
    ${resp}=    Edit uplinkset    ${update_Uplinksets1["name"]}    ${update_Uplinksets1}    ${LI1}
    Wait For Task2   ${resp}    timeout=240