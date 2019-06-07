*** Settings ***
Documentation		Generate-Resource-Json.robot  -  Generate resource JSON data file into the specified ${dataFileDir} location
...                     Example workflow, generate a resource data and save it to /tmp/jason.json/jason.json:
...                     pybot -d /tmp/logs/Generate-Resource-Json.robot -LTRACE -vAPPLIANCE_IP:<OneView IP> -vdataFileDir:/tmp/jason.json -vFILENAME:jason.json Generate-Resource-Json.robot
...                     Required argument:
...                         -vAPPLIANCE_IP:[OneView IP Address]
...
...                     Optional argument:
...                         -vtbirdEnv:[True|False]: Set it to True for Synergy/t-bird env. False for C7000. Default will be script detecting your enclosure type.

Variables           ../resources/data_variables.py
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             Collections

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${FILENAME}                     None
${tbirdEnv}                     None
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
#@{AllResourcesList}             ic  ictype  uplinkset  li  servers  profiles
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  stackingDomainId

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

GenerateJson--Generate resource data variable file
    ${ovData} =   Get OneView Resources    ${AllResourcesList}   tbirdEnv=${tbirdEnv}
    ${FILENAME} =   Run Keyword If   "${FILENAME}" != "${null}"   Set Variable   ${FILENAME}
    ...             ELSE   Create Generated File Name
    Write JSONfile   ${ovData}  ${FILENAME}


*** Keywords ***
Create Generated File Name
    [Documentation]   Auto-generate a json file name.
    ${timestamp} =   Get Concatenated Timestamp
    ${testname} =   Fetch From Left   ${TEST_Name}  --
    ${generatedFileName} =   Set Variable   data-${testname}-${timestamp}.json
    [Return]   ${generatedFileName}
