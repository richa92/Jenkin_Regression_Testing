*** Settings ***
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections
Resource             ./keywords.txt
Resource             ../resource.txt
Resource             ../../API/Fusion_Env_Setup/keywords.txt

Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser And Clear Base Resources    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F166/Regression_data.xml  # Data File Location
${APPLIANCE_IP}             ${None}         # leave it as ${None} if you want this test to create a new one
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url
${admin_credentials}        ${C7000EnvSetup.${Team_Name}.Common.admin_credentials}
${ExpectedStatus}           OK
${ExpectedPowerStatus}      On
${Team_Name}                SHQA
${Ring}                     WPST26
${FTS}                      false
${Add_Storage}              false
${Add_Enclosure}            true

*** Test Cases ***
Migrate Enclosure with two Vlan Ethernet link to one external uplink to OV
    Log into Fusion appliance as Administrator

    Log to Console        Initializing the VCM configuration...
    ${vc_config_file}=    Join Path    ${CURDIR}  \  ${TestData.F166p003.vcminfo.name}
    ${enc}=               Set Variable  ${TestData.F166p003.enclosure}
    ${oaCredential}=      Create Dictionary  oaIpAddress=${enc[0].oa1hostname}  oaUsername=${enc[0].oa1username}  oaPassword=${enc[0].oa1password}
    ${vcm_info}=            Set Variable  ${TestData.F166p003.vcminfo}
    ${vcmCredential}=     Create Dictionary  vcmIpAddress=${vcm_info.hostname}  vcmUsername=${enc[0].vcmusername}  vcmPassword=${enc[0].vcmpassword}
    Delete and Re-configure VC Domain    ${vcmCredential}  ${oaCredential}  ${vc_config_file}

    Log To Console     Waiting blade server booting to OS...
    ${ilo_creds}=      Set Variable    ${TestData.ilo_credentials[0]}
    ${ilo_credentials}=    Create Dictionary  username=${ilo_creds.username}  password=${ilo_creds.password}
    Set Suite Variable     ${ilo_credentials}
    :FOR    ${ilo}  IN    @{ilo_list}
    \       Wait For Blade To Reach POST State Using ILO  ${ilo}

    Log To Console        Migrate enclosure from VCM to OV.
    ${status}=            Fusion Ui Add Enclosure    @{TestData.F166p003.enclosure}
    Should Be True        ${status}    msg=Failed to migrate enclosure

    Log To Console        Validate server hardware info after migration result
    ${status}=            Fusion UI Validate Server Hardware Page Hardware    @{TestData.F166p003.verifyservers}
    Should Be True        ${status}    msg=Failed to validate Server Hardware

    Log To Console        Validate server profiles informations after migration result
    ${status}=            Fusion UI Validate Server Profile Status     ${ExpectedStatus}    @{TestData.F166p003.verifyserverprofiles}
    Should Be True	      ${status}	   msg=Failed to validate server profile status

    Log To Console        Validate server profiles Power status after migration result
    ${status}=            Fusion UI Verify Server Profile Power Status     ${ExpectedPowerStatus}  @{TestData.F166p003.verifyserverprofiles}
    Should Be True	      ${status}	    msg=Failed to validate Server Profiles power status

    Log To Console        Validate server profiles connections after migration result
    ${status}=            Fusion UI Verify Server Profile Connections Info    @{TestData.F166p003.verifyspsconnections}
    Should Be True        ${status}    msg=Failed to validate Server Profiles connections
