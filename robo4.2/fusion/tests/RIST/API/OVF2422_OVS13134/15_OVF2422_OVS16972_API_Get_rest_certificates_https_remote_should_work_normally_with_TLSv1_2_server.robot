*** Settings ***
Documentation        OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1_2_server
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${RMOTE_TLSV1.2_SERVER_IP}      ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1_2_server
    [Documentation]  OVF2422_OVS16972_API_Get_rest_certificates_https_remote_should_work_normally_with_TLSv1.2_server.robot

    Log    check if get /rest/certificate/https/remote work with TLSv1.2     console=True

    ${response} =  Fusion Api Get Remote Certificate   ${RMOTE_TLSV1.2_SERVER_IP}
    Should Be Equal As Integers  ${response['status_code']}    200       msg = Get / rest / certificate / https / remote failed to get TLSv1.2 server cert
    Log  \n - Get/rest/certificates/https/remote for TLSv1.2 server cert successfully    console=True
