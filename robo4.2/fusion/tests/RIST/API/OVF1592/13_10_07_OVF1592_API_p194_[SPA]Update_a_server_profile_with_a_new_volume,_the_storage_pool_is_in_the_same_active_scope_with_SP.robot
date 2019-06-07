*** Settings ***
Documentation        Update a server profile with a new volume, the storage pool is in the same active scope with SP
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Suite Teardown        Run Keywords    Revert SP Environment After Test    ${Edit_sp_network_base}
...                   AND             Remove The Added Volume After Test
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Update a server profile with a new volume, the storage pool is in the same active scope with SP
    [Documentation]  OVF1592_UI_p194 [SPA] Update a server profile with a new volume, the storage pool is in the same active scope with SP
    Log     Edit server profiles sp2 with new volume active pool2      console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_pool1}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600
    Log   Check sp2 information   console=True
    Validate Volume Assigned/Unassigned To Server Profile  ${new_vol_name}  ${sp_list[1]}  ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SVOL:${new_vol_name}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SVOL:${new_vol_name}   ${False}

*** Keywords ***
Remove The Added Volume After Test
    [Documentation]   Remove The Added Volume After Test
    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resplist} =  Remove Storage Volumes Async  ${new_volumes_list}  param=?suppressDeviceUpdates=false
    Wait For Task2  ${resplist}  timeout=30  interval=10