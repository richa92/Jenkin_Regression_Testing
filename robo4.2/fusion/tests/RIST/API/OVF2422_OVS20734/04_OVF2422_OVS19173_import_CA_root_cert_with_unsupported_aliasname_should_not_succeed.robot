*** Settings ***
Documentation        OVF2422_OVS19173_import_CA_root_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
*** Test Cases ***
OVF2422_OVS19173_import_CA_root_cert_with_unsupported_aliasname_should_not_succeed
    [Documentation]  OVF2422_OVS19173_import_CA_root_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)
    Log    import_CA_root_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)   console=True
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${CNSA_ROOT_CERT}  ${Unable_Aliasname['name']}
    Log    post /rest/certificate/ca import the CA root cert with unsupprted aliasname...    console=True
    ${resp} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import ca root cert
    Verify Invalid Aliasname Error    ${resp}  ${Unable_Aliasname['type'][1]}
    Log     import a ca root cert with unsupported aliasname not in (Alpha_numeric_space_dot_colon_hyphen_underscore) failed    console=True