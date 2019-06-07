*** Settings ***

Resource    firmware_config.txt
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers


*** Test Cases ***

Login to appliance
    Set Log Level   TRACE
    Log Variables

    ${user}=    Get Data By Property    ${TestData.users}    name    Administrator
    Fusion UI Login to Appliance    ${user[0].name}

################# LE NEGATIVE TESTS ###########################################

1.NEGATIVE-ORCHESTRATED-DOWNGRADE FW update for LE--without force option-Shared Infrastructure
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware13}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware13}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg4}=    Convert To Lowercase    ${ExpectedErrorMsg4}
    ${ExpectedErrorMsg5}=    Convert To Lowercase    ${ExpectedErrorMsg5}
    ${ExpectedErrorMsg5_1}=    Convert To Lowercase    ${ExpectedErrorMsg5_1}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg4}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg5}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg5_1}    Expected Error Message Not seen

2.NEGATIVE-ORCHESTRATED-Same Version FW update for LE--without force option-Shared Infrastructure
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware16}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware16}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg1}=   Convert To Lowercase    ${ExpectedErrorMsg1}
    ${ExpectedErrorMsg2}=   Convert To Lowercase    ${ExpectedErrorMsg2}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg2}    Expected Error Message Not seen

3.Negative-PARALLEL-LE UPDATE Without Server Powered OFF-Shared INFRA
    fusion_ui_power_on_server_profile    @{TestData.CreateProfile}

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware1}

    ${Status}=    Convert To Lowercase    ${Status}
    ${expmsg}=    Catenate    ${ExpectedErrorMsg22}   ${TestData.CreateProfile[0].server}    ${ExpectedErrorMsg23}
    ${expmsg}=    Convert To Lowercase    ${expmsg}
    ${ExpectedErrorMsg24}=    Convert To Lowercase    ${ExpectedErrorMsg24}

    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${expmsg}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${ExpectedErrorMsg24}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware1}
    ${Status}=    Encode string to bytes    ${Status}    ASCII    errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${expmsg}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${ExpectedErrorMsg24}

    fusion_ui_power_off_server_profile    @{TestData.CreateProfile}


4.NEGATIVE-PARALLEL-Same Version FW update for LE--without force option-Shared Infrastructure

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware10}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware10}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg1}=   Convert To Lowercase    ${ExpectedErrorMsg1}
    ${ExpectedErrorMsg2}=   Convert To Lowercase    ${ExpectedErrorMsg2}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg2}    Expected Error Message Not seen

5.NEGATIVE-PARALLEL-Same Version FW update for LE--without force option-Shared Infrastructure and profiles

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware12}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware12}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg1}=   Convert To Lowercase    ${ExpectedErrorMsg1}
    ${ExpectedErrorMsg2}=   Convert To Lowercase    ${ExpectedErrorMsg2}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg2}    Expected Error Message Not seen

6.NEGATIVE-PARALLEL-Downgrade FW of LE--without force option-Shared Infrastructure
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware11}
    Log To Console    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware11}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg4}=    Convert To Lowercase    ${ExpectedErrorMsg4}
    ${ExpectedErrorMsg5}=    Convert To Lowercase    ${ExpectedErrorMsg5}
    ${ExpectedErrorMsg5_1}=    Convert To Lowercase    ${ExpectedErrorMsg5_1}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg4}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg5}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg5_1}    Expected Error Message Not seen


7.NEGATIVE-Refresh Enclosure and trigger FW update - UPdate fails with message- There is an ongoing operation on the resource
    fusion_ui_refresh_enclosure_by_name    ${TestData.firmware14.enclosure[0].name}    False
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware14}
    ${Status}=    Encode string to bytes    ${Status}    ASCII    errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg12}=    Convert To Lowercase    ${ExpectedErrorMsg12}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg12}    Expected Error Message Not seen

    fusion_ui_wait_for_enclosure_refresh_complete   ${TestData.firmware10.enclosure[0].name}

################# LI NEGATIVE TESTS ###########################################

