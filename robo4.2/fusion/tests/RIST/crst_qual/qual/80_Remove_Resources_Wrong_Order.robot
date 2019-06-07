*** Settings ***
Documentation        Remove Resources Incorrect Order
Resource             ../resource.txt
Resource             ../plexxi.txt

Variables            ../Common.py
Variables            ../${DATA_FILE}

Suite Setup          QUAL Suite Setup    ${admin_credentials}
Suite Teardown       QUAL Suite Teardown

*** Test Cases ***
Attempt Remove Rack Servers With Profile Applied
    [Tags]    80    RM_DL_NEG

    ${assigned}    ${unassigned} =    Get Profiles Assigned Counts
    Log    Assigned Profiles: ${assigned}    console=${CONSOLE}
    Log    Unassigned Profiles: ${unassigned}    console=${CONSOLE}

    Set Suite Variable    ${Assigned_Not_Removed)    0

    ${resp} =     Fusion Api Get Server Hardware
    ${count}=    Convert To String  ${resp['count']}
    Run Keyword If    '${count}'=='0'    Log    No Server Hardware to remove
    Return From Keyword If    '${count}'=='0'
    :FOR    ${sh}    IN    @{resp['members']}
    \    Run Keyword If    '${sh['state']}'=='ProfileApplied'     Remove SH Neg    ${sh['uri']}
    \    Run Keyword If    '${sh['state']}'=='NoProfileApplied'    Log    ${sh['name']} does not have a profile

    Log   Assigned Not Removed Should Equal Assigned: ${Assigned_Not_Removed}
    Should Be Equal As Integers    ${assigned}    ${Assigned_Not_Removed}

Attempt Remove Logical Switch Group While In Use
    [Tags]    80    RM_LSG_NEG
    ${uri} =    Get LSG URI    ${LSG_NAME}
    ${resp} = 	Fusion Api Delete LSG		uri=${uri}
	Should Be Equal As Integers    ${resp['status_code']}    ${BADREQUEST}
    Should Match Regexp    ${resp['message']}    A logical switch group cannot be deleted while it is being referenced by logical switches.

Attempt Remove Logical Switch While In Use
    [Tags]    80    RM_LS_NEG
    ${uri} =    Get LS URI    ${LS_NAME}
    ${resp} = 	Fusion Api Delete LS		uri=${uri}
	Should Be Equal As Integers    ${resp['status_code']}    ${BADREQUEST}
    Should Match Regexp    ${resp['message']}    The logical switch cannot be deleted while profiles are assigned to ports within this logical switch.

Attempt Remove Fabric While In Use
    [Tags]    80    RM_FABRIC_NEG
    ${uri} =    Get Fabric Uri By Name    ${FABRIC_NAME}
    ${resp} = 	Fusion Api Delete Fabric		uri=${uri}
	Wait For Task2    ${resp}    PASS=Error    errorMessage=FABRIC_DELETE_SWITCH_ASSOCIATED_WITH_LS

*** Keywords ***
Remove SH Neg
    [Documentation]      Removes SH expecting a failure as a profile is still applied
    [Arguments]    ${uri}
    ${resp} =     Fusion Api Delete Server Hardware        uri=${uri}
    Should Be Equal As Integers    ${resp['status_code']}    ${FORBIDDEN}
    Should Match Regexp    ${resp['message']}    Server {*${uri}}* has an active profile and thus cannot be removed.
    ${anr} =    Evaluate    ${Assigned_Not_Removed} + 1
    Set Suite Variable    ${Assigned_Not_Removed)   ${anr}

Get Profiles Assigned Counts
    [Documentation]    Returns the number of assigned and unassigned profiles
    ${assigned} =    Set Variable    0
    ${profiles} =    Fusion Api Get Server Profiles
    ${profile_count} =   Set Variable    ${profiles['total']}

    :FOR    ${profile}    in   @{profiles['members']}
    \    LOG    SHU: ${profile['serverHardwareUri']}
    \    ${this_profile} =    Profile Assigned    ${profile['serverHardwareUri']}
    \    Log   TP: ${this_profile}
    \    ${assigned} =    Evaluate    ${assigned} + ${this_profile}

    ${unassigned} =    Evaluate    ${profile_count} - ${assigned}
    [Return]    ${assigned}    ${unassigned}

Profile Assigned
    [Documentation]    Returns 'Assigned' or 'Unassgned' depending on profile serverHardwareUri
    [Arguments]     ${shu}
    LOG    shu: ${shu}
    Return From Keyword If    '${shu}'=='None'    0    # unassigned
    Return From Keyword If    '${shu}'!='None'    1    # assigned.