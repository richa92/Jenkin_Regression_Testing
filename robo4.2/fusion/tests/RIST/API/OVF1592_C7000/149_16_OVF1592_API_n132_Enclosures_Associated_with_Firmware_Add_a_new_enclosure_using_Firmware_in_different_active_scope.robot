*** Settings ***
Documentation        Enclosures Associated with Firmware_Add a new enclosure using existing FIrmware, they are in the different active scope
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


*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Enclosures Associated with Firmware_Add a new enclosure using existing FIrmware, they are in the different active scope
  [Documentation]  OVF1592_API_n132 Enclosures Associated with Firmware_Add a new enclosure using existing Firmware, they are in the different active scope
  log    Enclosures Associated with Firmware_Add a new enclosure using existing FIrmware, they are in the different active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    firmware-baselines:${fw_bundle}
  Update Scope With Resources    scope_name=${Scope_List[0]}    resources_list=${resources_list}    add_flag=${False}
  ${resources_list} =    Create List    EG:${EG}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Login Appliance  ${APPLIANCE_IP}    ${credentials['sa_credentials']}
  ${resps}=  Add Enclosures from variable Async  ${Add_Encs1}
  Should Match Regexp        '${resps[0]['errorCode']}'      'ASSOCIATION_FORBIDDEN_BY_SCOPE'
  Should Be Equal            '${resps[0]['status_code']}'    '403'
  ${resp}=  Get Enclosure URI  ${new_ethernet_name}
  Should Contain  '${resp}'    '/bad_enclosure_uri'  msg=Enclosures Associated with EG_Add a new enclosure using existing EG, they are in the different active scopeis faild
  log    Successfully! Test Case : OVF1592_API_n132 Enclosures Associated with Firmware_Add a new enclosure using existing FIrmware, they are in the different active scope    console=true
