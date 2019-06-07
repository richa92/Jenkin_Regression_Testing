*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Create new LIG which is in the active scope
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
Logical Interconnect Groups supports SBAC Create new LIG which is in the active scope
  [Documentation]  OVF1592 API p059 Logical Interconnect Groups supports SBAC Create new LIG which is in the active scope

  Log   Create new Logical interconnect group LIG5     console=True
  ${resp}=  Add LIG from variable   ${create_LIG1}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LIG:${new_LIG_name}   ${True}
