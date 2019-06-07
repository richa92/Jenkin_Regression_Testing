*** Settings ***
Documentation        Cannot configure manually specify directory domain with incorrect values
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
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_doamin}    certificateDomainIdentifier
${domain_pattern}   certificateDomainIdentifierPattern


*** Test Cases ***
Set manually specify cert domain with incorrect values
    [Documentation]    Configure manually specify cert domain with incorrect values , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${value}    IN    @{invalid_domain_values2}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[3]}    ${domain_pattern}    ${value}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot configure manually specify cert domain with invalid values
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Invalid_domain_value_error2']}'    msg= Show incorrect error message when configure manually specify cert domain with invalid values
    Fusion Api Logout Appliance
