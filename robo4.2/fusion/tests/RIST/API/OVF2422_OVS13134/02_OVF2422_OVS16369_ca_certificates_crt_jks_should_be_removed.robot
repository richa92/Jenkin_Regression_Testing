*** Settings ***
Documentation        Check if / etc / pki / tls / certs / cachains / ca_certificates.crt / jks should be removed

Library              SSHLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16369_ca_certificates_crt_jks should be removed
    [Documentation]  ca_certificates.crt / jks should be removed

    Log  \n - SSH to oneview appliance ...   console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    Login to Fusion via SSH
    : FOR    ${file}  IN    @{FILES_REMOVED}
    \       SSHLibrary.File Should Not Exist  ${file}
    Log     ca_certificates.* file are not existed    console=True
    Log     Log out SSH    console=True
    Logout of Fusion Via SSH
