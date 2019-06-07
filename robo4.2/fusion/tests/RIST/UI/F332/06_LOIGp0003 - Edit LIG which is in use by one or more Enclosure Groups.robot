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
LOIGp0003 - Edit LIG which is in use by one or more Enclosure Groups
    Log Into Fusion Appliance As Administrator

    ${status}=    Fusion UI Create Tbird Enclosure Group  @{TestData.LOIGp0003.encgroups}
    Should Be True    ${status}    msg=Faild to Create Enclosure Groups

    ${status}=    Fusion Ui Validate Warning Message When Edit Logical Interconnect Group  @{TestData.LOIGp0003.ligs1}
    Should Be True    ${status}    msg=The warning message should not be shown

    ${status}=    Fusion UI Delete Enclosure Group  @{TestData.LOIGp0003.encgroups}
    Should Be True    ${status}    msg=Faild to Create Enclosure Groups