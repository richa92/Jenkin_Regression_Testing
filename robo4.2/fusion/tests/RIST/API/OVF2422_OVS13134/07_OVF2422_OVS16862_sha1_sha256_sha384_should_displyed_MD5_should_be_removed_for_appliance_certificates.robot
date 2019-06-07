*** Settings ***
Documentation        OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_appliance_certificates

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16862_sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_appliance_certificates
    [Documentation]  sha1_sha256_sha384_should_displyed_MD5_should_be_removed_for_appliance_certificates
    Log    check appliance cert sha1_sha256_sha385 disply, md5 removed    console=True
    ${response} =  Fusion Api Get Remote Certificate   ${APPLIANCE_IP}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}
    ${msg} =  Run Keyword And Expect Error   *   should not be empty  ${response['certificateDetails'][0]['MD5Fingerprint']}
    Should End With    ${msg}   failed: KeyError: 'MD5Fingerprint'
    Log     sha1_${response['certificateDetails'][0]['sha1Fingerprint']}    console=True
    Log     sha256_${response['certificateDetails'][0]['sha256Fingerprint']}    console=True
    Log     sha384_${response['certificateDetails'][0]['sha384Fingerprint']}    console=True
