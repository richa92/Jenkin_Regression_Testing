*** Settings ***
Documentation       OVF2422_OVS16444_self_signed_leaf_certificate_without_EKU_Server_Authentication_should_fetched_successfully
...                 OVF2422_OVS16444_self_signed_leaf certificate(without EKU = Server Authentication) should fetched successfully
...                 OVF2422_OVS16444_self_signed_leaf certificate(without EKU = Server Authentication) should get by aliasname successfully
...                 OVF2422_OVS16444_self_signed_leaf certificate(without EKU = Server Authentication) should put successfully
...                 OVF2422_OVS16444_self_signed_leaf certificate(without EKU = Server Authentication) should delete successfully
...                 covered by ovs688_ovs5874

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}

*** Test Cases ***
OVF2422_OVS16444_self_signed_leaf_certificate_without_EKU_Server_Authentication_should_fetched_successfully
    [Documentation]  OVF2422_OVS16444_self_signed_leaf_certificate_without_EKU_Server_Authentication_should_fetched_successfully

    ${resp} =  Fusion Api Get Remote Certificate  ${REMOTE_SERVER_SELF_SIGN}
    Should Be Equal As Strings  ${resp['status_code']}   200   msg =  Fetch certificate fail
    Log    Fetch certifciate (without EKU=Server_Authentication)successfully    console=True
