*** Settings ***
Documentation        OVF2072_OVS1860_API_N003_upload duplicated CRL file

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Resource             ./keywords.txt
Variables            ${CURDIR}\\${DATA_FILE}
Variables            ../dto.py

*** Variables ***
${APPLIANCE_IP}         unknown
${rootca_uri}    /rest/certificates/ca/testca1

*** Test Cases ***
OVF2072_OVS1860_API_N003_upload duplicated CRL file
    [Documentation]  OVF2072_OVS1860_API_N003_upload duplicated CRL file

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Add root CA certificate to OV    console=yes
    Import rootca certificate    ${ca_cert_body}    ${rootca_uri}
    ${localfile_1} =  Join Path    ${CURDIR}    \    ${CA1_ORIG_PEM_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile_1}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile_1}
    Sleep    30s

    Log    \n-Upload duplicated CRL file...    console=true
    ${localfile} =  Join Path    ${CURDIR}    \    ${CA1_ORIG_PEM_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile}
    Sleep    30s

    log   \n response is: \n ${resp}    console=true
    Should Be Equal As Integers       ${resp['status_code']}  ${CRL_DUPLICATE_ERROR_STATUS_CODE}  msg=Status code should be ${CRL_DUPLICATE_ERROR_STATUS_CODE}, but it's ${resp['status_code']}
    Should Contain                    ${resp['details']}  ${ERR_MSG_DUPLICATE_DETIAL}
    Should Contain                    ${resp['recommendedActions']}  ${ERR_MSG_DUPLICATE_RECOMMAND}

    Log     \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance