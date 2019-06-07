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
Fresh install appliance, add iPDU should be successfully
    [Documentation]    add iPDU cert firstly, then add iPDU
    Add Cert Of SelfSigned REPO Or IPDU    ${add_ipdu_cert}
    Log    add ipdu    console=Yes
    ${resp} =    Fusion Api Discover Power Device    ${add_ipdu}
    Wait For Task2    ${resp}    timeout=120    interval=5