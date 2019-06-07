*** Settings ***
Resource        ../resource.txt

Test Setup      Load Test Data And Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F332/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
ENGRn0002 - Selection of a LIG conflicts with a previously selected LIG when editing EG
    Log Into Fusion Appliance As Administrator

    ${status}=  Fusion UI Validate Selection Of LIG Conflicts With Previously Selected When Editing EG     @{TestData.ENGRn0002}
    Should Be True    ${status}  msg=validate selection of lig conflicts failed

    ${status}=  Fusion Ui Delete Enclosure Group  @{TestData.ENGRn0002}
    Should Be True    ${status}  msg=Failed to delete enclosure group

    ${status}=  Fusion Ui Delete Logical Interconnect Group  @{TestData.ligs}
    Should Be True    ${status}  msg=Failed to delete ligs