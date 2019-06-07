*** Settings ***
Documentation       Feature Test: Fusion i3S Integration
Resource            ../resource.robot
Suite Setup         Set Log Level    TRACE


*** Test Cases ***
Check if all ov appliances are reachable
    [Documentation]    Check if all ov appliances are reachable
    [Tags]    critical    INITIAL-SETUP    COPY-OV-BUILD
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    resource.Wait For Appliance To Become Pingable    ${ov_ip}

Check if all ov appliances have usbs mounted
    [Documentation]    Check if all ov appliances have usbs mounted
    [Tags]    critical    INITIAL-SETUP    COPY-OV-BUILD
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Is usb mounted on appliance    ${ov_ip}

Remove builds in ov appliances
    [Documentation]    Remove builds in ov appliances
    [Tags]    critical    INITIAL-SETUP    COPY-OV-BUILD
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Login to Appliance via SSH    ${ov_ip}
    \    ${output} =    Execute Command    rm -rf /mnt/usb/*
    \    ${output} =    Execute Command    cd /mnt/usb;ls | wc -l
    \    Should Contain    ${output}    0

Copy OV build to ov appliances
    [Documentation]    Copy OV build to ov appliances
    [Tags]    critical    INITIAL-SETUP    COPY-OV-BUILD
    ${buildName} =    Extract Build Name    ${Ov_Build}
    Set Suite Variable    ${ovBuildName}    ${buildName}
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Login to Appliance via SSH    ${ov_ip}
    \    ${output} =    Execute Command    cd /mnt/usb;curl -O 'http://[${build_server}%bond0]/${Ov_Build}'
    \    ${output} =    Execute Command    find / -name ${ovBuildName}
    \    Should Contain    ${output}     /mnt/usb/${ovBuildName}

Unzip OV build in ov appliances
    [Documentation]    Unzip OV build in ov appliances
    [Tags]    critical    INITIAL-SETUP    COPY-OV-BUILD
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Login to Appliance via SSH    ${ov_ip}
    \    ${output} =    Execute Command    cd /mnt/usb;unzip ${ovBuildName}
    \    ${output} =    Execute Command    echo $?
    \    Should Contain    ${output}    0
