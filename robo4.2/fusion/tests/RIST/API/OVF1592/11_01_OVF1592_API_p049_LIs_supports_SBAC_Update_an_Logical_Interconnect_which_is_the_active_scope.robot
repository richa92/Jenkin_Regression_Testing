*** Settings ***
Documentation        Logical Interconnects supports SBAC_Update an Logical Interconnect which is the active scope
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
Logical Interconnects supports SBAC_Update an Logical Interconnect which is the active scope
  [Documentation]  OVF1592_API_p049 Logical Interconnects supports SBAC_Update an Logical Interconnect which is the active scope
  ${resources_list} =    Create List    LI:${LI1}
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  log    Interconnects supports SBAC_Update an Logical Interconnect which is the active scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resps}=  Edit Telemetry Configurations for LI  ${li_profile}
  Wait For Task2    ${resps}   600    10
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  LI:${LI1}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
  ${resps}=  Edit Telemetry Configurations for LI  ${li_profile_back}
  Wait For Task2    ${resps}   600    10
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  LI:${LI1}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_p049 Logical Interconnects supports SBAC_Update an Logical Interconnect which is the active scope    console=true
