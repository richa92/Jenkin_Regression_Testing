*** Settings ***
Documentation    Check current security mode, Add old servers, directory servers, repo, storage, Sam Manager and create support dump on 4.1 fresh installed appliance
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Library              robot.libraries.Process
Resource             ./keywords.txt


Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***


*** Test Cases ***
Fresh install appliance, appliance current security mode should be Legacy
    [Documentation]    Check if the current security mode is Legacy
    ${resp} =    Fusion Api Get Current Security Mode
    ${modeName} =    Get From Dictionary    ${resp}    modeName
    Should Be Equal    ${modeName}    LEGACY