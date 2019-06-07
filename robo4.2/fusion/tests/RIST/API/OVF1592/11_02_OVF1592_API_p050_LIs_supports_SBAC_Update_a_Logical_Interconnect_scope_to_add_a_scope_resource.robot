*** Settings ***
Documentation        Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to add a scope resource
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
Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to add a scope resource
    [Documentation]  OVF1592_API_p050 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to add a scope resource
    log    Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to add a scope resource    console=true
    Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
    ${resp} =    Patch Resources Scopes  LI:${LI1}   ${Patch_add_Scope3}
    Wait For Task2    ${resp}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}  ${TRUE}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  LI:${LI1}  ${TRUE}
    log    Successfully! Test Case : OVF1592_API_p050 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is the active scope to add a scope resource    console=true
