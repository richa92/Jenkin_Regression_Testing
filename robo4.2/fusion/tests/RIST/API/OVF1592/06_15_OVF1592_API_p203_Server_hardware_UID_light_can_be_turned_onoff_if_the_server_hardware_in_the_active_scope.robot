*** Settings ***
Documentation        Server hardware support SBAC_UID light can be turned onoff if the server hardware in the active scope
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
Server hardware support SBAC_UID light can be turned onoff if the server hardware in the active scope
    [Documentation]  OVF1592_API_p203 Server hardware support SBAC_UID light can be turned onoff if the server hardware in the active scope
    log    Server hardware support SBAC_UID light can be turned onoff if the server hardware in the active scope    console=true
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
    ${resources_list} =    Create List    SH:${sh_name}
    Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
    Fusion Api Logout Appliance
    Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
    ${resp}=     Patch Server Hardware  ${sh_name}  op=replace  path=/uidState  value=On
    Wait For Task2  ${resp}  timeout=60  interval=5
    ${resp}=     Patch Server Hardware  ${sh_name}  op=replace  path=/uidState  value=Off
    Wait For Task2  ${resp}  timeout=60  interval=5
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SH:${sh_name}  ${FALSE}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
    log    Successfully! Test Case :OVF1592_API_p203 Server hardware support SBAC_UID light can be turned onoff if the server hardware in the active scope    console=true
