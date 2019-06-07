*** Settings ***
Documentation        OVF688(ovs5874)_API_N0003_ Self - signed leaf certificate with invalid x.509 Version should not be imported by POST / rest / certificates / servers/
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}

*** Test Cases ***
Self signed leaf certificate with invalid x509 Version should not be imported by POST
    Log   Self - signed leaf certificate with invalid x.509 Version should not be imported by POST /rest/certificates/servers/    console=True
    Log    \n - Import invalid x509 certificate    console=True
    set to dictionary   ${CERTIFICATE['certificateDetails'][0]}    base64Data   ${LINUX_CERT_WITH_INVALID_X509}
    ${resp} =  Fusion Api Import Server Certificate    ${CERTIFICATE}
    Wait For Task2       ${resp}     50    5   PASS=Error   errorMessage=Invalid_X509_Cert
    Log   \n - X509 version is not valid, so can not be imported    console=True