*** Settings ***
Documentation   Delete Server Profile which is configured to New volume - permanent option is selected, verify the volume is still present

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Delete Server Profile which is configured to New volume - permanent option is selected, verify the volume is still present
    ${rc}                               Fusion UI Delete Server Profile By Name                                    ${TestData.F1408UI028.Delete[0].name}
    Should Be True                      ${rc}   msg=Failed to delete server profile with New volume - permanent option is selected

    ${rc}                               Fusion UI Validate Storage Volume Existing By Name                         ${TestData.F1408UI028.Verify[0].name}
    Should Be True                      ${rc}   msg=Failed to validate storage volume in volumes list

    ${rc}                               Fusion UI Delete Storage Volumes                                           @{TestData.F1408UI028.DeleteVolume}
    Should Be True                      ${rc}   msg=Failed to delete storage volumes