*** Settings ***
Documentation    Reports Page Test suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  reports  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
Report Item Names Should Match Page Names
    [Documentation]  Verify that the report names in the list match main pane titles when clicked
    Navigate to Page  Reports
    ${items}=  Get Webelements  xpath=//table[@id='hp-report-master-table']/tbody/tr
    :FOR  ${report}  in  @{items}
    \    ${name}=  Get Text  ${report}
    \    Click Element  ${report}
    \    Element Should Be Visible  xpath=//header[@class='hp-details-header']/h1[text()='${name}']
