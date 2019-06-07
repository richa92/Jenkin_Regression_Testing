*** Settings ***
Documentation       Download  OneView Support Dumps
Library                FusionLibrary
Library              BuiltIn
Library                Collections
Library             json
Library              Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables             ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}        16.114.209.223
${DATA_FILE}        Regression_Data.py
${VERIFY}            ${FALSE}

*** Test Cases ***
Login the Users
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Create and Download LE Support dump
    ${LE_SD_NAME_LOCATION}=     Create Support name and location  ${OUTPUT_DIR}    LE
    ${LE_URI}=    Get Logical Enclosure URI    ${LE_NAME}
    ${LE_URI}=    Remove String    ${LE_URI}    '
    ${LE_URI}=    Run Keyword If    '${LE_URI}'=='/rest/Logical_Enclosure_${LE_NAME}_not_found'     Get Logical Enclosure URI    ${LE_NAME_NEW}   ELSE    Get Variable Value    ${LE_URI}
    ${le_ID}=    Remove String Using Regexp    ${LE_URI}    /rest/logical-enclosures/
    Convert to String    ${le_ID}
    ${task_uri}=    Create LE Support Dump    ${LE_support_dump}    ${le_ID}
    ${task} =  Fusion Api Get Task  uri=${task_uri}
    Wait For Task2  ${task}  timeout=1200  interval=10
    ${task} =  Fusion Api Get Task  uri=${task_uri}
    Log variables
    ${associatedResource}=     Get From Dictionary     ${task}    associatedResource
    ${ledumpUri}=     Get From Dictionary     ${associatedResource}    resourceUri
    Log    Downloading LE support dump to ${LE_SD_NAME_LOCATION}    console=true
    ${respdownload} =     Fusion Api Download Support Dump    ${ledumpUri}   ${LE_SD_NAME_LOCATION}
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '${STATUS_CODE}'    msg=Verification of status_code in downloading LE support dumps has FAILED    values=False

Create and Download CI Support dump
    ${SD_NAME_LOCATION}=    Create Support name and location  ${OUTPUT_DIR}    CI
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}  
    ${respdownload} =     Fusion Api Download Support Dump    ${dump_uri}   ${SD_NAME_LOCATION}
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '${STATUS_CODE}'    msg=Verification of status_code in downloading CI support dumps has FAILED    values=False

*** Keywords ***

Create LE Support Dump
    [Documentation]    Creates LE support dump in a bactch one after the other on one view appliance. Input is a list of dictionary for various users to create.
    [Arguments]      ${LE_support_dump}     ${le_id}   ${VERIFY}=${FALSE}   ${STATUS_CODE}=200
    ${resp} =     fusion api get logical enclosure support dump    ${LE_support_dump}     ${le_id}
    ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${resp['headers']}  location
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${resp['status_code']}'   '${STATUS_CODE}'    msg=Verification of status_code in create support dumps response body has FAILED    values=False
    Run keyword if    '${VERIFY}'=='True' and '${resp['status_code']}' == '${STATUS_CODE}'    Should Not Be Empty    ${task_uri}    msg=Verification of uri in create support dumps response body has FAILED
    Return From Keyword    ${task_uri}

Create Support name and location
    [Documentation]    Create Support name and location
    [Arguments]     ${OUTPUT_DIR}    ${sd_type}   ${VERIFY}=${FALSE}   ${STATUS_CODE}=200
    ${sd_name} =    Get Time
    ${sd_name} =    Catenate    SEPARATOR=-    ${sd_name}     ${sd_type}
    ${sd_name} =    Catenate    SEPARATOR=.    ${sd_name}    sdmp
    ${sd_name} =    Replace String Using Regexp    ${sd_name}    ( |:)    _
    ${sd_name} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${sd_name}
    Log    sd_name:${sd_name}    console=true
    [Return]    ${sd_name}
