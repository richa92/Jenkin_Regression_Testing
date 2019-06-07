*** Setting ***
Documentation    Resource for ui.robot file

Library      robot.api.logger
Library      OperatingSystem
Library      FusionLibrary
Library      RoboGalaxyLibrary
Library      tests.ovs.OvsLibrary
Resource     ../../wpst_crm/ci_fit/tests/robustness/resources/common.robot
Resource     ../../cim/ui/Resource/CIM_CommonResource.txt
Library      BuiltIn
Library      Collections
Library      SSHLibrary
Library      XML
Variables    Supportool_data.py

*** Variable ***

${DataFile}         E:\\Robo-OVS-new\\fusion\\tests\\ovs\\MAT-I\\ui.xml
${Browser}          ff
${SeleniumSpeed}    0.1
${ApplianceUrl}     https://${SSH_HOST}
${SSH_HOST}         15.212.144.183
${DownloadPath}     C:/tmp/
${searchtext}       fixme-OVD12345.bin,Upload upgrade tar file succeeded.
${activityname}     Update appliance
${resource}         Appliance
${activitystate}    Completed
${activityowner}    Administrator
${searchtext1}      Preview dump created successfully
${searchtext2}      Total elapsed time in backup
${diag_flag}        off
${activityname1}    Create support dump
${fixmepath}        C:/fixmelog
*** Keyword ***

Upload fixme
    [Documentation]    Logins to the appliance and upload the fixme.bin file
    Log into Fusion appliance as Administrator
    tests.ovs.OvsLibrary.Fusion Ui Update Fixmebin    @{TestData.update_appliance}

Fix Should Be Applied
    [Documentation]    To check whether the fix is applied or not
    Open Connection And Login To Host    ${SSH_HOST}    ${ssh_cred['username']}    ${ssh_cred['password']}
    ${out}=    Execute Command     cat /ci/support/diags/diagnostic
    ${result}=    Split String    ${out}    \n
    log    [check debug equals to on]#:${result}    console=true
    :FOR     ${line}    in    @{result}
    \    ${value}=     Evaluate    'debug=on'
    \    ${status}    ${taskState} =  Run Keyword and Ignore Error    Should Contain    ${line}    ${value}
    \    Run keyword if    '${status}'=='PASS'    Exit for loop
    Run keyword if    '${status}'!='PASS'    FAIL    Failed to apply the fix

Audit Log should contain fixme log
    [Documentation]   Check audit log to for the fixme log
    #Fusion UI Navigate to Dashboard Page
    Download and verify entry in Audit log file    ${DownloadPath}/FIXME_AUDIT    ${searchtext}

Activity Page Should Contain Fixme Alert
    [Documentation]    check fixme state in activity page
    #Fusion UI Navigate to Dashboard Page
    Browse Activity Page and check for alert    ${activityname}    ${activitystate}    ${activityowner}

Browse Activity Page and check for alert
    [Documentation]    Code implementation for Verification of fixme update tasks in appliance activity page
    [Arguments]    ${activityname}    ${activitystate}    ${activityowner}
    Fusion UI Navigate To Activity Page
    wait for element visible    //*[@id='hp-activities']/tbody//tr[1][//span[text()='${activityname}'] and td/span[text()='${activitystate}'] and td/div[text()='${activityowner}']] 30
    ${count}=    Get Matching XPath Count    //*[@id='hp-activities']/tbody//tr[1][//span[text()='${activityname}'] and td/span[text()='${activitystate}'] and td/div[text()='${activityowner}']]
    Run Keyword If  ${count} == ${activityCount}    Log    Given alert '${activityname}' with state '${activitystate}' is present in the activity page    console=true
    Run Keyword Unless  ${count} == ${activityCount}     Fail   Given alert '${activityname}' with state '${activitystate}' is not present in the activity page ${activityCount} and ${count}

Get fixmeinstallog details
    [Documentation]    Gets the latest fixme log file from /updatelogs/fixme_install.log
    Open Connection And Login To Host    ${SSH_HOST}    ${ssh_cred['username']}    ${ssh_cred['password']}
    ${fixmeinstalllog}=    Execute Command    cat /updatelogs/fixme_install.log
    ${LastLine}=    Get Line    ${fixmeinstalllog}    -1
    ${fixmeLog}=    Split String    ${LastLine}    ,
    [Return]    ${fixmeLog}

