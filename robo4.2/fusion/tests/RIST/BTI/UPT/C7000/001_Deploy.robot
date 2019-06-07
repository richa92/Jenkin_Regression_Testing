*** Settings ***
Documentation   Deploy OVA
Resource        resource.txt

*** Variables ***
${DEPLOY_URL}                   http://ci-nexus.vse.rdlabs.hpecorp.net/Fusion/release/3.00.05/OVA/SSH/HPEOneView-SSH_3.00.05_271823_RC7.ova
${FUSION_NAME}                  UPT-OVA-C7000
${OVFtool}                      "C:\\ovftool\\ovftool.exe"
${OVFtool1}                     ovftool.exe
${vSphere_IP}                   risttestvcenter.vse.rdlabs.hpecorp.net
${vSphere_Username}             wpst-srm
${vSphere_Password}             wpstsrm1
${vSphere_Datastore}            "OneView"
${vSphere_Network}              "hpcorpnet-16.114"
${Target_Locator}               "vi://wpst-srm:wpstsrm1@risttestvcenter.vse.rdlabs.hpecorp.net/TEST/host/test-cluster"
${vSphere_vmFolder}                     "UPT"

*** Test Cases ***
C7000 UPT Deploy OVA Check OVFtool
    [Documentation]    Check If OVFTool installed on automation client
    ...    If it is not installed Fusion VM deployment will fail
    ${RC}   ${Output}=  Run and Return Rc and Output    dir ${OVFtool}
    Run Keyword Unless      '${RC}' == '0'      Fatal Error
    ...     msg=Could not find ovftool.exe. Is it installed?

C7000 UPT Deploy OVA Deploy Fusion
    [Documentation]    Deploy Fusion VM using latest build
    ${OVA_BUILD} =  Get OVA Build  ${DEPLOY_URL}
    Set Suite Variable  ${OVA_BUILD}
    ${FUSION_NAME} =  Set Variable  ${FUSION_NAME}-${OVA_BUILD}
    Set Suite Variable  ${FUSION_NAME}
    Log    \nDeploying VM: ${FUSION_NAME}  console=True
    ${Command}=    Catenate    ${OVFtool1}
    ...     --skipManifestCheck
    ...     --noSSLVerify
    ...     --acceptAllEulas
    ...     --machineOutput
    ...     --powerOn
    ...     --ipProtocol=IPv4
    ...     --powerOffTarget
    ...     --overwrite
    ...     --name="${FUSION_NAME}"
    ...     --datastore=${vSphere_Datastore}
    ...     --network=${vSphere_Network}
    ...     --diskMode=thin
    ...     --vmFolder=${vSphere_vmFolder}
    ...     ${Deploy_URL}
    ...     ${Target_Locator}
    Log     ${Command}
    ${RC}   ${Output}=      Run and Return Rc and Output    ${Command}
    Run Keyword Unless      '${RC}' == '0'      Fatal Error     msg=Could not deploy new VM ${Output}

C7000 UPT Deploy OVA Get Fusion IP Address
    [Documentation]    Get IP from newly deployed Fusion VM
    Connect To VI Server    ${vSphere_IP}   ${vSphere_Username}     ${vSphere_Password}
    #Wait for 5 minutes since Fusion IP sometimes takes time to get assigned
    Sleep   5 minutes
    Wait Until Keyword Succeeds     10 min      60 sec      Get VM IPv4 Addresses       ${FUSION_NAME}
    @{IPs}=     Get VM IPv4 Addresses       ${FUSION_NAME}
    ${Count}=       Get Length      ${IPs}
    Run Keyword If      ${Count} == 0       Fatal Error     msg=No IP address returned from vSphere
    ${IP}=      Get From List       ${IPs}      0
    Should Match RegExp     ${IP}       [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
    ...     msg=No valid IP address returned from vSphere
    Set Global Variable     ${APPLIANCE_IP}     ${IP}
    Set Global Variable     ${Fusion_URL}       https://${APPLIANCE_IP}
    Set Environment Variable    FUSION_URL      ${Fusion_Url}
    Set Environment Variable    FUSION_IP       ${APPLIANCE_IP}
    Log     \nYour FusionVM URL is: ${Fusion_URL}       console=True

C7000 UPT Deploy OVA Wait for VM Startup
    [Documentation]    Wait for VM startup
    Wait For Appliance To Be Ready      ${APPLIANCE_IP}

