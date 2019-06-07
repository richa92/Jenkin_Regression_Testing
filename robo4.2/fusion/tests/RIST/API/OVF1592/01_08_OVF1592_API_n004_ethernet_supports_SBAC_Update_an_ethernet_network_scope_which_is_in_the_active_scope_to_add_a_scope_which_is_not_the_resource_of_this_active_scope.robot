*** Settings ***
Documentation        Update an ethernet network scope which is in the active scope to add a scope which is not the resource of this active scope
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
Update an ethernet network scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  OVF1592 API n004 ethernet supports SBAC Update an ethernet network scope which is in the active scope to add a scope which is not the resource of this active scope

  Log  add scopes1 to eth3    console=True
  ${resp}=   Patch Resources Scopes  ETH:${Ethernet_Networks[2]['name']}   ${Patch_add_Scope3}

  Log  chenk result information    console=True
  Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

  Validate Resource Assigned/Unassigned To Scope  ${Scope_List[0]}   ETH:${Ethernet_Networks[2]["name"]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}   ETH:${Ethernet_Networks[2]["name"]}  ${FALSE}
