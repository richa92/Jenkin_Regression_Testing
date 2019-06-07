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
ENGRp0002 - Edit EG by selecting multiple LIGs
    Log Into Fusion Appliance As Administrator

    ${status}=    Fusion UI Validate Lig Selection When Edit Tbird Enclosure Group  @{TestData.ENGRp0002.encgroups}
    Should Be True    ${status}    msg=Faild to Edit Enclosure Groups

    ${status}=    Fusion UI Validate Enclosure Group Info  @{TestData.ENGRp0002.informations}
    Should Be True    ${status}    msg=Faild when validate EG View

