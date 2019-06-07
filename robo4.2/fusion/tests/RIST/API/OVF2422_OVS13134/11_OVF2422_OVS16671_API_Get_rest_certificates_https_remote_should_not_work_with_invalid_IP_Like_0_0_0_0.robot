*** Settings ***
Documentation        OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_not_work_with_invalid_IP_Like_0_0_0_0.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_not_work_with_invalid_IP_Like_0_0_0_0
    [Documentation]  OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_not_work_with_invalid_IP_Like_0_0_0_0.robot

    Log    check get /rest/certificate/https/remote should not work with invalid ip    console=True

    ${response} =  Fusion Api Get Remote Certificate   0.0.0.0
    Should Not Be Equal As Integers  ${response['status_code']}    200        msg = Get / rest / certificate / https / remote with 0.0.0.0 successfully
    Should Be Equal As Strings   ${response['details']}   ${SERVER_ADDRESS_NOT_VALID_ERROR}
    Log    \n - Get/rest/certificates/https/remote can not get invalid ip 0.0.0.0 successfully    console=True

