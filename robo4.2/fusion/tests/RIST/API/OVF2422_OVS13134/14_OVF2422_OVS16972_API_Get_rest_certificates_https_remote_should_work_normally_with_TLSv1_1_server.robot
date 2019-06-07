*** Settings ***
Documentation        OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1_1_server
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
17_OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1_1_server
    [Documentation]  17_OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1.1_server.robot

    Log    check if get /rest/certificate/https/remote work with TLSv1.1     console=True

    ${response} =  Fusion Api Get Remote Certificate   ${REMOTE_SERVER_SELF_SIGN_TLSV1_1}
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'  Should Be Equal As Integers  ${response['status_code']}    200       msg=Get /rest/certificate/https/remote failed to get TLSv1.1 server cert
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Should Be Equal As Integers  ${response['status_code']}    200       msg=Get /rest/certificate/https failed to get TLSv1.1 server cert under FIPS mode
    Run Keyword If  '${SECURITY_MODE}' == 'CNSA'   Should Not Be Equal As Integers  ${response['status_code']}    200       msg=Get /rest/certificate/https can not get TLSv1.1 certificate under CNSA mode

    Log   \n - Get/rest/certificates/https/remote for TLSv1.1 server cert successfully    console=True

