*** Settings ***
Documentation        LIGs Associated with network Update a LIG in active scope with delete an ethernet which in the inactive scope
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
LIGs Associated with network Update a LIG in active scope with delete an ethernet which in the inactive scope
  [Documentation]  OVF1592 API n070 LIGs Associated with network_Update a LIG in active scope with delete an ethernet which in the inactive scope

   Log   Delete eth4 from Logical interconnect group LIG1    console=True
   ${resp}=   Edit Lig    ${Edit_lig_network7}
   Wait For Task2   ${resp}