*** Setting ***
Documentation    Resource for PreviewDumpTestcase file

Library          robot.api.logger
Library          OperatingSystem
Library          FusionLibrary
Library          RoboGalaxyLibrary
Library          tests.ovs.OvsLibrary
Library          BuiltIn
Library          Collections
Library          SSHLibrary
Library          XML
Variables        Supportool_data.py
Resource         support_resource1.txt
Resource         ../../cim/ui/Resource/CIM_CommonResource.txt

*** Variable ***

${Browser}                ff
${SeleniumSpeed}          0.1
${ApplianceUrl}           https://${SSH_HOST}
${SSH_HOST}               15.212.144.183
${PDpath}                 C:/support_dump/PD
${N_groups}               ${0}
${decyrpt_file}           ${PDpath}\\ci_ovspreviewdump.sdmp
${decryptor_path}         ${CURDIR}\\..\\..\\..\\tools\\Decryptor
${updateUnzipPath}        ${PDpath}\\update
${auditUnzipPath}         ${PDpath}\\audit
${messagesUnzipPath}      ${PDpath}\\messages

*** Keyword ***
Check if all the tar files exists in preview dump
    [Arguments]    ${PDpath}=${PDpath}
    [Documentation]    verifies if audit log,cidebug log,messages.tar, sar.tar files exists
    @{pd_contents}=    Create List    audit.tar.gz    ciDebug.tar.gz    messages.tar.gz    update.tar.gz
    :FOR     ${file}    in    @{pd_contents}
    \    ${file1}=    Run Keyword and Return Status    OperatingSystem.File Should Exist    ${PDpath}\\${file}
    \    Run Keyword If    '${file1}' == 'True'    OperatingSystem.File Should Not Be Empty    ${PDpath}\\${file}
    \    ...    ELSE IF    '${file1}' == 'False'    Run Keyword And Continue On Failure    Fail    msg= ${file} doesnt exist.

Appliance commands should be present in PD
    [Documentation]   Checks all the appliance command exists and has data in it, under appliance\\commands directory in Preview Dump.
    [Arguments]    ${PDpath}
    @{items}=    OperatingSystem.List Directory    ${PDpath}\\appliance\\commands
    Run Keyword And Continue On Failure    List Should Contain Sub List    ${items}    ${appliance_commands}    msg=${space}${space}${space}${space}*Below commands file is missing
    :FOR    ${cmd}    in    @{appliance_commands}
    \    ${CmdStatus}=    Run Keyword and Return Status    OperatingSystem.File Should Not Be Empty    ${PDpath}\\appliance\\commands\\${appliance_commands[${N_groups}]}
    \    Run Keyword If    '${CmdStatus}' == 'True'    Log    The File ${N_groups} : ${appliance_commands[${N_groups}]} is present in appliance\\commands directory    console=True
    \    ...    ELSE IF    '${CmdStatus}' == 'False'    Run Keyword And Continue On Failure    Fail    msg= The File ${N_groups}: ${appliance_commands[${N_groups}]} has no data in it.
    \    ${N_groups}=    Evaluate    ${N_groups} + 1

Boot log, version and postgres command files should exist
    [Documentation]   Checks boot log , appliance  verison, postgress command files exists and has a data init.
    @{list} =    Create List    version    boot.log    pg_files
    :FOR     ${files}    in    @{list}
     \    Run Keyword And Continue On Failure    Run Keyword If    '${files}' == 'version'    version file should not be empty
     \    ...    ELSE IF    '${files}' == 'boot.log'   Boot log file should present with data init
     \    ...    ELSE IF    '${files}' == 'pg_files'   Check Postgres Commands Files Exist

version file should not be empty
    [Documentation]  verifies version file exists and has data init
    ${version}=     OperatingSystem.List Directory    ${PDpath}\\appliance\\ci\\etc
    ${versionfile}=    Run Keyword and Return Status     List Should Contain Sub List        ${version}    ${pd_version}
    Run Keyword If    '${versionfile}' == 'True'    OperatingSystem.File Should Not Be Empty    ${PDpath}\\appliance\\ci\\etc\\${pd_version[0]}
    ...    ELSE    Fail    msg= ${pd_version[0]} file under${PDpath}\\appliance\\ci\\etc is missing

Boot log file should present with data init
    [Documentation]  verifies boot log file exists and has data init
    ${boot}=     OperatingSystem.List Directory    ${PDpath}\\appliance\\var\\log
    ${bootfile}=    Run Keyword and Return Status     List Should Contain Sub List    ${boot}    ${pd_boot}
    Run Keyword If    '${bootfile}' == 'True'    OperatingSystem.File Should Not Be Empty    ${PDpath}\\appliance\\var\\log\\${pd_boot[0]}
    ...    ELSE    Fail    msg= ${pd_boot[0]} file under${PDpath}\\appliance\\var\\log is missing

