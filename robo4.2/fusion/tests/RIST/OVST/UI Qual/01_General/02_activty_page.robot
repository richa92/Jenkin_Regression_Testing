*** Settings ***
Documentation    Activity Page Test Suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  activity  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Variables ***
${expected_dialog_msg}    No items are selected
@{expected_action_list}   Assign  Clear  Restore

*** Test Cases ***
Dialog Boxes Elements Should Appear As Expected
    [Documentation]  Activity Page Dialog Boxes Elements Should Appear As Expected
    ...    \n Actions menu should be visible
    ...    \n Click Actions menu
    ...    \n Ensure that selecting  "Assign", "Clear", or "Restore" *without* selecting an alert creates a dialog
    ...        Title should be: Assign Alerts
    ...        Message should be: No items are selected
    ...        "OK" button should be visible

    Navigate to Page  Activity
    :For  ${action}  In  @{expected_action_list}
    \    log  Select '${action}' from Action menu without selecting alert  console=yes
    \    Select Item From Action or Panel Drop Menu  hp-activity-actions  ${action}
    \    Dialog Should Be Visible  ${action} Alerts
    \    ${msg} =  Get Text  xpath=//div[@class='hp-dialog-notification']/div[@class='hp-message']
    \    Run Keyword If  '${msg}'=='${expected_dialog_msg}'  log  Dialog message is per expected '${msg}'  console=yes
    \    Run Keyword Unless  '${msg}'=='${expected_dialog_msg}'  Fail  Dialog message is not as per expected '${msg}'
    \    ${action} =  Convert To Lowercase  ${action}
    \    Click Element  id=hp-alert-${action}-cancel
    \    Dialog Should Not Be Visible  ${action} Alerts

Action Dropdown Menu Should Display Elements As Expected
    [Documentation]  Activity Page Action Dropdown should display the items "Assign", "Clear" and "Restore"
    Navigate to Page  Activity
    ${actual_action_list} =  Create List From Action or Panel Drop Menu  hp-activity-actions
    lists should be equal  ${actual_action_list}  ${expected_action_list}

Assign Alert Dialog Should Display Elements As Expected
    [Documentation]    Activity page Assign Alert dialog should display element as expected
    ...    \n Click Actions menu
    ...    \n Choosing "Assign" from the Actions menu displays a dialog:
    ...    \n Title should be: Assign Alerts
    ...    \n Buttons should be visible: Assign and Cancel

    Navigate to Page  Activity
    Select Alert From Activity Page  xpath=//table[@id='hp-activities']/tbody/tr[td//div[@data-id='unassigned']][1]
    Select Item From Action or Panel Drop Menu  hp-activity-actions  Assign
    Dialog Should Be Visible  Assign Alerts
    Element Should Be Visible  css=#hp-alert-assign-ok.hp-primary
    Click Element  id=hp-alert-assign-cancel
    Dialog Should Not Be Visible  Assign Alerts
