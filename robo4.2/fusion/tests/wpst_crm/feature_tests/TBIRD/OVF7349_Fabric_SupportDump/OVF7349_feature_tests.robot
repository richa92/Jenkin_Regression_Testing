*** Settings ***
Documentation    OVF7349 Support Dump for Composable Rack at Fabric Level
...
...    - Goal:
...      |  - Test the following:
...      |  \ \ - Fabric dump request body 'errorCode' validation Negative test
...      |  \ \ \ \ - length greater than 10
...      |  \ \ \ \ - errorCode length 0
...      |  \ \ \ \ - errorCode not provided
...      |  \ \ \ \ - unsupported character: need to be alphanumeric and hyphen, sample test _
...      |  \ \ - Create the encrypted and non-encrypted Fabric support dump
...      |  \ \ \ \ - use errorCode with max length and supported character set
...      |  \ \ - Can download and save the support dump
...      |  \ \ - Can expand and analyze the support dump
...      |  \ \ \ \ The non-encrypted support dump will be unpacked and ensure the following are collected
...      |  \ \ \ \ - OneView Appliance support dump
...      |  \ \ \ \ - CFM support bundles
...
...    - Usage:
...      |  - full test:
...      |  \ \ - robot -V data_OVF7349.py -T -d <ResultDir> OVF7349_feature_tests.robot
...      |  - skip precondition setup: robot -V data_OVF7349.py -v skipSetup:True
...      |  \ \ \ \ -T -d <ResultDir>  OVF7349_feature_tests.robot
...      |  - run tagged cases: robot -V data_OVF7349.py -i CRDLUnEncrypt -i Analyze
...      |  \ \ \ \ -T -d <ResultDir>  OVF7349_feature_tests.robot
...
...    - Environment:
...      |  - Plexxi Rig with 1 or more racks, each rack contains 2 plexxi switches and 2 DL servers
...      |  - OneView 5.00
...      |  - CFM (Plexxi Connect)
...      |  \ \ Note:
...      |  \ \ - CFM is deployed by tools stop after DISCOVER_FABRIC
...      |  \ \ - test set up
...      |  \ \ \ \ - enable Composable Cloud Integration Set in CFM
...      |  \ \ \ \ - Integrate OneView to CFM
...      |  \ \ \ \ - Claim Fabric in OneView
...

Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FC_Nitro_OVF3323/DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py

Suite Setup      Suite Precondition Setup
Suite Teardown   Suite Min Teardown

# Setup for each test case
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${skipSetup}    ${False}
${FABRIC_URI}    None
${FABRIC_SD_FILEPATH}    None


*** Test Cases ***
OVF7349 Negative SupportDump errorCode verification
    [Tags]    Negative
    [Documentation]    The following are tested that violoate the errorCode requirement
    ...                no errorCode provided
    ...                errorCode empty string
    ...                errorCode length > 10 characters
    ...                errorCode unsupported characters

    Log    ${\n}Fabric dump errorCode negative test    console=True
    :FOR    ${err_rb}    IN    @{err_rb_list}
    \    ${resp} =    Fusion Api Create Fabric Support Dump    ${FABRIC_URI}    ${err_rb['rb']}
    \    Should Be Equal As Integers    ${resp['status_code']}    400
    \    Should Be Equal As Strings    ${resp['errorCode']}     ${err_rb['exp_error']}


OVF7349 Create Unencrypted Fabric Support Dump and Download as Local File
    [Documentation]    Create Fabric support dump and download as local file
    [Tags]    CRDLUnEncrypt

    Log    ${\n}Perform Fabric Unencrypted support dump    console=True

    Create and Download Fabric Support Dump    ${FABRIC_SD_UNENCRYPT_RB}


OVF7349 Analyze Unencrypted Fabric Support Dump
    [Documentation]    Analyze the Fabric dump downloaded file to ensure OneView Appliance log
    ...                and CFM support bundles are collected
    [Tags]    Analyze

    Log    ${\n}unpack the download file ${FABRIC_SD_FILEPATH}    console=True

    # rename the file with '.gz' suffix, so it can be unzipped
    ${file_no_ext}    ${ext} =    Split Extension    ${FABRIC_SD_FILEPATH}
    ${renamed_file} =    Catenate    SEPARATOR=.    ${file_no_ext}    gz
    Move File     ${FABRIC_SD_FILEPATH}    ${renamed_file}

    Log    ${\n}unzipped the renamed dump file ${renamed_file}    console=True
    ${rc} =    Run and Return RC    gunzip ${renamed_file}
    Should Be Equal As Integers    ${rc}    0    msg=gunzip ${renamed_file} failed with rc ${rc}

    # after gunzip, the file is without the suffix
    ${rc}    ${output} =    Run and Return Rc and Output    tar -tvf ${file_no_ext}
    Should Be Equal As Integers    ${rc}    0    msg=untar with tvf option failed with rc ${rc}

    Log    ${\n}check the tar file content for OV appliance log and CFM bundles    console=True
    # Should Contain   ${output}   ${OV_APPLIANCE_DIR}   msg=dump does not contain OneView appliance dir
    Should Contain   ${output}   ${OV_APPLIANCE_LOG}   msg=dump does not contain OneView appliance log
    # Should Contain   ${output}   ${CFM_DUMP_DIR}   msg=dump does not contain CFM support bundles directory
    Should Match    ${output}    ${CFM_LOG_PATTERN}    msg=dump does not contain CFM support bundles


OVF7349 Create Encrypted Fabric Support Dump and Download as Local File
    [Documentation]    Create Fabric support dump and download as local file
    [Tags]    CRDLEncrypt

    Log    ${\n}Perform Fabric Encrypted support dump    console=True

    Create and Download Fabric Support Dump    ${FABRIC_SD_ENCRYPT_RB}


