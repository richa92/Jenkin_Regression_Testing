*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC_Delete a LIG which in the inactive scope
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
Logical Interconnect Groups supports SBAC Delete a LIG which in the inactive scope
  [Documentation]  OVF1592 API n065 Logical Interconnect Groups supports SBAC Delete a LIG which in the inactive scope

  Log   Can not delete LIG4    console=True
  ${resps}=   Fusion Api Delete Lig  ${LIG[3]}
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  LIG:${LIG[3]}  ${True}
