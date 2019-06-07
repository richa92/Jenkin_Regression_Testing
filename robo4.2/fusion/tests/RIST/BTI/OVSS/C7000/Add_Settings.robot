*** Settings ***
Documentation           Add Settings
Resource                resource.txt
Suite Setup             Suite Setup
Suite Teardown          Suite Teardown

*** Test Cases ***
C7000 OVSS Add Settings Add Licenses
    [Documentation]   Add Licenses
    ${licenses} =  Get Variable Value  ${licenses}
    ${responses} =  Run Keyword If  ${licenses} is not ${null}    Add Licenses from variable    ${licenses}
    Run Keyword If   ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resource  ${licenses}

C7000 OVSS Add Settings Add Users
    [Documentation]  Add users
    ${responses} =  Run Keyword If  ${users} is not ${null}     Add Users from variable  ${users}
    Run Keyword If   ${responses} is not ${null}  Run Keyword And Continue On Failure    Wait For Task2   ${responses}
    Verify Resource  ${expected_users}  enabled=True