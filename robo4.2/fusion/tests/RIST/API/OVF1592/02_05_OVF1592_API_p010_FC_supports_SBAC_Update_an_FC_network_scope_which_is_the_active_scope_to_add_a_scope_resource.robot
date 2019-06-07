*** Settings ***
Documentation        FC supports SBAC Update an FC network scope which is the active scope to add a scope resource
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
FC supports SBAC Update an FC network scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p010 FC supports SBAC Update an FC network scope which is the active scope to add a scope resource

  Log  Add scopes1 to fc2    console=True
  ${resp}=   Patch Resources Scopes  FC:${fc_networks[1]['name']}   ${Patch_add_Scope3}
  Wait For Task2  ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}   FC:${fc_networks[1]["name"]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}   FC:${fc_networks[1]["name"]}  ${True}
