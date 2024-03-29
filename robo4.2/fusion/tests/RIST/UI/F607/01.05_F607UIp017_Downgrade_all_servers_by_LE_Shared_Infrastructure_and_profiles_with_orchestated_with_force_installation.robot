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
F607UIp017 Downgrade all servers by LE shared Infrastructure and profiles with Orchestrated with force installation

    Power off ALL servers

    Fusion Ui Logical Enclosure Firmware Update    @{TestData.editsnap6forceLEOrchestrated}
    ${rc}=   Fusion Ui Validate Logical Enclosure Firmware    @{TestData.editsnap6forceLEOrchestrated}
    Should Be True                      ${rc}   msg=Some logical enclosure firmware update unsuccessfully

