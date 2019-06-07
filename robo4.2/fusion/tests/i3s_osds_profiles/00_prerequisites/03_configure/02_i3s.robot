*** Settings ***
Documentation    I3S Enablement Prerequisites
...              Usage =
...              cmdline: pybot -d ../logs  --timestampoutputs -t <target test case> <target test file>
...              Workflows:
...              pybot -v fusion_api_resource:"C:/new_src/fusion/Resources/api/fusion_api_resource.txt" "C:\new_src\i3s\tests\i3s\I3sFusionEnablement\prerequisites\i3s_prerequisites.txt"

Resource         ../resource.robot
Suite Setup      Login to Fusion Via REST    ${fusion_ip}    ${admin_credentials}
Suite Teardown   I3S Suite Teardown

*** Test Cases ***
Get i3s Appliance Cluster IP and Login
    [Documentation]    Login to I3s Using Onview Authtoken
    [Tags]    LOGIN    I3S-SETUP
	Set Log Level    Trace
    ${authtoken} =     Login to Fusion Via REST    ${fusion_ip}    ${admin_credentials}
    ${i3s_details} =     Fusion Api Get i3sCluster IP
    ${i3s_ip} =    Get From Dictionary    ${i3s_details['members'][0]}    primaryIPV4
    Log    \nI3s IP: ${i3s_ip}    console=True
    I3S API LOGIN APPLIANCE    ${i3s_ip}    ${authtoken}

Add Golden Images
    [Documentation]    Add Golden Images
    [Tags]   ADD-GI    I3S-SETUP    P0
    :FOR    ${goldenimage}    IN    @{golden_images}
    \    ${gi_resp} =    Get Goldenimage URI    ${goldenimage['name']}
    \    Run Keyword If    '${gi_resp}'!='None'    Run Keywords
    \    ...    Log    \n...Golden Image ${goldenimage['name']} already exists in appliance    console=True    AND
    \    ...    Continue For Loop
    \    Log    Adding Golden Image ${goldenimage['name']}   console=True
    \    ${NAME}=    Get From Dictionary     ${goldenimage}    name
    \    ${DESC}=    Get From Dictionary     ${goldenimage}    description
    \    ${GI_PATH}=    Get From Dictionary    ${goldenimage}    path
    \    ${Response}=    i3s api add golden images    ${GI_PATH}    param=?name=${NAME}&description=${DESC}
    \    Should Be Equal as Strings    ${Response['status_code']}    202    msg=Failed to create GoldenImage
    \    Run Keyword If    ${Response['status_code']}==202    Wait For GI Complete  ${Response}   ${NAME}

Add Artifact Bundle
    [Documentation]   Add Artifact Bundle
    [Tags]    ADD-AB    I3S-SETUP    P0
    ${name} =    Get From Dictionary    ${artifactbundle_add}    name
    Log    \Add Artifact Bundle ${name}.    console=True
    ${response} =    i3s Api Add Artifact Bundle    ${artifactbundle_add['path']}
    Should Be Equal as Strings    ${response['status_code']}    202    msg=Failed to add Artifact Bundle.
    # Wait for task to complete
    ${retryInterval}    Convert To Number     60
    ${retries}          Convert To Integer    20
    ${resp}=    i3s API Wait For Task To Complete    ${response['headers']['Location']}    sleep_time=${retryInterval}    retries=${retries}
    # Check for errors
    ${errors}=    Get From Dictionary    ${resp}    taskErrors
    ${errCount}=    Get Length    ${errors}
    Should be True    ${errCount} == 0    msg=Errors encountered while adding Artifact Bundle

Extract Artifact Bundle
    [Documentation]    Extract Artifact Bundle
    [Tags]    EXTRACT-AB    I3S-SETUP    P0
    ${ab_uri} =    Get ArtifactBundle Uri    ${artifactbundle_add['name']}
    Run Keyword If    '${ab_uri}'=='None'    Fail    \n...Artifact Bundle ${artifactbundle_add['name']} not exists in appliance

    Log    \Extract Artifact Bundle ${artifactbundle_add['name']}    console=True
    ${response} =    i3s Api Extract Artifact Bundle    ${ab_uri}
    Should Be Equal as Strings    ${response['status_code']}    202    msg=Failed to extract Artifact Bundle.
    # Wait for task to complete
    ${retryInterval}    Convert To Number     60
    ${Retries}          Convert To Integer    20
    ${resp}=    i3s API Wait For Task To Complete    ${response['headers']['Location']}    sleep_time=${retryInterval}    retries=${Retries}
    # Check for errors
    ${errors}=    Get From Dictionary    ${resp}    taskErrors
    ${errCount}=    Get Length    ${errors}
    Should be True    ${errCount} == 0    msg=Errors encountered while adding Artifact Bundle
    Sleep    3min

Create Plan Script
    [Documentation]    Create Plan Script
    [Tags]    PS    I3S-SETUP    P0

    :For    ${script}    IN    @{planscript}
    \    ${ps_resp} =    i3s Api Get Plan Scripts    param=?filter="'name'=='${script['name']}'"
    \    Continue For Loop If    ${ps_resp['count']}==1
    \    ${response} =    I3s Api Create Plan Scripts    ${script}
    \    Should Be Equal as Strings    ${response['status_code']}    201    msg=Failed to Create PlanScripts

Create OSBuildplan
    [Documentation]    Create OS Build plan
    [Tags]    OSBP    I3S-SETUP    P0

    :For    ${buildPlan}    IN    @{buildPlans}
    \    ${osbp_resp} =    i3s Api get buildplan    param=?filter="'name'=='${buildPlan['name']}'"
    \    Continue For Loop If    ${osbp_resp['count']}==1
    \    ${bp_body} =    Create Build Plan Payload    ${buildPlan}
    \    ${resp} =    i3S_api_create_buildplan    ${bp_body}
    \    Should Be Equal as Strings    ${resp['status_code']}    201    msg=Failed to Create Build Plan with Type Deploy

Create OE Deployment Plan
    [Documentation]    Create OE Deployment Plan
    [Tags]    OEDP    I3S-SETUP    P0

    :For    ${oedp}    IN    @{deploymentplans}
    \    ${oedp_resp} =    i3s Api Get Deploymentplan    param=?filter="'name'=='${oedp['name']}'"
    \    Continue For Loop If    ${oedp_resp['count']}==1
    \    ${dp_body} =    Create Deploymentplan Payload    ${oedp}
    \    ${resp} =    i3s Api Create Deploymentplan    ${dp_body}
    \    Should Be Equal as Strings    ${resp['status_code']}    201    msg=Failed to Create DeploymentPlan
