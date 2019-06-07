*** Settings ***
Documentation        OVF2072_OVS1860_API_P002_upload CRL file in DER format

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
OVF2072_OVS1860_API_P002_upload CRL file in DER format
    [Documentation]  OVF2072_OVS1860_API_P002_upload CRL file in DER format

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Add root CA certificate to OV    console=yes
    Import rootca certificate    ${ca_cert_body}    ${rootca_uri}
    Log    \n-Upload CRL file in DER format...    console=true
    ${localfile} =  Join Path    ${CURDIR}    \    ${CA2_ORIG_DER_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile}

    log   \n response is: \n ${resp}    console=true
    ${stat_code}=  Convert To String    ${resp['status_code']}
    Run Keyword If  '${stat_code}' == '202'    Wait For Task2       ${resp}     50    5
    ...  ELSE       Should Be Equal As Integers          ${resp['status_code']}  202  msg=Status code should be 202, but it's ${resp['status_code']}
    Log    \n-Delete root CA certificate from OV    console=yes
    Delete rootca certificate    ${CA1_ALIASNAME}

    Log     \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance