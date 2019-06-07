*** Settings ***
Documentation        Can configure manually specify directory domain with correct values
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
Set maniually specify cert domain with correct values
    [Documentation]    Configure correct manually specify cert domain name , it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${value}    IN    @{manually_specify_domain_values}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_doamin}    ${correct_domain_names[3]}    ${domain_pattern}    ${value}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to set correct domain
    \    Check updated 2FA validation configurations    ${domain_pattern}    ${value}
    Fusion Api Logout Appliance
