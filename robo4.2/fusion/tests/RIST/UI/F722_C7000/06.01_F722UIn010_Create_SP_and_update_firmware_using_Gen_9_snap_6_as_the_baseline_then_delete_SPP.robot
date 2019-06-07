*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F722_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F722UIn010 Create SP and update firmware using Gen 9 snap 6 as the baseline, then delete SPP
    Fusion UI Create Server Profile      @{TestData.notwaitsnap6profile}
    Fusion UI Validate Server Profile Task Step     @{TestData.notwaitsnap6profile}
    Fusion Ui Validate Cannot Delete Firmware Bundle     @{TestData.snap6spp}

