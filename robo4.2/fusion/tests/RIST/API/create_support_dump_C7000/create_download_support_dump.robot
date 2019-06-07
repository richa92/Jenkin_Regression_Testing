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
${VERIFY}            ${FALSE}

*** Test Cases ***
Login the Users
    [Documentation]    Login the Users
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Create and Download CI Support dump
    [Documentation]    Create and Download CI Support dump
    ${SD_NAME_LOCATION}=    Create Support name and location  ${OUTPUT_DIR}    CI
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}
    ${respdownload} =     Fusion Api Download Support Dump    ${dump_uri}   ${SD_NAME_LOCATION}
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '${STATUS_CODE}'    msg=Verification of status_code in downloading CI support dumps has FAILED    values=False

*** Keywords ***
Create Support name and location
    [Documentation]   Create Support name and location
    [Arguments]     ${OUTPUT_DIR}    ${sd_type}   ${VERIFY}=${FALSE}   ${STATUS_CODE}=200
    ${sd_name} =    Get Time
    ${sd_name} =    Catenate    SEPARATOR=-    ${sd_name}     ${sd_type}
    ${sd_name} =    Catenate    SEPARATOR=.    ${sd_name}    sdmp
    ${sd_name} =    Replace String Using Regexp    ${sd_name}    ( |:)    _
    ${sd_name} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${sd_name}
    Log    sd_name:${sd_name}    console=true
    [Return]    ${sd_name}

