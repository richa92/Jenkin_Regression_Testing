*** Settings ***
#FVT-CRM OVF297 - Synergy Carbon: Support and display throughput and Utilization data for carbon modules.
# The test cases covered in the suites are - OVTC108. OVTC109, OVTC110, OVTC111,OVTC112,OVTC113,1OVTC14,OVTC115,OVTC116
Documentation       OVF297 - SuiteName : Configuring and validating the throughtput and utilization data for carbon interconnects.


Library         json
Library         FusionLibrary
Library         RoboGalaxyLibrary
Variables       data_variables.py
Library         Collections
Library         OperatingSystem
Library         Process
Library         ServerOperations.py
Library         port_monitor_support_module.py
Library         local_keywords.py
Resource        resource.txt

Suite Setup               Suite Setup Tasks
Suite Teardown            Suite Teardown Tasks

Resource            ../../../../resource/fusion_api_all_resource_files.txt

*** Variables ***
${module_file_path1}      ${CURDIR}\\PerformIO.py
${module_file_path2}      ${CURDIR}\\FetchIO.py
${ICM_Scripts}      ${CURDIR}/ICM_Scripts/*.sh


*** Test Cases ***

1_Verify the number of samples configured for in the LIG, and the sample count is 10 in interconnect bay 4 and interconnect bay 1 Q1
    [Documentation]    Verify the number of samples configured for in the LIG, and the sample count is 10 in interconnect bay 4 and interconnect bay 1 Q1

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_4}   ${portno_for_statistics_4_1}      ${total_samples_10}     ${expected_samples}

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_1}  ${portno_for_statistics_1_Q1}      ${total_samples_10}     ${expected_samples}

2_Edit the LI and configure the utililzation samples count as 60 and sample interval as 60
    [Documentation]     Edit the LI and configure the utililzation samples count as 60 and sample interval as 60
    FVT Edit Telemetry Configurations Of LI     ${les['le1']['name']}   ${LI}   ${telemetry_60}     ${true_flag}
    sleep   60

    # Running IO Traffic
    Run IO Traffic
    sleep   60

    # verify the sample count in both interconnects 1 and 4

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_4} ${portno_for_statistics_4_1}    ${total_samples_60}     ${expected_samples}

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_1} ${portno_for_statistics_1_Q1}   ${total_samples_60}     ${expected_samples}

3_Edit the LI and configure the Utilization sample count as 24 and the sample interval as 3600
    [Documentation]     Edit the LI and configure the Utilization sample count as 24 and the sample interval as 3600
    FVT Edit Telemetry Configurations Of LI     ${les['le1']['name']}   ${LI}   ${telemetry_24}     ${true_flag}
    sleep   60

    # Running IO Traffic
    Run IO Traffic
    sleep   60

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_4} ${portno_for_statistics_4_1}    ${total_samples_24}     ${expected_samples}

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_1} ${portno_for_statistics_1_Q1}   ${total_samples_24}     ${expected_samples}

4_Do Update from the group and verify the sample count as 10 and the sample interval as 6
    [Documentation]     Update from the group and verify the sample count as 10 and the sample interval as 6
    ${le_uri}=  Get LE URI      ${les['le1']['name']}
    Perform an Update From Group   ${le_uri}    15 min      15 s

    # Running IO Traffic
    Run IO Traffic
    sleep   60

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data    ${fc_bay_num_4}    ${portno_for_statistics_4_1}   ${total_samples_24}     ${expected_samples}

    sleep   120

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_1}     ${portno_for_statistics_1_Q1}   ${total_samples_24}     ${expected_samples}

5_Edit the LIG and set the sample count as 24 and sample interval as 3600 and perform update from group
    [Documentation]     Edit the LIG and set the sample count as 24 and sample interval as 3600 and perform update from group
    ${lig_body} =   Build LIG body      ${ligs['lig2']}
    Edit LIG and Perform an Update From Group LI     ${lig_body}    ${ligs['lig2']['name']}     ${les['le1']['name']}
    Log to console and logfile  update from group completed

    Run IO Traffic
    sleep   60

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data    ${fc_bay_num_4}    ${portno_for_statistics_4_1}   ${total_samples_60}     ${expected_samples}

    sleep   120

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data    ${fc_bay_num_1}    ${portno_for_statistics_1_Q1}  ${total_samples_60}     ${expected_samples}

6_Edit the LIG and set the sample count as 60 and sample interval as 60 and perform update from group
    [Documentation]     Edit the LIG and set the sample count as 60 and sample interval as 60 and perform update from group
    ${lig_body} =   Build LIG body      ${ligs['lig3']}
    Edit LIG and Perform an Update From Group LI     ${lig_body}    ${ligs['lig3']['name']}     ${les['le1']['name']}
    Log to console and logfile  update from group completed

    Run IO Traffic
    sleep   60

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data    ${fc_bay_num_4}    ${portno_for_statistics_4_1}   ${total_samples_60}     ${expected_samples}

    sleep   120

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data    ${fc_bay_num_1}    ${portno_for_statistics_1_Q1}  ${total_samples_60}     ${expected_samples}

7_Edit the LIG and set the sample count as 10 and sample interval as 6 and perform update from group
    [Documentation]     Edit the LIG and set the sample count as 10 and sample interval as 6 and perform update from group
    ${lig_body} =   Build LIG body      ${ligs['lig1']}
    Edit LIG and Perform an Update From Group LI     ${lig_body}    ${ligs['lig1']['name']}     ${les['le1']['name']}
    Log to console and logfile  update from group completed

    Run IO Traffic
    sleep   60
    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_4} ${portno_for_statistics_4_1}    ${total_samples_10}     ${expected_samples}

    sleep   120

    Wait Until Keyword Succeeds    20 min   15s    Verify utilization data      ${fc_bay_num_1} ${portno_for_statistics_1_Q1}   ${total_samples_10}     ${expected_samples}

8_Negative - Pass the sample count as 0 and verify the error message from the LI page
    [Documentation]     Pass the sample count as 0 and verify the error message from the LI page
    ${resp_error}=      LI Edit Telemetry Configurations        ${les['le1']['name']}   ${LI}   ${telemetry_0}      ${true_flag}
    Run Keyword If  ${resp_error['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0

9_Negative - Pass the sample interval as 0 and verify the error message from the LI page
    [Documentation]     Pass the sample interval as 0 and verify the error message from the LI page
    ${resp_error}=      LI Edit Telemetry Configurations        ${les['le1']['name']}   ${LI}   ${telemetry_interval_0}     ${true_flag}
    Run Keyword If  ${resp_error['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0

10_Negative - pass the telemetry enabled value as False, verify the error message
    [Documentation]     pass the telemetry enabled value as False, verify the error message
    ${resp_error}=      LI Edit Telemetry Configurations        ${les['le1']['name']}   ${LI}   ${telemetry_enable}     ${false_flag}
    Log to Console      ${resp_error}
    Run Keyword If  ${resp_error['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0

11_Negative - Edit the LIG and pass the sample interval as 0 and verify the status
    [Documentation]     Edit the LIG and pass the sample interval as 0 and verify the status
    ${lig_body} =   Build LIG body      ${ligs['lig_neg']}

    ${res}= Edit LIG negative     ${lig_body}   ${ligs['lig_neg']['name']}      ${les['le1']['name']}
    Run Keyword If  ${res['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0 from LIG
    Log to Console          ${res}

12_Negative - Edit the LIG and pass the sample count as 0 and verify the status
    [Documentation]     Edit the LIG and pass the sample count as 0 and verify the status
    ${lig_body} =   Build LIG body      ${ligs['lig_neg1']}
    ${res}= Edit LIG negative     ${lig_body}   ${ligs['lig_neg1']['name']}     ${les['le1']['name']}
    Run Keyword If  ${res['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0 from LIG
    Log to Console          ${res}

13_Negative - Edit the LIG and pass the enable telemetry as false and verify the status
    [Documentation]    Edit the LIG and pass the enable telemetry as false and verify the status
    ${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
    ${lig_body} =   Build LIG body      ${ligs['lig_neg2']}
    ${res}= Edit LIG negative     ${lig_body}   ${ligs['lig_neg2']['name']}     ${les['le1']['name']}
    Run Keyword If  ${res['status_code']} !=400    fail    Warning !!! Unexpected behavior - sample interval is set to 0 from LIG
    Log to Console          ${res}

***keywords***

Perform an Update From Group LI
    [Documentation]     Perform an Update From Group LI
    [Arguments]     ${liuri}    ${timeout}=5 min    ${interval}=15s
    ${resp} =       Fusion Api Update From Group   uri=${li_uri}
    Run Keyword If  ${resp['status_code']} !=202    fail    Update from group
    ${task} =       Wait For Task   ${resp}     ${timeout}      ${interval}

Edit LIG negative
    [Documentation]     Edit LIG negative
    [Arguments]     ${lig_body}     ${LIG1}     ${LE1}

    ${lig_uri} =    Get LIG Uri     ${LIG1}
    Log to Console      ${lig_uri}
    ${resp} =   Fusion Api Edit LIG     body=${lig_body}    uri=${lig_uri}
    [Return]        ${resp}

Edit LIG and Perform an Update From Group LI
    [Documentation]     Edit LIG and Perform an Update From Group LI
    [Arguments]     ${lig_body}     ${LIG1}     ${LE1}

    ${lig} =        Get LIG Member     ${LIG1}
    Log to Console      ${lig}
    ${ethernetSettings} =   Get From Dictionary   ${lig}  ethernetSettings
    Set to dictionary   ${lig_body}     ethernetSettings    ${ethernetSettings}
    ${lig_uri} =    Get LIG Uri     ${LIG1}
    Log to Console      ${lig_uri}
    ${resp} =   Fusion Api Edit LIG     body=${lig_body}    uri=${lig_uri}
    ${task} =   Wait For Task   ${resp}     120s    2s
    ${li_uri} =     Get LI URI      ${LE1}-${LIG1}-1
    Perform an Update From Group LI   ${li_uri} 15 min      15 s


Perform an Update From Group
    [Documentation]     Perform an Update From Group
    [Arguments]     ${leuri}    ${timeout}=5 min    ${interval}=15s

    ${resp} =       Fusion Api Update Logical Enclosure from Group   uri=${le_uri}
    ${task} =       Wait For Task   ${resp}     ${timeout}      ${interval}
    log to Console      ${task}
    Validate Response   ${task} ${valDict}


Get LE URI
    [Documentation]     Get LE URI
    [Arguments]     ${le}

    ${resp} =   Fusion Api Get Logical Enclosure        param=?filter="'name'=='${le}'"
    ${uri} =    Get From Dictionary     ${resp['members'][0]}   uri
    [Return]    ${uri}


LI Edit Telemetry Configurations
    [Documentation]     LI Edit Telemetry Configurations
    [Arguments]     ${LE}   ${LI}   ${telemetry}    ${flag}

    Log To Console  \n Edit Telemetry Configurations Of LI ${LI}
    ${LI_URI} =     Get LI URI   ${LI}
    #${LI_URI} =    Set Variable if ${resp} != None ${resp['uri']}  '/${LI} does not exist'
    ${res}=     fusion_api_get_li   ${LI_URI}
    ${resp} Fusion Api Update Li Telemetry Configuration    ${telemetry}    ${res['telemetryConfiguration']['uri']} 400
    Log to Console      respoknse is
    [Return]        ${resp}

FVT Edit Telemetry Configurations Of LI
    [Documentation]     FVT Edit Telemetry Configurations Of LI
    [Arguments]     ${LE}   ${LI}   ${telemetry}    ${flag}

    Log To Console  \n Edit Telemetry Configurations Of LI ${LI}
    ${LI_URI} =     Get LI URI   ${LI}
    #${LI_URI} =    Set Variable if ${resp} != None ${resp['uri']}  '/${LI} does not exist'
    ${res}=     fusion_api_get_li   ${LI_URI}
    ${resp} Fusion Api Update Li Telemetry Configuration    ${telemetry}    ${res['telemetryConfiguration']['uri']} 400
    Log to Console      ${resp}
    Should Be Equal As Integers ${resp['status_code']}  202
    Wait For Task   ${resp} timeout=30 m    interval=1 s
    ${resp} Fusion Api Get Li   ${LI_URI}
    Should Be Equal As Strings  ${resp['consistencyStatus']}    NOT_CONSISTENT
    Should Be Equal ${resp['telemetryConfiguration']['enableTelemetry']}    ${flag}
    Should Be Equal As Integers ${resp['telemetryConfiguration']['sampleCount']}    ${telemetry['sampleCount']}
    Should Be Equal As Integers ${resp['telemetryConfiguration']['sampleInterval']} ${telemetry['sampleInterval']}
    #${resp}    Fvt Api Get Logical Enclosure By Name   ${LE}
    #Should Be Equal As Strings ${resp['state']}    Inconsistent

Edit Telemetry Configurations Of LI
    [Documentation]     Edit Telemetry Configurations Of LI
    [Arguments]     ${LE}   ${LI}   ${telemetry}    ${flag}

    Log To Console  \n Edit Telemetry Configurations Of LI ${LI}
    ${LI_URI} =     Get LI URI   ${LI}
    #${LI_URI} =    Set Variable if ${resp} != None ${resp['uri']}  '/${LI} does not exist'
    ${res}=     fusion_api_get_li   ${LI_URI}
    ${resp} Fusion Api Update Li Telemetry Configuration    ${telemetry}    ${res['telemetryConfiguration']['uri']} 400
    Log to Console      ${resp}
    Should Be Equal As Integers ${resp['status_code']}  202
    Wait For Task   ${resp} timeout=30 m    interval=1 s
    ${resp} Fusion Api Get Li   ${LI_URI}
    log to console      ${resp}
    [Return]        ${resp}

Verify the Throughput and utilization data
    [Documentation]     Verify the Throughput and utilization data
    [Arguments]    ${bay_no}    ${port}     ${total_samples}    ${exp_samples}

    ${out}=     fusion_api_get_interconnect
    ${fc_uri}=  set variable    ${empty}
    ${enc_details}= fusion_api_get_enclosures
    Log to Console  ${enc_details['members'][0]['name']}

    ${interconnect_name}=   catenate    ${enc_details['members'][0]['name']}, interconnect ${bay_no}
    Log to console      ${interconnect_name}
    :FOR    ${ele}  in  @{out['members']}
    \   ${fc_uri}=      Set variable if '${ele['name']}' == '${interconnect_name}'  ${ele['uri']}
    \   Run Keyword If  '${ele['name']}' == '${interconnect_name}'  Exit For Loop
    Log to Console      "The interconnect URI is "  ${\n}
    Log to console      ${fc_uri}

    #${uri}=    catenate    ${out['members'][${bay_no}]['uri']}/statistics
    ${uri}= catenate    ${fc_uri}/statistics
    Log to Console  ${uri}

    ${out1}=        fusion_api_get_interconnect ${uri}
    #Log to Console     ${out1}
    ${output}=  vaildate_port_statistics    ${port} ${out1} ${total_samples}    ${exp_samples}
    [Return]                    ${output}

Login to Fusion via SSH

    [Documentation]             Connect to Fusion VM Bash via SSH
    ...                         Example:\n| Login to Fusion Via SSH | 10.0.12.106 | Administrator | hpvse123 |

    [Arguments]                 ${IP}=${FUSION_IP}      ${USERNAME}=${FUSION_SSH_USERNAME}
    ...                         ${PASSWORD}=${FUSION_SSH_PASSWORD}    ${PROMPT}=${FUSION_PROMPT}
    ...                         ${TIMEOUT}=${FUSION_TIMEOUT}    ${ALIAS}=Fusion_SSH
    Log Many                    ${IP}                   ${USERNAME}     ${PASSWORD}     ${PROMPT}   ${TIMEOUT}
    Set Default Configuration   prompt=${PROMPT}        timeout=${TIMEOUT}
    ${Id}=                      Open Connection         ${IP}    alias=${ALIAS}
    ${Output}=                  Login                   ${USERNAME}     ${PASSWORD}
    [Return]                    ${Id}

Login to IC via SSH

    [Documentation]             Connect to Fusion VM Bash via SSH
    ...                         Example:\n| Login to Fusion Via SSH | 10.0.12.106 | Administrator | hpvse123 |

    [Arguments]                 ${IP}   ${PASSWORD}   ${USERNAME}=${IC_SSH_USERNAME}
    ...                             ${PROMPT}=${IC_PROMPT}
    ...                         ${TIMEOUT}=${IC_TIMEOUT}    ${ALIAS}=Ic_SSH
    Log Many                    ${IP}                   ${USERNAME}     ${PASSWORD}     ${PROMPT}   ${TIMEOUT}
    Set Default Configuration   prompt=${PROMPT}        timeout=${TIMEOUT}
    ${Id}=                      Open Connection         ${IP}    alias=${ALIAS}
    ${Output}=                  Login                   ${USERNAME}     ${PASSWORD}
    [Return]                    ${Id}

Verify interconnect state
    [Documentation]     Verify interconnect state
    [Arguments]    ${interc}
    # Verify the interconnect state is configured or not

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${interc}'"
    Log to Console      "The state of the interconnect is as follows:"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Configured"    fail     The Interconnect module ${interc} is not in configured state!!  ${\n}

Get Server iLO IP

    [Documentation]   Keyword to retrieve iLO IP for server bay
    [Arguments]    ${bay}
    ${server_info}=    Get Server Info    ${bay}
    ${ilo_ip}=    Get Server iLO Address    ${server_info}
    [Return]    ${ilo_ip}

Get Server iLO Address

    [Documentation]   Keyword to retrieve iLO IP for server bay
    [Arguments]    ${server_bay_info}
    ${mpHostInfo}=    Get From Dictionary    ${server_bay_info}    mpHostInfo
    ${mpIpAddresses} =    Get From Dictionary    ${mpHostInfo}    mpIpAddresses
    ${l} =  Get Length  ${mpIpAddresses}
    :FOR    ${x}    IN RANGE    0   ${l}
    \    ${enc} =    Get From List    ${mpIpAddresses}    ${x}
    \    ${type}=    Get From Dictionary    ${enc}    type
    \    Run Keyword If    '${type}'!='DHCP'    Continue For Loop
    \    ${address}=    Get From Dictionary     ${enc}    address
    [Return]    ${address}

Create LIG and Check Status

    [Documentation]    Creates the LIG with a body and check for the status
    [Arguments]    ${body}    ${lig_name}
    ${resp} =      Fusion Api Create LIG     ${body}
    Run Keyword If  ${resp['status_code']} !=202    fail    msg=\n${lig_name} Creation Failed. \n ErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     120s    2s
    Run Keyword If  '${task['taskState']}' !='Completed'  or  ${task['status_code']} !=200   fail    msg=\n${lig_name} Creation Failed. \n ErrorCode:${task[‘taskErrors’][0][errorCode]}\n :Message ${task[‘taskErrors’][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\n${lig_name} Created Successfully !!

Add FC Networks
    [Documentation]     Add FC Networks
    [Arguments]     @{fcnets}
    Log to console and logfile    \n-Adding FC Networks
    :FOR   ${fcnet}   IN   @{fcnets}
    \       ${resp} =    Fusion Api Create FC Network   body=${fcnet}
    \       Log to Console  ${resp}
    \       ${task} =   Wait For Task   ${resp}     30s    2s

Run IO Traffic
    [Documentation]     Run IO Traffic
    # Getting the ILO IP of the  server

    ${iloip} =     Get Server iLO IP    ${server_bay_3}
    Log to Console      ${iloip}
    Set To Dictionary    ${ilo_details}    ilo_ip   ${iloip}

    # Starting the IO traffic for 60sec

    Log to Console and Logfile   \nStarting IO traffic\n
    ${cmd}  ${out_file} ${msg}=     executes        ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path1}    "${diskspd_cmd_60s}"
    Run keyword unless  '${msg}'== 'PASS'   Fail    "Unable to Start the IO Traffic"    Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nStarted IO traffic\nCommand--${cmd}\nOutputFile--${out_file}\n

    Sleep   60s

    Log to Console and Logfile   \nVerifying IO traffic\n
    ${cmd}  ${exeout}   ${msg}=     ioresults       ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path2}    "${out_file}"
    Run keyword unless  '${msg}'== 'PASS'   Fail    "Unable to Finish the IO Traffic"   Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nIO traffic Success!!\nCommand--${cmd}\nOutput--${exeout}\n

Verify utilization data
    [Documentation]    Verify utilization data
    [Arguments]    ${fc_bay_num}     ${portno_for_statistics}   ${total_samples}        ${expected_samples}
    ${flag}     ${out}=     Verify the Throughput and utilization data      ${fc_bay_num}    ${portno_for_statistics}   ${total_samples}        ${expected_samples}
    Run Keyword If  '${flag}' =='False'    fail   ${out}
    ...         ELSE    Log to console and logfile  ${out}

Suite Setup tasks
    [Documentation]     Suite Setup tasks
    ${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}

    # Create Two FC networks

    Add FC Networks     @{fcnets}
    Log to Console      "Two FC networks are created successfully!"
    Sleep   60
    # Create LIG

    Log to console and logfile    \n Creating LIG and EG configuration!
    ${body} =   Build LIG body      ${ligs['lig1']}
    Create LIG and Check Status     ${body}     ${Lig_name}
    Sleep   120

    # Verify the Uplinksets are present in the LIG

    ${resp} =    Fusion Api Get Lig     param=?filter="'name'=='${ligs['lig1']['name']}'"
    Log to Console      ${resp}
    Log to console and logfile  \n\n Verify the created uplink sets are exists in OV
    ${uplink_len} =    Get Length      ${resp['members'][0]['uplinkSets']}
    Run Keyword If  ${uplink_len} !=2    fail    ${uplink_len} Uplinksets are not exist in appliance \n${resp}
    ...         ELSE    Log to console and logfile  \n${uplink_len} Uplinksets are exist in appliance

    # Creating the Enclosure Group

    Add Enclosure Group from variable   ${enc_groups['enc_group_1']}
    Add Logical Enclosure from variable   ${les['le1']}

    # Creating server profiles and poweron the servers

    ${resp}     Add Server Profiles from variable   ${server_profiles}
    Log to Console      ${resp}
    Power on server    ${server_profiles[0]['serverHardwareUri']}
    ${resp}     Add Server Profiles from variable   ${server_profiles2}
    Log to Console      ${resp}
    Power on server    ${server_profiles2[0]['serverHardwareUri']}
    ${resp}     Add Server Profiles from variable   ${server_profiles3}
    Log to Console      ${resp}
    Power on server    ${server_profiles3[0]['serverHardwareUri']}

    #Verify the carbon modules state of the LE and profile creation

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    Log to Console      "The state of the interconnect is :"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Configured"    fail     The Interconnect module ${INTERCONNECTS[0]} is not in configured state!!    ${\n}

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    Log to Console      "The state of the interconnect is :"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Configured"    fail     The Interconnect module ${INTERCONNECTS[1]} is not in configured state!!    ${\n}

    sleep   600
    # Getting the ILO IP of the  server

    ${iloip} =     Get Server iLO IP    ${server_bay_3}
    Log to Console      ${iloip}
    Set To Dictionary    ${ilo_details}    ilo_ip   ${iloip}

    # Starting the IO traffic for 60sec

    Log to Console and Logfile   \nStarting IO traffic\n
    ${cmd}  ${out_file} ${msg}=     executes        ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path1}    "${diskspd_cmd_60s}"
    Run keyword unless  '${msg}'== 'PASS'   Fail    "Unable to Start the IO Traffic"    Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nStarted IO traffic\nCommand--${cmd}\nOutputFile--${out_file}\n

    Sleep   60s

    Log to Console and Logfile   \nVerifying IO traffic\n
    ${cmd}  ${exeout}   ${msg}=     ioresults       ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path2}    "${out_file}"
    Run keyword unless  '${msg}'== 'PASS'   Fail    "Unable to Finish the IO Traffic"   Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nIO traffic Success!!\nCommand--${cmd}\nOutput--${exeout}\n

    #Create Different Users

    :FOR    ${i}    IN  @{users}
    \   ${Response}     Fusion Api Add User    ${i}
    \   Run keyword unless  ${Response['status_code']}== 200    Fail    "Unable to Create users"
    \   Log To Console    \n${Response['userName']} is created Successfully
    Sleep   20s

Suite Teardown Tasks

    [Documentation]     Returns appliance to a 'clean' state by removing all resources\enclosures
    Log to console and logfile  [TEARDOWN]
    Run Keyword If All Tests Passed    Power off ALL Servers
    Run Keyword If All Tests Passed    Remove All Server Profiles
    Run Keyword If All Tests Passed    Remove All Logical Enclosures
    Run Keyword If All Tests Passed    Remove ALL Enclosure Groups
    Run Keyword If All Tests Passed    Remove ALL LIGs
    Run Keyword If All Tests Passed    Remove ALL LS
    Run Keyword If All Tests Passed    Remove ALL LSGs
    Run Keyword If All Tests Passed    Remove ALL Ethernet Networks
    Run Keyword If All Tests Passed    Remove ALL FC Networks
    Run Keyword If All Tests Passed    Remove ALL FCoE Networks
    Run Keyword If All Tests Passed    Remove ALL Network Sets
    Run Keyword If All Tests Passed    Remove ALL Users