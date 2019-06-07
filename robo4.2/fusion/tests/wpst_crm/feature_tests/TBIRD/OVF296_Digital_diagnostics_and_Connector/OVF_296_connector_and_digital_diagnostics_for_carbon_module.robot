*** Settings ***
#FVT-CRM OVF296: Validating the connector and digital diagnostics information of Carbon module.
# The test cases covered in the suites are - OVTC117, OVTC118, OVTC119, OVT120, OVTC121, OVTC121, OVTC768
Documentation       OVF296 - SuiteName : Verifying Connector and Digital diagnostics information of Carbon modules


Library         json
Library         FusionLibrary
Library         RoboGalaxyLibrary
Variables       data_variables.py
Library         Collections
Library         local_keywords
Library         OperatingSystem
Library         Process
Library         ServerOperations

Suite Setup               Suite Setup Tasks
Suite Teardown            Suite Teardown Tasks

Resource            ../../../../resource/fusion_api_all_resource_files.txt

*** Variables ***
${module_file_path1}      ${CURDIR}\\PerformIO.py
${module_file_path2}      ${CURDIR}\\FetchIO.py


*** Test Cases ***

1_Verify the Connector and Digital diagnostics informations are avilable for API version 400
    [Documentation]    Verify the Connector and Digital diagnostics informations are avilable for API version 400
    # Verify both digital diagnostics and connector information is available for API version 400

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_16} ${resp['_content']}
    Log to Console      "The return Flag value of the output is "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Run Keyword If  ${flag} =="Fail"    fail    ${msg}  ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

2_Verify only Connector information is available and Digital diagnostics informations is not avilable for API version 300
    [Documentation]   Verify only Connector information is available and Digital diagnostics informations is not avilable for API version 300

    # Check Only the Connector information is available without the digital diagnostics, when API is 300

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    300     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_16} ${resp['_content']}     True
    Log to Console      "The return Flag value of the output is "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Run Keyword If  ${flag} =="Fail"    fail    ${msg}  ${\n}
    Log to Console      ${msg}
    Log to Console      "The connector information without Digital diagnostics information as follows"
    Log to Console      ${resp}

3_Verify no connector and digital diagnostics information is avilable after the poweroff of the interconnect
    [Documentation]     Verify no connector and digital diagnostics information is avilable after the poweroff of the interconnect
    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${body}    Set To Dictionary    ${edit_power_body[0]}    value=${power_value[0]}
    ${resp1}    fusion_api_patch_interconnect    body=${edit_power_body}    uri=${resp['members'][0]['uri']}

    sleep   300

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    Log to Console      "The state of the interconnect after Powered OFF"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Maintenance"    fail     The Interconnect module ${INTERCONNECTS[0]} is not in Maintenance state!!  ${\n}

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}=    Split string    ${resp['members'][0]['uri']}    /

    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    Log to Console      "The response of pluggable module information after powering of the interconnect"
    Log to Console      ${resp}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_16} ${resp['_content']}     True
    Log to Console      "The return Flag value of the output is "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" !="Off"    fail    "Connector and digital diagnostics information are availalbe after poweroff ICM!!" ${\n}
    Log to Console      ${msg}
    Log to Console      ${resp}

4_Verify connector and digital diagnostics information is available after the poweron of the interconnect
    [Documentation]     Verify connector and digital diagnostics information is available after the poweron of the interconnect

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${body}    Set To Dictionary    ${edit_power_body[0]}    value=${power_value[1]}
    ${resp1}    fusion_api_patch_interconnect    body=${edit_power_body}    uri=${resp['members'][0]['uri']}

    sleep   300

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    Log to Console      "The state of the interconnect after it Powered On :"
    Log to Console      ${resp['members'][0]['state']}

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /

5_Verify both digital diagnostics and connector information is available after poweron of the interconnect

    #Verify both digital diagnostics and connector information is available after poweron of the interconnect
    [Documentation]    Verify both digital diagnostics and connector information is available after poweron of the interconnect

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_16} ${resp['_content']}
    Log to Console      "The return Flag value of the output is "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Run Keyword If  ${flag} =="Fail"    fail    ${msg}  ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

6_Verify both digital diagnostics and connector information is available for API version 400 with FC 8Gb Connector

    [Documentation]     Verify both digital diagnostics and connector information is available for API version 400 with FC 8Gb Connector

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    Log to Console    \n${resp['_content']}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_8}  ${resp['_content']}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

7_Verify only connector information is available not digital diagnostics information for API version 300 with FC 8Gb Connector

    [Documentation]     Verify only connector information is available  not digital diagnostics information for API version 300 with FC 8Gb Connector

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    300     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_8}  ${resp['_content']}     True
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

