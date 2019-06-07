*** Settings ***
Documentation       CDT Performance - Upload Bin File into Appliance, Update Appliance with it and measure performance.
Library             Collections
Library             String
Resource            ../resource.txt
Resource            ../../../../Resources/api/settings/appliance_networking.txt

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Test Cases ***
Upgrade OneView Appliance
    [Tags]    UPGRADE_OV    performance
    ${update_bin_filename}    fetch from right    ${UPGRADE_BIN_FILE_WEB_URL}    /
    Fusion Api Download Upgrade File
    ...         ${UPGRADE_BIN_FILE_WEB_URL}
    ...         ${update_bin_filename}
    Log    Uploading the upgrade bin file: ${update_bin_filename} ...  console=True
    ${Response}=                    Fusion Api Upload Appliance Firmware
    ...                             ${update_bin_filename}
    Should Be Equal As Integers   ${Response['status_code']}  200

    Login to Fusion Via SSH
    ${existing_version} =        Get OneView Version
    Log    Upgrade from : ${existing_version}    console=True

    Log    Upgrading Appliance...    console=True
    ${Response}=                    Fusion Api Upgrade Appliance Firmware
    ...                             ${update_bin_filename}
    ${initiated_time}=      Get Current Time                Initiated Upgrade

    Log    Waiting for OneView state to change to "UPGRADE"    console=True
    Wait For Appliance State To Be Expected State    ExpectedState=UPGRADE    timeout=20 mins      interval=5 s
    Log    Waiting for OneView state to change to "OK"  console=True
    Wait For Appliance State To Be Expected State    ExpectedState=OK    timeout=150 mins    interval=60 s

    ${completed_time}=      Get Current Time                Completed Upgrade
    ${upgrade_time}=    Get Time Duration    ${initiated_time}    upgrade_state_time
    Login to Fusion Via SSH
    ${new_version} =        Get OneView Version
    Log    Upgrade to : ${new_version}    console=True

    ${old_ov_version}    fetch from left    ${existing_version}    ,
    ${new_ov_version}    fetch from left    ${new_version}    ,
    Run keyword if    '${new_ov_version}'=='${old_ov_version}'    FAIL    Upgrade failed and reverted the OV to existing version.

    ${payload}=         Create Dictionary
    Set To Dictionary   ${payload}
    ...                 UPGRADE_FROM    ${existing_version}
    ...                 UPGRADE_TO    ${new_version}
    ...                 UPGRADE_START_TIME    ${initiated_time}
    ...                 UPGRADE_END_TIME    ${completed_time}
    ...                 UPGRADE_TIME    ${upgrade_time}
    Post Data to ELK    ${cdt-ci-upgrade_elk_index}     ${payload}
