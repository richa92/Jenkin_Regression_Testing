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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Suite Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet_Delete a uplink-set for LI which in the active scope with an ethernet which in the active scope
    Log    \nRemive uplinkset ${add_Uplinksets1["name"]}    console=True
    ${resp}=   Remove Uplinkset By Name    ${add_Uplinksets1["name"]}
    Wait For Task2    ${resp}  timeout=240
