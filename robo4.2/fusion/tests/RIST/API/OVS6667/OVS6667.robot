*** Settings ***
Documentation   Q2: As a tester, validate operations on the switch and drive enclosures are prevented when in Maintenance
...				During the firmware update and support dump operations, the switches and drive enclosures are brought under maintenance state. It's not recommended to perform any operations on the switch while the firmware update operation is in progress. This may result in data loss for the customers. As a result the following operations must be prevented under such circumstances.
...
...				1. CrUD operations on the LJBOD
...				2. CrUD operations on the LJBOD attachments
...				3. Power management operations on both the switches and the drive enclosures
...				4. Refresh operations on both the switches and the drive enclosures
...				5. Hard/Soft reset of both the switches and drive enclosures
...				6. Reapply configuration
...				7. Update from Group operation
...
...				Demo script:
...				1. Create an LI
...				2. Create a server
...				 profile with LJBODs
...				3. Upload an SPP with SAS switch firmware to update
...				4. Perform firmware update action on the LI
...				5. While firmware update is in progress, try the following operations. These operations to fail with a message mentioning about the firmware update operation in progress, and with a resolution asking the user to wait for the operation to complete and retry.
...				    5.1 Creating a logical JBOD.
...				    5.2 Delete a logical JBOD.
...				    5.3 Reapply the coniguration
...				    5.4 Power on/off the interconnect
...				    5.5 Power on/off the drive enclosure
...				    5.6 Refresh the SAS interconnect
...				    5.7 Refresh the drive enclosure
...				    5.8 Hard/Soft reset of the interconnect
...				    5.9 Hard/Soft reset of the drive enclosure
...				    6.0 Perform Update From Group operation
...
...             UI is used for FW Bundle upload as API takes a LONG time.  Must use Firefox 41 at time of development.

Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         String
Library                         json

Resource                       ./../../../../Resources/api/fusion_api_resource.txt
Resource                       ../global_variables.robot

Variables 		                ${DATA_FILE}

Suite Setup                     Set Up
Suite Teardown                  Tear Down

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

${wordy}                        ${True}

&{Off}                      op=replace    path=/powerState    value=Off
@{turnOff}                  ${Off}
&{On}                       op=replace    path=/powerState    value=On
@{turnOn}                   ${On}

&{Hard}                     op=replace    path=/hardResetState    value=Reset
@{hardreset}                ${Hard}
&{Soft}                     op=replace    path=/softResetState    value=Reset
@{softreset}                ${Soft}

&{Uon}                      op=replace    path=/uidState    value=On
@{uidOn}                    ${Uon}
&{Uoff}                     op=replace    path=/uidState    value=Off
@{uidOff}                   ${Uoff}

${timeout}                  5
${interval}                 1
${PAUSE}                    ${FALSE}


*** Test Cases ***
Update LI Firmware
    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Update LI Firmware
    Set Suite Variable    ${LI_IN_PROGRESS}    ${FALSE}
    ${resp} =    Update SAS Logical Interconnect Firmware    ${SAS_LI_NAME}    ${SPP_NAME}    WFT2=${FALSE}
    Set Suite Variable    ${LI_IN_PROGRESS}    ${TRUE}
    Set Suite Variable    ${Update_SAS_LI_Task}    ${resp}

Wait Until DE and SASIC are in Maintenance State
    Run Keyword If    ${LI_IN_PROGRESS}==${FALSE}    Fatal Error     LI Firmware update failed, aborting the test.
    Wait Until Keyword Succeeds    2 min    10 sec    Verify Resource    ${SASIC}
    Wait Until Keyword Succeeds    1 min    5 sec    Verify Resource    ${DE}

Create Logical JBOD Expect Error
    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Create JBOD
    ${resp} =    Edit Server Profile    ${EDIT_PROFILE_ADD_JBOD}
    Wait For Task2    ${resp}    timeout=120    interval=2    PASS=Error    errorMessage=Unable_Reserve_JBOD    name=${JBOD2}
    ${profile} =    Get Resource    SP:${SERVER_PROFILE['name']}
    
Delete Logical JBOD Expect Error
    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Delete JBOD
    ${resp} =    Edit Server Profile    ${EDIT_PROFILE_DEL_JBOD}
    Wait For Task2    ${resp}    timeout=300    interval=2    PASS=Error    errorMessage=Unable_Release_JBOD    name=${JBOD1}
    ${profile} =    Get Resource    SP:${SERVER_PROFILE['name']}

Update SAS LI From Group Expect Error
    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Edit Update SAS LI
    Edit SAS LIG from list  ${EDIT_SASLIG}
    ${resp} =    Update SAS LI from Group    ${SASLI}    WFT2=${FALSE}
    Wait For Task2    ${resp}   PASS=Error    errorMessage=Unable_Update_From_Group
    Edit SAS LIG from list  ${SASLIG}

Reapply SAS LI Coniguration Expect Error
    ${resp} =  Fusion API Reapply SAS LI Configuration  ${SASLI_URI}
    Wait for Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=Unable_Reapply