1.NEGATIVE-PARALLEL-Staging to the baseline version for firmware update-same version-without Force

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[0]
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg}=    Catenate    ${expectedmsg1}    ${TestData.lifwnegative[0].LIname}
    ${expmsg}=    Convert To Lowercase    ${expmsg}
    ${expmsg}=    Encode string to bytes    ${expmsg}    ASCII   errors=ignore
    Should Contain    ${Status}    ${expmsg}

2.NEGATIVE-PARALLEL-Activate to the staged baseline tests(upgrade)-Nothing to activate

    ${Status}=    Run Keyword and Expect Error    *    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[1]
    ${Status}=    Encode string to bytes    ${Status}   ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg}=    Convert To Lowercase    ${expectedmsg2}
    should contain    ${Status}    ${expmsg}

3.NEGATIVE-PARALLEL-Update Firmware(Stage+Activate) test (upgrade)-same version-without force

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[2]
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg}=    Catenate    ${expectedmsg1}    ${TestData.lifwnegative[2].LIname}
    ${expmsg}=    Convert To Lowercase    ${expmsg}
    ${expmsg}=    Encode string to bytes    ${expmsg}    ASCII   errors=ignore
    Should Contain    ${Status}    ${expmsg}

4.NEGATIVE-ORCHESTRATED-Staging to the baseline version for firmware update-downgrade-without Force

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[3]
    Log To Console    ${Status}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}

    ${expectedmsg3}=    Convert To Lowercase    ${expectedmsg3}
    Should Contain    ${Status}    ${expectedmsg3}

5.NEGATIVE-ORCHESTRATED-Update Firmware(Stage+Activate) test (upgrade)-downgrade-without force

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[4]
    Log To Console    ${Status}
    ${Status}=    Encode string to bytes    ${Status}    ASCII   errors=ignore
    ${Status}=    Convert To Lowercase    ${Status}

    ${expectedmsg3}=    Convert To Lowercase    ${expectedmsg3}
    Should Contain    ${Status}    ${expectedmsg3}

2.Negative-PARALLEL-LE UPDATE Without Server Powered OFF-Shared INFRA and Profiles
    # UPDATE FIRMWARE
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware4}

    ${Status}=    Convert To Lowercase    ${Status}
    ${expmsg}=    Catenate    ${ExpectedErrorMsg25}   ${TestData.CreateProfile[0].name}    ${ExpectedErrorMsg26}
    ${expmsg}=    Convert To Lowercase    ${expmsg}
    ${ExpectedErrorMsg27}=    Convert To Lowercase    ${ExpectedErrorMsg27}

    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${expmsg}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${ExpectedErrorMsg27}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware4}
    ${Status}=    Convert To Lowercase    ${Status}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${expmsg}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   ${ExpectedErrorMsg27}

    fusion_ui_power_off_server_profile    @{TestData.CreateProfile}

8.NEGATIVE-PARALLEL-Reapply LI configuration and trigger FW update-UPdate fails with message-There is an ongoing operation on the resource

    fusion_UI_reapply_li_configuration_of_le    ${TestData.firmware14.lename}   false
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware14}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware14}
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg11_1}=    Convert To Lowercase    ${ExpectedErrorMsg11_1}
    ${ExpectedErrorMsg13}=    Convert To Lowercase    ${ExpectedErrorMsg13}
    ${ExpectedErrorMsg14}=    Convert To Lowercase    ${ExpectedErrorMsg14}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg13}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg14}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg11_1}    Expected Error Message Not seen

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3.enclosure[0].name}    500

########################## NON REDUNDANT LI _ LE UPGRADE ###########################################

CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS-FOR LI-2
    fusion_ui_delete_server_profile_by_name    ${TestData.CreateProfile[0].name}
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_delete_logical_enclosure    ${TestData.les[0]}

Create LE-MultiLI scenario testing-2
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_create_tbird_logical_enclosure    ${TestData.les[1]}
    Log To Console    ******CREATE LE operations completed**********

