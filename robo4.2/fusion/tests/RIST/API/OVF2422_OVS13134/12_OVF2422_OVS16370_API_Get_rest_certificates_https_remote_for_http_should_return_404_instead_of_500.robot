*** Settings ***
Documentation        OVF2422_OVS16370_API_Get_rest_certificates_https_remote_for_http_should_return_404_instead_of_500.robot
...                  Refer to bug OVD8205, test with ipdu http 16.125.78.14

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${RMOTE_SERVER_IP}      16.125.78.14


*** Test Cases ***
15_OVF2422_OVS16370_API_Get_rest_certificates_https_remote_for_http_should_return_404_instead_of_500
    [Documentation]  API_Get_rest_certificates_https_remote_for_http_should_return_404_instead_of_500.robot

    Log    check get /rest/certificate/https/remote return 404 instead of 500    console=True

    ${response} =  Fusion Api Get Remote Certificate   ${RMOTE_SERVER_IP}
    Should Be Equal As Integers  ${response['status_code']}    404        msg = Get / rest / certificate / https / remote retrun not equal 404
    Log   \n - Get/rest/certificates/https/remote fot http return 404 instead of 500 successfully    console=True
