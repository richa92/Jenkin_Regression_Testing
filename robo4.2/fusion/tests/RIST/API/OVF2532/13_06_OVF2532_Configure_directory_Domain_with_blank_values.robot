*** Settings ***
Documentation        Cannot configure directory domain with blank values
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
${cert_doamin}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern


*** Test Cases ***
Configure directory domain with blank values
    [Documentation]    Configure 2FA cert domain with blank values , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \nCannot configure Subject directory domain with blank values    console=yes
    @{index_list} =  Create List    0    1
    ${index} =  Set Variable    0
    :For    ${index}    IN    @{index_list}
    \    ${validation_body1} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[0]}    ${domain_pattern}    ${blank_values_list[${index}][0]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body1}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure Subject directory domain with blank value
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_domain_error']}'    msg= Show incorrect error message when fail to configure directory domain with blank value

    Log    \nCannot configure SAN directory domain with blank values    console=yes
    :For    ${index}    IN    @{index_list}
    \    ${validation_body2} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[1]}    ${domain_pattern}    ${blank_values_list[${index}][0]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body2}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure SAN directory domain with blank value
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_domain_error']}'    msg= Show incorrect error message when fail to configure directory domain with blank value

    Log    \Cannot configure Issuer directory domain with blank values    console=yes
    :For    ${index}    IN    @{index_list}
    \    ${validation_body3} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[2]}    ${domain_pattern}    ${blank_values_list[${index}][0]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body3}
    \    Should be equal    '${resp['status_code']}'  '400'  msg= Cannot configure Issuer directory domain with blank value
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_domain_error']}'    msg= Show incorrect error message when fail to configure directory domain with blank value

    Log    \Cannot configure manually specify directory domain with blank values    console=yes
    :For    ${index}    IN    @{index_list}
    \    ${validation_body4} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[3]}    ${domain_pattern}    ${blank_values_list[${index}][0]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body4}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure manually specify directory domain with blank value
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_domain_error']}'    msg= Show incorrect error message when fail to configure directory domain with blank value

    Fusion Api Logout Appliance