Get updatelogs details
    [Documentation]    Gets latest fixmelog details from /updatelogs/update.log
    Open Connection And Login To Host    ${SSH_HOST}    ${ssh_cred['username']}    ${ssh_cred['password']}
    ${updatefixlog}=    Execute Command    cat /updatelogs/update.log
    @{logs}=    Get Regexp Matches    ${updatefixlog})    NAME\\s:.*STATUS
    ${logdetails}=    Set Variable    @{Logs}[-1]
    ${updatelogDetails}=    Split String    ${logdetails}    ,
    ${Getstatus}=    Get Lines Matching Regexp    ${updatefixlog}    [Ff]ix for OVD\\d+    partial_match=True
    @{getlastlog}=    SplitString    ${Getstatus}    \n
    ${getfixmeStatus}=    Set Variable    @{getlastlog}[-1]
    ${Condition}=    Run Keyword and Return Status    Should Match Regexp    ${getfixmeStatus}    Fix for OVD\\d+ successfully applied
    Run Keyword If    '${Condition}' == 'True'    Set Suite Variable    ${fixmestatus}    STATUS : success
    ...    ELSE IF    '${Condition}' == 'False'    Set Suite Variable    ${fixmestatus}    STATUS : failed
    Remove from List    ${updatelogDetails}    3
    Append To List    ${updatelogDetails}    ${fixmestatus}
    [Return]   ${updatelogDetails}

Fixme and Update logs Should Be Equal
    [Documentation]   fixmeinstall log present in upadtelog file should match with /updatelogs/fixmeinstall.log
    ${fixmelog}=    Get fixmeinstallog details
    ${updatelogsDetails}=    Get updatelogs details
    ${Condition}=    Run Keyword and Return Status    Lists Should Be Equal    ${fixmelog}    ${updatelogsDetails}
    Run Keyword If    '${Condition}' == 'True'    Log    fixmeinstalllog content validation completed    console=True
    ...    ELSE IF    '${Condition}' == 'False'    Fail   fixmeinstall log in /updatelogs/fixmeinstall.log is not correct and it is not matching with update log contents    console=True

Download fixmeinstallation details and validate it contents
    [Documentation]    compares both downloaded fixme install log from ui with updatelogs
    ${updatelogsDetails}=    Get updatelogs details
    #Remove File    ${FixmeUilog}\\fixme_install.log
    # Log into Fusion appliance as Administrator
    Empty Directory    ${fixmepath}
    Fusion Ui Download Fixme Installation Details    ${FixmeUilog}
    ${fixmeuiinstalllog}=    OperatingSystem.Get File    ${FixmeUilog}\\fixme_install.log
    ${LatestLog}=    Get Line    ${fixmeuiinstalllog}    -1
    ${splitLatestuiinstalllogdetails}    Split String    ${LatestLog}    ,
    ${status}=    Run Keyword and Return Status    Lists Should Be Equal    ${splitLatestuiinstalllogdetails}    ${updatelogsDetails}
    Run Keyword If    '${status}' == 'True'    Log    Downloaded fixmeinstalllog content validation completed    console=True
    ...    ELSE IF    '${status}' == 'False'    Fail    Downloaded fixmeinstall log is not correct and it is not matching with update log contents     console=True

Audit Log message for Support Dump
    [Documentation]   verifies audit log to check the Support Dump Log messages
    # Fusion UI Navigate to Dashboard Page
    Empty Directory    ${DownloadPath}
    Download and verify entry in Audit log file    ${DownloadPath}/SD_AUDIT    ${searchtext1}

Download audit log for Support Dump creation in appliance
    [Documentation]    Verifies audit log to check whether the log is created for support dump creation
    #Log into Fusion appliance as Administrator
    ${Status}=    Fusion UI create support dump    @{TestData.createsupportdump}
    Should Be True    ${Status}    msg=Failed to create support dump
    Audit Log message for Support Dump

