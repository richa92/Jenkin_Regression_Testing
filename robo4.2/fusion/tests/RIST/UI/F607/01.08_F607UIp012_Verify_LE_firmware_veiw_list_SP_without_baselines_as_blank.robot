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
F607UI0012 Verify LE firmware veiw list SP without baselines as blank

    Fusion Ui Create Server Profile      @{TestData.profile}
    ${rc}=   Fusion Ui Validate Logical Enclosure Firmware    @{TestData.profileNobaselineLE}
    Should Be True                      ${rc}   msg=Some logical enclosure firmware update unsuccessfully

