*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Add Managed Enclosure and Verify
    [Tags]    SETUP  ENCLOSURE  C7000
    [Documentation]  Add Enclosures to OneView
    ${responses}=    Run Keyword If  ${enclosures} is not ${null}  Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength}=    get length   ${responses}
    Run Keyword If   '${reslength}' is not '${0}'   Run Keyword for List with kwargs  ${responses}  Wait For Task2  timeout=1200  interval=10
    Run Keyword If   '${reslength}' is not '${0}'   Sleep  180s
    Run Keyword If   ${expected_enclosures} is not ${null}  Verify Enclosures from list  ${expected_enclosures}  state=Configured
