 *** Settings ***
Documentation       Dtask Script Of Support-Tools
Library                RoboGalaxyLibrary
Library                Collections
Library                String
Library                FusionLibrary
Library             tests.ovs.OvsLibrary
Variables           Supportool_data.py

 *** Variables ***

${SSH_HOST}
${param}    ?filter="taskType=User"&deleteNonTerminalTasks=true
${event_param}    ?waitToProcess=true
 *** Keyword ***

Get Trusted Token
    [Documentation]    Get Trusted Token for creating task
    ${Response}    ${AUTHTOKEN}    tests.ovs.OvsLibrary.Fusion Api Login Appliance    ${SSH_HOST}    ${admin1_credentials}
    ${Pri_Key} =          SSHLibrary.Execute Command         /ci/bin/./get-trustedtoken.sh 'DigitalSig'
    Log    ${Pri_Key}
    [Return]    ${Pri_Key}

Parse Dictionary Key Value Pair
    [Documentation]     Parse Dictionary Key Value Pair
    [Arguments]    ${dtask}
    ${Output}=    Create Dictionary
    ${dlines} =     Split To Lines    ${dtask}    4
    :FOR    ${line}    IN    @{dlines}
    \    ${key}    ${value}=    Split String From Right    ${line}    |     1
    \    Set To Dictionary     ${Output}    ${key.strip()}    ${value.strip()}
    Log Dictionary    ${Output}
    [Return]    ${Output}

Parse Dictionary Key Value Pair For Event
    [Documentation]     Parse Dictionary Key Value Pair
    [Arguments]    ${dtask}
    ${Output}=    Create Dictionary
    ${dlines} =     Split To Lines    ${dtask}    3
    :FOR    ${line}    IN    @{dlines}
    \    ${key}    ${value}=    Split String From Right    ${line}    |     1
    \    Set To Dictionary     ${Output}    ${key.strip()}    ${value.strip()}
    Log Dictionary    ${Output}
    [Return]    ${Output}

Create Task
    [Documentation]        Create task in Fusion
    [Arguments]        ${api}=800
    ${trusted_token} =    dtaskResource.Get Trusted Token
    Login to OV Via REST API
    ${Response}=    Fusion Api Create Task Trusted Token       ${task}     ${api}    auth=${trusted_token}
    ${status}=        Get From Dictionary        ${Response}        status_code
    Log     ${status}
    Log    ${Response}
    Should Contain    ['200','201','202','203']       '${status}'        msg=Failed to Trigger Create Task. Verify it manually.
    ${uri}=        Get From Dictionary        ${Response}        uri
    ${taskid}    Fetch From Right    ${uri}    /
    Log    Task Created with TaskID:${taskid}    console=True
    [Return]    ${taskid}

Delete Task
    [Documentation]     Delete Task
    [Arguments]    ${api}=800
    Login to OV Via REST API
    ${Response} =     Fusion Api Delete Task     ${uri}    ${api}      auth=${trusted_token}    param=${param}
    ${status}=        Get From Dictionary        ${Response}        status_code
    Log     ${status}
    Log    ${Response}
    ${dstatus} =     Run Keyword and Return Status    Should Contain    ['204']       '${status}'        msg=Failed to Delete Task. Verify it manually.
    [return]    ${dstatus}

Dtask Event Check
    [Documentation]    Execute dtask script and verify the output
    ${taskid} =    Create Task
    ${dtasklist} =    Create Dictionary
    ${dtaskdelete} =    Create Dictionary
    ${tid} =          SSHLibrary.Execute Command         psql -A -t --dbname=cidb --user=postgres -c "select id from taskt.taskentity where id = '${taskid}';"
    Log    Entry in DB found With created TaskID:${tid}    console=True
    ${dtasklist} =     SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && ./dtask.py -l Running
    ${Output} =     Parse Dictionary Key Value Pair    ${dtasklist}
    ${status} =     Run Keyword and Return Status    Dictionary Should Contain Value    ${Output}    ${tid}    msg=Dtask Script Failed to list the Task
    Log    STATUS OF DTASK LIST:${status}    console=True
    Run Keyword If    '${status}' != 'True'    Fail    ********Dtask Verification for Listing the task Failed********
    ...    ELSE IF    '${status}' == 'True'    Log    ********Dtask Verification for Listing the task Passed******    console=true
    ${dstatus} =    SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && yes | ./dtask.py -dt -i ${taskid}
    ${delid} =          SSHLibrary.Execute Command         psql -A -t --dbname=cidb --user=postgres -c "select id from taskt.taskentity where id = '${taskid}';"
    Log    Entry in DB Not found With Deleted TaskID:${delid}    console=True
    ${dtaskdelete} =     SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && ./dtask.py -l Running
    ${dOutput} =    Parse Dictionary Key Value Pair    ${dtaskdelete}
    ${delstatus} =     Run Keyword and Return Status     Dictionary Should Not Contain Value    ${dOutput}    ${taskid}    msg=Dtask Script Failed to delete the Task
    Log    STATUS of DELETE TASK:${delstatus}    console=True
    Run Keyword If    '${delstatus}' != 'True'    Fail    ********Dtask Verification for Deleting the task Failed********
    ...    ELSE IF    '${delstatus}' == 'True'    Log    ********Dtask Verification for Deleting the task Passed********    console=True

