*** Settings ***
Resource             ../Fusion_Env_Setup/keywords.txt
Resource             ./keywords.txt
Resource             ../../../../Resources/api/fusion_api_resource.txt
Variables            ./Regression_Data2.py

Suite Setup     Precondition Setup
Suite Teardown  Clear Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA

*** Keywords ***
Precondition Setup
    [Documentation]  Setup environment for 2FA API test: add Active Directory with SA binding type, enable 2FA flag.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log   \n-Import certificates for Directory servers...    console=True
    :FOR    ${cert-alias}    IN   @{CERT_ALIAS_PAIRS}
    \       ${cert} =   Get From Dictionary    ${cert-alias}     cert
    \       ${alias} =   Get From Dictionary    ${cert-alias}     alias
    \       Log   \n-Adding certificate ${alias} ...    console=True
    \       ${cert_body}=  Run Keyword If    '${alias}'=='${CNSA_LDAP_LEAF_ALIAS_NAME}' or '${alias}'=='${FIPS_LDAP_LEAF_ALIAS_NAME}'    Generate Leaf Certificate Payload    ${LEAF_CERT_BODY}    ${cert}  ${alias}    ELSE    Generate Certifiate Payload    ${CERT_BODY}  ${cert}  ${alias}
    \       ${resp}=  Run Keyword If    '${alias}'=='${CNSA_LDAP_LEAF_ALIAS_NAME}' or '${alias}'=='${FIPS_LDAP_LEAF_ALIAS_NAME}'   Fusion Api Import Server Certificate    ${cert_body}    ELSE    Fusion Api Import External Ca Certificates    ${cert_body}
    \       Wait For Task2       ${resp}     50    5

    Log   \n-Add directories ...    console=True
    :FOR    ${direct_body}    IN    @{directory}
    \       Log   \n-Adding one directory ...    console=True
    \       ${resp}=  Fusion Api Add Directory  ${direct_body}
    \       Wait For Task2       ${resp}     50    5

    Fusion Api Logout Appliance

Clear Setup
    [Documentation]  clean up environment for 2FA API test: disable 2FA flag, delete Active Directory with SA binding type, and remove root CA.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log   \n-Delete directories ...    console=True
    :FOR    ${logindomain}    IN    @{ALIAS_NAME_LIST}
    \       Log   \n-Deleting directory ${logindomain} ...    console=True
    \       ${name}=  Get Directoy Logindomain Id By Name   ${logindomain}
    \       ${resp}=  Fusion Api Delete Directory    uri=/rest/logindomains/${name}
    \       Wait For Task2       ${resp}     50    5

    Log   \n-Delete certificates ...    console=True
    :FOR    ${alias}    IN    @{CERT_ALIAS_LIST}
    \       Log   \n-Deleting certificate ${alias} ...    console=True
    \       ${resp}=  Run Keyword If    '${alias}'=='${CNSA_LDAP_LEAF_ALIAS_NAME}' or '${alias}'=='${FIPS_LDAP_LEAF_ALIAS_NAME}'    Fusion Api Delete Server Certificate    ${alias}    ELSE    Fusion Api Remove External Ca Certificates    ${alias}
    \       Wait For Task2       ${resp}     50    5

    Fusion Api Logout Appliance