Check postgres commands files exist
    [Documentation]  check alert and task file exist and has data init
    ${postgres}=    OperatingSystem.List Directory    ${PDpath}\\postgres\\commands
    Log    Postgress command files verification    console='True'
    Run Keyword And Continue On Failure     List Should Contain Sub List    ${postgres}    ${pd_pg_cmds}    msg=Files are missing
    :FOR    ${pgfiles}    in    @{pd_pg_cmds}
    \    ${pgCmdStatus}=    Run Keyword and Return Status    OperatingSystem.File Should Not Be Empty     ${PDpath}\\postgres\\commands\\${pd_pg_cmds[${N_groups}]}
    \    Run Keyword If    '${pgCmdStatus}' == 'True'    Log    The File ${N_groups} : ${pd_pg_cmds[${N_groups}]} is present in postgres\\commands Directory      console=True
    \    ...    ELSE IF    '${pgCmdStatus}' == 'False'    Run Keyword And Continue On Failure    Fail    msg= The File ${pd_pg_cmds[${N_groups}]} has no data in it.
    \    ${N_groups}=    Evaluate    ${N_groups} + 1

Download Preview Dump via Rest api
    [Documentation]  creates support and preview dump, downloads preview dump
    [Arguments]    ${PDpath}
    Login to OV Via REST API
    Empty Directory    ${PDpath}
    CIM_CommonResource.Create Folder If Not Exists    ${PDpath}
    ${sdmp_body}=    Create Dictionary    encrypt=${true}    errorCode=CI    dump=both
    log    \n creating support and preview dump in ${SSH_HOST} appliance\n    console=true
    ${resp}    Fusion Api Create Support Dump    ${sdmp_body}
    ${sd_status}=    Get From Dictionary     ${resp}    status_code
    Should Be Equal As Integers    ${sd_status}    200    msg= Failed to create support dump\n
    log    Support dump successfully created\n    console=true
    ${uri}=     Get From Dictionary    ${resp}    preview_dump_uri
    log    Preview Dump uri is : ${uri}\n    console=true
    log    Downloading preview dump...\n    console=true
    ${dl_resp}=    Fusion Api Download Support Dump    uri=${uri}    localfile=${decyrpt_file}
    ${download_status}=    Get From Dictionary     ${dl_resp}    status_code
    Should Be Equal As Integers    ${download_status}    200    msg= Failed to download preview dump\n
    log    Preview dump successfully downloaded...\n    console=true

Preview dump log verification
    [Documentation]   Checks all  appliance commands are executed successfully.
    [Arguments]    ${PDpath}    ${CMD_LIST}
    ${logfiles}=    OperatingSystem.List Files In Directory    ${PDpath}    *_support_dump.log
    ${logfile}=    Get From List     ${logfiles}    0
    ${get_PD_log}=    OperatingSystem.Get File    ${PDpath}\\${logfile}
    @{logs}=    Get Regexp Matches    ${get_PD_log}     Command(.*?)executed
    log    \n..........FETCH SUCCESSFULLY EXECUTED COMMANDS FROM PREVIEW DUMP LOGS.........\n    console=true
    @{ScoreList}=    Create List
    : For    ${i}     IN    @{logs}
    \    ${remove}=    Remove String Using Regexp   ${i}   \x00    Command\\s    \\sexecuted
    \    Append To List    ${ScoreList}    ${remove}
    \    log    ${N_groups} : ${ScoreList[${N_groups}]}\n    console=true
    \    ${N_groups}=    Evaluate    ${N_groups} + 1
    Run Keyword And Continue On Failure    List Should Contain Sub List        ${ScoreList}    ${CMD_LIST}    msg=Following commands were not executed
    Run Keyword And Continue On Failure    List Should Contain Sub List        ${ScoreList}    ${tasks_CMD}    msg=Task command is not executed
    List Should Contain Sub List        ${ScoreList}    ${alerts_CMD}    msg=alert command is not executed

Extract tar file in preview dump
    [Documentation]  Extract tar files
    [Arguments]       ${UnzipPath}    ${tarfile}
    Create Directory    ${UnzipPath}
    Empty Directory    ${UnzipPath}
    ${extractstatus}=    Run Keyword and Return Status    extract zip file    ${PDpath}\\${tarfile}    ${UnzipPath}
    Run Keyword If    '${extractstatus}' == 'True'    Log    ${tarfile} extracted succesfully on {UnzipPath}
    ...    ELSE    Fail    msg=unable to extract ${tarfile} log

