*** Settings ***
Documentation         DOWNLOADING SUPPORT DUMP FROM OneView Appliance
Resource              resource.txt
Suite Setup           Suite Setup
Suite Teardown        Suite Teardown

*** Test Cases ***
C7000 UPT Get Support Dumps Check Appliance State
    [Documentation]  Check appliance State
    ${state}=  Get Appliance State
    Run keyword if  '${state}'=='STARTING'  Wait Until Keyword Succeeds  60m  1s  Appliance State Should Match  ((?i)OK)
    Run keyword if  '${state}'=='UPGRADE'  Wait Until Keyword Succeeds  60m  1s  Appliance State Should Match  ((?i)OK)

C7000 UPT Get Support Dumps Create and Download CI Support dump
    [Documentation]    Support Dump Download from Appliance
    ${SD_NAME_LOCATION}=    Create Support name and location  ${LOG_DIR}    CI
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}
    ${respdownload} =     Fusion Api Download Support Dump    ${dump_uri}   ${SD_NAME_LOCATION}
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${respdownload['status_code']}'   '200'    msg=Verification of status_code in downloading CI support dumps has FAILED    values=False

C7000 UPT Get Support Dumps Download Database Dumps
    [Documentation]  Download the database dumps
    Download Database Dumps  ${LOG_DIR}

