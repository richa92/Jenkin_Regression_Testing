*** Settings ***
Documentation    OVF3323 FC on Nitro User Story
...              - Allowed Max FC (FA and DA combined) uplinksets on LI and LIG
...              - LIG with FC uplinksets (FA and DA combined) exceeding max allowed per ICM
...              - LI wth FC uplinksets (FA and DA combined) exceeding max allowed per ICM (A and Bside ICM)
...
...              robot -v data_max_us_rd.py -T -d <result_dir> OVF3323_max_us_tests.robot
...              robot -v data_max_us_ha.py -T -d <result_dir> OVF3323_max_us_tests.robot
...
...              run selected tagged tests, e.g.,
...              robot -v data_max_us_ha.py -i FC -i ExceedMaxLigUS -T -d <result_dir> OVF3323_max_us_tests.robot


# Variables        ./data_common.py
# Variables        ./data_max_us_rd.py

Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ./DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py

# Setup for each test case
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***

*** Test Cases ***
OVF3323 Create FabricAttach and DirectAttach Networks
    [Tags]  FC
    Add FC Networks from variable    ${fanetworks}
    Add FC Networks from variable    ${danetworks}


OVF3323 LIG Exceeding Max FC Uplinksets per ICM Error Check
    [Tags]  ExceedMaxLigUS
    [Documentation]    Create LIG with FC uplinksets exceeding max allowed per ICM on Aside
    ...                Create LIG with 16 FC uplinksets on Aside,
    ...                Expect taskError errorCode CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY

    Log    ${\n}Create LIG with FC uplinksets exceeding max allowed per ICM    console=True
    ${body} =    Build LIG body    ${ligs['LIG-MAX-US-ERR1']}
    ${task} =    Fusion Api Create LIG    ${body}
    ${resp} =    Wait for Task2    ${task}    2m    5
    ...                                       PASS=Error
    ...                                       errorMessage=CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY


OVF3323 LIG Exceeding Max FC Uplinksets per LI Error Check
    [Tags]  ExceedMaxLigUS
    [Documentation]    Create LIG with total FC uplinksets exceeding max allowed (30) per LI with 2 ICMs
    ...                Create LIG with 15 FC uplinksets on Aside, and 16 FC uplinksets on Bside
    ...                Expect taskError errorCode CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY


    ${body} =    Build LIG body    ${ligs['LIG-MAX-US-ERR2']}
    Log    ${\n}Create LIG with FC uplinksets exceeding max allowed    console=True
    ${task} =    Fusion Api Create LIG    ${body}
    ${resp} =    Wait for Task2    ${task}    2m    5
    ...                                       PASS=Error
    ...                                       errorMessage=CRM_MAX_FC_NETWORKS_EXCEEDED


OVF3323 LIG with Max allowable FC uplinksets
    [Tags]  MaxLigUS
    [Documentation]    Create LIG with Max allowed FC uplinksets in LE with 2 ICMs

    # Create LIG with ME/HA or SE/Redundant with 15 FC (7DA and 8FA) uplinksets on each side
    Log    ${\n}Create LIG with max allowed FC uplinksets per ICM

    # this keyword Fail if task completes with Error
    ${task} =    Add LIG from variable    ${ligs['${LIG}']}


OVF3323 Add LE with Max allowable FC uplinksets, incuding FabricAttach and DirectAttach
    [Tags]  MaxLiUS
    [Documentation]    Create LE using LIG with Max allowed FC uplinksets per ICM
    ...                Note that not all uplnks are wired for FC so the LI status is not OK
    ...                Ensure ICMs are Configured after LE is created

    Log    ${\n}Create 2 frame LE with max allowed FC uplinksets per ICM    console=True
    ${resp} =    Add Enclosure Group from variable    ${enc_group['${EG}']}

    ${task} =    Add Logical Enclosure from variable    ${les['${LE}']}

    Log     ${\n}Verify Both Nitro in Configured state        console=True
    Verify Named Interconnect     ${NITROA}    state=Configured
    Verify Named Interconnect     ${NITROB}    state=Configured

    Verify Logical Interconnect    ${LI}    consistencyStatus=CONSISTENT
    Verify Named Logical Enclosure    ${LE}    state=Consistent


OVF3323 Exceeding Max LI FC Uplinksets on Aside ICM Error checking
    [Tags]  ExceedMaxLiUSA    ExceedMaxLiUS
    [Documentation]    Create LI uplinkset exceeding max uplinkset per interconnect
    ...                Create 16th LI uplinksets on IC3; expect error
    ...                httpstatus 400 and OV errorCode CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY

    ${li_uri} =    Get LI URI    ${LI}

    Log    ${\n}Exceed max allowed FC uplinksets on Aside in LE HA    console=True

    ${us} =     Copy Dictionary    ${li_add_uplinkset1}
    ${body} =    Build US body    ${us}    ${li_uri}
    ${resp} =    Fusion Api Create Uplink Set    body=${body}
    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    Should Be Equal As Strings    ${resp['errorCode']}    CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY
    Should Match Regexp    ${resp['message']}    ${MSG_CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY}


OVF3323 Exceeding Total Max LI FC Uplinksets on Bside ICM Error checking
    [Tags]  ExceedMaxLiUSB     ExceedMaxLiUS
    [Documentation]    Create LI uplinkset exceeding max uplinkset per interconnect
    ...                Create 16th LI uplinksets on IC6; expect error
    ...                httpstatus 400 and OV errorCode CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY


    Log    ${\n}Exceed max allowed FC uplinksets on Bside in LE HA    console=True
    ${li_uri} =    Get LI URI    ${LI}

    ${us} =     Copy Dictionary    ${li_add_uplinkset2}
    ${body} =    Build US body    ${us}    ${li_uri}
    ${resp} =    Fusion Api Create Uplink Set    body=${body}
    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    Should Be Equal As Strings    ${resp['errorCode']}    CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY
    Should Match Regexp    ${resp['message']}    ${MSG_CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY}


*** Keywords ***
Login OV
    [Documentation]    Login to OneView
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance    ${appliance_ip}    ${data_common.admin_credentials}

Common Test Setup
    [Documentation]    Pre-condition keyword run before each test case
    # Run Keyword and Ignore Error    Write To ciDebug Log
    Login OV

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    # Pass Execution
    fusion api logout appliance