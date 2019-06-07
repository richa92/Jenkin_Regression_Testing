*** Settings ***
Documentation        Ethernet supports SBAC Update an ethernet network which is the active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Ethernet supports SBAC Update an ethernet network which is the active scope
   [Documentation]  OVF1592 API p002 ethernet supports SBAC Update an ethernet network which is the active scope

   Log   set eth1 name to "eth5"    console=True
   ${resp}=   Edit Network     ${Update_Ethernet}
   Wait For Task2    ${resp[0]['task_resp']}

   Log   restore Network reset name to "eth1"    console=True
   ${resps}=   Edit Network    ${Update_Ethernet2}
   Wait For Task2    ${resps[0]['task_resp']}
