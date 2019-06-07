*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Add Licenses
    [Tags]  SETUP    LICENSES  TBIRD  C7000
    [Documentation]  Add Licenses to OneView
    ${licenses} =    Get Variable Value  ${licenses}
    Run Keyword If   ${licenses} is not ${null}  Add Licenses from variable  ${licenses}  ${VERIFY}
