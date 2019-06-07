*** Settings ***
Documentation        LIGs Associated with network Create a LIG in active scope with an ethernet which in the inactive scope
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
LIGs Associated with network Create a LIG in active scope with an ethernet which in the inactive scope
  [Documentation]  OVF1592 API n067 LIGs Associated with network Create a LIG in active scope with an ethernet which in the inactive scope

   Log   Can not Edit Logical interconnect group LIG5 with network eth4 which inactive scope    console=True
   ${resp}=   Add LIG from variable async    ${create_LIG_network3}  status_code=403
   Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
