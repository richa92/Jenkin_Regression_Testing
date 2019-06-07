*** Settings ***
Documentation        OVF2422_OVS11296_Post_rest_certificates_ca_should_handle_concurrent_requests_for_adding_CA_certs
...                  Parallel request to import same CA cert should be handled.
...                  Only first request should be accepted

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Teardown        Clear Certs  ${Enable_Aliasname_Chain[0]['type']}  ${Enable_Aliasname_Chain[0]['name']}
*** Test Cases ***
OVF2422_OVS11296_Post_rest_certificates_ca_should_handle_concurrent_requests_for_adding_CA_certs
    [Documentation]  OVF2422_OVS11296_Post_rest_certificates_ca_should_handle_concurrent_requests_for_adding_CA_certs.robot
    Log    check if when post /rest/certificate/ca import the same CA cert twice,Only first request should be accepted    console=True
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${CNSA_ROOT_CERT}  ${Enable_Aliasname_Chain[0]['name']}
    Log    post /rest/certificate/ca import the same CA cert firsttime...    console=True
    ${resp1} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp1['status_code']}   202    msg=Fail to import CA cert
    log    post /rest/certificate/ca import the same CA cert secondtime...    console=True
    ${resp2} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp2['status_code']}   500    msg=Fail to import CA cert
    Wait For Task2         ${resp1}       50    5
    Wait For Task2         ${resp2}       50    5    PASS=Error    errorMessage=Certificate_Already_Exists
    Log    post /rest/certificate/ca import the same CA cert secondtime cannot be accepted.    console=True