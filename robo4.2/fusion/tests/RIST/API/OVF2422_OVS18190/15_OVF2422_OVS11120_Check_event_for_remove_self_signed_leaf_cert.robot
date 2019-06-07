*** Settings ***
Documentation        Should show correct event message for remove self signed leaf cert
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
Resource             ./../../../../Resources/api/activity/tasks.txt
Resource             ./keywords.txt
Variables            ../dto.py
Variables            ${DATA_FILE}


*** Variables ***
${selfsigned_leafcert_uri}    /rest/certificates/servers/leaf_cert
${leafcert_aliasname}    leaf_cert

*** Test Cases ***
Check event for remove self signed leaf cert
    [Documentation]    Check whether the event message for remove self signed leaf cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Delete Server Certificate    ${leafcert_aliasname}
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove self signed leaf cert
    Wait For Task2    ${resp}    2min    5
    ${get_cert} =  Fusion Api Get Server Certificate    ${selfsigned_leafcert_uri}
    Should Be Equal    '${get_cert['status_code']}'    '404'    msg=Fail to retrieve the self signed leaf cert
    Should Be Equal    ${get_cert['message']}    ${leaf_cert_error}    msg=Cannot find the self signed leaf cert
    ${resp} =  Fusion Api Get Task    uri=${resp${TASK_URI}}
    Should Be Equal    '${resp['name']}'    '${alert_messages['Remove_Cert_Name']}'    msg=Incorrect message for removing self signed leaf cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Remove_leaf_cert']}
    Fusion Api Logout Appliance
