*** Settings ***
Documentation        OVF2072_OVS1860_API_P004_update CRL by a file with different format

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
OVF2072_OVS1860_API_P004_update CRL by a file with different format
    [Documentation]  OVF2072_OVS1860_API_P004_update CRL by a file with different format

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Add root CA certificate to OV    console=yes
    Import rootca certificate    ${ca_cert_body}    ${rootca_uri}
    Log    \n-Update CRL by a file with different format...    console=true
    ${localfile_1} =  Join Path    ${CURDIR}    \    ${CA1_ORIG_PEM_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile_1}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile_1}
    Sleep    30s

    ${localfile} =  Join Path    ${CURDIR}    \    ${CA1_NEW_DER_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile}
    Sleep    30s

    log   \n response is: \n ${resp}    console=true
    ${stat_code}=  Convert To String    ${resp['status_code']}
    Run Keyword If  '${stat_code}' == '202'    Wait For Task2       ${resp}     50    5
    ...  ELSE       Should Be Equal As Integers          ${resp['status_code']}  202  msg=Status code should be 202, but it's ${resp['status_code']}

    Log     \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance