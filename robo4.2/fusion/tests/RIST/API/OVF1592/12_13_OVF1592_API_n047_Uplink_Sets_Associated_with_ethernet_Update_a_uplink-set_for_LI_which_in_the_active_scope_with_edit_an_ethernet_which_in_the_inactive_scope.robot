*** Settings ***
Documentation        Uplink Sets Associated with ethernet Update a uplink-set for LI which in the active scope with delete an ethernet which in the active scope
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
Uplink Sets Associated with ethernet_Update a uplink-set for LI which in the active scope with edit an ethernet which in the inactive scope
    [Documentation]  This should be a positive case, but using the error tag n047
    Log    \nEdit the uplinkset to add inactive network eth4    console=True
    ${resp}=    Edit uplinkset    ${update_Uplinksets3["name"]}    ${update_Uplinksets3}    ${LI1}
    Wait For Task2   ${resp}   timeout=240

    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    Log    \nEdit the uplinkset to edit inactive network eth4    console=True
    ${resp}=    Edit uplinkset    ${update_Uplinksets5["name"]}    ${update_Uplinksets5}    ${LI1}
    Wait For Task2   ${resp}   timeout=480    VERBOSE=True
