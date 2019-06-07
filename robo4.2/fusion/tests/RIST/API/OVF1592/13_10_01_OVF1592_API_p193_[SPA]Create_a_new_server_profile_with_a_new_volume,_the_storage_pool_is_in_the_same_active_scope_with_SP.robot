*** Settings ***
Documentation        Create a new server profile with a new volume, the storage pool is in the same active scope with SP
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
Suite Teardown        Run Keywords    Clear Environment After Test   ${create_server_profile_volume1}  Remove
...                   AND             Remove The Added Volume After Test

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Create a new server profile with a new volume, the storage pool is in the same active scope with SP
    [Documentation]  OVF1592 API p193 [Server Profile Administrator] Create a new server profile with a new volume, the storage pool is in the same active scope with SP
    set log level   TRACE
    Log     Create new server profiles sp5 with new volume active pool2      console=True
    ${resp}=  Add Server Profile  ${create_server_profile_pool1}    param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600
    Log   Check sp5 information   console=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SVOL:${new_vol_name}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SVOL:${new_vol_name}   ${False}
    Validate Volume Assigned/Unassigned To Server Profile  ${new_vol_name}  ${new_sp_name}  ${True}

*** Keywords ***
Remove The Added Volume After Test
    [Documentation]   Remove The Added Volume After Test
    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    ${resplist} =  Remove Storage Volumes Async  ${new_volumes_list}  param=?suppressDeviceUpdates=false
    Wait For Task2  ${resplist}  timeout=30  interval=10