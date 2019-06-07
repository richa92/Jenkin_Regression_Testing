*** Settings ***
Documentation   Capture Appliance Support Dump

Resource        ../resource.txt
Resource        ../plexxi.txt

Variables       ../${DATA_FILE}

Suite Setup        QUAL Suite Setup    ${admin_credentials}
Suite Teardown     QUAL Suite Teardown

*** Test Cases ***
Create and Download CI Support dump
    [Tags]    Test    99   CI_SD
    ${SD_NAME_LOCATION}=    Create Support name and location  ${OUTPUT_DIR}    CI
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}
    ${respdownload} =     Fusion Api Download Support Dump    ${dump_uri}   ${SD_NAME_LOCATION}
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '${OK}'    msg=Verification of status_code in downloading CI support dumps has FAILED    values=False

*** Keywords ***
Create Support name and location
    [Documentation]    Create Support name and location
    [Arguments]     ${OUTPUT_DIR}    ${sd_type}
    @{time} =    Get Time    year month day
    ${sd_name} =    Catenate    SEPARATOR=_    ${SD_PREFIX}    ${time[1]}    ${time[2]}    ${time[0]}     ${sd_type}
    ${sd_name} =    Catenate    SEPARATOR=.    ${sd_name}    sdmp
    ${sd_name} =    Replace String Using Regexp    ${sd_name}    ( |:)    _
    ${sd_name} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${sd_name}
    Log    sd_name:${sd_name}    console=true
    [Return]    ${sd_name}
