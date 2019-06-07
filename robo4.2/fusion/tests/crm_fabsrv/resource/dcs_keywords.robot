*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    ../library/dcs_utils.py
Library    SSHLibrary
Library    robot.api.logger
Library    String

*** Variables ***
${http}             http://
${INSTANCES_URL}    /dcs/rest/schematic/instances/
${TYPES_URL}        /dcs/rest/schematic/types/
${DCS_Package}      dcs

*** Keywords ***
List All Devices of Type
    [Arguments]     ${device_type}    ${dcs_ip}
    [Documentation]    Retrieve a list of all instances of specified type.
    ...    Example:\n| ${devices}= | List All Devices of Type | procurve | 172.17.4.137 |
    Log    ${\n}Return a list of ${device_type}s on DCS at: ${dcs_ip}    console=yes
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${INSTANCES_URL}    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${devices}=    List of Devices    ${json}    ${device_type}
    ${device_count}=    Get Length    ${devices}
    Log    ${device_count} ${device_type}s found: ${devices}    console=yes
    Delete All Sessions
    [Return]  ${devices}

List All Types of Devices
    [Arguments]     ${dcs_ip}
    [Documentation]    Retrieve a list of device types on installed schematic.
    ...    Example:\n| ${types}= | List All Types of Devices | 172.17.4.137 |
    Log    ${\n}Return a list of device types on DCS at: ${dcs_ip}    console=yes
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${TYPES_URL}    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${types}=    List of Types    ${json}
    ${type_count}=    Get Length    ${types}
    Log    ${type_count} device types found: ${types}    console=yes
    Delete All Sessions
    [Return]  ${types}

Print All Verbs in Device
    [Arguments]     ${type}    ${dcs_ip}
    [Documentation]    Retrieve a list of all verbs for specified device type.
    ...    Example:\n| ${verb_list}= | Print All Verbs in Device | procurve | 172.17.4.137 |
    Log    ${\n}${type}    console=yes
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${TYPES_URL}${type}/supportedverbs    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${verbs}=   List of Verbs    ${json}
    ${verb_list}=    List of One Hack    ${verbs}
    :FOR    ${verb}    IN    @{verb_list}
    \    ${options}=    Get Verb Options String    ${verb}    ${type}    ${dcs_ip}
    \    Log    \x20\x20\x20\x20${options}   console=yes
    [Return]  ${verb_list}

Get Verb Options String
    [Arguments]     ${verb}    ${type}    ${dcs_ip}
    [Documentation]    Retrieve options for a verb for specified device type.
    ...    Example:\n| ${vo_string}= | Get Verb Options String | PowerSupply_LineVoltageProblem | C7000 | 172.17.4.137 |
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${TYPES_URL}${type}/${verb}    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${options}=    Set Variable    ${resp.json()}
    ${vo_string}=    Get From Dictionary    ${options}   String
    [Return]   ${vo_string}

Print All Attributes in Device
    [Arguments]     ${type}    ${dcs_ip}
    [Documentation]    Retrieve a list of all attributes for specified device type.
    ...    Example:\n| ${attribute_list}= | Print All Attributes in Device | procurve | 172.17.4.137 |
    Log    ${\n}${type}    console=yes
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${TYPES_URL}${type}/attributes    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${attributes}=   List of Attributes    ${json}
    ${attribute_list}=    List of One Hack    ${attributes}
    [Return]  ${attribute_list}

Get Attribute Value String
    [Arguments]     ${attribute}    ${type}    ${dcs_ip}
    [Documentation]    Retrieve a list of all attributes for specified device type.
    ...    Example:\n| ${av_string}= | Print All Attributes in Device | ports | procurve | 172.17.4.137 |
    Log    ${\n}${attribute}    console=yes
    Log    'Get Attribute Value String'    console=yes
    ${attribute_name}=    Get From Dictionary    ${attribute}    name
    Log    Attribute Name = ${attribute_name}    console=yes
    ${root_url}=    Catenate    SEPARATOR=    ${http}    ${dcs_ip}
    Create Session    httpbin    ${root_url}
    ${headers}    Create Dictionary    Accept-Type=application/json
    ${params}=    create dictionary    depth=1    link_state=up
    ${resp}=    Get Request    httpbin    ${TYPES_URL}${type}/${attribute_name}    headers=${headers}
    Should be Equal as Strings    ${resp.status_code}    200
    ${options}=    Set Variable    ${resp.json()}
    ${av_string}=    Get From Dictionary    ${options}   String
    [Return]   ${av_string}

