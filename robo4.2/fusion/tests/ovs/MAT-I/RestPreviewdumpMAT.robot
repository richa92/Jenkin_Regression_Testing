*** Setting ***
Documentation    testcase file to validate the content of preview dump
Resource        PreviewDumpResource.robot

*** Test Cases ***

Preview Dump should be downloaded via REST api
   [Documentation]  Preview Dump should be downloaded to specified location
   [Tags]           TCPD
   Download Preview Dump via Rest api    ${PDpath}

preview dump should be decrypted and extracted
    [Documentation]  preview dump should be decrypted and extracted
    Decrypt and extract preview dump

Check if all the tar files exists in preview dump
    [Documentation]  audit,messages,sar,update,cidebug tar file should be present in preview dump
    Check if all the tar files exists in preview dump

Check if boot log, version and postgres command files are present
    [Documentation]  Boot,version,postgress file should be present in preview dump
    Boot log, version and postgres command files should exist

Appliance commands should be present in PD
    [Documentation]  All the appliance commands file should be present in preview dump
    appliance commands should be present in PD    ${PDpath}

Preview dump log verification
    [Documentation]  From support dump log verifies if all the appliance command are succesfully executed
    Preview dump log verification    ${PDpath}    ${CMD_LIST}

Extract update log and check all the file exist
    [Documentation]  Extracts update log, verifies if all files exist, verify if fixme install log content
    Extract update log and check all the file exist

Extract audit log and veify if audit log file exist
    [Documentation]  Extracts audit log
    Extract audit log and veify if audit log file exist

Extract messages.tar file and messeages file should exist
    [Documentation]  Extract messages.tar file in preview dump and checks if all the messages files exists
    Extract messages.tar messages log file in appliance should exist
