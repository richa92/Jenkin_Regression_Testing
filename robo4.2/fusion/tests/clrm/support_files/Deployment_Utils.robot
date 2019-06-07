*** Settings ***
Documentation    Deploy Fusion OVA
Library          SSHLibrary
Library          String
Library          RoboGalaxyLibrary
Library          FusionLibrary
Library          robot.api.logger
Library          copy
Resource         ../../../Resources/api/fusion_api_resource.txt
Variables        ../Deployment_Inputs/Ring_Data.py
Variables        ../Deployment_Inputs/DTO.py
Variables        ../Deployment_Inputs/data.py
*** Variables ***
${APP_TIMEOUT}          600
${APP_PROMPT}           #
${feature-toggle-loc}    /ci/bin/set-feature-toggles
${OV_HOSTNAME}    ${None}
${TAO_HOSTNAME}    ${None}

*** Keywords ***
Generate VM Name
    [Documentation]     Generate VM name
    [Arguments]    ${OVA_BUILD_LOCATION}    ${VM_NAME_PREFIX}=None
    ${name} =       Fetch From Right    ${OVA_BUILD_LOCATION},    /
    ${name} =       Fetch From Left     ${name},    .ova
    ${name}=        Catenate    SEPARATOR=_   ${VM_NAME_PREFIX}    ${name}
    [return]    ${name}

Deploy OVA Template
    [Documentation]    Creates a VM in the vCenter from an OVA. The power state of the VM can be defined by the user.
    ...    VM_NAME_PREFIX is used to prefix the VM name
    ...    FILESERVER_BUILDLOCATION is used to get builds
    ...    VSPHERE_NETWORK specify the networks as per the OVA
    [Arguments]    ${powerState}    ${VM_NAME_PREFIX}=None    ${FILESERVER_BUILDLOCATION}=None    ${VSPHERE_NETWORK}=None
    ${rc}   ${output}=  Run and Return Rc and Output    dir ${OVFTOOL}
    Return From keyword if    '${rc}' != '0'    ${rc}    Could not find ovftool.exe. Please check the OVFTool installtion in you setup
    ${Extract_NAME}=    Generate VM Name    ${FILESERVER_BUILDLOCATION}    ${VM_NAME_PREFIX}
    Set Suite Variable      ${Fusion_Name}      ${Extract_NAME}
    Console    \nDeploying VM: ${FUSION_NAME}
    ${command}=    Catenate    ${OVFTOOL}\\ovftool.exe
    ...     --skipManifestCheck
    ...     --noSSLVerify
    ...     --acceptAllEulas
    ...     --machineOutput
    ...     --ipProtocol=IPv4
    ...     --overwrite
    ...     --name="${FUSION_NAME}"
    ...     --datastore=${vSphere_Datastore}
    ...     --diskMode=thin
    @{keys} =  get dictionary keys  ${VSPHERE_NETWORK}
    :FOR  ${key}  in  @{keys}
    \    ${command}=    catenate  ${command}  --net:"${key}"="${VSPHERE_NETWORK['${key}']}"
    ${power_state} =    Run Keyword IF      "${powerState}" == "on"    Set Variable    --powerOn
    ...     ELSE IF     "${powerState}" == "off"     Set Variable    --powerOffTarget
    ${command} =    catenate  ${command}    ${power_state}
    ${command} =    catenate  ${command}
    ...     ${FILESERVER_BUILDLOCATION}
    ...     ${Target_Locator}
    Log    ${command}    console=True
    ${rc}   ${output}=      Run and Return Rc and Output    ${command}
    Log    ${output}    console=True
    [Return]    ${rc}    ${output}

Enable Feature Toggles For OV
    [Documentation]     Enables Debug Logging for CLRM and Enables Feature Toggles
    [Arguments]    ${APPLIANCE_IP}    @{FEATURE_TOGGLES}
    Deployment_Utils.Wait For Appliance To Become Pingable    ${APPLIANCE_IP}    30min    60sec
    Login to Appliance via SSH    ${APPLIANCE_IP}    ${FUSION_SSH_USERNAME}    ${FUSION_SSH_PASSWORD}
    Log    ${FEATURE_TOGGLES}    console=True
    ${command} =    catenate    ${feature-toggle-loc} -n
    :FOR    ${FEATURE}    IN    @{FEATURE_TOGGLES}
    \    ${command} =    catenate    ${command}
    \    ...    -e  ${FEATURE}
    Log    ${command}    console=True
    ${stdout} =  Execute Command    ${command}
    ${stdout} =  Execute Command    reboot
    Sleep    3m
    Deployment_Utils.Wait For Appliance To Become Pingable    ${APPLIANCE_IP}    5min    60sec
    Wait Until Keyword Succeeds    20min  3sec    Wait For Appliance To Be Ready    [${APPLIANCE_IP}]    20min    60sec

