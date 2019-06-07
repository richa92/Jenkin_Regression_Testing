*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Add Logical Enclosure
    [Tags]   ADDLE  TBIRD
    Add Logical Enclosure from lists  ${logical_enclosure}
    Verify Resources for List         ${expected_logical_enclosure}

Verify Enclosure
    [Tags]   VERIFY  TBIRD
    ${verify_enc_statuses} =   Create List
    ${enc_status} =  Create List
    :FOR  ${enc}  IN  @{configured_enclosures}
    \   ${verify_enc}=   Verify TBird Resource   ${enc}
    \   Append To List   ${verify_enc_statuses}  ${verify_enc}
    :FOR  ${verify_enc}  IN  @{verify_enc_statuses}
    \   Run Keyword If   '${verify_enc['status']}'=='False'  Log  Verify Enclosure Failed for Enclosure ${verify_enc['name']}  WARN
    \   Run Keyword If   '${verify_enc['status']}'=='False'  Append to List  ${enc_status}  Critical
    ${len} =   Get Length  ${enc_status}
    Run Keyword Unless  '${len}'=='0'   Fail   msg=Enclosure Verification Failed
