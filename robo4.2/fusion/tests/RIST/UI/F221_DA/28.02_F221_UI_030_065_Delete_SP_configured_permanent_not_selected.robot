*** Settings ***
Documentation   Delete Server Profile which is configured to New volume - permanent option is not selected, verify the volume is not present

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Delete Server Profile which is configured to New volume - permanent option is not selected, verify the volume is not present
    ${rc}                               Fusion UI Delete Server Profile By Name                                         ${TestData.F221UI030.Delete[0].name}
    Should Be True                      ${rc}   msg=Failed to delete server profile with New volume - permanent option is not selected

    ${rc}                               Fusion UI Validate Storage Volume Not Existing By Name                          ${TestData.F221UI030.Verify[0].name}
    Should Be True                      ${rc}   msg=Failed to validate storage volume not in volumes list