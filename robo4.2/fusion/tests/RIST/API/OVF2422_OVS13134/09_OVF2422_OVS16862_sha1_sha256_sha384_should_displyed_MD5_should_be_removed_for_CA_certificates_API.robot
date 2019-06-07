*** Settings ***
Documentation        OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_CA_certificates_API.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Teardown        Clear env    root   ${ALIASNAME}
*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            ca_signed_certificate


*** Test Cases ***
OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_CA_certificates_API
    [Documentation]  sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_CA_certificates_API.robot

    Log    check server cert sha1_sha256_sha385 disply, md5 removed    console=True

    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}  aliasName   ${ALIASNAME}
    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}   base64Data   ${ROOT_CA_CERT}
    ${resp} =  Fusion Api Import External Ca Certificates    ${CA_CERTIFICATE}
    Wait For Task2         ${resp}       50      5

    ${response} =  Fusion Api Get Ca Certificate    param=/${ALIASNAME}
    Should Not Be Empty  ${response['certificateDetails']['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails']['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails']['sha384Fingerprint']}
    ${msg} =  Run Keyword And Expect Error   *   should not be empty  ${response['certificateDetails']['MD5Fingerprint']}
    Should End With    ${msg}   failed: KeyError: 'MD5Fingerprint'
    Log     \n - Get/rest/certificates/https/remote to check sha1, sha256, sha384, md5, done, pass    console=True

    Log     \n - Delete certificate...    console=True
    Fusion Api Remove External CA Certificates   ${ALIASNAME}
