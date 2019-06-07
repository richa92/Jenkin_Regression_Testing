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
Fresh install appliance, create Support Dump should be successfully
    [Documentation]    Check if create support dump is successful
    ${resp} =    Fusion Api Create Support Dump    ${support_dump}
    Should Be Equal    '${resp['status_code']}'    '200'    msg= Support dump is not created
    ${uri} =     Get from DIctionary    ${resp}    uri
    Should Contain    ${uri}    .sdmp    msg= Support dump is not created
    Log    Support dump is created for the appliance    console=Yes
    ${response} =    Fusion Api Download Support Dump    ${uri}    ${dump_filename}
    Should Be Equal    '${resp['status_code']}'    '200'    msg= SD download failed
    Remove File    ${dump_filename}