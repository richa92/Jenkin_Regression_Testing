*** Settings ***
Documentation        OVF2422_OVS19173_import_ca_root_intemedaite_and_leaf_certificate_with_supported_aliasname_should_successfully(only_Alphanumeric_space_dot_colon_hyphen_underscore_are_allowed.)


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Teardown        Clear Certs  ${Enable_Aliasname_Chain[0]['type']}  ${Enable_Aliasname_Chain[0]['name']}  ${Enable_Aliasname_Chain[1]['type']}  ${Enable_Aliasname_Chain[1]['name']}
*** Test Cases ***
OVF2422_import_ca_root_intemedaite_and_leaf_cert_with_supported_aliasname_should_succeed
    [Documentation]  OVF2422_OVS19173_import_ca_root_intemedaite_and_leaf_certificate_with_supported_aliasname_should_successfully(only_Alphanumeric_space_dot_colon_hyphen_underscore_are_allowed.)
    Log    import_ca_root_intemedaite_and_leaf_certificate_with_supported_aliasname_should_successfully(only_Alpha_numeric_space_dot_colon_hyphen_underscore_are_allowed.)   console=True
    ${SERVER_CERTIFICATE_CHAIN} =  Set Server Certificate Chain  ${CA_LEAF_CERT}  ${Enable_Aliasname_Chain[2]['name']}  ${CA_INTER_CERT}  ${Enable_Aliasname_Chain[1]['name']}  ${CNSA_ROOT_CERT}  ${Enable_Aliasname_Chain[0]['name']}
    Log    post /rest/certificate/servers import the ca root intemedaite and leaf cert with supprted aliasname...    console=True
    ${resp} =  fusion api import server certificate  ${SERVER_CERTIFICATE_CHAIN}
    Log    ${resp}    console=True
    Should Be Equal As Integers  ${resp['status_code']}    202    msg=Fail to import ca root intemedaite and leaf cert
    Wait For Task2         ${resp}       50    5
    Log    import ca root intemedaite and leaf cert with supported aliasname in(Alpha_numeric_space_dot_colon_hyphen_underscore) successful    console=True

