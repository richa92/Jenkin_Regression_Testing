*** Settings ***
Documentation    Firmware Bundle Page Test Suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  firmwarebundle  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
'Add Firmware Bundle' Dialog Elements Should Appear As Expected
    [Documentation]  Firmware Bundle Page 'Add Firmware Bundle' dialog should display elements as expected
    ...    \n Click "Add Firmware Bundle" and verify dialog is displayed.
    ...    \n Browse button should be visible
    ...    \n OK button should be visible and disabled
    ...    \n Close button should be visible

    Navigate to Page  Firmware Bundles
    Click Element     link=Add Firmware Bundle
    Dialog Should be Visible      Add Firmware Bundle
    Element Should be Visible     xpath=//div[input[@id='hp-file-chooser-file']]
    Element Should be Visible     xpath=//input[@id='cic-fwdriver-add-ok' and @disabled='disabled']
    Click Element                 xpath=//a[@class='hp-button hp-primary' and text()='Close']
    Dialog Should Not be Visible  Add Firmware Bundle