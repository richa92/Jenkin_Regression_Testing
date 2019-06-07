*** Settings ***
Documentation       Efuse the blades and interconnects and factory reset the interconnects.
...                 Deploy the dd image onto the active and standby CIMs.
...                 pybot -v ENCLOSURE:Ring6ActiveCIM -v 001_Deploy.robot
Resource            resource.txt
Variables           variables.py  ${ENCLOSURE}
Suite Setup         Suite Setup

*** Variables ***
${ENCLOSURE}                    Ring6ActiveCIM
${INSTALLATION_TIME}            90 minutes
${JSON_PATH}                    3.10.04

*** Test Cases ***
Synergy UPT Issue E-Fuse for all blades
    [Tags]    all    blades
    ${encs} =    Fusion Api Get Enclosures
    ${type} =    Set Variable    deviceBays
    :FOR    ${enc}   IN     @{encs['members']}
    \    Log    \n${enc['name']} ${enc['uri']}   console=True
    \    Process Bays   ${enc['${type}']}   ${type}   ${enc['uri']}
    Sleep  1080s

Synergy UPT Issue E-Fuse for all interconnects
    [Tags]    all    interconnects
    ${encs} =    Fusion Api Get Enclosures
    ${type} =    Set Variable    interconnectBays
    :FOR    ${enc}   IN     @{encs['members']}
    \    Process Bays   ${enc['${type}']}   ${type}   ${enc['uri']}
    Sleep  900s

Synergy UPT Factory Reset All Natasha
    [Documentation]  Factory reset Natasha in enclosure
    log  EM SERIAL is ${EM_SERIAL}  console=True
    log  FUSION IP is ${FUSION_IP}  console=True
    Factory Reset Natasha in Enclosure  ${EM_SERIAL}

Synergy UPT Deploy DD Image Prepare For Firmware Update
    [Documentation]  Prepare For Firmware Update
    Log Variables
    Log  \nSet log level to ${SUITE_LOG_LEVEL}
    Set Log Level  ${SUITE_LOG_LEVEL}
    Log  \nCheck appliance cluster status on ${ENCLOSURE}...  console=True
    Check Appliance Cluster Status
    Log  \nCluster ok on ${ENCLOSURE}  console=True
    Log  \nGet firmware versions on ${ENCLOSURE}...  console=True
    Get Firmware Versions

Synergy UPT Setup CIM USB Keys
    [Documentation]    Setup CIM USB keys
    Setup CIM USB Key    ${ACTIVE_CIM}
    Setup CIM USB Key    ${STANDBY_CIM}

Synergy UPT Deploy DD Image Deploy Firmware Update On Two Node HA
    [Documentation]  Initiate DD Reimage script from primary CIM
    Log  \nInitiate DD Reimage script from primary CIM...  console=True
    Initiate DD Reimage On Two Node HA  ${ACTIVE_CIM}
    Wait For Fusion Install and Startup

Synergy UPT Deploy DD Image Verify After Deploy
    [Documentation]  Verify the cluster and the enclosures after deploy
    Log  \nCheck appliance cluster status on ${ENCLOSURE}...  console=True
    Check Appliance Cluster Status
    Log  \nCluster ok on ${ENCLOSURE}  console=True
    Log  \nVerify enclosures ${ENCLOSURE} after deploy...  console=True
    Run Keyword and Ignore Error  Verify Claimed Enclosure

*** Keywords ***
Process Bays
   [Documentation]    issues efuse command for all bays for the given bay type
   ...                valid types are in the REST API refrerence.
   ...                ex:   deviceBays, interconnectBays
   [Arguments]   ${bays}   ${type}   ${encuri}
   :FOR   ${bay}   IN   @{bays}
   \    ${body} =    json.loads    [{"op": "replace", "path": "/${type}/${bay['bayNumber']}/bayPowerState","value":"E-Fuse"}]
   \    ${resp} =    Fusion Api Patch Enclosure   ${body}   ${encuri}   api=300
   \    Log    \nE-Fuse request status_code: ${resp['status_code']} for ${encuri} bay ${bay['bayNumber']}   console=True

