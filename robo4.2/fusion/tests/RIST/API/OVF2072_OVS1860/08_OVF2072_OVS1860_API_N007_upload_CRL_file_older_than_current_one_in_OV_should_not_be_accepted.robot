*** Settings ***
Documentation        OVF2072_OVS1860_API_N007_upload CRL file older than current one in OV should not be accepted

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Variables            ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}         unknown


*** Test Cases ***
OVF2072_OVS1860_API_N007_upload CRL file older than current one in OV should not be accepted
    [Documentation]  OVF2072_OVS1860_API_N007_upload CRL file older than current one in OV should not be accepted

    Log     \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Upload CRL file older than current one in OV should not be accepted...    console=true
    ${localfile} =  Join Path    ${CURDIR}    \    ${CA1_ORIG_PEM_CRL_FILE}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp}=  Fusion Api Upload Crl By Aliasname    ${CA1_ALIASNAME}  ${localfile}

    log   \n response is: \n ${resp}    console=true
    Should Be Equal As Integers       ${resp['status_code']}  400  msg=Status code should be 400, but it's ${resp['status_code']}
    Should Contain                    ${resp['details']}  ${ERR_MSG_OLDER_DETIAL}
    Should Contain                    ${resp['recommendedActions']}  ${ERR_MSG_OLDER_RECOMMAND}

    Log     \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance