*** Settings ***
Documentation        OVF2422_OVS19173_import_leaf_certificate_with_supported_aliasname_should_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Teardown        Clear Certs   ${Enable_Aliasname['type']}  ${Enable_Aliasname['name']}
*** Test Cases ***
OVF2422_OVS19173_import_leaf_cert_with_supported_aliasname_should_succeed
    [Documentation]  OVF2422_OVS19173_import_leaf_certificate_with_supported_aliasname_should_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)

    Log    import_leaf_certificate_with_supported_aliasname_should_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed    console=True
    ${CERTIFICATE} =  Set Certificate    ${CNSA_LEAF_CERT}  ${Enable_Aliasname['name']}
    Log    post /rest/certificate/servers import leafcert with aliasname in (Alpha_numeric_space_dot_colon_hyphen_underscore)...    console=True
    ${resp} =  Fusion Api Import Server Certificate    ${CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import LEAF cert
    Wait For Task2         ${resp}       50    5
    Log     import leafcert with aliasname in (Alpha_numeric_space_dot_colon_hyphen_underscore) successful    console=True