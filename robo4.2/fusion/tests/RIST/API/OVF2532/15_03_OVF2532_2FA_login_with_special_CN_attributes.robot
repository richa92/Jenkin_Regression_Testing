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
${Subject_certowner}    subjectPatterns

*** Test Cases ***
2FA login with special CN attributes for Subeject cert owner field
    [Documentation]    Can 2FA login with special CN attributes based on correct client certs
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation2}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations

    Log    \n-2FA login with special CN attribute to match only user names starting with "t" use CN=(^t.*$)    console=yes
    ${validation_body} =  Update 2FA validation values    ${Subject_certowner}    ${Subject_certowner_info1[10]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure Subject cert owner
    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[10]}
    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with special CN attribute to match only user names starting with "t" use CN=(^t.*$)

    Log    \n-2FA login with special CN attribute to match only user names containing only numbers CN=(^[0-9]+$)    console=yes
    ${validation_body} =  Update 2FA validation values    ${Subject_certowner}    ${Subject_certowner_info1[12]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure Subject cert owner
    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[12]}
    ${resp} =  2FA Login    ${curl_commands['part12']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with special CN attribute to match only user names containing only numbers CN=(^[0-9]+$)

    Log    \n-2FA login with special CN attribute to match only user names in "LastName, FirstName" format use CN=(^[a-zA-Z]*, [a-zA-Z]+$)    console=yes
    ${validation_body} =  Update 2FA validation values    ${Subject_certowner}    ${Subject_certowner_info1[10]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure Subject cert owner
    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[10]}
    ${resp} =  2FA Login    ${curl_commands['part11']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with special CN attribute to match only user names in "LastName, FirstName" format use CN=(^[a-zA-Z]*, [a-zA-Z]+$)

    Fusion Api Logout Appliance
