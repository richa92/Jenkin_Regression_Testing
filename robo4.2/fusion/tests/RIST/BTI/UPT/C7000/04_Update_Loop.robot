*** Settings ***
Documentation     Update the appliance through the hops
Suite Setup       Run Keywords  Cleanup Dir  ${UPDATEBIN_DIR}
...                             AND  Download Update Hops Files
...                             AND  Suite Setup
...                             AND  Verify Base Resources
...                             AND  Verify Storage Resources
Suite Teardown    Run Keywords  Suite Teardown
...                             AND  Remove Local Updatebin Files  ${UPDATEBIN_DIR}
Resource          resource.txt

*** Test Cases ***
C7000 UPT Update Loop Log Check Update Hops Files
    [Documentation]  Check Update Hops Files
    ${check}=  Check Update Hops Files  ${UPDATEBIN_DIR}  ${hops}  ${updatebin_urls}
    Run Keyword If  ${check}==${False}  Fail  msg=Missing updatebin Files for hops

C7000 UPT Update Loop Build Updatebin Files
    [Documentation]  Build updatebin files
    ${updatebin_files}=  Build Updatebin Files  ${updatebin_urls}
    Set Global Variable  ${updatebin_files}
    Log  ${updatebin_files}  console=True

C7000 UPT Update Loop Add Preupdate Resources
    [Documentation]  Add preupdate resources
    ${resp}=  Fusion Api Get Appliance Version
    Log  \nThe preupdate appliance software version is ${resp['softwareVersion']}  console=True
    Log  \nAdd the preupdate profiles  console=True
    Power Off Servers in Profiles  ${preupdate_profiles}
    ${resplist}=  Add Server Profiles from variable	 ${preupdate_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Get Resources Alerts  ${preupdate_profiles}  severity=Critical
    Get Resources Alerts  ${preupdate_profiles}  severity=Warning
    Log  \nVerify preupdate resources  console=True
    ${error_status}=  Verify resources  ${expected_preupdate_profiles}  ${resp['softwareVersion']}
    Run keyword if  ${error_status}==${True}  Fail  msg=Verify preupdate resources fail
    Log  \nGet preupdate interconnects ports status  console=True
    Get All Interconnects Ports Status
    Log  \nCreate preupadte database dump  console=True
    Create Database Dump  ${resp['softwareVersion']}

C7000 UPT Update Loop Update the Appliance
    [Documentation]  Update the appliance through the hops
    Suppress Warnings during Appliance Reboot
    ${ERRORS} =  set variable  ${0}
    ${len}=  get length  ${hops}
    : FOR  ${i}  IN RANGE  0  ${len}
    \   ${hop}=  set variable  ${hops[${i}]}
    \   Log  \nIncrease vm appliance cpu and memory for ${hop} if need to ...  console=True
    \   Increase VM Cpu and Memory  ${hop}  8  24
    \   Log  \nUpdate appliance to hop ${hop}...  console=True
    \   Update the Appliance  ${updatebin_files["${hop}"]}
    \   Postupdate Checks  ${hop}
    \   Log  \nAdd new profiles after update to hop ${hop}  console=True
    \   ${error_status}=  Add New Profiles  ${upt_hops_profiles[${i}]['new_profiles']}  ${hop}
    \   ${ERRORS} =  set variable if  ${error_status}==${True}  ${ERRORS + 1}  ${ERRORS}
    \   Log  \nVerify resources after update to hop ${hop}  console=True
    \   ${error_status}=  Verify resources  ${upt_hops_profiles[${i+1}]['pre_existing_profiles']}  ${hop}
    \   ${ERRORS} =  set variable if  ${error_status}==${True}  ${ERRORS + 1}  ${ERRORS}
    \   Log  \nGet profiles alerts after update to hop ${hop}  console=True
    \   Get Resources Alerts  ${upt_hops_profiles[${i+1}]['pre_existing_profiles']}  severity=Critical
    \   Get Resources Alerts  ${upt_hops_profiles[${i+1}]['pre_existing_profiles']}  severity=Warning
    \   Log  \nGet interconnects ports status before update to next hop  console=True
    \   Get All Interconnects Ports Status
    \   Log  \nCreate Database dump before update to next hop  console=True
    \   ${build}=  Get Updatebin Build  ${updatebin_files["${hop}"]}
	\   Create Database Dump  ${build}
	\   Log  \nCreate LE dump before update to next hop  console=True
	\   Take LE Support Dumps  ${build}
    Set Global Variable  ${ERRORS}
    Run keyword if  ${ERRORS}!=0  Fail  msg=There are ERRORS create profile or verify resources.

C7000 UPT Update Loop Get Profiles Critical Alerts
    [Documentation]  Get profiles critical alerts
    ${profiles} = 	Fusion Api Get Server Profiles  param=?sort=name:ascending
    ${CRIT_ALERT_COUNT} =  Run keyword if  ${profiles['count']}!=0  Get Resources Alerts  ${profiles['members']}  severity=Critical
    ...         ELSE  set variable  ${0}
    Set Global Variable  ${CRIT_ALERT_COUNT}
    Run keyword if  ${CRIT_ALERT_COUNT}!=0  Log  There are active critical alerts for profiles.  ERROR
    Run keyword if  ${CRIT_ALERT_COUNT}!=0  Fail  msg=There are critical alerts for the profiles.

C7000 UPT Update Loop Get Profiles Warning Alerts
    [Documentation]  Get profiles warning alerts
    ${profiles} = 	Fusion Api Get Server Profiles  param=?sort=name:ascending
    ${WARN_ALERT_COUNT} =  Run keyword if  ${profiles['count']}!=0  Get Resources Alerts  ${profiles['members']}  severity=Warning
    ...         ELSE  set variable  ${0}
    Set Global Variable  ${WARN_ALERT_COUNT}
    Run keyword if  ${WARN_ALERT_COUNT}!=0  Log  There are active warning alerts for profiles.  ERROR
    Run keyword if  ${WARN_ALERT_COUNT}!=0  Fail  msg=There are warning alerts for the profiles.

C7000 UPT Update Loop Set Do Not Delete
    [Documentation]  Set Do Not Delete
    ${DO_NOT_DELETE} =  set variable if  ${ERRORS}!=0 or ${CRIT_ALERT_COUNT}!=0 or ${WARN_ALERT_COUNT}!=0  ${True}  ${False}
    Log  DO_NOT_DELETE=${DO_NOT_DELETE}  console=true
    Set Global Variable  ${DO_NOT_DELETE}

*** Keywords ***
Update the Appliance
    [Documentation]   Update the appliance
    [Arguments]  ${updatebin_file}
    Log  \nUploading ${updatebin_file} to the appliance  console=True
    ${resp}=  Fusion Api Upload Appliance Firmware  ${UPDATEBIN_DIR}/${updatebin_file}
    Should Be Equal As Integers   ${resp['status_code']}  200
    Log  \nUploaded ${updatebin_file} to the appliance  console=True
    Log  \nUpdating appliance to ${updatebin_file}  console=True
    ${resp}=  Fusion Api Upgrade Appliance Firmware  ${updatebin_file}
    Log  \nWaiting for OneView state to be UPGRADE  console=True
    Wait Until Keyword Succeeds  5 m  1 s  Appliance State Should Match  ((?i)UPGRADE)
    Log  \nWaiting for OneView state to be OK  console=True
    Wait Until Keyword Succeeds  ${APPLIANCE_UPDATE_TIMEOUT}  1 m  Appliance State Should Match  ((?i)OK)
    Log  \nWaiting for OneView state to be UPGRADE  console=True
    Run Keyword and Ignore Error  Wait Until Keyword Succeeds  5 m  1 s  Appliance State Should Match  ((?i)UPGRADE)
    Log  \nWaiting for OneView state to be OK  console=True
    Run Keyword and Ignore Error  Wait Until Keyword Succeeds  5 m  1 s  Appliance State Should Match  ((?i)OK)

Verify Resources
    [Documentation]  Verify resources preupdate
    [Arguments]  ${profiles}  ${hop}
    ${status1}  ${error} =  Run Keyword and Ignore Error  Verify Base Resources
    Run keyword if  '${status1}'=='FAIL'  Log  Verify base resources fail for hop ${hop}  ERROR  console=True
    ${status2}  ${error} =  Run Keyword and Ignore Error  Verify Storage Resources
    Run keyword if  '${status2}'=='FAIL'  Log  Verify storage resources fail for hop ${hop}  ERROR  console=True
    ${status3}  ${error} =  Run Keyword and Ignore Error  Run Keyword for List  ${profiles}  Verify Server Profile
    Run keyword if  '${status3}'=='FAIL'  Log  Verify profiles fail for hop ${hop}  ERROR  console=True
    ${error_status} =  set variable if  '${status1}'=='PASS' and '${status2}'=='PASS' and '${status3}'=='PASS'  ${False}  ${True}
    [Return]  ${error_status}

Postupdate Checks
    [Documentation]  Postupdate checks
    [Arguments]  ${hop}
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Log  \nCheck update appliance task
    ${resp} =  Get Task By Param  param=?filter="'name'='Update appliance' AND associatedResource.resourceName='Appliance'"&sort=created:descending&count=1
    Wait for task2  ${resp}  timeout=600  interval=10
    Log  \nCheck appliance software version
    ${build}=  Get Updatebin Build  ${updatebin_files["${hop}"]}
    Check Appliance Software Version  ${build}
    Log  \nCheck refresh enclosure tasks
    :FOR  ${enclosure}  IN  @{expected_enclosures}
    \   ${resp} =  Get Task By Param  param=?filter="'name'='Refresh' AND associatedResource.resourceName='${enclosure['name']}' AND owner='System'"&sort=created:descending&count=1
    \   ${status}  ${error} =  Run Keyword and Ignore Error  Wait for task2  ${resp}  timeout=1800  interval=10
    \   Run keyword if  '${status}'=='FAIL'  Log  Refresh ${enclosure['name']} fail  WARN  console=True

Add New Profiles
    [Documentation]  Add New Profiles
    [Arguments]  ${profiles}  ${hop}
    Power Off Servers in Profiles  ${profiles}
    ${resplist}=  Add Server Profiles from variable  ${profiles}
    ${status}  ${error} =  Run Keyword and Ignore Error  Wait for Task2  ${resplist}  timeout=3600  interval=10
    Run keyword if  '${status}'=='FAIL'  Log  Add new profiles fail for ${hop}  ERROR  console=True
    ${error_status} =  set variable if  '${status}'=='PASS'  ${False}  ${True}
    [Return]  ${error_status}

Take LE Support Dumps
    [Documentation]  Take LE Support Dumps
    [Arguments]  ${build}
    ${LE_LIST} =    fusion api get logical enclosure
    :FOR    ${element}    IN    @{LE_LIST['members']}
    \    Log  ${\n}Logical Enclosure Name ${element['name']}  console=True
    \    Log  ${\n}Logical Enclosure Name URI ${element['uri']}  console=True
    \    ${LE_SD_NAME_LOCATION}=     Create Support name and location  ${LOG_DIR}    ${element['name']}_${build}
    \    ${le_ID}=    Remove String Using Regexp    ${element['uri']}    /rest/logical-enclosures/
    \    Convert to String    ${le_ID}
    \    ${task_uri}=    Create LE Support Dump    ${LE_support_dump}    ${le_ID}
    \    ${task} =  Fusion Api Get Task  uri=${task_uri}
    \    Wait For Task2  ${task}  timeout=1200  interval=10
    \    ${task} =  Fusion Api Get Task  uri=${task_uri}
    \    Log variables
    \    ${associatedResource}=     Get From Dictionary     ${task}    associatedResource
    \    ${ledumpUri}=     Get From Dictionary     ${associatedResource}    resourceUri
    \    Log    Downloading LE support dump to ${LE_SD_NAME_LOCATION}  console=True
    \    ${respdownload} =     Fusion Api Download Support Dump    ${ledumpUri}   ${LE_SD_NAME_LOCATION}
    \    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '200'    msg=Verification of status_code in downloading LE support dumps has FAILED    values=False