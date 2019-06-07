*** Settings ***
Documentation        Logical Interconnects Associated with internal networks_Update a LI to delete a internal network which in the inactive scope
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


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnects Associated with internal networks_Update a LI to delete a internal network which in the inactive scope
  [Documentation]  OVF1592_API_p057 Logical Interconnects Associated with internal networks_Update a LI to delete a internal network which in the inactive scope
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    LI:${LI1}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  log    Logical Interconnects Associated with internal networks_Update a LI to delete a internal network which in the inactive scope    console=true
  ${resp}=  Update Logical Interconnect Internal Network  ${LI1}    ${li_internal_network_add_inactive}
  Wait For Task2    ${resp}    600    10
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp}=  Update Logical Interconnect Internal Network  ${LI1}    ${li_internal_network_remove}
  Wait For Task2   ${resp}    600    10
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  LI:${LI1}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_p057 Logical Interconnects Associated with internal networks_Update a LI to delete a internal network which in the inactive scope    console=true
