*** Settings ***
Documentation        Can 2FA login with correct validaiton configurations
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
${cert_domain}          certificateDomainIdentifier
${domain_pattern}       certificateDomainIdentifierPattern
${cert_OID}    validationOids
${SAN_certowner}    subjectAlternateNamePatterns
${Subject_certowner}    subjectPatterns

*** Test Cases ***
2FA login with correct validation configurations
    [Documentation]    Can 2FA login with correct validation configurations that meet attributes in client cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation1}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations

    Log    \n-2FA login with Subject domain    console=yes
    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[0]}    ${domain_pattern}    DC=(.*)
    ${resp1} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp1['status_code']}'    '200'    msg= Fail to configure domain value
    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[0]}

    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with Subject domain


    Log    \n-2FA login with Issuer domain    console=yes
    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[2]}    ${domain_pattern}    DC=(.*)
    ${resp1} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp1['status_code']}'    '200'    msg= Fail to configure domain value
    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[2]}

    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '200 OK'    msg=2FA login fail


    Log    \n-2FA login with correct manually specify domain    console=yes
    :For    ${item}    In    @{manually_specify_domain_values[0:5]}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[3]}    ${domain_pattern}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to configure correct domain values
    \    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[3]}
    \    Check updated 2FA validation configurations    ${domain_pattern}    ${item}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '200 OK'    msg=2FA login fail


    Log    \n-2FA login with correct OID boxes    console=yes
    :For    ${item}    In    @{manually_specify_domain_values[0:4]}
    \    ${validation_body} =  Update 2FA Validation Domain Values    ${cert_domain}    ${correct_domain_names[3]}    ${domain_pattern}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to configure correct domain values
    \    Check updated 2FA validation configurations    ${cert_domain}    ${correct_domain_names[3]}
    \    Check updated 2FA validation configurations    ${domain_pattern}    ${item}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '200 OK'    msg=2FA login fail


    Log    \n-2FA login without OID box    console=yes
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${blank_list}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to delete OID boxes from OV
    Check updated 2FA validation configurations    ${cert_OID}    ${blank_list}
    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with correct OID boxes


    Log    \n-2FA login with correct SAN cert owner    console=yes
    :For    ${index}    IN RANGE    0    1
    \    ${validation_body} =  Update 2FA validation values    ${SAN_certowner}    ${SAN_certowner_info1[${index}]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure SAN cert owner
    \    Check updated 2FA validation configurations    ${SAN_certowner}    ${SAN_certowner_info1[${index}]}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with correct SAN cert owner
    Fusion Api Logout Appliance


    Log    \n-2FA login with correct Subject cert owner    console=yes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation2}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations
    :For    ${index}    IN RANGE    0    1
    \    ${validation_body} =  Update 2FA validation values    ${Subject_certowner}    ${Subject_certowner_info1[${index}]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure Subject cert owner
    \    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[${index}]}
    \    ${resp} =  2FA Login    ${curl_commands['part2']}
    \    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with correct Subject cert owner
    Fusion Api Logout Appliance
