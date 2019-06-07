*** Settings ***
Documentation        OVF2422_OVS19173_import_CA_inter_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Teardown        Clear Certs  ${Enable_Aliasname_Chain[0]['type']}  ${Enable_Aliasname_Chain[0]['name']}
*** Test Cases ***
OVF2422_OVS19173_import_CA_inter_cert_with_unsupported_aliasname_should_not_succeed
    [Documentation]  OVF2422_OVS19173_import_CA_inter_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)
    Log    import_CA_inter_certificate_with_unsupported_aliasname_should_not_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)   console=True
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${CNSA_ROOT_CERT}  ${Enable_Aliasname_Chain[0]['name']}
    Log    post /rest/certificate/ca import the CA root cert with supprted aliasname...    console=True
    ${resp} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import ca root cert
    Wait For Task2         ${resp}       50    5
    Log     import a ca root cert with supported aliasname successful.    console=True
    ${CA_CERTIFICATE} =  Set Ca Certificate  ${CA_INTER_CERT}  ${Unable_Aliasname['name']}
    Log    post /rest/certificate/ca import the CA inter cert with unsupprted aliasname...    console=True
    ${resp} =  Fusion Api Import External Ca Certificates  ${CA_CERTIFICATE}
    Should Be Equal As Integers  ${resp['status_code']}   202    msg=Fail to import inter cert
    Verify Invalid Aliasname Error    ${resp}  ${Unable_Aliasname['type'][1]}
    Log     Import a ca inter cert with unsupported aliasname failed as expected   console=True