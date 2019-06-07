*** Settings ***
Documentation        Cannot configure SAN/Subject/Issuer directory domain with incorrect values
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./../../../../Resources/api/common/common.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_domain}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern


*** Test Cases ***
Set SAN / Subject / Issuer directory domain with incorrect values
    [Documentation]    Configure SAN / Subject / Issuer directory domain with wrong values , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \nConfigure Subject directory domain with incorrect values    console=yes
    :For    ${value}    IN    @{invalid_domain_values1}
    \    ${validation_body1} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[0]}    ${domain_pattern}    ${value}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body1}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure directory domain with invalid values
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Invalid_domain_value_error1']}'    msg= Show incorrect error message for invalid domain values

    Log    \nConfigure SAN directory domain with incorrect values    console=yes
    :For    ${value}    IN    @{invalid_domain_values1}
    \    ${validation_body2} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[1]}    ${domain_pattern}    ${value}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body2}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure directory domain with invalid values
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Invalid_domain_value_error1']}'    msg= Show incorrect error message for invalid domain values

    Log    \nConfigure Issuer directory domain with incorrect values    console=yes
    :For    ${value}    IN    @{invalid_domain_values1}
    \    ${validation_body3} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[2]}    ${domain_pattern}    ${value}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body3}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure directory domain with invalid values
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Invalid_domain_value_error1']}'    msg= Show incorrect error message for invalid domain values

    Fusion Api Logout Appliance
