*** Settings ***
Documentation        Uplink Sets Associated with ethernet Update a uplink-set for LI which in the active scope with edit an ethernet
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
Uplink Sets Associated with ethernet Update a uplink-set for LI which in the active scope with edit an ethernet
    Log   \nAdd a uplinkset without "portConfigInfos" & network
    ${resps}=   Add Uplinkset from variable Async    ${add_Uplinksets}
    Wait For Task2   ${resps}    timeout=240

    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    Log    \nEdit the uplinkset    console=True
    ${resp}=    Edit uplinkset    ${update_Uplinksets1["name"]}    ${update_Uplinksets1}    ${LI1}
    Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
