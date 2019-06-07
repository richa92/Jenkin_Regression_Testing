*** Settings ***
*** Settings ***
Documentation        Ethernet supports SBAC Create new ethernet network whcih is in the active scope
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
Ethernet supports SBAC Create new ethernet network whcih is in the active scope
  [Documentation]  OVF1592 API p001 ethernet supports SBAC Create new ethernet network which is in the active scope

  Log  Creating Network    console=True
  ${resps}=  Add Ethernet Networks from variable async  ${Create_Ethernet}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ETH:${new_ethernet_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ETH:${new_ethernet_name}  ${TRUE}
