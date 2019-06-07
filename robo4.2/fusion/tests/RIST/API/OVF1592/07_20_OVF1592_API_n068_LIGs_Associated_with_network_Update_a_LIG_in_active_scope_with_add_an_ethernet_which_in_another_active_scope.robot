*** Settings ***
Documentation        LIGs Associated with network Update a LIG in active scope with add an ethernet which in another active scope
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
LIGs Associated with network_Update a LIG in active scope with add an ethernet which in another active scope
  [Documentation]  OVF1592 API n068 LIGs Associated with network_Update a LIG in active scope with add an ethernet which in another active scope

   Log   Can not add eth3 to Logical interconnect group LIG5    console=True
   ${resp}=   Edit Lig    ${Edit_lig_network4}
   Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
