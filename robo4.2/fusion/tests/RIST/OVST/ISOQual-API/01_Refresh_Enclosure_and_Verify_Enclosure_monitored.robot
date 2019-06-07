*** Settings ***
Documentation    Tests to refresh Enclosure and verify enclosure
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***
Refresh Enclosure
   [Documentation]     Refresh Enclosure
    [Tags]      REFRESH
    Wait For ALL Servers Complete Refresh
    ${responses}=  Refresh Enclosures Async   ${monitored_enclosures}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=5000    interval=20

Verify Enclosure
    [Documentation]     Verify Enclosure
    [Tags]      VERIFY
    ${verify_enc_statuses} =   Create List
    ${enc_status} =     Create List
    :FOR    ${enc}  IN  @{monitored_enclosures}
    \   ${verify_enc}=   Verify TBird Resource     ${enc}
    \   Append To List  ${verify_enc_statuses}  ${verify_enc}
    :FOR    ${verify_enc}   IN  @{verify_enc_statuses}
    \   Run Keyword If  '${verify_enc['status']}'=='False'  Log   Verify Enclosure Failed for Enclosure ${verify_enc['name']}    status=REGEX:OK|Warning
    \   Run Keyword If  '${verify_enc['status']}'=='False'  Append to List    ${enc_status}     Critical
    ${len} =   Get Length  ${enc_status}
    Run Keyword Unless  '${len}'=='0'   Fail     msg=Enclosure Verification Failed
