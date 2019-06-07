*** Settings ***
Documentation     OVF2422_OVS18519_FIPS_mode_should_not_import_non-FIPS_compatible_certificate


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
*** Test Cases ***
OVF2422_OVS18519_FIPS_mode_should_not_import_non-CNSA_compatible_cert
    [Documentation]  OVF2422_OVS18519_FIPS_mode_should_not_import_non-_FIPS_compatible_certificate
    Log  \nrecognize the security-mode...   console=True
    Pass Execution If  '${SECURITY_MODE}' != 'FIPS'   Found this is not FIPS mode,so skip test
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${LEGACY_ROOT_CERT}  ${Enable_Aliasname_Chain[0]['name']}
    Log    post /rest/certificate/ca import the non-FIPS compatible ca cert...    console=True
    ${resp} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import ca root cert
    Wait For Task2       ${resp}      50    5    PASS=Error     errorMessage=Invalid_Public_Key_Length_FIPS_CNSA
    ${CERTIFICATE} =  Set Certificate  ${NON_FIPS_LEAF_CERT}  ${Enable_Aliasname['name']}
    Log    post /rest/certificate/servers import non-FIPS compatible leaf cert...    console=True
    ${resp} =  Fusion Api Import Server Certificate    ${CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import leaf cert
    Wait For Task2       ${resp}      50    5    PASS=Error     errorMessage=Invalid_Public_Key_Length_FIPS_CNSA
    Log     import non-FIPS compatible ca and leaf cert failed as exprcted.    console=True