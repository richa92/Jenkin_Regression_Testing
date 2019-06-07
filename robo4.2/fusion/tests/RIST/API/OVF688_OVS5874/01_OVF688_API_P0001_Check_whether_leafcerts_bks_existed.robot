*** Settings ***
Documentation        Check if all-certificates bks existed

Library              SSHLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
Check_whether_leafcerts_bks_existed
    [Documentation]  01_OVF688(ovs5874)_API_P0001_Check_whether_all-certificates.bks_existed.robot

    Log    \n - SSH to oneview appliance ...    console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    Login to Fusion via SSH
    SSHLibrary.File Should Exist   ${FILE}
    Log     - all-certificates file is existed    console=True
    Log     - Log out SSH    console=True
    Logout of Fusion Via SSH