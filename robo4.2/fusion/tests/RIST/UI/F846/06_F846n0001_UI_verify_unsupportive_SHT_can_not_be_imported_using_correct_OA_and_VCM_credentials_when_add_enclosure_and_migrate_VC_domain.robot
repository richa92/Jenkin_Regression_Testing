*** Settings ***
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections
Resource             ./keywords.txt
Resource            ../resource.txt

Test Setup      Load Test Data and Prepare Environment  ${Ring}  ${FTS}  ${Add_Enclosure}  ${Add_Storage}  ${Team_Name}
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F846/Regression_data.xml  # Data File Location
${APPLIANCE_IP}             ${None}         # leave it as ${None} if you want this test to create a new one
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url
${Team_Name}                SHQA
${Ring}                     WPST23
${FTS}                      false
${Add_Storage}              false
${Add_Enclosure}            true

*** Test Cases ***
Verify Unsupportive SHT Can Not Be Imported Using Correct VC Migration Payload
    Log To Console        Clear environment before testing.
    Clear Base Resources

    ${enc}=               Set Variable  ${TestData.F846n0001.enclosure}
    ${enclosure_credentials}=    Create Dictionary  oa1hostname=${enc[0].oa1hostname}  oa1username=${enc[0].oa1username}  oa1password=${enc[0].oa1password}
    Remove All SSO Hp Sim Certificates and Snmp Trap Receivers For OA  ${enclosure_credentials}

    Log to Console        Initializing the VCM configuration...
    ${vc_config_file}=    Join Path    ${CURDIR}  \  ${TestData.F846n0001.vcminfo.name}
    ${oaCredential}=      Create Dictionary  oaIpAddress=${enc[0].oa1hostname}  oaUsername=${enc[0].oa1username}  oaPassword=${enc[0].oa1password}
    ${vcm_info}=          Set Variable  ${TestData.F846n0001.vcminfo}
    ${vcmCredential}=     Create Dictionary  vcmIpAddress=${vcm_info.hostname}  vcmUsername=${enc[0].vcmusername}  vcmPassword=${enc[0].vcmpassword}
    Delete and Re-configure VC Domain    ${vcmCredential}  ${oaCredential}  ${vc_config_file}

    Log To Console        Migrate enclosure from VCM to OV.
    ${status}=            Fusion Ui Add Enclosure    @{TestData.F846n0001.enclosure}
    Should Be True        ${status}    msg=Failed to migrate enclosure

    Log To Console        Validate server hardware types info after migration result
    ${status}=            Fusion Ui Validate Server Hardware Types Page    @{TestData.F846n0001.verifyservertypes}
    Should Be True        ${status}    msg=Failed to validate Server Hardware Types

    Log To Console        Validate server profiles informations after migration result
    ${status}=            Fusion Ui Verify Server Profile General Info    @{TestData.F846n0001.verifyserverprofiles}
    Should Be True        ${status}    msg=Failed to validate Server Profiles
