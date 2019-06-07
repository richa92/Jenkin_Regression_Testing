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
Fresh install appliance, add storage system should be successfully
    [Documentation]    add Storage System
    Log    Add Storage System
    ${resp} =   Fusion Api Create Storage System    ${add_storagesystem}
    Wait For Task2    ${resp}  timeout=60  interval=5
    Log    Edit Storage System, get the storage id info firstly, then set the managedDomain, then update storage    console=Yes
    ${storage_put} =  Fusion Api Get Storage System    param=${storage_id}
    Remove From Dictionary  ${storage_put}  status_code  headers
    ${deviceSpecificAttributes} =  get from dictionary  ${storage_put}  deviceSpecificAttributes
    Set to dictionary  ${deviceSpecificAttributes}  managedDomain  ${managedDomain}
    Set to dictionary  ${storage_put}  deviceSpecificAttributes  ${deviceSpecificAttributes}
    ${resp} =  Fusion Api Update Storage System   ${storage_put}    uri=/rest/storage-systems${storage_id}
    Wait For Task2    ${resp}  timeout=30  interval=5
