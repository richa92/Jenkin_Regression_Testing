*** Settings ***
Documentation        OVF2072_OVS1860_API_P003_update CRL by a file with same format

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Resource             ./keywords.txt
Variables            ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}         unknown


*** Test Cases ***
OVF2072_OVS1860_API_P003_update CRL by a file with same format
    [Documentation]  OVF2072_OVS1860_API_P003_update CRL by a file with same format

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Update CRL by a file with same format...    console=true
    ${localfile} =  Join Path    ${CURDIR}    \    ${CA1_NEW_PEM_CRL_FILE}
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