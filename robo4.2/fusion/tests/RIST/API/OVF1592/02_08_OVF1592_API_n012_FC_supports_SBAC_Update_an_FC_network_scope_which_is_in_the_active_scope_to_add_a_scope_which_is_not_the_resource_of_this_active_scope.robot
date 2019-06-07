*** Settings ***
Documentation        FC supports SBAC Update an FC network scope which is in the active scope to add a scope which is not the resource of this active scope
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
FC supports SBAC Update an FC network scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  OVF1592 API n012 FC supports SBAC Update an FC network scope which is in the active scope to add a scope which is not the resource of this active scope

  Log  Add scopes1 to fc3    console=True
  ${resp}=   Patch Resources Scopes  FC:${fc_networks[2]['name']}   ${Patch_add_Scope3}
  Log  chenk result information    console=True
  Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}   FC:${fc_networks[2]["name"]}  ${False}
