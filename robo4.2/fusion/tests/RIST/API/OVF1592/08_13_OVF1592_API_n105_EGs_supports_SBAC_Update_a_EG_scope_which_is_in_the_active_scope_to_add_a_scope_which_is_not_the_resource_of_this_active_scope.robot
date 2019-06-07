*** Settings ***
Documentation        Enclosure Groups supports SBAC_Update a EG scope which is the active scope, but the active scope have no scope resources
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups supports SBAC_Update a EG scope which is the active scope to add a scope which is not the resource of this active scope
  [Documentation]  OVF1592 API n105 Enclosure Groups supports SBAC_Update a EG scope which is the active scope, but the active scope have no scope resources

  Log   Add scope1 for EG3     console=True
  ${resp}=  Patch Resources Scopes   EG:${EG_list[2]}   ${Patch_add_Scope3}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  EG:${EG_list[2]}   ${False}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  EG:${EG_list[2]}   ${True}