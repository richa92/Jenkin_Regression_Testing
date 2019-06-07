*** Settings ***
Documentation
...     This Test Suite is to expand VM Harddiks
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      VM
Resource                        ../resource.txt

*** Test Cases ***
Poweroff And Set Fusion VM CPU
    [Tags]    HDD  C7000-IncreaseVMDisk  3.00
    [Documentation]     Poweroff And Set Fusion VM CPU
    connect_to_vi_server   ${vcpu_preupgrade['vsphere_ip']}  ${vcpu_preupgrade['username']}  ${vcpu_preupgrade['password']}
    power_off_vm           ${Fusion_Name_Final}
    ${status}      expand_vmdisk   ${Fusion_Name_Final}    ${hdd_size}
    Run Keyword If   '${status}' == 'success'        Log           VM disk expanded successfully  console=True
    Run Keyword Unless    '${status}' == 'success'             Fail   Failed to expand vm disk

Wait for VM Startup
    [Documentation]    Wait for VM startup
    [Tags]    STARTUP  C7000-IncreaseVMDisk  3.00
    power_on_vm            ${Fusion_Name_Final}
    Wait For Appliance To Be Ready      ${APPLIANCE_IP}