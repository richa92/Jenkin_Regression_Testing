*** Settings ***
Documentation        OVF2422_OVS18519_CNSA_mode_should_import_CNSA_compatible_certificate


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Teardown        Clear Certs  ${Enable_Aliasname_Chain[0]['type']}  ${Enable_Aliasname_Chain[0]['name']}  ${Enable_Aliasname['type']}  ${Enable_Aliasname['name']}
*** Test Cases ***
OVF2422_OVS18519_CNSA_mode_should_import_CNSA_compatible_cert
    [Documentation]  OVF2422_OVS18519_CNSA_mode_should_import_CNSA_compatible_certificate
    Log  \nrecognize the security-mode...   console=True
    Pass Execution If  '${SECURITY_MODE}' != 'CNSA'   Found this is not CNSA mode,so skip ssh test
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${CNSA_ROOT_CERT}  ${Enable_Aliasname_Chain[0]['name']}
    Log    post /rest/certificate/ca import the CNSA compatible ca cert...    console=True
    ${resp} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import ca root cert
    Wait For Task2       ${resp}      50    5
    ${CERTIFICATE} =  Set Certificate  ${CNSA_LEAF_CERT}  ${Enable_Aliasname['name']}
    Log    post /rest/certificate/servers import CNSA compatible leaf cert...    console=True
    ${resp} =  Fusion Api Import Server Certificate    ${CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import leaf cert
    Wait For Task2         ${resp}       50    5
    Log     import CNSA compatible ca and leaf cert successful as exprcted.    console=True
