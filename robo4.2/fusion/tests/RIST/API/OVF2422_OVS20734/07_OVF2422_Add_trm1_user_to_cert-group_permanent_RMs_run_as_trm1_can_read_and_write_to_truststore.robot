*** Settings ***
Documentation    OVF2422_OVS19087_s_OneView_security_developer_I_shall_add_trm1_user_to_cert-group_permanently_so_that_RMs_running_as_trm1_can_read_and_write_to_truststores
Library          SSHLibrary
Resource         ../../../../Resources/api/fusion_api_resource.txt
Variables        ./Regression_Data.py
*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}
*** Test Cases ***
OVF2422_Add_trm1_user_to_cert-group_permanent_RMs_run_as_trm1_can_read_and_write_to_truststore
    [Documentation]    OneView_security_developer_I_shall_add_trm1_user_to_cert-group_permanently_so_that_RMs_running_as_trm1_can_read_and_write_to_truststores
    Log  \n- SSH to oneview appliance ...   console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    Login To Fusion Via SSH
    Execute SSH Command    ${COMMAND}    ${TRM1}
    Log  Trm1 are in the cert group    console=True
    Log  Log out SSH    console=True