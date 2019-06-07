*** Settings ***
Documentation        OVF2072_OVS1860_API_N001_upload CRL file in wrong format

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Resource             ./keywords.txt
Variables            ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}         unknown
${rootca_uri}    /rest/certificates/ca/testca1

*** Test Cases ***
OVF2072_OVS1860_API_N001_upload CRL file in wrong format
    [Documentation]  OVF2072_OVS1860_API_N001_upload CRL file in wrong format

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Add root CA certificate to OV    console=yes
    Import rootca certificate    ${ca_cert_body}    ${rootca_uri}
    Log    \n-Uploading CRL file in wrong format ...    console=true
    ${localfile} =  Join Path    ${CURDIR}    \    ${CA1_MAL_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile}

    log   \n response is: \n ${resp}    console=true
    Should Be Equal As Integers       ${resp['status_code']}  400  msg=Status code should be 400, but it's ${resp['status_code']}
    Should Contain                    ${resp['details']}  ${ERR_MSG_WRONG_DETIAL}
    Should Contain                    ${resp['recommendedActions']}  ${ERR_MSG_WRONG_RECOMMAND}
    Log    \n-Delete root CA certificate from OV    console=yes
    Delete rootca certificate    ${CA1_ALIASNAME}

    Log     \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance