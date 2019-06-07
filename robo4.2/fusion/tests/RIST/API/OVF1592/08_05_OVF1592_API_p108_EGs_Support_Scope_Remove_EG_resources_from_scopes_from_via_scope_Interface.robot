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
Suite Teardown        Remove Enclosure Group By Name  ${new_EG_name}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups Support Scope Remove EG resources from scopes from via scope Interface
  [Documentation]  OVF1592 API p108 Enclosure Groups Support Scope Remove EG resources from scopes from via scope Interface

  Log   Remove EG5 scope of production     console=True
  ${EG_list1} =  Create List    EG:${new_EG_name}
  ${resp}=  Update Scope With Resources   ${Scope_List[0]}  resources_list=${EG_list1}  add_flag=${False}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  EG:${new_EG_name}   ${False}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  EG:${new_EG_name}   ${True}