Import Certificate to OV
    [Documentation]    Adds the External_System Certificates from External_System to OneView Appliance
    [Arguments]    ${External_System_IP}    ${OV_IP}    ${OV_credentials}    ${alias_name}
    Fusion Api Login Appliance    ${OV_IP}    ${OV_credentials}
    ${response} =  Fusion Api Get Remote Certificate        ${External_System_IP}
    Set To Dictionary    ${CERTIFICATE['certificateDetails'][0]}    base64Data    ${response['certificateDetails'][0]['base64Data']}
    ${headers}=        Fusion APi Get Headers
    set to Dictionary        ${headers}        forceSaveLeaf=True
    set to Dictionary        ${CERTIFICATE['certificateDetails'][0]}        aliasName=${alias_name}
    ${resp}=        Fusion Api Import Server Certificate   ${CERTIFICATE}        headers=${headers}
    ${task}=       Wait For Task   ${resp}         timeout=500s            interval=5s
    ${response} =  Fusion Api Get Server Certificate   ${alias_name}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}

Add License and Verify that License is added
    [Documentation]     Add license
    [Arguments]    ${licenses}    ${type}
    ${count} =    set variable    0
    :FOR    ${ovLic}  IN  @{licenses}
    \    ${resp}=     Fusion Api Add License     ${ovLic['key']}    ${type}
    \    Should Be Equal    '${resp['status_code']}'    '201'    msg=Failed to Add License.
    \    Log to console and logfile    License is added to appliance
    \    ${lic-res} =    Get All OV Licenses
    \    ${response}=    Convert to Dictionary    @{lic-res}[${count}]
    \    ${key} =    Get From Dictionary    ${response}    key
    \    Log    ${key}
    \    Should Contain    ${ovLic['key']}    ${key}    msg=not added
    \    Log to console and logfile    "Verification on Adding a License into HP OneView has PASSED"
    \    ${count} =    Evaluate    ${count} + 1

Login to Appliance via SSH
    [Documentation]    Connect to Appliance CIM Bash via SSH
    ...    Example:\n| Login to Appliance Via SSH | 10.0.12.106 | Administrator | hpvse123 |
    [Arguments]    ${IP}    ${USERNAME}=${APP_SSH_USERNAME}
    ...    ${PASSWORD}=${APP_SSH_PASSWORD}
    ...    ${TIMEOUT}=${APP_TIMEOUT}    ${ALIAS}=APP_SSH
    ${Id} =    Open Connection    ${IP}    alias=${ALIAS}
    ${Output} =    Login    ${USERNAME}    ${PASSWORD}
    [Return]    ${Id}

Get Ipv6
    [Documentation]    Returns the first IPV6 Address of the VM
    [Arguments]    ${FUSION_NAME}
    Connect To VI Server   ${VSPHERE_IP}    ${VSPHERE_USERNAME}    ${VSPHERE_PASSWORD}
    ${powerState}=    Get VM Status    ${FUSION_NAME}
    Run Keyword if    '${powerState}' == 'poweredOff'    Power On VM    ${FUSION_NAME}
    ${macaddress}=    Get VM Network Devices    ${FUSION_NAME}
    ${eth0}=    Get From List    ${macaddress}    0
    ${resp}=    Get From Dictionary   ${eth0}    mac_address
    ${ipv6} =    Convert MAC to IPV6    ${resp}
    [return]    ${ipv6}

Set Fusion VM Memory and CPU
    [Documentation]     Configure First time setup for OneView Appliance
    [Arguments]    ${FUSION_NAME}    ${MEMORY_SIZE}=32768    ${VIRTUAL_SOCKETS}=8    ${CORE_PER_SOCKETS}=1
    Connect To VI Server    ${VSPHERE_IP}    ${VSPHERE_USERNAME}    ${VSPHERE_PASSWORD}
    set_vm_memory    ${FUSION_NAME}    ${MEMORY_SIZE}
    set_vm_cpu    ${FUSION_NAME}    ${VIRTUAL_SOCKETS}    ${CORE_PER_SOCKETS}
    Power On VM    ${FUSION_NAME}

