*** Settings ***
Documentation        LIGs Associated with network Update a LIG in active scope with add an ethernet which in the inactive scope
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
Suite Teardown        Clear Environment of LIG After Test   ${create_LIG1}    Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
LIGs Associated with network Update a LIG in active scope with add an ethernet which in the inactive scope
  [Documentation]  OVF1592 API n069 LIGs Associated with network_Update a LIG in active scope with add an ethernet which in the inactive scope

   Log   Can not add eth4 to Logical interconnect group LIG5    console=True
   ${resp}=   Edit Lig    ${Edit_lig_network5}
   Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