Extract update log and check all the file exist
     [Documentation]  Extract updatelog and verify all the files are present init
     Extract tar file in preview dump    ${updateUnzipPath}    update.tar.gz
     @{updatelogfiles}=    Create List    db_install_upgrade.log    fixme_install.log    postgres_filesys_layout.log    update.log
     @{updatelog}=    OperatingSystem.List Directory    ${updateUnzipPath}\\updatelogs
     log    \n..............VALIDATE IF ALL THE UPDATE LOG FILE EXIST IN PREVIEW DUMP............\n    console=true
     Run Keyword And Continue On Failure     List Should Contain Sub List    ${updatelog}    ${updatelogfiles}    msg=Files are missing
     :For    ${updatefiles}    IN    @{updatelogfiles}
     \    ${updatefilestatus}=    Run Keyword and Return Status    OperatingSystem.File Should Not Be Empty     ${updateUnzipPath}\\updatelogs\\${updatelogfiles[${N_groups}]}
     \    Run Keyword If    '${updatefilestatus}' == 'True'    Log    The File ${N_groups} : ${updatelogfiles[${N_groups}]} is present in ${PDpath}\\update\\updatelogs Directory      console=True
     \    ...    ELSE IF    '${updatefilestatus}' == 'False'     Run Keyword And Continue On Failure    Fail      msg= The File ${updatelogfiles[${N_groups}]} has no data in it.
     \    ${N_groups}=    Evaluate    ${N_groups} + 1

Extract audit log and veify if audit log file exist
    [Documentation]  Extract auditlog and audit log should exist with data init
    Extract tar file in preview dump    ${auditUnzipPath}    audit.tar.gz
    Open OVSSH Connection And Log In    ${ssh_cred['username']}    ${ssh_cred['password']}
    @{auditlogfile}=    SSHLibrary.List Files In Directory    /ci/data/logs/audit
    @{audit}=    OperatingSystem.List Directory    ${auditUnzipPath}\\\ci\\data\\logs\\audit
    Lists Should Be Equal    ${audit}    ${auditlogfile}    msg=doesnt have all the audit log files in preview dump
    ${status}=    Run Keyword and Return Status    OperatingSystem.File Should Not Be Empty    ${auditUnzipPath}\\\ci\\data\\logs\\audit\\${audit[0]}
    Run Keyword If    '${status}' == 'True'    Log    \nAudit Log is available in preview dump    console=True
    ...    ELSE IF    '${status}' == 'False'    Fail     Audit Log is empty in preview dump     console=true

Decrypt Support dump
    [Documentation]  preview dump should be decrypted
    [Arguments]    ${DecryptorPath}    ${SourcefilePath}
    @{GetDumpFile}=    OperatingSystem.List Files In Directory    ${SourcefilePath}    ci*.sdmp
    ${count}=    Get length    ${GetDumpFile}
    Run Keyword If    '${count}' > '1' or '${count}' == '0'    Fail    No files or More than one dump files found
    ${fetchtarfilename}    Remove String    ${GetDumpFile[0]}    \x00    .sdmp
    ${sdmptar}=    Set Variable    ${fetchtarfilename}-DECRYPTED.tar.gz
    ${filename}=    Join Path    ${SourcefilePath}    ${GetDumpFile[0]}
    ${rc}    ${output} =    Run and Return RC and Output    ${DecryptorPath}\\decrypt-support-dump.bat ${filename}
    log    ${output}    console=true
    [Return]    ${sdmptar}

Decrypt and extract preview dump
    [Documentation]  preview dump should be decrypted and extracted
    ${sdmptar}=    Decrypt Support dump    ${decryptor_path}    ${PDpath}
    ${dumpextractstatus}=    Run Keyword and Return Status    extract zip file    ${PDpath}\\${sdmptar}    ${PDpath}
    Run Keyword If    '${dumpextractstatus}' == 'True'    Log    \n Decryption and extraction of support dump is successfull    console=True
     ...    ELSE IF    '${dumpextractstatus}' == 'False'    Fail    \n Decryption or extraction of support dump failed     console=True

Extract messages.tar messages log file in appliance should exist
    [Documentation]  Extract messages and verifies none of the files are empty
     Extract tar file in preview dump    ${messagesUnzipPath}    messages.tar.gz
    @{messages}=    OperatingSystem.List Directory    ${messagesUnzipPath}\\messages
    :FOR    ${msgfiles}    IN    @{messages}
    \    ${msgstatus}=    Run Keyword and Return Status    OperatingSystem.File Should Not Be Empty     ${messagesUnzipPath}\\messages\\${msgfiles}
    \    Run Keyword If    '${msgstatus}' == 'True'    Log    \n The File ${msgfiles} contains data in it      console=True
    \    ...    ELSE IF    '${msgstatus}' == 'False'    Run Keyword And Continue On Failure    Fail    msg= The File ${msgfiles} has no data in it.