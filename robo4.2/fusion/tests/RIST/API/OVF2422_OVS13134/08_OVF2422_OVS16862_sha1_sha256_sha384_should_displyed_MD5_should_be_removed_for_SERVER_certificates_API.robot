*** Settings ***
Documentation        OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_SERVER_certificates_API.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Teardown        Clear env    server   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            self_signed_certificate


*** Test Cases ***
OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_SERVER_certificates_API
    [Documentation]  11_OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_SERVER_certificates_API.robot

    Log    check server cert sha1_sha256_sha385 disply, md5 removed    console=True

    ${response} =  Fusion Api Get Remote Certificate   ${REMOTE_SERVER_SELF_SIGN}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}
    ${msg} =  Run Keyword And Expect Error   *   should not be empty  ${response['certificateDetails'][0]['MD5Fingerprint']}
    Should End With   ${msg}   failed: KeyError: 'MD5Fingerprint'
    Log     Get/rest/certificates/https/remote to check sha1, sha256, sha384, md5, done, pass    console=True

    Log     \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate...
    ${body} =  Generate Certificate Payload     ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate   ${body}
    Wait For Task2       ${resp}     50    5
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_SELF_SIGN}   True

    ${response} =  Fusion Api Get Server Certificate   ${ALIASNAME}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}
    ${msg} =  Run Keyword And Expect Error   *   should not be empty  ${response['certificateDetails'][0]['MD5Fingerprint']}
    Should End With    ${msg}   failed: KeyError: 'MD5Fingerprint'
    Log    Get/rest/certificate/svers/aliasname to check sha1, sha256, sha384, md5, done, pass    console=True
    Log   \n - Delete certificate...
    Remove Server Certificate By Aliasname  ${ALIASNAME}

    Log   Verify trust status info..
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_SELF_SIGN}   False
