*** Settings ***
Documentation    Check if all_certificates bks and crt are existed
Library          SSHLibrary
Resource         ../../../../Resources/api/fusion_api_resource.txt
Variables        ${DATA_FILE}

*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}


*** Test Cases ***
OVF2422 OVS15895 all certificates files should exist
    [Documentation]    all certificates files should exist
    Log  \n - SSH to oneview appliance ...   console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    Login to Fusion via SSH
    : FOR    ${file}  IN    @{FILES}
    \       SSHLibrary.File Should Exist   ${file}
    Log  all - certificates file are existed    console=True
    Log  Log out SSH    console=True
    Logout of Fusion Via SSH
