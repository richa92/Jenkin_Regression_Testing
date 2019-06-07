*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance
Force Tags        TBIRD  C7000

*** Test Cases ***
Delete Server Profiles
    [Tags]  TEARDOWN  R-SP  C7000  TBIRD
    [Documentation]   Remove Server Profiles
    ${responses}=     Remove All Server Profiles Async
    Run Keyword If    ${responses} is not ${null}  Wait For Task2   ${responses}  timeout=600  interval=5
    Run Keyword If    ${responses} is not ${Null}  Verify Server profile exists

Delete Server Profile Templates
    [Tags]  TEARDOWN  R-SPT  C7000  TBIRD
    [Documentation]   Remove Server Profiles Templates for servers
    Remove All SPT
    Verify Server Profile Templates exist
