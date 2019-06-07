*** Settings ***
Documentation        LIGs Associated with network Create a LIG in active scope with an ethernet which in the other active scope
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
LIGs Associated with network Create a LIG in active scope with an ethernet which in the other active scope
  [Documentation]  OVF1592 API n066 LIGs Associated with network Create a LIG in active scope with an ethernet which in the other active scope

   Log   Can Edit Logical interconnect group LIG5 with network eth2 which in the same scope   console=True
   ${resp}=   Add LIG from variable async    ${create_LIG_network1}
   Wait For Task2   ${resp}
