*** Settings ***
Documentation                   Resource file for keywords to validate Oops Feature in OV
Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json
Library                         SSHLibrary
Library                         tests.ovs.OvsLibrary
Resource                        ../../wpst_crm/ci_fit/tests/robustness/resources/common.robot
Resource                        ../../cim/ui/Resource/CIM_CommonResource.txt
Resource                        ../../cim/ui/Resource/CIM_SupportDump.txt
Resource                        ../../cim/ui/Resource/CIM_Appliance.txt
Resource                        support_resource1.txt
Library                         RoboGalaxyLibrary\\utilitylib\\file_utils.py
Variables                       Supportool_data.py
Variables                       ../../../FusionLibrary/ui/business_logic/general/base_elements.py
Variables                       ../../../FusionLibrary/ui/general/login_elements.py
Variables                       ../../../FusionLibrary/ui/settings/settings_elements.py

*** Variables ***
${SSH_HOST}                  15.212.144.163
${ApplianceUrl}              https://${SSH_HOST}
${DataFile}                  E:\\Robo-OVS-new\\fusion\\tests\\ovs\\MAT-I\\ui.xml
${SeleniumSpeed}             1.0
${Browser}                   ff
${controller_state}          ERROR
${controller_state_msg}      manual

*** Keywords ***
Update Controller State
    [Documentation]     Edit file /var/www/html/controller-state.json
    [Arguments]    ${state}    ${msg}    ${source}=/var/www/html/controller-state.json    ${cmd}=/ci/bin/set-controller-state --state ${state} --message ${msg}
    ...    ${key}=state
    Open SSH and API
    ${controller_state}=    Execute Command    ${cmd}    return_stderr=True    return_rc=True
    ${controller_state2}    ${stderr}    ${rc}=    Execute Command    cat ${source}    return_stderr=True    return_rc=True
    ${controller_state3}=    Get Regexp Matches    ${controller_state2}    ${state}
    Run Keyword If    '${controller_state3[0]}'=='${state}'    Log    Appliance State Changed Successfully : ${controller_state2}    console=true
    ...       ELSE    Run Keyword And Continue On Failure    FAIL   Failed to change state in appliance!
    #Should Be Empty    ${stderr}                 msg=Error returned: ${rc} ${stderr}
    Should Be Equal As Integers    ${rc}    0    msg=non-zero return code ${rc}

Check Error Summary In OOPS Page
    [Documentation]    Verifies the Error Summary details section on OOPS page
    [Arguments]    ${Administrator_Username}    ${Administrator_Password}

    wait for element and click    ${FusionSettingsPage.ID_OOPS_DETAILS_BTN}    50
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_INPUT_OOPS_DETAILS_USERNAME}
    Input Text    ${FusionSettingsPage.ID_INPUT_OOPS_DETAILS_USERNAME}    ${Administrator_Username}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_INPUT_OOPS_DETAILS_PASSWORD}
    Input Text    ${FusionSettingsPage.ID_INPUT_OOPS_DETAILS_PASSWORD}    ${Administrator_Password}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_BTN_OPEN_ERRORSUMMARY_OK}
    Click Element    ${FusionSettingsPage.ID_BTN_OPEN_ERRORSUMMARY_OK}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_ERRORSUMMARY_LABEL}
    Click Element    ${FusionSettingsPage.ID_ERRORSUMMARY_LABEL}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_SYSTEM_RESOURCES_LABEL}
    Capture Page Screenshot
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_SYSTEMSUMMARY_TEXT}
    ${response}    Get Text    ${FusionSettingsPage.ID_SYSTEMSUMMARY_TEXT}
    Run Keyword And Continue On Failure    Should Not Be Empty    ${response}    SYSTEM RESOURCES ELEMENT HAS EMPTY OUTPUT
    Log    PERCENTAGE OF SYSTEM RESOURCES USED:-    console=true
    Log    \n${response}    console=true
    # GET LAST 5 ACTIONS FROM THE LOGS
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_ACTIONLIST_TEXT}
    ${response1}    Get Text    ${FusionSettingsPage.ID_ACTIONLIST_TEXT}
    Run Keyword And Continue On Failure    Should Not Be Empty    ${response1}    THE LAST 5 ACTIONS HAS EMPTY OUTPUT
    Log    THE LAST 5 ACTIONS ARE:-    console=true
    Log    \n${response1}    console=true
    # GET THE PROBABLE ROOT CAUSE OF THE ERROR IN ONEVIEW
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_ROOTCAUSE_TEXT}
    ${response2}    Get Text    ${FusionSettingsPage.ID_ROOTCAUSE_TEXT}
    Run Keyword And Continue On Failure    Should Not Be Empty    ${response2}    PROBABLE ROOT CAUSE HAS EMPTY OUTPUT
    Log    PROBABLE ROOT CAUSE :-    console=true
    Log    \n${response2}    console=true