Connect To DCS Via SSH
    [Arguments]                 ${ip}      ${username}       ${pswd}    ${prompt}    ${timeout}
    [Documentation]             Connect to system via SSH.
    ...                         Example:\n| Connect to DCS Via SSH  |10.0.12.106|  |root|  |hpvse123|    |Prompt|    |timeout|
    SSHLibrary.Open Connection         ${ip}     timeout=${timeout}
    ${output}=    SSHLibrary.Login      ${username}       ${pswd}
    ${output}=          SSHLibrary.Read
    SSHLibrary.Write    ${\n}
    ${output}=          SSHLibrary.Read until     ${prompt}
    ${output}=          SSHLibrary.Read

Disconnect from DCS
    Close Connection

Get DCS Status
    [Documentation]         Returns current state of DCS.
    Set Suite Variable      ${Command}      dcs status
    ${stdout}               ${stderr}       ${rc}=      Execute Command     ${Command}      return_stderr=True
    ...                     return_rc=True
    Log                     ${\n}${stdout}       console=yes
    Log                     ${stderr}       console=yes
    ${stdout}=      Split To Lines      ${stdout}
    ${status}=      Get From List       ${stdout}               0
    ${match}        ${group1}=          Should match Regexp     ${status}   (?im)DCS is (.*)
    [Return]        ${group1}

Get DCS Schematic
    [Documentation]         Returns the name of the installed schematic.
    Set Suite Variable      ${Command}      dcs status
    ${stdout}               ${stderr}       ${rc}=      Execute Command     ${Command}      return_stderr=True
    ...                     return_rc=True
    Log                     ${\n}${stdout}       console=yes
    Log                     ${stderr}       console=yes
    ${stdout}=      Split To Lines      ${stdout}
    ${status}=      Get From List       ${stdout}               1
    [Return]        ${status}

Start DCS With New Schematic
    [Arguments]             ${SCHEMATIC}    ${ip}      ${username}       ${pswd}    ${prompt}    ${timeout}
    [Documentation]         Starts DCS process using the specified schematic.
    Set Suite Variable      ${Command}      dcs start /dcs/schematic/${SCHEMATIC} cold
    ${stdout}               ${stderr}       ${rc}=      Execute Command     ${Command}      return_stderr=True
    ...                     return_rc=True
    Log                     ${\n}stdout = ${stdout}    console=yes
    Log                     stderr = ${stderr}    console=yes
    Should match Regexp     ${stdout}    .*(DCS daemon is already running|Data Center Simulator started).*
    Should match Regexp     ${stdout}    .*DCS daemon process id \\d+.*
    [Return]                ${stdout}

Stop DCS
    [Documentation]         Stops DCS Process.
    Set Suite Variable      ${Command}      dcs stop
    ${stdout}               ${stderr}       ${rc}=        Execute Command    ${Command}    return_stderr=True
    ...                     return_rc=True
    Log                     ${\n}stdout = ${stdout}    console=yes
    Log                     stderr = ${stderr}    console=yes
    ${match}    ${group1}=      Should match Regexp     ${stdout}   (.*DCS is Stopped.*|.*DCS daemon\\s+is not running.*)
    [Return]    ${group1}

Restart DCS With New Schematic
    [Arguments]        ${schematic}  ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    [Documentation]    Restart DCS using the specified Schematic
    Connect To DCS Via SSH   ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    Stop DCS
    Start DCS With New Schematic    ${schematic}  ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    Disconnect From DCS

Verify DCS Status Running
    [Arguments]        ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    Connect To DCS Via SSH   ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    ${status}=    Get DCS Status
    Log    ${status}    console=yes
    Should Be Equal As Strings    ${status}    Running
    Disconnect From DCS

Verify DCS Schematic
    [Arguments]        ${schematic}  ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    Connect To DCS Via SSH   ${ip}  ${user}  ${pass}  ${prompt}  ${timeout}
    ${schm}=    Get DCS Schematic
    Log    schm = ${schm}    console=yes
    ${match}=      Should match Regexp     ${schm}   /${schematic}$
    Disconnect From DCS