Factory Reset Natasha in Enclosure
    [Documentation]  Factory reset Natasha in bay set 1
    [Arguments]  ${enc}
    Get EM IP  enc_serial=${enc}
    Get EM Token  ${enc}
    Factory Reset ICM  1
    Factory Reset ICM  4

Check Appliance Cluster Status
    [Documentation]  Check Appliance Cluster Status
    Login to Fusion via SSH
    ${Command}=  Set Variable  crm_mon -1
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Run Keyword If  ${rc}!=0  Fail  msg=Failed to run crm_mon on ${ENCLOSURE}
    Log  \n crm_mon output: ${stdout}
    ${status}  ${response} =  Run Keyword and Ignore Error
    ...  Should Match Regexp  ${stdout}  (?i)2 Nodes configured
    Run Keyword If  '${status}'=='FAIL'  Fail  msg=Appliance cluster not ok on ${ENCLOSURE}
    Log  Cluster has 2 Nodes configured  console=True
    Logout of Fusion Via SSH

Get Firmware Versions
    [Documentation]  Get firmware versions
    Login to Fusion via SSH
    Get Fusion Version
    Get iLO Version
    Get NIC Version
    Logout of Fusion Via SSH

Get Fusion Version
    [Documentation]  Get Fusion version
    ${Command}=  Set Variable  cat /ci/etc/version
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Should Be Equal As Integers  ${rc}  0  msg=Failed to get Fusion Version.
    Log  \nFusion Version: ${stdout}  console=True
    [Return]  ${stdout}

Get iLO Version
    [Documentation]  Get iLO version
    ...              OPTIONS="-s ${IP} -u ${USERNAME} -p ${PASSWORD}"
    [Arguments]  ${options}=${EMPTY}
    ${stdout}  ${rc}=  Execute Command  /ci/bin/ilo_get_health.sh ${options} -t FIRMWARE_INFORMATION  return_rc=True
    Log  \niLO Versions:  console=True
    ${ilo_fw_versions}  Create Dictionary
    ${fw_info}=  Parse XML  ${stdout}
    ${size}=  Get Length  ${fw_info}
    :FOR   ${index}  IN RANGE  1  ${size}+1
    \  ${index_fw_info}=  XML.Get Element  ${fw_info}  INDEX_${index}
    \  ${name}=  XML.Get Element Attribute  ${index_fw_info}  VALUE  xpath=FIRMWARE_NAME
    \  ${version}=  XML.Get Element Attribute  ${index_fw_info}  VALUE  xpath=FIRMWARE_VERSION
    \  Log To Console  ${name}: ${version}
    \  Set To Dictionary  ${ilo_fw_versions}  ${name}  ${version}
    [Return]   ${ilo_fw_versions}

Get NIC Version
    [Documentation]  Get NIC version
    ${Command}=  Set Variable  ethtool -i eth0
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Should Be Equal As Integers  ${rc}  0  msg=Failed to get NIC Version.
    Log  \nNIC Versions:\n ${stdout}  console=True
    [Return]  ${stdout}

Verify Claimed Enclosure
    [Documentation]  Login to OV using SSh and verify claimed enclosure
    Login to Fusion via SSH
    ${command}=  Set Variable  /ci/bin/tbird/appliance-hal.sh list-enclosures
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${command}  return_stderr=True
    ...      return_rc=True
    Should Be Equal As Integers  ${rc}  0  msg=Failed to get claimed enclosures.
    Should Not Be Equal As Strings  ${stdout}   ${empty}
    ...  msg=Failed to get an enclosure name returned
    Log  Found Claimed Enclosure: ${stdout}  console=True
    Logout of Fusion Via SSH

Wait For Fusion Install and Startup
    [Documentation]  Sleep for ${Installation_Time}.
    ${DateTime}=  Get Current Date
    Log  Time: ${DateTime}  console=True
    Console  \nSleep for ${Installation_Time}.
    Sleep  ${INSTALLATION_TIME}  reason=Waiting for installation, reboot and startup.

