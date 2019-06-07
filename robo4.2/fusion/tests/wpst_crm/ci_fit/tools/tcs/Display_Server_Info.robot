*** Settings ***
Documentation        Log to console various server information
...                  Example:
...                          time pybot -d /tmp/logs/Display_Server_Info/ -LTRACE -v APPLIANCE_IP:15.186.9.62 -v ENC_NAME:CN7544044K -v INFO:POWER,ILO -v INVERT:True -v POWER:On -v CONTAINS:*iLO* Display_Server_Info.robot
...                   REQUIRED: INFO --> POWER, ILO, ROM, ADAPTER, STATE, FIRMWARE, ALL
...                                      You can use multiple options with a comma as a separator (ex: INFO:power,ilo,rom)
...                                      ALL does not include FIRMWARE
...                   OPTIONAL: CONTAINS --> Filter string.  Will only display if the results have the filter within it.  '*' is a wildcard.
...                   OPTIONAL: PATH --> Path where the log file will be created.  Default is current path.
...                   OPTIONAL: POWER --> Will only display servers that are in the state mentioned.  Choose ALL if you want to see all power states.  (Default is ALL)
...                                       ex: on, off, resetting, powering off, etc
...                   OPTIONAL: INVERT --> Used with TYPE:POWER - Will display the power states that are NOT in the POWER variable.  Options are True or False.
...                                        ex: INVERT:True POWER:on will display all servers that do NOT have the powerState of "on"
...                   OPTIONAL: ENC_NAME --> Will display the power states on the given enclosure, instead of all consoles in the ME.

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../tests/robustness/resources/common.robot
Library            ../../tests/robustness/resources/robustness-helper.py
Library             Collections


*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${PATH}                         ./
${POWER}                        ALL
${INVERT}                       False
${ENC_NAME}                     None
${INFO}                         None
${CONTAINS}                     *

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Display Server Info
    Create File   ${PATH}/Display_Server_Info.csv
    ${Enclosures} =   Run Keyword If   "${ENC_NAME}" != "${null}"   fusion api get enclosures   param=?filter="name=='${ENC_NAME}'"
	...       ELSE   fusion api get enclosures   param=?sort=name:ascending
	Should Not Be Empty   ${Enclosures['members']}   msg=No Enclosures found.
    :FOR   ${enc}   IN   @{Enclosures['members']}
    \   Traverse Device Bays for Server Info   ${enc['deviceBays']}
    Log To Console   \n

*** Keywords ***
Traverse Device Bays for Server Info
    [Documentation]   traverse device bays
    [Arguments]   ${devices}
    Append To File   ${PATH}/Display_Server_Info.csv   \n
    Log To Console   \n
    :FOR   ${device}   IN   @{devices}
    \   ${uri} =   Get From Dictionary   ${device}   deviceUri
    \   ${bay} =   Get From Dictionary   ${device}   bayNumber
    \   ${server} =   Fusion Api Get Server Hardware   uri=${uri}
    \   ${present} =   Get From Dictionary   ${device}   devicePresence
    \   Run Keyword If   '${present}' == 'Absent' or '${present}' == 'Subsumed'   Run Keywords   Log To Console   Device in bay number ${bay} is Absent or Subsumed (Full Height).   AND   Continue For Loop
    \   Continue For Loop If   '${present}' == 'Absent' or '${present}' == 'Subsumed'
    \   Traverse INFO Argument   ${server}

Traverse INFO Argument
    [Documentation]   Go through the INFO argument for multiple selections
    [Arguments]   ${server}
    ${splitINFO} =   Split String   ${INFO}   separator=,
    :FOR   ${display}   IN   @{splitINFO}
    \   ${display} =   Convert To Uppercase   ${display}
    \   Run Keyword If   '${display}' == 'POWER'   Display Power State   ${server}
    \   ...    ELSE IF   '${display}' == 'ILO'   Display ILO Version   ${server}
    \   ...    ELSE IF   '${display}' == 'ROM'   Display ROM Version   ${server}
    \   ...    ELSE IF   '${display}' == 'ADAPTER'   Display Adapters   ${server}
    \   ...    ELSE IF   '${display}' == 'STATE'   Display State   ${server}
    \   ...    ELSE IF   '${display}' == 'FIRMWARE'   Display Firmware   ${server}
    \   ...    ELSE IF   '${display}' == 'ALL'   Display All   ${server}
    \   ...       ELSE   Log To Console   -v INFO is a required argument and must be one or more of these [POWER | ILO | ROM | ADAPTER | STATE | ALL ]

Display Power State
    [Documentation]   Display server power status
    [Arguments]   ${server}
    ${POWER} =   Convert To Uppercase   ${POWER}
    ${powerState} =   Get From Dictionary   ${server}   powerState
    ${powerState} =   Convert To Uppercase   ${powerState}
    ${INVERT} =   Convert To Uppercase   ${INVERT}
    Run Keyword If   '${POWER}' == 'ALL'   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${powerState}\n   AND   Log To Console   '${server['name']}' ...... Power State: '${powerState}'
    ...    ELSE IF   '${POWER}' == '${powerState}' and '${INVERT}' == 'FALSE'   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${powerState}\n   AND   Log To Console   '${server['name']}' ...... Power State: '${powerState}'
    ...    ELSE IF   '${POWER}' != '${powerState}' and '${INVERT}' == 'TRUE'   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${powerState}\n   AND   Log To Console   '${server['name']}' ...... Power State: '${powerState}'

