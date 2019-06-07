*** Settings ***
Documentation		Compare-Json-Files.robot  -  Compare JSON data file against each other
...                     Example: Compare /tmp/file1.json against ./Appliance-Backup-Restore/dataFiles/golden-preBackup.json
...                     pybot -d /tmp/logs/Compare-Json-Files.robot -LDEBUG -vFILE1:/tmp/file1.json -vFILE2:./Appliance-Backup-Restore/dataFiles/golden-preBackup.json Compare-Json-Files.robot
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Library             Collections

*** Variables ***
${FILE1}                        None
${FILE2}                        None
${tbirdEnv}                     ${True}
${RESOLVE_NAME}                 ${False}
@{IGNORE_LIST}                  uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  remotePortDescription  remoteSystemDescription  interconnects_ADD_ports_15_portTypeExtended  interconnects_ADD_ports_15_connectorType  interconnectUri_ADD_ports_15_portTypeExtended  interconnectUri_ADD_ports_15_connectorType  settingId  optionId

*** Test Cases ***
Check FILE1
   Run Keyword If   "${FILE1}" == "${null}"   Fail   msg=FILE1 is not specified in the data variable file nor in the command line argument. Please define FILE1 variable.

Check FILE2
   Run Keyword If   "${FILE2}" == "${null}"   Fail   msg=FILE2 is not specified in the data variable file nor in the command line argument. Please define FILE2 variable.

Compare Json Files
    Set Log Level	TRACE
    Compare All with Expected    ${FILE1}   ${FILE2}   moreList=${IGNORE_LIST}   resolve_name=${RESOLVE_NAME}
