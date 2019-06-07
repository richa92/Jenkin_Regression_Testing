*** Settings ***

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables           ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}     16.114.222.180

${DATA_FILE}         wpst10_variables.py

*** Test Cases ***
Initialize the Variables and Log In
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Set up Volumes
   Add Storage Volumes Async  ${vol_sp}

Power off servers
    ${resp} =  Power off Servers in Profiles  ${sp_power}

Create the Negative Profiles
    Run Negative Tasks for List  ${negative_sp_tasks}

Create Server Profiles
    ${resp} =  Add Server Profiles from variable  ${sp_1}
    Run Keyword for List with kwargs  ${resp}  Wait for Task2   timeout=900  interval=10

Verify Server Profiles
    :FOR    ${sp}  IN  @{sp_1}
    \   Verify Server Profile  ${sp}

HW: Add secondary iSCSI boot connection using edit
    ${resp} =  Edit Server Profile  ${sp_hw_edit_add_secondary_connection}
    Wait for Task2  ${resp}  timeout=900  interval=5
    Verify Server Profile  ${sp_hw_edit_add_secondary_connection}

HW: Edit Profile Boot Volume
    ${resp} =  Edit Server profile  ${sp_hw_edit_boot_volume}
    Wait for Task2  ${resp}  timeout=900  interval=10
    Verify Server Profile  ${sp_hw_edit_boot_volume}

Negative Create Server Profile using already assigned Volume
    Run Negative Tasks for List  ${negative_sp_tasks_9}
    ${resp} =       Get Resource  SP:${negative_sp_9['name']}
    ${statusCode}=  Convert To String  ${resp['status_code']}
    Should Be Equal  ${statusCode}  404

Delete Server Profiles and Volumes
    ${resp} =  Remove Server Profiles from variable  ${sp_1}
    Wait for Task2  ${resp}  timeout=900  interval=10
    ${resp} =  Remove Storage Volumes Async  ${vol_sp}  ?suppressDeviceUpdates=${FALSE}
    Wait for Task2  ${resp}  timeout=900  interval=5