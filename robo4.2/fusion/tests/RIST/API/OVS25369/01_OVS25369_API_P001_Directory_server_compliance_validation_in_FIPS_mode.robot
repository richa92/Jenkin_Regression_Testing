*** Settings ***
Documentation        OVS25369 API P001: verify status of directory servers in FIPS compatibility report
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data2.py

Test Setup           Case Setup    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Case Teardown

*** Variables ***
${APPLIANCE_IP}         unknown


*** Test Cases ***
01_OVS25369_API_P001_Directory_server_compliance_validation_in_FIPS_mode
    [Documentation]  OVS25369_API_P001_Directory_server_compliance_validation_in_FIPS_mode
    Log    \n- Create FIPS compatibility report    console=True
    ${body}=    Create Dictionary    currentMode=LEGACY  targetMode=FIPS
    ${resp}=    Fusion Api Create Security Compatibility Report  ${body}
    Wait For Task2  ${resp}  300    6

    Log    \n- Get and verify FIPS compatibility report    console=True
    ${resp}=    Fusion Api Get Security Compatibility Report
    ${mode}=    Get From Dictionary  ${resp}  targetMode
    Should Be Equal As Strings  ${mode}    FIPS
    ${dom_members}=   Get From Dictionary    ${resp}     members
    :FOR    ${member}    IN    @{dom_members}
    \        ${category}=    Get From Dictionary  ${member}  resourceCategory
    \        Log    \n- resourceCategory is: ${category}    console=True
    \        Should Not Be True    '${category}'=='LOGINDOMAINS'

