*** Settings ***
Documentation        Logical Interconnects support SBAC_Try to "update from group" for LI which in the active scope
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
Logical Interconnects support SBAC_Try to "update from group" for LI which in the active scope
  [Documentation]  OVF1592_API_p053 Logical Interconnects support SBAC_Try to "update from group" for LI which in the active scope
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    LIG:${LIG[4]}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  log    Logical Interconnects support SBAC_Try to "update from group" for LI which in the active scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =  Update Logical Interconnect Internal Network  ${LI1}    ${li_internal_network_add_active1}
  Wait For Task2   ${resp}    timeout=600    interval=10
  ${resp} =  Update Logical Interconnect from Group    ${li_update_dto}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  LI:${LI1}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_p053 Logical Interconnects support SBAC_Try to "update from group" for LI which in the active scope    console=true
