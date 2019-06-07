*** Settings ***
Documentation
...     This Test Suite is to edit VM CPU and Memory
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      VM
Resource                        ../resource.txt

*** Test Cases ***
Poweroff And Set Fusion VM CPU And Memory
    [Tags]    VCPU  C7000
    [Documentation]     Poweroff And Set Fusion VM CPU and Memory
    Set Log Level          TRACE
    connect_to_vi_server   ${vcpu_preupgrade['vsphere_ip']}  ${vcpu_preupgrade['username']}  ${vcpu_preupgrade['password']}
    power_off_vm           ${Fusion_Name_Final}
    set_vm_memory          ${Fusion_Name_Final}  ${vcpu_preupgrade['memory_size']}
    set_vm_cpu             ${Fusion_Name_Final}  ${vcpu_preupgrade['sockets']}  ${vcpu_preupgrade['core_per_sockets']}
    power_on_vm            ${Fusion_Name_Final}

Wait for VM Startup
    [Documentation]    Wait for VM startup
    [Tags]    STARTUP  C7000
    Set Log Level          TRACE
    Wait For Appliance To Be Ready      ${APPLIANCE_IP}