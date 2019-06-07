*** Settings ***
Documentation    OVF2422_OVS16204_Check_CA_POST_PUT_GET_DELETE_API_should_not_expect_thumb_prints_as_user_specifiled_input
Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource     ./keywords.txt
Variables    ${DATA_FILE}

Test Teardown        Clear env    root   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}          root_ca_external

*** Test Cases ***
OVF2422_OVS16204_Check_CA_POST_PUT_GET_DELETE_API_should_not_expect_thumb_prints_as_user_specifiled_input
    [Documentation]  OVF2422_OVS16204_Check_CA_POST_PUT_GET_DELETE_API_should_not_expect_thumb_prints_as_user_specifiled_input, focus on Get,Delete

    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}  aliasName   ${ALIASNAME}
    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}   base64Data   ${ROOT_CA_CERT}
    ${resp} =  Fusion Api Import External Ca Certificates    ${CA_CERTIFICATE}
    Wait For Task2         ${resp}       50      5

    ${thumbprint}=  Get Certificate ThumbPrint   ${ALIASNAME}
    ${resp}=  Fusion Api Get Ca Certificate   param=/${thumbprint}
    Should Not Be Equal  ${resp['status_code']}   200     msg=Certificate should not be get by tthumbprint
    Should Contain   ${resp['message']}     No matching certificate found for the specified alias
    Log    Get /rest/certificate/ca can not get certificate by thumbprint    console=True

    ${resp}=  Fusion Api Remove External Ca Certificates  ${thumbprint}
    Wait For Task2       ${resp}     50    5   PASS=Error    errorMessage=Delete_Cert_Error
    Log    Get /rest/certificate/ca can not delete certificate by thumbprint    console=True

    Log    \n - Delete certificate...    console=True
    Fusion Api Remove External CA Certificates   ${ALIASNAME}