*** Settings ***
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections
Resource             ./keywords.txt
Resource            ../resource.txt

Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F846/Regression_data.xml  # Data File Location
${APPLIANCE_IP}             ${None}         # leave it as ${None} if you want this test to create a new one
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url
${Team_Name}                SHQA
${Ring}                     WPST22
${FTS}                      false
${Add_Storage}              false
${Add_Enclosure}            true

*** Test Cases ***
Verify Migration Will Be Abort Using Wrong VCM Credential
    Log into Fusion appliance as Administrator

    Log To Console        Clear environment before testing.
    Clear Base Resources

    Log To Console        Migrate enclosure from VCM to OV.
    ${status}  ${msg}=    Run Keyword and Ignore Error    Fusion Ui Add Enclosure    @{TestData.F846n0005.enclosure}
    Should Be Equal as Strings  ${status}  FAIL
    Should Contain        ${msg}    Provide a valid IP address or hostname, username, and password
