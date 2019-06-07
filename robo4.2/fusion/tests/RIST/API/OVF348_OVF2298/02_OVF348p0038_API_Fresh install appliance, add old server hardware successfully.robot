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
Fresh install appliance, add old server hardware successfully
    [Documentation]    add old servers
    Pass Execution    Will manually run this test
#    ${resp}=         Fusion Api Get Appliance Version
#    ${mode_type}=    Set Variable  ${resp["modelNumber"]}
#    Pass Execution If   '${mode_type}' == 'Synergy Composer'   "Add server hardware" just for C7000, skip this test on "Synergy Composer"
#    ${resp} =    Fusion Api Add Server Hardware    ${addGen6requestody}
#    Wait For Task2    ${resp}    timeout=180    interval=5
#    Verify Old Sever Added    ${GEN6_IP}
#    ${resp} =    Fusion Api Add Server Hardware    ${addGen7requestody}
#    Wait For Task2    ${resp}    timeout=180    interval=5
#    Verify Old Sever Added    ${GEN7_IP}
