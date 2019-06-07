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
Verify supportive SHT Gen7 Can Be Imported Using Correct VC Migration Payload
    Log into Fusion appliance as Administrator

    Log To Console        Clear environment before testing.
    Clear Base Resources

    Log To Console        Migrate enclosure from VCM to OV.
    ${status}=            Fusion Ui Add Enclosure    @{TestData.F846p0001.enclosure}
    Should Be True        ${status}    msg=Failed to migrate enclosure

    Log To Console        Validate server hardware types info after migration result
    ${status}=            Fusion Ui Validate Server Hardware Types Page    @{TestData.F846p0001.verifyservertypes}
    Should Be True        ${status}    msg=Failed to validate Server Hardware Types

    Log To Console        Validate server profiles informations after migration result
    ${status}=            Fusion Ui Verify Server Profile General Info    @{TestData.F846p0001.verifyserverprofiles}
    Should Be True        ${status}    msg=Failed to validate Server Profiles