Display ILO Version
    [Documentation]  Display iLO Information
    [Arguments]   ${server}
    :FOR   ${ilo}   IN   @{server['mpHostInfo']['mpIpAddresses']}
    \   ${mpIP} =   Run Keyword If   '${ilo['type']}' == 'DHCP'   Set Variable   ${ilo['address']}
    Run Keyword If   ${server['position']} < 10   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['mpHostInfo']['mpHostName']},${server['mpModel']},${server['mpFirmwareVersion']},${mpIP}\n   AND   Log To Console   '${server['name']}' ...... iLO Details: '${server['mpHostInfo']['mpHostName']}' \t ${server['mpModel']} \t '${server['mpFirmwareVersion']}' \t ${mpIP}
    ...       ELSE   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['mpHostInfo']['mpHostName']},${server['mpModel']},${server['mpFirmwareVersion']},${mpIP}\n   AND   Log To Console   '${server['name']}' ..... iLO Details: '${server['mpHostInfo']['mpHostName']}' \t ${server['mpModel']} \t '${server['mpFirmwareVersion']}' \t ${mpIP}

Display ROM Version
    [Documentation]  Display the ROM version
    [Arguments]   ${server}
    Run Keyword If   ${server['position']} < 10   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['romVersion']}\n   AND   Log To Console   '${server['name']}' ...... ROM: '${server['romVersion']}'
    ...       ELSE   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['romVersion']}\n   AND   Log To Console   '${server['name']}' ..... ROM: '${server['romVersion']}'

Display Adapters
    [Documentation]  Display the adapters
    [Arguments]   ${server}
    :FOR   ${adapter}   IN   @{server['portMap']['deviceSlots']}
    \   ${len} =   Get Length   ${adapter['physicalPorts']}
    \   @{WWPN} =   Run Keyword If   ${len} > 0   Traverse Physical Ports   ${adapter}
    \   ${strippedWWPN} =   Strip WWPN String   @{WWPN}
    \   Run Keyword If   ${server['position']} < 10   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},Adapter slot ${adapter['slotNumber']},${adapter['deviceName']},@{WWPN},@{strippedWWPN}\n   AND   Log To Console   '${server['name']}' ...... Adapter slot ${adapter['slotNumber']} = '${adapter['deviceName']}' \t WWPN: '@{WWPN}' \t '@{strippedWWPN}'
    ...           ELSE   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},Adapter slot ${adapter['slotNumber']},${adapter['deviceName']},@{WWPN},@{strippedWWPN}\n   AND   Log To Console   '${server['name']}' ..... Adapter slot ${adapter['slotNumber']} = '${adapter['deviceName']}' \t WWPN: '@{WWPN}' \t '@{strippedWWPN}'
    Append To File   ${PATH}/Display_Server_Info.csv   \n
    Log To Console   \n

Strip WWPN String
    [Documentation]  Strip the colons (:) from the WWPN string
    [Arguments]   @{WWPN}
    @{stripWWPN} =   Create List
    :FOR   ${port}   IN   @{WWPN}
    \   ${stripped} =   Run Keyword If   ${port} != None   Remove String   ${port}   :
    \   Append To List   ${stripWWPN}   ${stripped}
    [Return]   @{stripWWPN}

Traverse Physical Ports
    [Documentation]  Go through all the physical ports on a device and return the WWPNs
    [Arguments]   ${adapter}
    @{WWPN} =   Create List
    ${resp} =   Set Variable   ''
    :FOR   ${physicalPort}   IN   @{adapter['physicalPorts']}
    \   ${resp} =   Run Keyword If   '${physicalPort['type']}' == 'FibreChannel'   Set Variable   '${physicalPort['wwn']}'
    \   ...                   ELSE   Set Variable    '${physicalPort['virtualPorts'][1]['wwpn']}'
    \   Append To List   ${WWPN}   ${resp}
    [Return]   @{WWPN}

Display State
    [Documentation]  Display Profile State
    [Arguments]   ${server}
    Run Keyword If   ${server['position']} < 10   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['state']}\n   AND   Log To Console   '${server['name']}' ...... System state: ${server['state']}
    ...       ELSE   Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${server['state']}\n   AND   Log To Console   '${server['name']}' ..... System state: ${server['state']}

Display Firmware
    [Documentation]   Display firmware of various components related to SPP
    [Arguments]   ${server}
    ${gen} =   Set Variable   ${server['generation']}
    ${uri} =   Set Variable   ${server['uri']}
    ${resp} =   Fusion Api Get Server Hardware Firmware   uri=${uri}
    :FOR   ${component}   IN   @{resp['components']}
    \   ${nameFilter} =   Run Keyword and Ignore Error   Should Match   '${component['componentName']}'   '${CONTAINS}'
    \   ${versionFilter} =   Run Keyword and Ignore Error   Should Match   '${component['componentVersion']}'   '${CONTAINS}'
    \   Run Keyword If   '${nameFilter[0]}' == 'PASS' or '${versionFilter[0]}' == 'PASS'    Run Keywords   Append To File   ${PATH}/Display_Server_Info.csv   ${server['name']},${gen},${component['componentName']},${component['componentVersion']}\n   AND   Log To Console   '${server['name']}' '${gen}' ...... '${component['componentName']}' \t '${component['componentVersion']}'
    Append To File   ${PATH}/Display_Server_Info.csv   \n
    Log To Console   \n

Display All
    [Documentation]  Display all the info
    [Arguments]   ${server}
    Set Global Variable   ${POWER}   ALL
    Display Power State   ${server}
    Display ILO Version   ${server}
    Display ROM Version   ${server}
    Display State         ${server}
    Display Adapters      ${server}
