*** Settings ***
Documentation        Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the same active scope
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
Variables            ./Regression_Data.py
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt


Test Teardown        Remove Enclosure    ${new_enc_name}    param=?force=True

*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the same active scope
  [Documentation]  Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the same active scope
  log    Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the same active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    EG:${EG}   firmware-baselines:${fw_bundle}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  Add Enclosures from variable  ${Add_Encs1}    timeout=40min
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${new_enc_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_p143 Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the same active scope    console=true
