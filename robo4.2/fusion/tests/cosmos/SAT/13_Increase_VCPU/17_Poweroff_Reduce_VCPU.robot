*** Settings ***
Documentation
...     This Test Suite is to edit VM CPU
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      VM
Resource                        ../resource.txt

*** Test Cases ***
Poweroff And Set Fusion VM CPU
    [Tags]    VCPU  C7000-ReduceVCPU  4.0  3.10
    [Documentation]     Poweroff And Set Fusion VM CPU
    connect_to_vi_server   ${vcpu_postupgrade['vsphere_ip']}  ${vcpu_postupgrade['username']}  ${vcpu_postupgrade['password']}
    power_off_vm           ${Fusion_Name_Final}
    set_vm_cpu             ${Fusion_Name_Final}  ${vcpu_postupgrade['sockets']}  ${vcpu_postupgrade['core_per_sockets']}
    power_on_vm            ${Fusion_Name_Final}

Wait for VM Startup
    [Documentation]    Wait for VM startup
    [Tags]    STARTUP  C7000-ReduceVCPU  4.0  3.10
    Wait For Appliance To Be Ready      ${APPLIANCE_IP}