Ping Ipv4 Address
    [Documentation]  Ping the IP address and retun Unreachable or Pingable.
    [Arguments]  ${ipv4address}
    ${rc}  ${output} =  Run and return RC and Output  ping -n 4 ${ipv4address}
    ${gottask}   ${response} =  Run Keyword and Ignore Error  Should be equal
    ...  ${rc}  ${0}  \n${output}
    ${value1}=  Evaluate  'Request timed out'
    ${value2}=  Evaluate  'Destination host unreachable'
    ${failStatus1}   ${response} =  Run Keyword and Ignore Error
    ...  Should Contain  ${output}  ${value1}
    ${failStatus2}   ${response} =  Run Keyword and Ignore Error
    ...  Should Contain  ${output}  ${value2}
    Run Keyword If  '${failStatus1}'=='PASS' or '${failStatus2}'=='PASS'
    ...  Return From Keyword  Unreachable
    ...  ELSE  Return From Keyword  Pingable

Wait For Primary CIM To Reboot
    [Documentation]  Ping and wait for primary CIM untill reboots
    [Arguments]  ${ipv4address}  ${max_try}=20
    Log  Waiting for CIM reboots to start Oneview installation ...  console=True
    #Ping until IP becomes unreachable
    :FOR  ${index}   in range  1  ${max_try}
    \  ${res} =   Ping Ipv4 Address  ${ipv4address}
    \  Exit For Loop If  '${res}'=='Unreachable'
    \  Sleep  60s
    Run Keyword If   ${index} == ${max_try}-1
    ...  Fail   Failed to start DD reimage, plese check the /mnt/usb/reimage_logs

Setup CIM USB Key
    [Documentation]     setup CIM USB Key
    [Arguments]    ${IP}
    Login to Fusion via SSH  ${IP}
    # Check the json file
    SSHLibrary.File Should Exist    /mnt/usb/${JSON_PATH}/cic-manager-setup-config.json
    # remove the old json file
    ${command}=    Set Variable
    ...    /bin/rm /mnt/usb/cic-manager-setup-config.json
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Run Keyword If  ${rc}!=0  Fail  msg=Failed to remove the json file on ${IP}
    # remove the old dd image
    ${command}=    Set Variable
    ...    /bin/rm /mnt/usb/HPEOneView-*
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Run Keyword If  ${rc}!=0  Fail  msg=Failed to remove dd image on ${IP}
    # copy the json file
    ${command}=    Set Variable
    ...    /bin/cp -f /mnt/usb/${JSON_PATH}/cic-manager-setup-config.json /mnt/usb/cic-manager-setup-config.json
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Run Keyword If  ${rc}!=0  Fail  msg=Failed to cp the json file on ${IP}
    # copy the dd image
    ${command}=    Set Variable
    ...    /bin/cp -f /mnt/usb/${JSON_PATH}/HPEOneView-* /mnt/usb/
    ${stdout}  ${stderr}  ${rc}=  Execute Command  ${Command}  return_stderr=True  return_rc=True
    Run Keyword If  ${rc}!=0  Fail  msg=Failed to copy the dd image on ${IP}
    Logout of Fusion Via SSH

Initiate DD Reimage On Two Node HA
    [Documentation]  SSH to Oneview appliance and run
    ...  "/ci/etc/usb-reimage/developer_usb_reimage_two_node.sh -u $baseurl -f $ddimage"
    [Arguments]   ${IP}=${MAINTANENCE_IP}    ${USERNAME}=${FUSION_SSH_USERNAME}
    ...       ${PASSWORD}=${FUSION_SSH_PASSWORD}  ${PROMPT}=${FUSION_PROMPT}
    ...       ${TIMEOUT}=${FUSION_TIMEOUT}  ${ALIAS}=Fusion_SSH
    Log Many  ${IP}   ${USERNAME} ${PASSWORD} ${PROMPT}   ${TIMEOUT}
    ${id}=  Open Connection  ${IP}  alias=${ALIAS}
    ${output}=  Login  ${USERNAME}  ${PASSWORD}
    Set Client Configuration  timeout=20 minutes
    ${command}=  Set Variable
    ...  /ci/etc/usb-reimage/developer_usb_reimage_two_node.sh -R -F
    Log  Executing Command '${command}'  console=True
    SSHLibrary.Write  ${command}
    Wait Until Keyword Succeeds    10 m   1 s
    ...    Read Until    Factory resetting the EMs.
    Log  Factory resetting the EMs...  console=True
    Wait for Primary CIM To Reboot    ${IP}