Update Diagnostic State
    [Documentation]     Edit file /ci/support/diags/diagnostic
    [Arguments]    ${debug_state}    ${source}=/ci/support/diags/diagnostic
    ...  ${state}=debug=on    ${state2}=debug=off

    Open Connection And Login To Host    ${SSH_HOST}    ${ssh_cred['username']}    ${ssh_cred['password']}
    ${diag_state}=    Execute Command    cat ${source}

    ${cmd}=    Run Keyword if    '${diag_state}'=='${state}'    Set Variable    's/debug=on/debug=${debug_state}/g'
    ...                                           ELSE    Set Variable    's/debug=off/debug=${debug_state}/g'
    ${stdout}    ${stderr}    ${rc}=    Execute Command    sed -i ${cmd} ${source}    return_stderr=True    return_rc=True
    Run Keyword If    '${rc}'=='0'    Log    Diagnostic State Changed Successfully
    ...       ELSE    Run Keyword And Continue On Failure    FAIL   Failed to change diagnostic flag in appliance!
    #Should Be Empty    ${stderr}                 msg=Error returned: ${rc} ${stderr}
    Should Be Equal As Integers    ${rc}    0    msg=non-zero return code ${rc}

    ${diag_state2}=    Execute Command    cat ${source}
    Run Keyword If    '${diag_state2}'=='${state}'    Log    Diagnostic Flag Changed Successfully To Enabled State : ${diag_state2}    console=true
    ...       ELSE IF    '${diag_state2}'=='${state2}'    Log    Diagnostic Flag Changed Successfully To Disabled State : ${diag_state2}    console=true
    ...       ELSE    Run Keyword And Continue On Failure    FAIL   Failed to change Diagnostic Flag in appliance!

Download and unzip ciDebug log file
      [Documentation]    Download cidebug from UI , Extract ciDebug tar/gz file and return actual log file path
      [Arguments]       ${DownloadPath}=${DownloadPath}/cidebug    ${ExtractedPath}=${DownloadPath}/ci/logs
      #[Return]          ${cidebuglogfilepath}
      Create Folder If not Exists    ${DownloadPath}
      Empty Directory    ${DownloadPath}
      Fusion UI Download Cidebug Logs    ${DownloadPath}
      Sleep    5
      ${logfiles} =     OperatingSystem.List Files In Directory       ${DownloadPath}         *.gz
      ${logfile} =      Get From List     ${logfiles}    0
      ${unzipfilepath} =      Set Variable      ${DownloadPath}/${logfile}

      #Unzip ciDebug.tar file
      extract zip file    ${unzipfilepath}    ${DownloadPath}
      ${cidebuglogfiles} =      OperatingSystem.List Files In Directory    ${ExtractedPath}    *.log
      ${cidebuglogfile} =    Get From List     ${cidebuglogfiles}    0
      ${cidebuglogfilepath} =   Set Variable      ${ExtractedPath}/${cidebuglogfile}
      [Return]    ${cidebuglogfilepath}

ciDebug log File Should Contain
      [Documentation]    Searches string in extracted log file
      [Arguments]       ${cidebuglogfilepath}     ${searchtext}    ${blnExpected}=True    ${reverse}=False
      ${bln_logentry_exists} =    file_contains    ${cidebuglogfilepath}    ${searchtext}    ${reverse}
      Should Be Equal As Strings    ${bln_logentry_exists}  ${blnExpected}    msg=Entry ${searchtext} not available in log file.

Download and verify entry in ciDebug log file
      [Documentation]    Combine Download and search keywords for cidebug feature
      [Arguments]       ${DownloadPath}    ${searchtext}
      ${filepath}=      Run Keyword And Return    Download and unzip ciDebug log file   ${DownloadPath}
      ciDebug log File Should Contain      ${filepath}    ${searchtext}

CiDebug download and check for backup entry
    [Documentation]    Creates backup , enables cidebug flag and verify backup entry in extracted cidebug logs
    Update Diagnostic State    ${diag_flag}
    Log into Fusion appliance as Administrator
    # Fusion UI Navigate to Dashboard Page
    Fusion UI Create Backup
    Download and verify entry in ciDebug log file    ${DownloadPath}/cidebug    ${searchtext2}