1.NEGATIVE--Non redundant MULTI LI-ORCHESTRATED-ORCHESTRATED-Update Firmware(Stage+Activate) test (upgrade-1

    ${Status}=    Run Keyword And Expect Error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[7]
    Log To Console    ${Status}

    ${Status}=    Convert To Lowercase    ${Status}
    ${expmsg1}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[7].LIname}    ${ExpectedErrorMsg18}

    ${expmsg1}=    Convert To Lowercase    ${expmsg1}
    ${ExpectedErrorMsg19}=    Convert To Lowercase    ${ExpectedErrorMsg19}
    ${ExpectedErrorMsg21}=    Convert To Lowercase    ${ExpectedErrorMsg21}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg19}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg21}    Expected Error Message Not seen

2.NEGATIVE--Non redundant MULTI LI-ORCHESTRATED-ORCHESTRATED-Staging followed by activation-2

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[8]
    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    Run Keyword and Expect Error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[9]
    Log To Console    ${Status}
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg1}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[8].LIname}    ${ExpectedErrorMsg18}

    ${expmsg1}=    Convert To Lowercase    ${expmsg1}
    ${ExpectedErrorMsg19}=    Convert To Lowercase    ${ExpectedErrorMsg19}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg19}    Expected Error Message Not seen

3.NEGATIVE--Non redundant MULTI LI-ORCHESTRATED-ORCHESTRATED-Update Firmware(Stage+Activate) test (upgrade)-2

    ${Status}=    Run Keyword And Expect Error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[10]
    Log To Console    ${Status}
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg1}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[10].LIname}    ${ExpectedErrorMsg18}

    ${expmsg1}=    Convert To Lowercase    ${expmsg1}
    ${ExpectedErrorMsg19}=    Convert To Lowercase    ${ExpectedErrorMsg19}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg19}    Expected Error Message Not seen

4.NEGATIVE-Non redundant MULTI LI-ORCHESTRATED-ORCHESTRATED-Staging followed by activation-1

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[5]
    Should Be Equal    '${Status}'    'True'    ${Status}

    ${Status}=    Run Keyword and Expect Error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.lifwnegative}[6]
    Log To Console    ${Status}
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg1}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[5].LIname}    ${ExpectedErrorMsg18}

    ${expmsg1}=    Convert To Lowercase    ${expmsg1}
    ${ExpectedErrorMsg19}=    Convert To Lowercase    ${ExpectedErrorMsg19}
    ${ExpectedErrorMsg21}=    Convert To Lowercase    ${ExpectedErrorMsg21}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg19}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg21}    Expected Error Message Not seen

5.NEGATIVE-Non redundant MULTI LI-ORCHESTRATED-Upgrade FW of LE-Shared Infrastructure

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware15}
    Log To Console    ${Status}
    
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedErrorMsg15}=    Convert To Lowercase    ${ExpectedErrorMsg15}
    ${ExpectedErrorMsg16}=    Convert To Lowercase    ${ExpectedErrorMsg16}
    ${ExpectedErrorMsg20}=    Convert To Lowercase    ${ExpectedErrorMsg20}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg15}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg16}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg20}    Expected Error Message Not seen

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY FOR MESSAGES********
    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware15}
    Log To Console    ${Status}
    ${Status}=    Convert To Lowercase    ${Status}

    ${expmsg1}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[6].LIname}    ${ExpectedErrorMsg18}
    ${expmsg2}=    Catenate    ${ExpectedErrorMsg17}   ${TestData.lifwnegative[7].LIname}    ${ExpectedErrorMsg18}

    ${expmsg1}=    Convert To Lowercase    ${expmsg1}
    ${expmsg2}=    Convert To Lowercase    ${expmsg2}
    ${ExpectedErrorMsg19}=    Convert To Lowercase    ${ExpectedErrorMsg19}
    ${ExpectedErrorMsg21}=    Convert To Lowercase    ${ExpectedErrorMsg21}

    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg1}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${expmsg2}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg19}    Expected Error Message Not seen
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedErrorMsg21}    Expected Error Message Not seen