First Time Setup with IPV6
    [Documentation]     Configure First time setup for OneView Appliance
    [Arguments]    ${APPLIANCE_IP}    ${newPassword}=admin123
    Log    ${APPLIANCE_IP}    console=True
    Log    \nWiating for Appliance to startup it takes 12 min    console=True
    Deployment_Utils.Wait For Appliance To Become Pingable  ${APPLIANCE_IP}    5min    60sec
    Wait For Appliance To Be Ready    [${APPLIANCE_IP}]    40min    60sec
    ${eula}=    Fusion Api Save EULA    [${APPLIANCE_IP}]
    Return From Keyword If    ${eula['status_code']}!=200    ${eula['status_code']}   EULA is not saved
    ${update_password} =    Create Dictionary
    ...    newPassword=${newPassword}
    ...    oldPassword=admin
    ...    userName=Administrator
    ${password}=   Fusion Api Change Administrator password    host=[${APPLIANCE_IP}]    body=${update_password}
    Run Keyword If   ${password['status_code']}==400  Log    Password is already set    WARN
    Run Keyword If   ${password['status_code']}==200  Log    Password is set
    ${admin_credentials} =    Create Dictionary    password=admin123
    ...    userName=Administrator
    Log    \nLogging in to the appliance after change password    console=True
    ${response}    ${session_id}=    Fusion Api Login Appliance    [${APPLIANCE_IP}]    ${admin_credentials}
    ${body}=    Run Keyword IF      "${APPLIANCE_TYPE}" == "TAO"    Update Appliance Data TAO    ${appliance_TAO}
    ...     ELSE IF     "${APPLIANCE_TYPE}" == "OV"     Update Appliance Data OV    ${appliance_OV}
    ...     ELSE        Fatal Error     msg=Could Not found Provided APPLIANCE_TYPE : ${APPLIANCE_TYPE}. Possible Options are TAO/OV
    ${resp}=    Fusion Api Configure Appliance Interfaces    ${body}
    Log    ${resp}    console=True
    Return From Keyword If    ${resp['status_code']}!=202    ${resp['status_code']}    ${resp['errorCode']}
    ${Appliance_IPv4}=    Run Keyword IF      "${APPLIANCE_TYPE}" == "TAO"    Set Variable    ${TAO_IP}
    ...     ELSE IF     "${APPLIANCE_TYPE}" == "OV"     Set Variable    ${OV_IP}
    ...     ELSE        Fatal Error     msg=Could Not found Provided APPLIANCE_TYPE : ${APPLIANCE_TYPE}. Possible Options are TAO/OV
    Deployment_Utils.Wait For Appliance To Become Pingable    ${Appliance_IPv4}    5min    60sec
    ${response}    ${session_id}=    Fusion Api Login Appliance    ${Appliance_IPv4}    ${admin_credentials}
    Wait For Task2    ${resp}    timeout=10m    interval=1m    errorMessage=Network Configuration Failed
    [return]    ${resp['status_code']}    ${resp['status_code']}

Update Appliance Data OV
    [Documentation]    New appliance IP, iptype and hostname will be updated at run time
    [Arguments]    ${body}
    ${resp} =   Fusion Api Get Appliance Interface Mac    eth0
    Set to dictionary   ${body['applianceNetworks'][0]}    macAddress  ${resp}
    Run keyword if    '${OV_TYPE}' != 'DCS'    Set to dictionary   ${body['applianceNetworks'][0]}    app1Ipv4Addr  ${OV_IP}
    ...    ELSE    Set to dictionary   ${body['applianceNetworks'][0]}    virtIpv4Addr  ${OV_IP}
    Run keyword if    '${OV_HOSTNAME}' != 'None'    Set to dictionary   ${body['applianceNetworks'][0]}    hostname  ${OV_HOSTNAME}
    Log    ${body}    console=True
    [return]    ${body}

Wait For Appliance To Become Pingable
    [Documentation]    Waits for an appliance to become pingable
    [Arguments]    ${appliance}={IP}    ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds    ${timeout}    ${interval}    Deployment_Utils.Appliance is pingable    ${appliance}

Appliance is pingable
    [Documentation]    Checks the IPV6 Ping in Windows
    [Arguments]    ${appliance}
    Run keyword if    os.name == "nt"    Deployment_Utils.Windows ping    ${appliance}
    ...    ELSE    Unix ping    ${appliance}