*** Keywords ***
Login OV
    [Documentation]    Login to OneView
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance    ${appliance_ip}    ${admin_credentials}

Common Test Setup
    [Documentation]    Pre-condition keyword run before each test case
    # Run Keyword and Ignore Error    Write To ciDebug Log
    Login OV
    ${resp} =    Run Keyword If    '${FABRIC_URI}' == 'None'     Fvt Api Get Fabric By Name    ${Fabric_name}
    Run Keyword If    '${FABRIC_URI}' == 'None'    Set Suite Variable    ${FABRIC_URI}    ${resp['uri']}

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    # Pass Execution
    fusion api logout appliance

Suite Precondition Setup
    [Documentation]    Suite Pre-condition setup run before suite start
    ...                - Integrate OneView to Plexxi connect, with Plexxi Fabric info pushed to OneView
    ...                - Claim Plexxi Fabric in OneView

    Remove Files    ${SD_DIR}/*${UNENCRYPT_ERRCODE}*    ${SD_DIR}/*${ENCRYPT_ERRCODE}*

    Return from keyword if    ${skipSetup}    is    ${True}

    Login OV

    Enable Composable Cloud Integration Set in CFM

    Integrate OneView To CFM

    Claim Composable Rack Fabric In OneView

    ${FABRIC_URI} =     FVT API Get Fabric by Name    ${Fabric_name}


Suite Min Teardown
    [Documentation]    Suite Post-condtion cleanup
    Pass Execution    Nothing to cleanup right now
    # fusion api logout appliance


Create and Download Fabric Support Dump
    [Documentation]    Create Fabric support dump and download as local file
    [Arguments]    ${request}

    Log    ${\n}Perform Fabric support dump    console=True

    ${resp} =    Fusion Api Create Fabric Support Dump    ${FABRIC_URI}    ${request}
    ${task} =    Wait For Task    ${resp}    ${FABRIC_DUMP_WAIT}    30s
    Should Be Equal As Strings    ${task['taskState']}    Completed

    # Retieve the supportdump uri
    ${supportDumpUri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri

    ${sdName} =    Fetch From Right    ${supportDumpUri}     /
    ${sdFullPath} =    Catenate    SEPARATOR=/    ${SD_DIR}    ${sdName}

    Log    ${\n}download Fabric support dump to local ${sdFullPath}    console=True
    ${resp} =    Fusion Api Download Fabric Support Dump    ${supportDumpUri}    ${sdFullPath}
    Should Be Equal As Integers    ${resp['status_code']}    200
    ...                            msg=Failed to download Fabric dump ${supportDumpUri}
    File Should Not Be Empty    ${sdFullPath}

    # set to Suite Variable only when all are successful
    Set Suite Variable    ${FABRIC_SD_FILEPATH}    ${sdFullPath}


# Set up
Enable Composable Cloud Integration Set in CFM
    [Documentation]   Enable composable cloud integration set in Composable Fabric Manager

    Log    ${\n}Add Composable Cloud Integration Set to CFM    console=True

    Plexxi Api Login    ${cfm_ip}    ${cfm_credentials['userName']}    ${cfm_credentials['password']}

    ${resp} =    Plexxi Api Enable Composable Cloud Integration Set

    ${status_code} =    Set Variable     ${resp['status_code']}

    # if integration set is already enabled, re-enable is forbideen and will get http status 403
    Return from Keyword if    '${status_code}' == '200'
    Return from Keyword if    '${status_code}' == '403'

    Fail    Failed enabling Integration Set status: ${status_code}


Integrate OneView To CFM
    [Documentation]    Integrate OneView To Plexxi Connect

    Log    ${\n}Integrate OneView to CFM    console=True

    Plexxi Api Login    ${cfm_ip}    ${cfm_credentials['userName']}    ${cfm_credentials['password']}
    ${task} =    Plexxi Api Add OneView Configuration    ${oneview_config}
    Should Be Equal As Integers    ${task['status_code']}    200

    Log    ${\n}Wait For Fabric ${Fabric_name} imported in OV as Unmanaged    console=True

    Wait For Fabric State    ${Fabric_name}    Unmanaged


Claim Composable Rack Fabric In OneView
    [Documentation]    Claim The Fabric In OneView and wait for fabric switch to be Configured


    Log    ${\n}Claim Composable Rack Fabric in OneView    console=True

    ${resp} =    Fvt Api Get Fabric By Name    ${Fabric_name}
    ${resp1} =    Fusion Api Patch fabric    uri=${resp['uri']}    body=${fabric_claim_request}
    ${task} =    Wait for Task    ${resp1}    5m    20s
    Should Be Equal As Strings    ${task['taskState']}    Completed

    Log    ${\n}Wait for Fabric to be Configured ans switches imported   console=True
    Wait For Fabric State    ${Fabric_name}    Configured

    # It takes a while for switch to turn Configured after fabric is Configured
    Log    ${\n}Wait for imported fabric switches become Configured    console=True
    sleep   50s

    ${resp} =    Fusion Api Get Switches Without Ports
    ${count} =    Set Variable     ${resp['count']}
    Run Keyword If    ${count} == 0    FAIL    switches not added


    # It takes a while for switch to turn Configured after fabric is Configured
    :FOR    ${x}    IN RANGE    0    ${count}
    \    Run Keyword Unless    '${resp['members'][${x}]['state']}' == 'Configured'
    \    ...   FAIL   ${resp['members'][${x}]['name']} not in Configured state: ${resp['members'][${x}]['state']}
