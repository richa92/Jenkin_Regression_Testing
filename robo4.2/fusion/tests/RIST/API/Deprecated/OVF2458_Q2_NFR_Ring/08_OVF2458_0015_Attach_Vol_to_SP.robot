*** Settings ***
Documentation   Attaches Volumes to Existing Assigned Server profiles.
...             12 attachments each.  1 Private Existing, 1 Private New, 10 Shared

Resource        ../../../../Resources/api/fusion_api_resource.txt

#Variables       ./build_volAttach.py

Library         ./pythonHelperFunctionsCGW.py

Suite Setup       Run Keyword    Set Log Level    DEBUG
Suite Teardown    Fusion Api Logout Appliance

*** Variables ***
# used for development on Daisy
&{P1}                      name=CN754406WS_Bay_9_480_1
&{P2}                      name=MXQ7100868_Bay_7_480_1
&{P3}                      name=CN754404R9_Bay_3_480_1
@{members}                  ${P1}    ${P2}    ${P3}

*** Test Cases ***
OVF2458 Attach Volumes to Server Profiles
    [Documentation]    Attaches Volumes to Existing Assigned Server profiles.
   	[Tags]    Performance    server_profiles-condition-everything
    [Setup]                           Run Keyword and Ignore Error    Write To ciDebug Log

#   If executed via __init__.robot, will be logged in thus don't login again.
    ${active} =    Run Keyword and Return Status    Fusion Api Get Active User
    Run Keyword if    '${active}'=='False'    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Attach Volumes to Server Profiles

    [Teardown]                        Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Attach Volumes to Server Profiles
	[Documentation]	GET server profile then create sanStorage item, attach to payload and PUT back to profile

# This section is for Daisy volume attachments
    Power off ALL Servers
    ${profiles} =     Fusion Api Get Server Profiles  param=?sort=name:ascending
    @{task_list} =    Create List
    :FOR    ${member}     in    @{profiles['members']}
    \    Log    profile: ${member['name']}    console=yes
    \    Remove From Dictionary    ${member}    headers
    \    Remove From Dictionary    ${member}    state
    \    Remove From Dictionary    ${member}    status
    \    Remove From Dictionary    ${member}    status_code
    \    ${new_sanStorage} =    Vol Attach Helper    ${profile_sanStorage['${member['name']}']}
    \    Set To Dictionary    ${member}    sanStorage    ${new_sanStorage['sanStorage']}
#    \    Log    NSS:${new_sanStorage}
    \    ${resp} =     Fusion Api Edit Server Profile        body=${member}        uri=${member['uri']}
    \    Append To List    ${task_list}    ${resp}

    # Wait on all profile updates
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
    Wait For Task2    ${task_list}    timeout=600    interval=20


# This section is used for development on Daisy
#    :FOR    ${member}    in    @{members}
#    \    ${new_sanStorage} =    Vol Attach Helper    ${profile_sanStorage['${member['name']}']}
#    \    Log    ${new_sanStorage['sanStorage']}    console=yes

# This setion is used for dev on Ring 1/2
#    ${resource} =    Get Resource    SP:RonProfile
#    ${new_sanStorage} =    Vol Attach Helper    ${ron_sanStorage['RonProfile']}
#    Set To Dictionary    ${resource}    sanStorage    ${new_sanStorage['sanStorage']}
#    Remove From Dictionary    ${resource}    headers
#    Remove From Dictionary    ${resource}    state
#    Remove From Dictionary    ${resource}    status
#    Remove From Dictionary    ${resource}    status_code
#    Log    ${resource}
#    ${resp} =     Fusion Api Edit Server Profile        body=${resource}        uri=${resource['uri']}
#    Wait For Task2    ${resp}    timeout=300    interval=20

Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
