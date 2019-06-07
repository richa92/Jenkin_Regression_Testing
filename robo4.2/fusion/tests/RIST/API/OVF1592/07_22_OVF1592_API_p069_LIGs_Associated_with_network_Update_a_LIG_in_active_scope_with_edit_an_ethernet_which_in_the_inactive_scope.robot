*** Settings ***
Documentation        LIGs Associated with network Update a LIG in active scope with edit an ethernet which in the inactive scope
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
LIGs Associated with network Update a LIG in active scope with edit an ethernet which in the inactive scope
  [Documentation]  OVF1592 API p069 LIGs Associated with network_Update a LIG in active scope with edit an ethernet which in the inactive scope

   Log   add eth4 To Logical interconnect group LIG1    console=True
   ${resp}=   Edit Lig    ${Edit_lig_network6}
   Wait For Task2   ${resp}
   Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
   Log   edit eth4 native to Logical interconnect group LIG1    console=True
   ${resp}=   Edit Lig    ${Edit_lig_network8}
   Wait For Task2   ${resp}
