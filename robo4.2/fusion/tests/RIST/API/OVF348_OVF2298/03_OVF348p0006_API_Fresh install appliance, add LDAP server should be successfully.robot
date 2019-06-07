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
Fresh install appliance, add LDAP server should be successfully
    [Documentation]    Add LDAP server on appliance, Add group, then relogin with LDAP user
    Log    Add CA certs    console=Yes
    ${resp} =    Fusion Api Import External CA Certificates    ${add_ldap_rootcacert}
    Wait For Task2    ${resp}    timeout=30    interval=5
    ${resp} =    Fusion Api Import External CA Certificates    ${add_ldap_intermediatecacert}
    Wait For Task2    ${resp}    timeout=30    interval=5
    Log    Add directory server    console=Yes
    ${resp} =    Fusion Api Add Directory     ${add_ldap}
    Wait For Task2    ${resp}    timeout=30    interval=5
    Log    Assign role to group    console=Yes
    ${resp} =    Fusion Api Assign Roles To Directory Group    ${ldap_group}
    Should Be Equal As Numbers  ${resp['status_code']}  201
    Log    relogin with dirctory server user    console=Yes
    Fusion Api Logout Appliance
    ${resp} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ldap_user}
    Should Be Equal As Numbers  ${resp[0]['status_code']}  200