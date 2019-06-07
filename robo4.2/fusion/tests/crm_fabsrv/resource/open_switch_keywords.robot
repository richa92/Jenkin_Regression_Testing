*** Settings ***
Library    robot.libraries.String
Library    Collections
Library     String
Library    SSHLibrary
Library    HttpLibrary.HTTP
Variables    open_switch_variables.py

*** Variables ***
${USER_KEY}    user

*** Keywords ***
Reboot via SSH
    [Arguments]  ${switch_mgmt_ip}
    Set Default Configuration   timeout=${SSH_TIMEOUT}
    Open Connection    ${switch_mgmt_ip}    alias=switchReboot
    Wait Until Keyword Succeeds   2 min    5 sec    Login    root    ${EMPTY}
    Start Command   shutdown -r now
    Close Connection

    Sleep     15 seconds    REASON=Give reboot a chance to process - takes 75 seconds on the switch end anyways

    Set Default Configuration   timeout=${SSH_TIMEOUT}
    Open Connection    ${switch_mgmt_ip}    alias=checkReboot
    Wait Until Keyword Succeeds    2 min    5 sec    Login    root    ${EMPTY}
    Close Connection
    Log    Successful reboot of switch

Parse Response For Login Token
    [Arguments]    ${response}
    ${cookie_dict}=    Convert To Dictionary    ${response.cookies}
    Dictionary Should Contain Key    ${cookie_dict}    ${USER_KEY}    msg=Login response cookie missing entry for user
    ${token}=    Get From Dictionary    ${cookie_dict}    ${USER_KEY}
    [Return]    ${token}

Parse Response For VLANs
    [Arguments]    ${response}
    Should Be Valid Json    ${response.content}
    ${vlans}=    Parse Json    ${response.content}
    [Return]  ${vlans}