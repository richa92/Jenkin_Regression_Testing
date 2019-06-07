*** Settings ***
Documentation        OV should send corrent event message for add selfsigned leaf cert
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
Check event for add self signed leaf cert
    [Documentation]    Check whether the event for add self-sgiend leaf cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${add_leafcert} =  Fusion Api Import Server Certificate    ${self_signed_leaf_cert}
    Should be equal    '${add_leafcert['status_code']}'    '202'    msg=Fail to add self signed leaf cert
    Wait For Task2    ${add_leafcert}    30    5
    ${retrieve_leafcert} =  Run Keyword And Return Status    Fusion Api Get Server Certificate    ${leafcert_aliasname}
    Should Be Equal    '${retrieve_leafcert}'    '${True}'    msg=Cannot find the self signed leaf certificate
    ${resp} =  Fusion Api Get Task    uri=${add_leafcert${TASK_URI}}
    Should be equal    '${resp['name']}'    '${alert_messages['Add_Cert_Name']}'    msg=Incorrect message for adding self signed leaf cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Add_leaf_Cert']}
    Fusion Api Logout Appliance
