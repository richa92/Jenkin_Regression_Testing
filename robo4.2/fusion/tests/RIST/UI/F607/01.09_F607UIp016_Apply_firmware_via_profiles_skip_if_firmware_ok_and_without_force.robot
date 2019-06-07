*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F607/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F607UI0016 Apply firmware via profiles skip if firmware ok and without force
    Fusion UI Edit Server Profile        @{TestData.firmwareprofile}
#    Fusion UI Validate Server Profile Task Step     @{TestData.firmwareprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.firmwareprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
    ${rc}=    Fusion Ui Validate Logical Enclosure Firmware    @{TestData.profilebaselineLE}
    Should Be True                      ${rc}   msg=Some logical enclosure firmware update unsuccessfully
    Fusion Ui Delete Server Profile      @{TestData.firmwareprofile}
    ${rc}=   Fusion Ui Delete Logical Enclosure      @{TestData.snap6LE}
    Should Be True                      ${rc}   msg=Remove logical enclosure failed, error message:${rc}

