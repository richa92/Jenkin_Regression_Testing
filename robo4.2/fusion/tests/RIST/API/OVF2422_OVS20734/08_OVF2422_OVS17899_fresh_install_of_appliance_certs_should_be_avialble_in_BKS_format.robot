*** Settings ***
Documentation    _installOn fresh install of appliance certs should be avialble in Bouncy Castle key store (BKS) format
...              no *.jks exist
Library          SSHLibrary
Resource         ../../../../Resources/api/fusion_api_resource.txt
Variables        ./Regression_Data.py
*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}
*** Test Cases ***
OVF2422_OVS17899_fresh_install_of_appliance_certs_should_be_avialble_in_BKS_format
    [Documentation]    _installOn fresh install of appliance certs should be avialble in Bouncy Castle key store (BKS) format
    Log  \n- SSH to oneview appliance ...   console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    Login To Fusion Via SSH
    Execute SSH Command    ${JKSCOMMAND1}    ${JKSNUM}
    Log  No jks file in /etc/pki/tls/certs     console=True
    Login To Fusion Via SSH
    Execute SSH Command    ${JKSCOMMAND2}    ${JKSNUM}
    Log  No jks file in /etc/pki/tls/certs/cachains    console=True
    Login To Fusion Via SSH
    Execute SSH Command    ${BKSCOMMAND}    ${BKSNUM}
    Log  Bks files are in /etc/pki/tls/certs/cachains    console=True
    Log  Log out SSH    console=True