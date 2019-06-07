*** Settings ***
Documentation                   Build Initial Template
Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Library                         ./Build_Initial_Template.py

Resource            ../../../fusion/Resources/api/fusion_api_resource.txt

Variables 		    ./Build_data.py

*** Variables ***
${X-API-VERSION}			    500
${IP}                 change_me
${NAME}                change_me
${TYPE}                change_me

#${NAME}                wpst10-eg
#${TYPE}                EG

#${X-API-VERSION}			    200
#${IP}                 16.114.219.157

*** Test Cases ***
Build Initial Template
    [DOCUMENTATION]    Builds the initial template
    ...     You must supply the IP, NAME and TYPE
    ...     pybot -v IP:#.#.#.# -v NAME:Profile-1  -v TYPE:SP   Build_Initial_Template.robot
    ...
    ...     Once executed without errors :-), Expand the last "Log to console and logfile" - Builtin.Log section
    ...     Cut/paste the json as your template.   Make final edits as needed.  Remove non-postable items
    ...     Ideally, add those items to Build_data.py expected_exclude{}
    ...
    ...     You MUST edit your pasted template by replacing null with None, true with True and false with False.


    Set Log Level    level=TRACE
    Log Variables    level=TRACE

    Should Not Be Equal As Strings    ${IP}    change_me
    Should Not Be Equal As Strings    ${NAME}    change_me
    Should Not Be Equal As Strings    ${TYPE}    change_me

    ${admin_session} =    Fusion Api Login Appliance 		${IP}		${admin_credentials}
    ${session} =    Get From List    ${admin_session}     0
    ${status}    ${error} =    Run Keyword And Ignore Error     Get From Dictionary     ${session}    message
    Run Keyword If     '${status}'=='PASS'    Fail    Unable to login: ${error}

    ${responseBody} =    Get Resource    ${TYPE}:${NAME}

    ${responseBody} =    Build_Initial_Template.get    ${response_body}    wordy=${True}

    ${nicelyFormated}    json.dumps    ${responseBody}    indent=${4}
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    null    None
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    true    True
    ${nicelyFormated} =    Replace String    ${nicelyFormated}    false    False

    Create File    BUILT/${TYPE}.temp    ${nicelyFormated}

    Log To Console and Logfile    ${nicelyFormated}

	Fusion Api Logout Appliance