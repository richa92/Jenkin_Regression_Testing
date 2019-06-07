*** Settings ***
Documentation       Feature Test: Fusion i3S Integration
Resource            ../resource.robot
Suite Setup         Set Log Level    TRACE

*** Test Cases ***
Check if all i3s appliances are reachable
    [Documentation]    Check if all i3s appliances are reachable
    [Tags]    critical    INITIAL-SETUP
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    resource.Wait For Appliance To Become Pingable    ${i3s_ip}

Check if all i3sappliances have usbs mounted
    [Documentation]    Check if all i3sappliances have usbs mounted
    [Tags]    critical    INITIAL-SETUP
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Is usb mounted on appliance    ${i3s_ip}

Remove builds in I3S appliances
    [Documentation]    Remove builds in I3S appliances
    [Tags]    critical    INITIAL-SETUP
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Login to Appliance via SSH    ${i3s_ip}
    \    ${output} =    Execute Command    rm -rf /mnt/usb/*
    \    ${output} =    Execute Command   cd /mnt/usb;ls | wc -l
    \    Should Contain    ${output}    0

Copy I3S build to I3S appliances
    [Documentation]    Copy I3S build to I3S appliances
    [Tags]    critical    INITIAL-SETUP
    ${buildName} =    Extract Build Name    ${I3S_Build}
    Set Suite Variable    ${i3sBuildName}    ${buildName}
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Login to Appliance via SSH    ${i3s_ip}
    \    ${output} =    Execute Command    cd /mnt/usb;curl -O 'http://[${build_server}%br0]/${I3S_Build}'
    \    ${output} =    Execute Command    find / -name ${buildName}
    \    Should Contain    ${output}    /mnt/usb/${buildName}

Unzip I3S build in I3S appliances
    [Documentation]    Unzip I3S build in I3S appliances
    [Tags]    critical    INITIAL-SETUP
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \   Login to Appliance via SSH  ${i3s_ip}
    \   ${output} =    Execute Command    cd /mnt/usb;unzip ${i3sBuildName}
    \   ${output} =    Execute Command    echo $?
    \   Should Contain    ${output}    0
