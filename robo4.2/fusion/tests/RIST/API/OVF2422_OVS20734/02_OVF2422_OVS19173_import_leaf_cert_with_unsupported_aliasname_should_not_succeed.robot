*** Settings ***
Documentation        OVF2422_OVS19173_import_leaf_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
*** Test Cases ***
OVF2422_OVS19173_import_leaf_cert_with_unsupported_aliasname_should_not_succeed
   [Documentation]  OVF2422_OVS19173_import_leaf_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)
    Log    import_leaf_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)   console=True
    ${CERTIFICATE} =  Set Certificate    ${CNSA_LEAF_CERT}  ${Unable_Aliasname['name']}
    Log    import leafcert with unsupported aliasname not in (Alpha_numeric_space_dot_colon_hyphen_underscore)...     console=True
    ${resp} =  Fusion Api Import Server Certificate    ${CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import leaf cert
    Verify Invalid Aliasname Error  ${resp}  ${Unable_Aliasname['type'][0]}
    Log     import leafcert with unsupported aliasname not in (Alpha_numeric_space_dot_colon_hyphen_underscore) failed as expected    console=True