Dtask Help Command
    [Documentation]    Verify the help command of Dtask Script of support tools
    ${Output}=  SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && ./dtask.py -h
    ${status}=    Run Keyword and Return Status    Should Contain   ${Output}    ${dtask_help}
    Run Keyword If    '${status}' != 'True'    Fail    ********Dtask Verification for Help Command Failed********
    ...    ELSE IF    '${status}' == 'True'    Log    ********Dtask Verification for Help Command Passed********    console=True

Create Event
    [Documentation]    Create an Event in Fusion and wait until event is processed with its respective alert
    [Arguments]        ${api}=800
    ${trusted_token} =    dtaskResource.Get Trusted Token
    Login to OV Via REST API
    ${Response}=    Fusion Api Create Event Trusted Token       ${event}     ${api}    auth=${trusted_token}    param=${event_param}
    ${status}=        Get From Dictionary        ${Response}        status_code
    Log     ${status}
    Log    ${Response}
    Should Contain    ['200','201','202','203']       '${status}'        msg=Failed to Trigger Create Event. Verify it manually.
    ${uri}=        Get From Dictionary        ${Response}        uri
    ${eventid}    Fetch From Right    ${uri}    /
    Log    Event Created with EventID:${eventid}    console=True
    [Return]    ${eventid}

Dtask Alert Check
    [Documentation]    Execute dtask script and verify the output for alerts
    ${EventId} =    Create Event
    ${alertlist} =    Create Dictionary
    ${aid} =    Create Dictionary
    ${aid} =    SSHLibrary.Execute Command    psql -At -d cidb -U postgres -c 'select alertid from "health-services".event where id = '${eventid}';'
    Log    Entry in DB found With created AlertID:${aid}    console=True
    ${alert_uri} =    Catenate    SEPARATOR=    ${alert_uri}    ${aid}
    ${alertlist} =     SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && yes | ./dtask.py -a Cleared
    ${Output} =     Parse Dictionary Key Value Pair For Event    ${alertlist}
    ${status} =     Run Keyword and Return Status    Dictionary Should Contain Value    ${Output}    ${aid}    msg=Dtask Script Failed to list the Task
    Log    STATUS OF DTASK LIST FOR ALERTS:${status}    console=True
    Run Keyword If    '${status}' != 'True'    Fail    ********Dtask Verification for Listing the alert Failed********
    ...    ELSE IF    '${status}' == 'True'    Log    ********Dtask Verification for Listing the alert Passed******    console=True
    ${dstatus} =    SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && yes | ./dtask.py -da -i ${aid}
    ${del_alert_id} =    SSHLibrary.Execute Command    psql -A -t -d cidb -U postgres -c 'select id from "health-services".alert where id = '${aid}';'
    Log    Entry in DB Not found With Deleted AlertID:${del_alert_id}    console=True
    ${dtask_Alert_delete} =     SSHLibrary.Execute Command    cd /ci/support/ovsupportability/scripts/ && ./dtask.py -a Cleared
    ${aOutput} =    Parse Dictionary Key Value Pair For Event    ${dtask_Alert_delete}
    ${delstatus} =     Run Keyword and Return Status     Dictionary Should Not Contain Value    ${aOutput}    ${aid}    msg=Dtask Script Failed to delete the Alert
    Log    STATUS of DELETE ALERT:${delstatus}    console=True
    Run Keyword If    '${delstatus}' != 'True'    Fail    ********Dtask Verification for Deleting the alert Failed********
    ...    ELSE IF    '${delstatus}' == 'True'    Log    ********Dtask Verification for Deleting the alert Passed********    console=True
    [return]    ${alert_uri}