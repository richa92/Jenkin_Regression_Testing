*** Settings ***
Documentation        Update a Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
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
Update a Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  OVF1592 API n036 Interconnects supports SBAC Update a Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
  log     Can not Update an inter3 add Scope1 to scopes     console=True
  ${resp}=   Patch Resources Scopes  IC:${interconects_list[2]}   ${Patch_add_Scope3}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  IC:${interconects_list[2]}  ${False}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  IC:${interconects_list[2]}  ${TRUE}