Power OFF/ON a SAS Interconnect Expect Error
    ${resp} =    Fusion Api Patch SAS Interconnect    ${turnOff}    ${SASIC_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}    interval=${interval}   errorMessage=SASIC_Maintenance

    ${resp} =    Fusion Api Patch SAS Interconnect    ${turnOn}    ${SASIC_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=SASIC_Maintenance
    
Power OFF/ON a Drive Enclosure Expect Error
    ${resp} =    Fusion Api Patch Drive Enclosure    ${turnOff}    ${DE_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=DE_Maintenance_Power

    ${resp} =    Fusion Api Patch Drive Enclosure    ${turnOn}    ${DE_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=DE_Maintenance_Power

Refresh a SAS Interconnect Expect Error
    ${resp} =    Refresh SAS Interconenct By Name    ${SASIC['name']}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=SASIC_Maintenance_Terse

Refresh a Drive Enclosure Expect Error
    ${resp} =    Refresh Drive Enclosure By Name    ${DE['name']}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=DE_Maintenance_Refresh

Hard/Soft Reset a SAS nterconnect Expect Error
    ${resp} =    Fusion Api Patch SAS Interconnect    ${hardreset}    ${SASIC_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}    interval=${interval}   errorMessage=SASIC_Maintenance

    ${resp} =    Fusion Api Patch SAS Interconnect    ${softreset}    ${SASIC_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=SASIC_Maintenance

Hard Reset a Drive Enclosure Expect Error
    ${resp} =    Fusion Api Patch Drive Enclosure    ${hardreset}    ${DE_URI}
    Wait For Task2    ${resp}    PASS=Error    timeout=${timeout}   interval=${interval}   errorMessage=DE_Maintenance_Reset
    
UID Operations Are Allowed
    Turn Sas Interconnects UID Off from list    ${SASIC_LIST}
    Turn Sas Interconnects UID On from list    ${SASIC_LIST}
    Turn Drive Enclosure UID Off from list    ${DE_LIST}
    Turn Drive Enclosure UID On from list    ${DE_LIST}

Wait Until DE and SASIC are back in Configured State
    Wait Until Keyword Succeeds    25 min    15 sec    Verify Resource    ${SASIC}    state=Configured
    Wait Until Keyword Succeeds    5 min    15 sec    Verify Resource    ${DE}    state=Configured

Reapply SAS LI Coniguration To Delete Logical JBODS
    ${resp} =  Fusion API Reapply SAS LI Configuration  ${SASLI_URI}
    Wait for Task2    ${resp}    timeout=180    interval=10

*** Keywords ***
Set up
    [Documentation]    Set up for OVS6667
    Set Log Level	DEBUG
    Should Not Be Equal As Strings    ${APPLIANCE_IP}    APPLIANCE_IP
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    ${session} =    Get From List    ${admin_session}     0
    ${status}    ${error} =    Run Keyword And Ignore Error     Get From Dictionary     ${session}    message
    Run Keyword If     '${status}'=='PASS'    Fail    Unable to login: ${error}

    ${de_uri} =    Common URI lookup by name    DE:${DE['name']}
    ${sasic_uri} =  Common URI lookup by name    SASIC:${SASIC['name']}
    ${sasli_uri} =  Common URI lookup by name    SASLI:${SASLI['name']}
    
    Set Suite Variable    ${DE_URI}    ${de_uri}
    Set Suite Variable    ${SASIC_URI}    ${sasic_uri}
    Set Suite Variable    ${SASLI_URI}    ${sasli_uri}

    ${server} =    Get Resource    ${SERVER_PROFILE['serverHardwareUri']}
    ${sp_uri} =    Get From Dictionary    ${server}    serverProfileUri
    ${sp_exist}    ${dontcare} =     Run Keyword and Ignore Error    Should Contain    ${sp_uri}    rest
    Run Keyword If   '${sp_exist}'=='PASS'    Remove and Add Server Profile    ${sp_uri}    ${SERVER_PROFILE}
    ...    ELSE    Add Server Profile and Wait For Task 2    ${SERVER_PROFILE}

    ${spp} =    Get Firmware Bundle    /rest/firmware-drivers
    Set Suite Variable    ${SPP_NAME}    ${spp['members'][0]['name']}
    Log   SPP_NAME: ${SPP_NAME}    console=true

Tear Down
    [Documentation]     Tear Down for OVS6667
    Wait For Task2    ${Update_SAS_LI_Task}    timeout=300    interval=15

    ${sp_uri} =  Common URI lookup by name    SP:${SERVER_PROFILE['name']}
    ${status}    ${dontcare} =    Run Keyword and Ignore Error    Should Not End With    ${sp_uri}    _not_found
    Run Keyword If   '${status}'=='FAIL'    Pass Execution    Profile already deleted

    Log    Remove Server Profile    console=true
    ${resp} =    Remove Server Profile    ${SERVER_PROFILE}    force=${TRUE}
    Wait For Task2    ${resp}    timeout=2400    interval=20

    Fusion Api Logout Appliance

Remove and Add Server Profile
    [Documentation]    Removes then adds a Server Profile
    [Arguments]     ${sp_uri}    ${server_profile}
    Log    Remove and Add    console=true
    ${profile} =    Get Resource by URI    ${sp_uri}
    Power off Server    ${server_profile['name']}
    ${resp} =    Remove Server Profile    ${profile}    force=${TRUE}
    Wait For Task2    ${resp}    timeout=1200    interval=20

    Add Server Profile and Wait For Task 2	${server_profile}

Add Server Profile and Wait For Task 2
    [Documentation]    Add Server profile the WFT2
    [Arguments]     ${server_profile}
    Log    Add and WFT2    console=true
    Power off Server    ${server_profile['name']}
    ${resp} = 	Add Server Profile	${server_profile}
    Wait For Task2    ${resp}    timeout=2400    interval=20

Upload SPP bundle
    [Documentation]    Read SPP bundle from a given path on mapped folder and upload it into OV
    [Arguments]     ${spp_path}
    @{spps_name} =  OperatingSystem.List Directory  ${spp_path}  *.iso  absolute
    :FOR    ${spp_name}  IN  @{spps_name}
    \  Upload Firmware Bundle By Curl  fw_absolute_path=${spp_name}  VERBOSE=True
    Log  Finished uploading ${spp_name} bundle  console=True