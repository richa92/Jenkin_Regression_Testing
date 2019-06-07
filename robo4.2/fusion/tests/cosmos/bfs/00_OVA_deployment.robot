*** Settings ***
Documentation    Deploy latest Fusion OVA
...     = Variables =
...     | FUSION_NAME | Required. VMware name for  the Fusion VM.
...     | DEPLOY_URL | Required. if we want to install build other than top of tree
...     | FUSION_DEPOT | URL specifying location of the OVA files.|
...     | | (default http://ci-nexus.vse.rdlabs.hpecorp.net/Fusion/rel/3.10/OVA/DCS/ ).|
...     | VSPHERE_DATASTORE | vShpere device to hold deployed VM (default fusionvm-1)|
Resource        resource.txt

*** Test Cases ***
Get Latest Fusion PASS Build URL
    [TAGS]    DEFAULT_URL
    [Documentation]    Get Latest Fusion PASS BUILD URL
    #For Selecting Pass build only use non_passed = False
    #${ova}=     Get LatestBuild Name        ${Fusion_Depot}     ''      ova
    #Set Suite Variable      ${DEPLOY_URL}       ${Fusion_Depot}${ova}
    Set Suite Variable      ${DEPLOY_URL}       ${Fusion_Depot}
    Log     \nDeploying from: ${DEPLOY_URL}
    Set Suite Metadata      Deployed URL    ${DEPLOY_URL}   top=True

Extract Build Id Number
    [Documentation]    Extract Build Id Number
     [TAGS]    BUILD-ID
    #Using regular expression to match the ID with URL
    ${status_non_pass} =        Run Keyword And Return Status
    ...    Should Match Regexp    ${DEPLOY_URL}    (\\d{6,7})\.ova$
    ${status_pass} =    Run Keyword And Return Status
    ...    Should Match Regexp    ${DEPLOY_URL}    (\\d{6,7})\_.*\.ova$
    ${id}=  Run Keyword If  ${status_non_pass} == True or ${status_pass} == True
    ...    get regexp matches    ${DEPLOY_URL}    (\\d{6,7})
    ${id_match}=        Get From List   ${id}   0
    Set Suite Variable    ${FUSION_ID}    ${id_match}
    Set Suite Metadata     Fusion Build Id    ${FUSION_ID}    top=True
    Set Global Variable    ${FUSION_NAME_FINAL}    ${FUSION_NAME}_${FUSION_ID}
    Set Suite Metadata     Fusion VM Name    ${FUSION_NAME_FINAL}    top=True

Check OVFtool
    [Documentation]    Check If OVFTool installed on automation client
    ...    If it is not installed Fusion VM deployment will fail
    [TAGS]   OVF
    ${rc}   ${output}=  Run and Return Rc and Output    dir ${OVFTOOL}
    Run Keyword Unless      '${rc}' == '0'      Fatal Error
    ...     msg=Could not find ovftool.exe. Is it installed?

Deploy Fusion
    [Documentation]    Deploy Fusion VM using latest build
    [TAGS]    DEPLOY
    Log    \nDeploying VM: ${Fusion_Name_Final}
    ${command}=    Catenate    ${OVFTOOL}
    ...     --skipManifestCheck
    ...     --noSSLVerify
    ...     --acceptAllEulas
    ...     --machineOutput
    ...     --powerOn
    ...     --ipProtocol=IPv4
    ...     --powerOffTarget
    ...     --overwrite
    ...     --name="${Fusion_Name_Final}"
    ...     --datastore="${vSphere_Datastore}"
    ...     --network="${vSphere_Network}"
    ...     --diskMode=thin
    ...     --vmFolder="${VMFOLDER}"
    ...     "${DEPLOY_URL}"
    ...     "${Target_Locator}"
    Log     ${command}
    ${rc}   ${output}=      Run and Return Rc and Output    "${command}"
    Run Keyword Unless    '${rc}' == '0'    Fatal Error    msg=Could not deploy new VM ${output}

Get Fusion IP Address
    [Documentation]    Get IP from newly deployed Fusion VM
    [TAGS]    GET-IP
    Connect To VI Server    ${VSPHERE_IP}   ${VSPHERE_USERNAME}     ${VSPHERE_PASSWORD}
    #Wait for 5 minutes since Fusion IP sometimes takes time to get assigned
    Sleep   5 minutes
    Wait Until Keyword Succeeds  10 min  60 sec  Get VM IPv4 Addresses  ${FUSION_NAME_FINAL}
    @{ips}=     Get VM IPv4 Addresses       ${FUSION_NAME_FINAL}
    ${count}=       Get Length      ${ips}
    Run Keyword If      ${count} == 0    Fatal Error     msg=No IP address returned from vSphere
    ${ip}=      Get From List       ${ips}      0
    Should Match RegExp     ${ip}       [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
    ...     msg=No valid IP address returned from vSphere
    Set Global Variable     ${APPLIANCE_IP}     ${ip}
    Set Environment Variable    FUSION_IP       ${APPLIANCE_IP}
    Log     \nYour Fusion IP is: ${APPLIANCE_IP}
    ${file_ip}=    set variable    ${CURDIR}\\..\\..\\..\\..\\file_with_ip.txt
    CreateFile     ${file_ip}      ${APPLIANCE_IP}

Set Fusion URL
    [Documentation]    Set global, environment variable and suite metada for Fusion URL.
    [TAGS]    SET-URL
    Set Global Variable     ${FUSION_URL}       https://${APPLIANCE_IP}
    Set Environment Variable    FUSION_URL      ${FUSION_URL}
    Set Suite Metadata      Fusion URL:     ${FUSION_URL}       top=True
    Log     \nYour Fusion URL is: ${FUSION_URL}

Wait for VM Startup
    [Documentation]    Wait for VM startup
    [TAGS]    START-VM
    Wait For Appliance To Be Ready      ${APPLIANCE_IP}  timeout=40 min
