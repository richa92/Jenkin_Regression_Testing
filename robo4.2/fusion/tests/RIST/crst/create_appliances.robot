*** Settings ***
Documentation		Creates OneView and Plexxi CFM appliances
...                 pybot -d /tmp/logs/ -L DEBUG -V <datafile> -v OV_OVA:<url or local file> -v CFM_OVA:<url or local file>
Library             RoboGalaxyLibrary
Suite Setup      connect to vi server   ${vcenter['server']}   ${vcenter['user']}   ${vcenter['password']}

*** Test Cases ***
Deploy OneView appliance
    [Tags]   ov
    should not be empty    ${OV_OVA}    msg=You must provide -v OV_OVA:<url or local file>
    ${resp} =   deploy ova   ova=${OV_OVA}
    ...                      importSpecParams=${ov_ova_data['import_spec']}
    ...                      resource_pool=${ov_ova_data['resource_pool']}
    Should not be true   ${resp}


Power ON OneView appliance
    [Documentation]   Power on OV
    [Tags]   Power_On    ov
    ${Status} =    Get VM Status   ${ov_vm}
    Should be Equal As Strings      poweredOff      ${Status}   msg=VM ${ov_vm} is not in Powered Off State.
    Power On VM     ${ov_vm}
    ${Status} =    Get VM Status   ${ov_vm}
    Should be Equal As Strings      poweredOn      ${Status}   msg=VM ${ov_vm} is not in Powered On State.


Deploy CFM appliance
    [Tags]   cfm
    should not be empty    ${CFM_OVA}    msg=You must provide -v CFM_OVA:<url or local file>
    ${resp} =   deploy ova   ova=${CFM_OVA}
    ...                      importSpecParams=${cfm_ova_data['import_spec']}
    ...                      resource_pool=${cfm_ova_data['resource_pool']}
    Should not be true   ${resp}


Power ON CFM appliance
    [Documentation]   Power on CFM
    [Tags]   Power_On    cfm
    ${Status} =    Get VM Status   ${cfm_vm}
    Should be Equal As Strings      poweredOff      ${Status}   msg=VM ${cfm_vm} is not in Powered Off State.
    Power On VM     ${cfm_vm}
    ${Status} =    Get VM Status   ${cfm_vm}
    Should be Equal As Strings      poweredOn      ${Status}   msg=VM ${cfm_vm} is not in Powered On State.