8_Verify only connector information is available not digital diagnostics information for API version 300 with QSFP+ connector

    [Documentation]     Verify only connector information is available not digital diagnostics information for API version 300 with QSFP+ connector

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    300     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${qsfp_connector1}  ${resp['_content']}     True
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output is "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

9_Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 1

    [Documentation]     Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 1

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${qsfp_connector1}  ${resp['_content']}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output is as follows: "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}


10_Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 2

    [Documentation]     Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 2

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${qsfp_connector2}  ${resp['_content']}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output is as follows: "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

11_Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 3

    [Documentation]     Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 3

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${qsfp_connector3}  ${resp['_content']}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output is as follows: "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}


12_Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 4

    [Documentation]     Verify both digital diagnostics and connector information is available for API version 400 with QSFP connector port 4

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${qsfp_connector4}  ${resp['_content']}
    Run Keyword If  "${flag}" =="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output is as follows: "
    Log to Console  ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Run Keyword If  "${flag}" =="False"    fail    ${msg}   ${\n}
    Log to Console      "The connector and Digital diagnostics information as follows"
    Log to Console      ${resp}

13_Verify both digital diagnostics and connector information is not available for API version 400 for Unsupported Module - 4GB SFP

    [Documentation]     Verify both digital diagnostics and connector information is not available for API version 400 for Unsupported Module 4GB SFP

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${unsupported_sfp}  ${resp['_content']}
    Run Keyword If  "${flag}" !="Off"    fail    ${msg} ${\n}
    Log to Console      "The return Flag value of the output as follows:"
    Log to Console      ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Log to Console      "The connector and Digital diagnostics information as follows :"
    Log to Console      ${resp}

14_Delete all the Profile Connections and delete the LE
    [Documentation]     Delete all the Profile Connections and delete the LE
    Power off ALL Servers
    Remove All Server Profiles
    Remove All Logical Enclosures

15_Verify the Carbon interconnects are in monitored state and then verify the connector and digital diagnostics details are not present or null
    [Documentation]     Verify the Carbon interconnects are in monitored state and then verify the connector and digital diagnostics details are not present or null.
    # Get the interconnect  state and verify it is in monitored state

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    Log to Console      "The State of the interconnect after deleting the LE enclosure"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Monitored"    fail     The Interconnect module ${INTERCONNECTS[1]} is not in Monitored state!!  ${\n}

    # Verify the digital diagnostics and connector information are not available for the interconnect.

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[1]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_16} ${resp['_content']}
    Run Keyword If      '${flag}' == 'False'   Log to console     ${msg}
    \        ...    ELSE IF      '${flag}' == 'Off'       Log to console      ${msg}
    \        ...    ELSE        FAIL        Unexpected behavior occured - Connector and digital diagnostics are avilable!!!

    #Run Keyword If  "${flag}" =="Off"    fail    ${msg}    ${\n}
    Log to Console      "The return Flag value of the output as follows:"
    Log to Console      ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Log to Console      "The connector and Digital diagnostics information as follows :"
    Log to Console      ${resp}

    # Get the interconnect  state and verify it is in monitored state

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    Log to Console      "The State of the interconnect after deleting the LE enclosure"
    Log to Console      ${resp['members'][0]['state']}
    Run Keyword If  "${resp['members'][0]['state']}" !="Monitored"    fail     The Interconnect module ${INTERCONNECTS[0]} is not in Monitored state!!  ${\n}

    # Verify the digital diagnostics and connector information are not available for the interconnect

    ${resp}=        Fusion Api Get Interconnect   param=?filter="'name'=='${INTERCONNECTS[0]}'"
    ${icm_uri}= Split string    ${resp['members'][0]['uri']}    /
    ${resp}     fusion_api_get_interconnect_pluggable_module_info   /rest/interconnects/    400     ${icm_uri[-1]}
    ${flag}     ${msg}      validate_connector_info     ${sfp_connector_8}  ${resp['_content']}

    Run Keyword If      '${flag}' == 'Off'   Log to console     ${msg}
    \        ...    ELSE IF      '${flag}' == 'False'       Log to console      ${msg}
    \        ...    ELSE        FAIL        Unexpected behavior occured - Connector and digital diagnostics are avilable!!!

    #Run Keyword If  "${flag}" !="Off"    fail    ${msg}    ${\n}
    Log to Console      "The return Flag value of the output as follows:"
    Log to Console      ${flag}
    Log to Console      "The return Message of the Connector method is as follows: "
    Log to Console      ${msg}
    Log to Console      "The connector and Digital diagnostics information as follows :"
    Log to Console      ${resp}


***keywords***

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
    # Create LIG

    Log to console and logfile    \n Creating LIG and EG configuration!
    ${body} =   Build LIG body      ${ligs['lig1']}
    Create LIG and Check Status     ${body}     ${Lig_name}

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

    sleep   900s

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

