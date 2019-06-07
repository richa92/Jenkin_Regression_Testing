*** Settings ***
Documentation        OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_work_with_valid_IP_address.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_work_with_valid_IP_address
    [Documentation]  OVF2422_OVS16671_API_Get_rest_certificates_https_remote_should_work_with_valid_IP_address.robot

    Log    check get /rest/certificate/https/remote should work with valid ip    console=True

    ${response} =  Fusion Api Get Remote Certificate   ${APPLIANCE_IP}
    Should Be Equal As Integers  ${response['status_code']}    200        msg = Get / rest / certificate / https / remote failed
    Log    \n - Get/rest/certificates/https/remote successfully    console=True
