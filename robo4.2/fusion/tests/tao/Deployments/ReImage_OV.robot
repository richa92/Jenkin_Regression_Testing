*** Settings ***
Documentation    Deploy Oneview OVA
Resource         ../support_files/Deployment_Utils.robot
Suite Setup      Set Log Level    Trace


*** Test Cases ***
Deploy OV
    [Documentation]    Creates a VM in the vCenter from an OVA
    [Tags]    ENB_MAT    Deploy
    ${rc}    ${output}=    Deploy OVA Template    on    ${VM_NAME_PREFIX}    ${FILESERVER_BUILDLOCATION}    ${VSPHERE_NETWORK}
    Run Keyword Unless    '${rc}' != '1'    Fatal Error
    ...    msg=${output}

Enable Dev Features
    [Documentation]    Enables Dev features. Feature toggles should be provided by the user
    [Tags]    ENB_MAT   Deploy    features
    ${VM_IPV6} =    Wait Until Keyword Succeeds    20 minutes    2 minutes    Get Ipv6    ${Fusion_Name}
    Run keyword if    ${FEATURE_TOGGLES}    Wait Until Keyword Succeeds    20 minutes    2 minutes    Enable Feature Toggles For OV    ${VM_IPV6}    @{FEATURE_TOGGLES}

FTS OV
    [Documentation]    Performs First time setup for the deployed appliance
    [Tags]    ENB_MAT   FTS
    ${VM_IPV6} =    Wait Until Keyword Succeeds    20 minutes    2 minutes    Get Ipv6    ${Fusion_Name}
    ${returncode}    ${msg}=    First Time Setup with IPV6     ${VM_IPV6}
    Run keyword IF    ${returncode}!=202    Fatal Error    ${msg}
