*** Settings ***
Suite Setup    OneView Suite Setup
Suite Teardown    OneView Suite Teardown
Library    RequestsLibrary
Library    Collections
Library    FusionLibrary
Library    SSHLibrary
Variables    ../resource/one_view_variables.py

*** Test Cases ***
Check Ilo-Discovery Service
    Set Default Configuration   prompt=${FUSION_PROMPT}    timeout=${FUSION_TIMEOUT}
    ${Id}=    Open Connection    ${ONE_VIEW_IP}    alias=vctor_ssh
    ${Output}=    Login    ${SSH_USER}    ${SSH_PASSWORD}
    Log    ${Output}
    SSHLibrary.Write    service ilo-discovery status
    ${Output}=    Read until    ${FUSION_PROMPT}
    Log    ${Output}
    Close Connection

Read Server Hardware
    [Documentation]  effort to use the existing fusion library stuff
    ${resp}=    Fusion Api Get Server Hardware
    :FOR    ${server}    IN    @{resp['members']}
    \    Log    ${server['serialNumber']}
    \    Log    ${server['mpHostInfo']['mpHostName']}

Read Networks
    ${response}=    Fusion Api Get Ethernet Networks
    :FOR    ${network}    IN    @{response['members']}
    \    Log    ${network['name']}

*** Keywords ***
OneView Suite Setup
    ${cred}=    Create Dictionary    userName=${API_USER}    password=${API_PASSWORD}
    Fusion API Login Appliance     ${ONE_VIEW_IP}    ${ADMIN_CREDENTIALS}

OneView Suite Teardown
    Fusion Api Logout Appliance