List Files in backup staging folder
    [Documentation]    Returns the filename of the support dump or backup file in backup staging folder
    [Return]    ${Filename}
    ${username}=    Set Variable    ${TestData.RootUserCredentials[0].username}
    ${password}=    Set Variable    ${TestData.RootUserCredentials[0].password}
    Log    uname:${username}
    Log    pwd:${password}
    ${command_to_list_backupstagingfolder_contents}=    Set Variable    cd /;cd backup_staging;ls
    ${output}=    Execute Command on Remote VM    ${SSH_HOST}    ${username}    ${password}    ${command_to_list_backupstagingfolder_contents}
    ${backup_filename}=    Get Lines Containing String    ${output}    .bkp
    ${command_to_list_supportdumpfolder_contents}=    Set Variable    cd /;cd backup_staging;cd support-dumps;ls
    ${output}=    Execute Command on Remote VM    ${SSH_HOST}    ${username}    ${password}    ${command_to_list_supportdumpfolder_contents}
    ${supportdump_filename}=    Get Lines Containing String    ${output}    .sdmp
    ${Filename}=    Set Variable    ${backup_filename}${supportdump_filename}

Support dump creation in OOPS page
    [Documentation]    Creating support dump in oops page and validating the file name change in staging directory
    [Arguments]    ${Default_Administrator_Username}    ${Default_Administrator_Password}
    #Enter credentials to create support dump
    ${Content_In_BackupStagingFolder_BeforeCreateSD}=    List Files in backup staging folder
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_LINK_CREATESUPPORTDUMP}
    Click Element    ${FusionSettingsPage.ID_LINK_CREATESUPPORTDUMP}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_INPUT_CREATESUPPORTDUMP_USERNAME}
    Input Text    ${FusionSettingsPage.ID_INPUT_CREATESUPPORTDUMP_USERNAME}    ${Default_Administrator_Username}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_INPUT_CREATESUPPORTDUMP_PASSWORD}
    Input Text    ${FusionSettingsPage.ID_INPUT_CREATESUPPORTDUMP_PASSWORD}    ${Default_Administrator_Password}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_BUTTON_CREATESUPPORTDUMP_OK}
    Click Element    ${FusionSettingsPage.ID_BUTTON_CREATESUPPORTDUMP_OK}
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_TEXT_SUPPORTDUMP_PROGRESS_NOTIFICATION}    10
    Wait Until Element Is Not Visible    ${FusionSettingsPage.ID_TEXT_SUPPORTDUMP_PROGRESS_NOTIFICATION}    360
    ${Is_Ok_Status_Displayed}    ${error_or_return_value}=    Run Keyword And Ignore Error    Wait Until Element Is Visible    ${FusionSettingsPage.ID_OOPS_DETAILS_BTN}    10
    Run Keyword If    '${Is_Ok_Status_Displayed}'=='PASS'    Log    Support dump was created successfully!    WARN
    ...    ELSE    Fail    Create support dump failed!
    ${Content_In_BackupStagingFolder_AfterCreateSD}=    List Files in backup staging folder
    ${SupportDump_Filename}=    Set Variable If    '${Content_In_BackupStagingFolder_BeforeCreateSD}'!='${Content_In_BackupStagingFolder_AfterCreateSD}'    ${Content_In_BackupStagingFolder_AfterCreateSD}    ${EMPTY}
    ${File_Location}=    Set Variable    ${SupportDump_Filename}
    Run Keyword If    '${File_Location}'=='${Content_In_BackupStagingFolder_AfterCreateSD}'    Log    Support dump file verified successfully on Appliance    WARN
    ...    ELSE    Fail    Support dump file verification failed


Check Restart Link in Oops Page
    [Documentation]    Induce Restart on OOPS page and validate if the appliance comes up healthy

    Reload page
    Wait Until Element Is Visible    ${FusionSettingsPage.ID_LINK_RESTART_ERRORPAGE}    60
    Click Element    ${FusionSettingsPage.ID_LINK_RESTART_ERRORPAGE}
    Wait Until Element Is Visible    //*[text()='Starting']    180
    # Click Element    ${FusionSettingsPage.ID_LINK_RESTART_ERRORPAGE}
    Reload page
    Log    Restart link clicked    WARN
    # Reload page
    ${IsApplianceStarting} =    Is Starting page displayed?    600    60
    Run Keyword If    '${IsApplianceStarting}'=='YES'    Log    Starting page displayed.    WARN
    ...       ELSE    FAIL
    ${IsApplianceIDLE} =    Is appliance in IDLE state?    1200    20
    Run Keyword If    '${IsApplianceIDLE}'=='YES'    Log    Appliance restart completed successfully!    WARN
    ...       ELSE    FAIL