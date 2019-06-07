*** Settings ***
Documentation   Example test suite for executing OS Deployment keywords
...   ex: (.venv) C:\fusion\f500\fusion\tests\RIST\crst\prep>pybot -V ..\resources\Vader6_rig_ov500.py  -v OV_IP:10.177.14.1 -v cpt_profiles:ProfileR4_U20,ProfileR5_U35 os_deploy_test_suite.robot
...   You can also provide the cpt_profiles as a list variable in the data file or test suite

Library         RoboGalaxyLibrary
Library         FusionLibrary
Library         os_deploy_data_file.py
Variables       os_deploy_data_file.py
Resource        ../../../../Resources/api/fusion_api_resource.txt

Suite Setup     Prepare Test Env


*** Variables ***
${OV_IP}        None
&{OV_CRED}      userName=Administrator      password=hpvse123


*** Keywords ***
Prepare Test Env
    [Documentation]     Prepares the testing environment by logging to the appliances
    Set Log Level   Trace
    CPT Login       ${cpt_host['host']}     ${cpt_host['user']}     ${cpt_host['password']}
    ${r}    ${s}=    Fusion Api Login Appliance  ${OV_IP}  ${OV_CRED}
    Run Keyword If  ${r['status_code']} is not 200    Fail      Unable to login


*** Test Cases ***
Parallel OS Deployment
    [Tags]   PARALLEL
    [Documentation]     Verifies multiple provisioning of OSes on different systems
    Variable should exist    ${cpt_profiles}   You must supply values for 'cpt_profile' variable \nex: -v cpt_profiles:ProfileR1_U1,ProfileR1_U2
    @{batch1} =   make_cpt_batch   ${server_hardware_cpt}   ${cpt_profiles}
    @{SR1}=     Create List
    :FOR   ${server}   IN   @{batch1}
    \      ${seed} =   create_seed   os=${server['os']}   net=${server['deployment_network']}   ilou=${server['username']}   ilop=${server['password']}
    \      ${SRV_URI} =    Get Server Profile URI    ${server['profile']}
    \      @{L}=    Create List   ${SRV_URI}    ${seed}
    \      &{pay}=         Create CPT Payload For OS Deployment    ${SRV_URI}      ${seed}
    \      Append to List    ${SR1}     ${pay}
    @{fn}=      CPT Parallel OS Deployment      ${SR1}    timeout=${40}

