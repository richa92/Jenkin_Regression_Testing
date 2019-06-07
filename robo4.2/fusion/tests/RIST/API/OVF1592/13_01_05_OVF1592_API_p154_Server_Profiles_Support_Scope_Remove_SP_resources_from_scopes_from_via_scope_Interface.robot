*** Settings ***
Documentation        Enclosure Groups Support Scope Remove EG resources from scopes from via scope Interface
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
Suite Teardown        Clear Environment After Test  ${create_server_profile}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles Support Scope_Remove SP resources from scopes from via scope Interface
  [Documentation]  Server Profiles Support Scope_Remove SP resources from scopes from via scope Interface
  Log   Remove SP5 scope of production     console=True
  ${SP_list1} =  Create List    SP:${new_sp_name}
  ${resp}=  Update Scope With Resources   ${Scope_List[0]}  resources_list=${SP_list1}  add_flag=${False}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SP:${new_sp_name}   ${False}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

