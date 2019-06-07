*** Settings ***
Documentation    OVF2422_OVS16369_ca_certificates_should_not_existed_in_curl_apache_rabbitmq_config_file

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16369_ca_certificates_should_not_existed_in_curl_apache_rabbitmq_config_file
    [Documentation]  OVF2422_OVS16369_ca_certificates_should_not_existed_in_curl_apache_rabbitmq_config_file

    Log     \n - SSH to oneview appliance ...   console=True
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ssh check
    : FOR    ${file}  IN    @{FILES_CONF}
    \       Validator CA Certificates Not In Config File   ${file}
    \       Log    ca certificates not in ${file}    console=True
