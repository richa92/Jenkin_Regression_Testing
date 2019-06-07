*** Settings ***
Documentation       OVF2422_OVS16365_Treat_iLO_default_certificate_as_self_signed_with_POST_rest_certificates_servers
...                 OVF2422_OVS16365_Treat iLO default certificate as self-signed with DELETE /rest/certificates/servers
...                 OVF2422_OVS16365_Treat iLO default certificate as self-signed with GET/rest/certificates/servers
...                 OVF2422_OVS16365_Treat_iLO_default_certificate_as_self_signed_with_Get_rest_certificate_https_remote

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

Test Teardown    Clear env   server   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            ilo_default_self_signed_Cert

*** Test Cases ***
OVF2422_OVS16365_Treat_iLO_default_certificate_as_self_signed_with_POST_rest_certificates_servers
    [Documentation]  OVF2422_OVS16365_Treat_iLO_default_certificate_as_self_signed_with_POST_rest_certificates_servers
    Pass Execution If  '${SECURITY_MODE}' == 'CNSA'   Found this is CNSA mode,so skip ILO cert check
    Validator Default ILO Treat AS Self Signed    ${ILO_HOST}
    #import ilo certificate
    ${body} =  Generate Certificate Payload     ${ILO_HOST}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate   ${body}
    Wait For Task2       ${resp}     50    5
    Log    \n - Verify certificate info...    console=True
    Verify Server Certificate Exist In Allcertificates    ${ILO_HOST}
    Verify Leaf Certificate Exist By Aliasname   ${ALIASNAME}
    Verify Server Certificate Trust Status    ${ILO_HOST}    True

    Log    \n - Delete certificate...    console=True
    Remove Server Certificate By Aliasname  ${ALIASNAME}

    Log    \n - Verify certificate info after deleting ...    console=True
    Verify Server Certificate Exist In Allcertificates   ${ILO_HOST}  False
    Verify Server Certificate Trust Status  ${ILO_HOST}   False
