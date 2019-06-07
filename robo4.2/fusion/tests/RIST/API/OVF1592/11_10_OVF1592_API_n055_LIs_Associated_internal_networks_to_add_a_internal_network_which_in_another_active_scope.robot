*** Settings ***
Documentation        Logical Interconnects Associated with internal networks_Update a LI to add a internal network which in another active scope
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
Logical Interconnects Associated with internal networks_Update a LI to add a internal network which in another active scope
    [Documentation]  OVF1592_API_n055 Logical Interconnects Associated with internal networks_Update a LI to add a internal network which in another active scope
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    LI:${LI1}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
#  ${resources_list} =    Create List    ETH:${ETH_INACTIVE}
#  Update Scope With Resources    scope_name=${Scope_List[0]}    resources_list=${resources_list}
    Log    Logical Interconnects Associated with internal networks_Update a LI to add a internal network which in another active scope    console=true
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp}=  Update Logical Interconnect Internal Network  ${LI1}    ${li_internal_network_add_active2}
    Wait For Task2   ${resp}   timeout=600   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  LI:${LI1}  ${FALSE}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
    Log    Successfully! Test Case : OVF1592_API_n055 Logical Interconnects Associated with internal networks_Update a LI to add a internal network which in another active scope    console=true
