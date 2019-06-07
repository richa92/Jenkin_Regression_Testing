*** Settings ***
Documentation    Add C7000 enclosure in FIPS should fail
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              robot.libraries.Process
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***


*** Test Cases ***
Add C7000 enclosure in FIPS should fail
    [Documentation]    Add C7000 enclosure in FIPS should fail
    ${compliant} =  C7000 Enclosure Compliancevalidator    ${Ring}    FIPS
    Pass Execution If   '${compliant}' == 'True'   Run this case just for default Legacy compliant C7000 enclosure, skip if c7000 enclosure cert was changed to FIPS compliant
    Switch Security Mode To    FIPS
    Check If Current Security Mode Meets Target Mode    FIPS
    Add C7000 Enclosure And Check The Error Code
