*** Settings ***
Documentation        OVS25369 API P002: verify status of directory servers in CNSA compatibility report
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
02_OVS25369_API_P002_Directory_server_compliance_validation_in_CNSA_mode
    [Documentation]  OVS25369_API_P002_Directory_server_compliance_validation_in_CNSA_mode
    Log    \n- Create CNSA compatibility report    console=True
    ${body}=    Create Dictionary    currentMode=LEGACY  targetMode=CNSA
    ${resp}=    Fusion Api Create Security Compatibility Report  ${body}
    Wait For Task2  ${resp}  300    6

    Log    \n- Get and verify CNSA compatibility report    console=True
    ${resp}=    Fusion Api Get Security Compatibility Report
    ${mode}=    Get From Dictionary  ${resp}  targetMode
    Should Be Equal As Strings  ${mode}    CNSA
    ${dom_members} =   Get From Dictionary    ${resp}     members
    :FOR    ${member}    IN   @{dom_members}
    \        ${category}=    Get From Dictionary  ${member}  resourceCategory
    \        Log    \n- resourceCategory is:${category}    console=True
    \        Run Keyword If    '${category}'!='LOGINDOMAINS'    Continue For Loop
    \        ...        ELSE              Verify Directory Server In Cnsa Report    ${member}