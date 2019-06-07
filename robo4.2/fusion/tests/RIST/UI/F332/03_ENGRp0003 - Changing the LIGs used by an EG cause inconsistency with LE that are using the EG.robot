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
ENGRp0003 - Changing the LIGs used by an EG cause inconsistency with LE that are using the EG
    Log Into Fusion Appliance As Administrator

    ${status}=    Fusion UI Validate Tbird Logical Enclosure Consistency State   @{TestData.ValidateConsistent.consistency}
    Should Be True    ${status}    msg=Faild when validate logical enclosure consistency state

    ${status}=    Fusion Ui Edit Logical Interconnect Group  @{TestData.ENGRp0003.AddUplinksets}
    Should Be True    ${status}    msg=Faild to Add uplinkset for LIG

    ${status}=    Fusion UI Validate Tbird Logical Enclosure Consistency State   @{TestData.ValidateConsistent.inconsistency}
    Should Be True    ${status}    msg=Faild when validate logical enclosure consistency state

    ${status}=    Fusion Ui Edit Logical Interconnect Group  @{TestData.ENGRp0003.RemoveUplinksets}
    Should Be True    ${status}    msg=Faild to remove uplinkset for LIG
