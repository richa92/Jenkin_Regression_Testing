*** Settings ***

Documentation       ICM Port Counters                   -  Below is the algorithm of this test suite:
...                                                      1. Login to the Appliance
...                                                      2. Get the list of emclosure wise ICMs names and URLs
...                                                      3. Do the clear port counters on supported ICMs
...                                                      4. Check the status of the task
...                                                      5. Do IC port counters for all the enclosures.
...                     Example:
...                              pybot -d /tmp/logs/ICMPortCounters -LTRACE -V <your test data variable file> ICMPortCounters.robot
...                     Required arguments:
...                         -V /root/ci-fit/config_files/est_robustness_DVF.py
...						For the data variable file template please refer the path,  tests/wpst_crm/ci_fit/tests/robustness/resources/c7000_robustness_data_variables_template.py
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<backup restore golden json> (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>

Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../../robustness/resources/common.robot
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Library             Collections
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             SSHLibrary


*** Variables ***

${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${ENC}                          None
${ONE_TIME_PASS}                None
${tbirdEnv}                     None
${SLEEP_BEFORE_PORT_COUNT}      1 min
${PORT_COUNT_WAIT_TIMEOUT}      7 min
${PORT_COUNT_WAIT_INTERVAL}     1 min

*** Test Cases ***

Login Appliance And Set Test
  [Tags]    LOGIN
  Set Log Level    TRACE
  Authenticate And Set Login

VerIfy for alerts or warnings
  [Tags]    VERIfYALERTS
  Set Log Level    TRACE
  Check Common Resource Attributes

Get Enclosure Wise ICM Details and Do Clear Port Counters on Randomly selected ICM
  [Tags]    ICPTCNTS
  ${ICM_Col}    Fusion Api Get Interconnect
  ${ICM_count} =    Get from Dictionary    ${ICM_Col}    total
  ${encs}    Fusion Api Get Enclosures
  ${enc_count} =    Get from Dictionary    ${encs}    count
  Should Not Be Equal as Integers    ${ICM_count}    0    msg=No ICMs for clearing the port counters    
  :FOR    ${enc}    IN    @{encs['members']}
  \   ${icm_uris} =    Get ICM Names    ${enc}
  \   ${icm} =    Evaluate    random.choice(${icm_uris})    random
  \   ${res}    Fusion Api Get Interconnect    uri=${icm}
  \   ${model} =    Get from Dictionary    ${res}    model
  \   Run Keyword If    $model not in $unsupported     Clear IC Port Counters    ${icm}

Send Email Notification
  [Tags]    SEND_A_MAIL
  Set Log Level    TRACE
  ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
  Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
  ${suitename} =   Fetch From Left   ${SUITE NAME}  --
  Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.
  
*** Keywords ***

Get ICM Names
    [Documentation]    Gets Enclosure Wise ICM Names and URLs
    [Arguments]    @{enc}
    set suite variable    ${ic_num}    ${0}
    ${enc_name}    Get from Dictionary    ${enc[0]}    name
    @{enc_ic_name}    Create List
    :FOR    ${ic}    IN    @{enc[0]['interconnectBays']}
    \   ${interconnectUri} =    Get from Dictionary    ${ic}    interconnectUri
    \   Append to List    ${enc_ic_name}    ${interconnectUri}
    \   ${icm_uris} =    Remove None Values From List     ${enc_ic_name}
    [Return]    ${icm_uris}

Remove None Values From List
    [Documentation]    Remove None Values From List
    [Arguments]    ${enc_ic_name}
    ${icm_uris}    Create List
    :FOR    ${ic_uri}    IN    @{enc_ic_name}
    \   ${status} =    Evaluate    '${ic_uri}'=='None'
    \   Run Keyword If    '${status}'=='False'    Collections.Append To List    ${icm_uris}    ${ic_uri}
    [Return]    ${icm_uris}

Validate Port Statistics
    [Documentation]    Validate the port statistics response
    [Arguments]    ${res1}    ${res2}
    ${Value} =    Create List
    :FOR    ${key}    IN    @{res1.keys()}
    \   ${bool} =    Evaluate   "rfc" in """${key}"""
    \   ${value1} =    Get From Dictionary    ${res1}    ${key}
    \   ${value2} =    Get From Dictionary    ${res2}    ${key}
    \   Run Keyword If    '${bool}' == 'True'    Verify Port Statistics    ${value1}    ${value2}     ${Value}    ELSE      Append To List     ${Value}   None
   ${retvalue} =    Set Variable If    False not in $Value     True     ELSE     False
   Run Keyword If    '${retvalue}'=='True'    Log    \nCompleted Clear Port Counters on the Selected ICM Successful    console=${True}     ELSE    Log    \nClear Port Counters on the Selected ICM is Unsuccessful    console=${True}
   

Verify Port Statistics
    [Documentation]    Verify the port statistics response for each key
    [Arguments]    ${value1}    ${value2}    ${Value}
    Run Keyword If    ${value1}>=${value2}     Append To List     ${Value}    True     ELSE      Append To List     ${Value}    False

Clear IC Port Counters
    [Documentation]    Clear IC Port Counters
    [Arguments]    ${icm}
    ${body}        Create Dictionary
    Log    \ninterconnectUri:${icm}    console=${True}
    ${stats}    ${resp1} =    Run Keyword And Ignore Error    Fusion Api Get Interconnect Port Statistics    uri=${icm}    param=${Port}
    ${resp}    Fusion Api clear Interconnect Ports    uri=${icm}    body=${body}
    ${task}    fusion_api_appliance_setup.Wait For Task    ${resp}    ${PORT_COUNT_WAIT_TIMEOUT}    ${PORT_COUNT_WAIT_INTERVAL}
    Log    \nCleared Port counters for the ICM ${icm}    console=${True} 
    Sleep And Log Reason To Console    ${SLEEP_BEFORE_PORT_COUNT}    reason=Wait for ${SLEEP_BEFORE_PORT_COUNT} and verify the port counter operation
	${status}    ${resp2} =    Run Keyword And Ignore Error    Fusion Api Get Interconnect Port Statistics    uri=${icm}    param=${Port}     
	Run Keyword If    '${status}' == 'PASS'    Validate Port Statistics    ${resp1['commonStatistics']}    ${resp2['commonStatistics']}     ELSE     Log    \nSpecified Port ${Port} not available on the Selected Interconnect to Verify the Clear Port Counters     console=${True}