Appliance is unreachable
    [Documentation]    Waits for an appliance to become unreachable
    [Arguments]    ${appliance}    ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds    ${timeout}    ${interval}    Windows ping unreachable check    ${appliance}
    Run keyword if    os.name == "nt"    Windows ping unreachable check    ${appliance}

Windows ping
    [Documentation]    Windows Ping
    [Arguments]    ${host}
    ${Output}=    Run    ping -n 4 ${host}
    Should Contain    ${Output}    Reply from
    [Return]    ${Output}

Windows ping unreachable check
    [Documentation]    Ping Check in Windows
    [Arguments]    ${host}
    ${Output}=    Run    ping -n 4 ${host}
    Should Contain    ${Output}    unreachable
    [Return]    ${Output}

Get IPV4 from network Settings
    [Documentation]    Gets the IPV4 from the Config file
    ${appliance_netwroks} =    Get From Dictionary    ${appliance}    applianceNetworks
    Log    ${appliance_netwroks}    console=True
    :For    ${Network}    IN    @{appliance_netwroks}
    \    Log    ${Network}
    \    ${device} =    Evaluate    $Network.get("device")
    \    ${Appliance_IPv4} =    Get from Dictionary    ${Network}    app1Ipv4Addr
    \    Run Keyword If    '${device}' == 'eth0'    Exit For Loop
    Log    ${Appliance_IPv4}    console=True
    [return]    ${Appliance_IPv4}

Convert MAC to IPV6
    [Documentation]    Converts the MAC address to IPV6
    [Arguments]    ${macaddress}
    @{parts}=    Split String    ${macaddress}    :
    Insert into list    ${parts}    3    ff
    Insert into list    ${parts}    4    fe
    ${a}=    Evaluate    "%x" % (int(${parts}[0], 16) ^ 2)
    set list value    ${parts}    0    ${a}
    ${ipv6parts} =     Create List
    ${count} =    Get Length    ${parts}
    : FOR    ${i}    IN RANGE    0    ${count}    2
    \    ${b} =    Evaluate    "".join(${parts}[${i}:${i}+2])
    \    Append to list    ${ipv6parts}    ${b}
    Log    ${ipv6parts}
    ${ipv6} =    Evaluate    "fe80::%s" % (":".join(${ipv6parts}))
    [return]    ${ipv6}

Tbird DCS Discover Hardware
    [Documentation]     Invoke Hardware Discovery
    Login to Appliance via SSH    ${OV_IP}    ${FUSION_SSH_USERNAME}    ${FUSION_SSH_PASSWORD}
    ${stdout}=  Execute Command    dcs status
    Log    ${stdout}    console=True
    Set Global Variable    ${FUSION_IP}    ${OV_IP}
    Log       X-API-Ver: ${X-API-VERSION}    console=True
    Fusion Api Login Appliance    ${OV_IP}    ${ADMIN_CREDENTIALS}
    Invoke Hardware Setup       timeout=720
    Sleep    60s
    Wait For ALL Enclosures In OK Status    timeout=1200
    Fusion Api Logout Appliance

C7000 DCS Set Schematic to virtualCenter_1.1
    [Documentation]     Change DCS Schematics to virtualCenter_1.1
    Login to Appliance via SSH    ${OV_IP}    ${FUSION_SSH_USERNAME}    ${FUSION_SSH_PASSWORD}
    ${changeStatus}=    Change DCS Schematic To C7000
    # Retry logic
    ${retryStatus}=    run keyword if    'partial success' in '''${changeStatus}'''    Change DCS Schematic To C7000
    ...    ELSE    Set Variable    ${changeStatus}
    Should Contain    ${retryStatus}    DCS is Running

Change DCS Schematic To C7000
    [Documentation]     Change DCS Schematics to virtualCenter_1.1
    ${stdout_dcsStop}=    Execute Command    dcs stop
    #Sleep    20s
    Log    ${stdout_dcsStop}    console=True
    Should Contain    ${stdout_dcsStop}    DCS is Stopped
    ${stdout_dcsStart}=    Execute Command    dcs start /dcs/schematic/virtualCenter_1.1/ cold
    #Sleep    60s
    Log    ${stdout_dcsStart}    console=True
    Run Keyword And Ignore Error    Should Contain    ${stdout_dcsStart}    Data Center Simulator started
    ${stdout_dcsStatus}=    Execute Command    dcs status
    Log    ${stdout_dcsStatus}    console=True
    [return]    ${stdout_dcsStatus}