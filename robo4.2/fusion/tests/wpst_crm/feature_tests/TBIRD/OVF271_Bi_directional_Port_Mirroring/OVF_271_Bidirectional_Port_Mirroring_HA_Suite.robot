*** Settings ***
#FVT-CRM OVF271 - Synergy Carbon: Support Bi-directional port mirroring with HA Configuration
# The test cases covered in the suites are - OVTC129, OVTC145, OVTC152, OVT154, OVTC155, OVTC156
Documentation       OVF271 - SuiteName : Validating the Bi-Directional port Mirroring for Carbon interconnect modules with High Available configuration


Library         json
Library         FusionLibrary
Library         RoboGalaxyLibrary
Variables       data_variables.py
Library         Collections
Library         OperatingSystem
Library         Process
Library         ServerOperations
Library         port_monitor_support_module
Resource        resource.txt


Suite Setup               Suite Setup Tasks
Suite Teardown            Suite Teardown Tasks

Resource            ../../../../resource/fusion_api_all_resource_files.txt

*** Variables ***
${module_file_path1}      ${CURDIR}\\PerformIO.py
${module_file_path2}      ${CURDIR}\\FetchIO.py
${ICM_Scripts}      ${CURDIR}/ICM_Scripts/*.sh


*** Test Cases ***

1_Log-out from the appliance
    [Documentation]     Log-out from the appliance
    ${Logout_response}      Fusion Api Logout Appliance
    Run keyword unless  ${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
    Log To Console    \n\nLogged_Out from Appliance as ${admin_credentials['userName']}

2_Log-in as Server Admininstrator
   [Documentation]      Log-in as Server Admininstrator
    ${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${serveradmin}
    Run keyword unless  ${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
    Log To Console    \n\nLogged in as ${serveradmin['userName']}

3_Enable Port Monitoring with Unauthorized User
    [Documentation]     Enable Port Monitoring with Unauthorized User
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[1]}    ${analyzer_port_qport}    true       ${LI}
    Log to Console  ${resp}
    Run Keyword If  ${resp['status_code']} !=401    fail    Warning !!! Unauthorized user have access for Port Monitor ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}

4_Log-out from the appliance
    [Documentation]     Log-out from the appliance
    ${Logout_response}      Fusion Api Logout Appliance
    Run keyword unless  ${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
    Log To Console    \n\nLogged_Out from Appliance as serveradmin
    Fusion Api Login Appliance      ${APPLIANCE_IP}     ${admin_credentials}

5_Configure Port Monitoring with Analyzer port as Q1_4 and Monitored port as 1 with direction as bi-directional
    [Documentation]     Configure Port Monitoring with Analyzer port as Q1.4 and Monitored port as 1 with direction as bi-directional
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${analyzer_port_qport}    true       ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Failed to Disable Port Monitor for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring with analyzer port as Q1:4!!!
    sleep   ${pm_timer}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_port_qport}  ${analyzer_dport}       ${interconnects[0]}     ${li_portmonitor['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI

    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[0]}     ${ic_bay1}  ${analyzer_port_qport}

6_Negative : Create or edit an Uplinkset and try to use the analyzerPort Q1:4 and verify the error message
    [Documentation]     Create or edit an Uplinkset and try to use the analyzerPort Q1:4 and verify the error message
    ${li_uri} =     Get LI URI   ${LI}
    Log to Console      ${li_uri}
    ${us} =         Copy Dictionary ${neg_uplink_sets}
    ${body} =       Build US body   ${us}   ${li_uri}
    ${uplinksets} =         Fusion Api Get Uplink Set   param=?filter="'name'=='${uplink_sets['UplinkSet_1']['name']}'"
    ${us} =                 Get From List   ${uplinksets['members']}    0
    ${us_uri} =             Get From Dictionary ${us}   uri
    ${resp} =               Fusion Api Edit Uplink Set  body=${body}    uri=${us_uri}
    Log to Console      ${resp}
    Run Keyword If  ${resp['status_code']} !=400    fail    Error - Unexpected Behavior Uplink set edited successfully  ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

7_Negative : Configure port monitoring with an uplink port [Q1:1] which is already in the uplink set
    [Documentation]     Configure port monitoring with an uplink port [Q1:1] which is already in the uplink set
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${used_uplink_port}     true     ${LI}
    Log to Console      ${resp}
    Run Keyword If  ${resp['status_code']} !=400    fail    Error - Enabling Port Monitor is succeed for Uplinkport which is already in the uplink set  ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

8_Disable the analyzer port Q1:4, and verify the port monitoring is disbaled
    [Documentation]     Disable the analyzer port Q1:4, and verify the port monitoring is disbaled
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${analyzer_port_qport}    false      ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Failed to Disable Port Monitor for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully disabled the port monitoring !!!

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

9_Configure the Port monitoring by swapping from bay 1 port Q1:4 to bay 4 port 2
    [Documentation]     Configure the Port monitoring by swapping from bay 1 port Q1:4 to bay 4 port 2
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[1]}    ${analyzer_port_2_bay4}    true      ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Switching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     300s    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring by suitching to new port!!!

    sleep   ${pm_timer}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[1]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_port_2_bay4} ${analyzer_dport}       ${interconnects[1]}     ${li_portmonitor['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI

    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[1]}     ${ic_bay2}  ${analyzer_port_2_bay4}

10_Disable the Port monitoring on the analyzer port 2 of bay 4
    [Documentation]     Disable the Port monitoring on the analyzer port 2 of bay 4
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[1]}    ${analyzer_port_2_bay4}    false     ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully disabled the analyzer port of the port monitoring !!!

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[1]}

11_Configure Port monitoring by switching from the port 2 to Q1:4
    [Documentation]     Configure Port monitoring by switching from the port 2 to Q1:4
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${analyzer_port_qport}    true       ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!

    sleep   ${pm_timer}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_port_qport}  ${analyzer_dport}       ${interconnects[0]}     ${li_portmonitor['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI

    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[0]}     ${ic_bay1}  ${analyzer_port_qport}

12_Configure Port monitoring by switching from the port Q1:4 to Q1:3
    [Documentation]     Configure Port monitoring by switching from the port Q1:4 to Q1:3
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${analyzer_qport3_bay1}    true      ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    sleep   ${pm_timer}
    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_qport3_bay1} ${analyzer_dport}       ${interconnects[0]}     ${li_portmonitor['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI

    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[0]}     ${ic_bay1}  ${analyzer_qport3_bay1}

13_Disable the Port monitoring configuration on the Analyzer port Q1:3
    [Documentation]     Disable the Port monitoring configuration on the Analyzer port Q1:3
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor}   ${interconnects[0]}    ${analyzer_qport3_bay1}    false     ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!


14_Configure Port monitoring by choosing the to server option for the Port Q1_3 in bay 1
    [Documentation]     Configure Port monitoring by choosing the to server option for the Port Q1.3 in bay 1
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor_to_server}     ${interconnects[0]}    ${analyzer_qport3_bay1}    true      ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    sleep   ${pm_timer}
    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[0]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_qport3_bay1} ${analyzer_dport}       ${interconnects[0]}     ${li_portmonitor_to_server['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI

    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[0]}     ${ic_bay1}  ${analyzer_qport3_bay1}

15_Configure Port monitoring by choosing the from server option for the Port 2 in bay 4
    [Documentation]     Configure Port monitoring by choosing the from server option for the Port 2 in bay 4
    ${resp}=    Configuring Port Monitoring in LI   ${li_portmonitor_from_server}   ${interconnects[1]}    ${analyzer_port_2_bay4}    true      ${LI}
    Run Keyword If  ${resp['status_code']} !=202    fail    Switching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     300s    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring by suitching to new port!!!

    sleep   ${pm_timer}

    # Verify the interconnect state is configured or not

    Verify interconnect state       ${interconnects[1]}

    # Verify the port is successfully configured as analyzer port with direction as bi-directional

    Wait Until Keyword Succeeds    20 min   15s    Verify Port Monitoring in IC        ${analyzer_port_2_bay4} ${analyzer_dport}       ${interconnects[1]}     ${li_portmonitor_from_server['monitoredPorts'][0]['portMonitorConfigInfo']}

    # Verify the port mirroring is configured properly in the interconnect CLI
    sleep   ${cli_login}
    Wait Until Keyword Succeeds    20 min   15s    verify port mirroring in ICM CLI        ${interconnects[1]}     ${ic_bay2}  ${analyzer_port_2_bay4}

***keywords***

verify port mirroring in ICM CLI
    [Documentation]     verify port mirroring in ICM CLI
    [Arguments]    ${interc}    ${ic_bay}   ${analyzer_port}
    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${interc}'"
    ${IC_IP}=      Get From Dictionary      ${resp['members'][0]['ipAddressList'][0]}    ipAddress
    Log to Console      ${IC_IP}

    Log to console and logfile    \n\nLogging into OneView SSH session
    Login to Fusion via SSH
    Log to console and logfile    \n\nCopying the ICM scripts to the Fusion SSH
    Put File      ${ICM_Scripts}       /root
    Log to console and log file   \n\nExecuting scripts to get the root password of ICM
    ${Perm}=    Execute Command     chmod +x readMECanmic.sh writeMECanmic.sh
    ${read}=    Execute Command    ./writeMECanmic.sh ${ic_bay} AQ==
    ${write}=   Execute Command    ./readMECanmic.sh ${ic_bay} 191
    ${op}=      Get Lines Containing String    ${write}    ICM Bay ${ic_bay}
    ${pwd}=     Fetch From Right    ${op}    :
    ${Password}=   Remove String Using Regexp    ${pwd.strip()}    \t
    Log to Console      ${password}

    Log to console and logfile    \n\nLogging into ICM with the static IP address.
    Login to IC via SSH     ${IC_IP}    ${Password}
    ${show}=    Execute Command    switchshow
    Execute Command     \n
    ${show}=    Execute Command    switchshow
    Log to Console      ${show}

    ${return_flag}=     validate_port_monitor_in_icm    ${port_map['${analyzer_port}']} ${show}
    Log to Console      ${return_flag}
    Run Keyword If  '${return_flag}' !='True'    fail    Log to Console     "Failed to verify the configured Mirrored port in the ICM!!!"

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
    Sleep   200

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

    sleep   720
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
    [Documentation]    Returns appliance to a 'clean' state by removing all resources\enclosures
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
