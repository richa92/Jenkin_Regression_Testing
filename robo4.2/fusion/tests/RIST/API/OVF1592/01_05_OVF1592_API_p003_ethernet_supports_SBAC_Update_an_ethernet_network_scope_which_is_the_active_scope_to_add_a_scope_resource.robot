*** Settings ***
Documentation        Update an ethernet network scope which is the active scope to add a scope resource
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
Update an ethernet network scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p003 ethernet supports SBAC Update an ethernet network scope which is the active scope to add a scope resource
  Set Log Level    TRACE

  Log  add scope1 to eth2    console=True
  ${resp}=   Patch Resources Scopes  ETH:${Ethernet_Networks[1]['name']}   ${Patch_add_Scope3}
  Wait For Task2   ${resp}
  Validate Resource Assigned/Unassigned To Scope  ${Scope_List[1]}  ETH:${Ethernet_Networks[1]["name"]}   ${TRUE}
  Validate Resource Assigned/Unassigned To Scope  ${Scope_List[3]}  ETH:${Ethernet_Networks[1]["name"]}   ${TRUE}
