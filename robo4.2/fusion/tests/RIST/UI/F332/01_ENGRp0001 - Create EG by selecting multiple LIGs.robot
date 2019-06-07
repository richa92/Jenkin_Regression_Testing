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
ENGRp0001 - Create EG by selecting multiple LIGs
    Log Into Fusion Appliance As Administrator

    ${lig}=    Fusion UI Create Tbird Logical Interconnect Group  @{TestData.ligs}
    Should Be True  ${lig}  msg=Unable to create all LIGs

    ${status}=    Fusion UI Validate Lig Selection When Create Enclosure Group  @{TestData.ENGRp0001.encgroups}
    Should Be True    ${status}    msg=Faild to Create Enclosure Groups

    ${status}=    Fusion UI Validate Enclosure Group Info  @{TestData.ENGRp0001.informations}
    Should Be True    ${status}    msg=Faild when validate EG View

