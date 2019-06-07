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
Fresh install appliance, add exteral self-signed repository should be successfully
    [Documentation]    add repo
    Add Cert Of SelfSigned REPO Or IPDU    ${add_repo_cert}
    ${resp} =    Fusion Api Add Repository    ${add_repo}
    Wait For Task2    ${resp}  120  5
    Should Be Equal As Numbers  ${resp['status_code']}  202    msg= Repo is not added
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    180s   5s    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}