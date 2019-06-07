*** Settings ***
Documentation    Tests to edit Enclosure Group with new LIG
...              Update from Group and  verify LE state and LI consistency status
...              Edit telemetry data of LI
...              Create and Download LE Support Dump
Resource                         ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

05_01 Edit EG with new LIG and Verify LE is inconsistent
    [Tags]     UFG01
    [Documentation]        Add LIG to EG
    ...                    Verify logical enclosure becomes inconsistent since EG no longer matches LE, LI remains consistent.
    ${resp}=    get resource    EG:${edit_enclosure_group['name']}
    Run Keyword If    ${resp['status_code']}!=200    FAIL    EG ${edit_enclosure_group['name']} does not exits
    Logical Enclosure State Should Be    ${logical_enclosure_state['name']}    Consistent
    ${response}=  Edit Enclosure Group    ${edit_enclosure_group}
    Run Keyword And Continue On Failure   Wait For Task2  ${response}  timeout=300    interval=5
    Logical Enclosure State Should Be    ${logical_enclosure_state['name']}    Inconsistent
    Logical Interconnect Consistency Status Should Be  ${logical_interconnect_state['name']}    CONSISTENT

05_02 Update From Group - verify LE state and LI consistency status
    [Tags]    UFG02
    [Documentation]        Invoke update from group on LE, verify LE is now consistent, LI remains consistent
    ${resp}=    get resource    LE:${update_logical_enclosure_from_group['name']}
    Run Keyword If    ${resp['status_code']}!=200    FAIL    LE ${update_logical_enclosure_from_group['name']} does not exits
    ${response}=    Run Keyword If    ${update_logical_enclosure_from_group} is not ${null}     Update Logical Enclosure from Group  ${update_logical_enclosure_from_group}  ${VERIFY}
    Logical Enclosure State Should Be    ${logical_enclosure_state['name']}    Consistent
    Logical Interconnect Consistency Status Should Be  ${update_logical_interconnect_from_group['name']}    CONSISTENT

05_03 Update From Group - LI and verify
    [Tags]    UFG03
    [Documentation]        Edit telemetry data of LI
    ...                    Verify LE and LI in NotConsistent state and then Update from Group
    ...                    Verify LE and LI in Consistent state
    ${resp}=	get resource	LI:${edit_li_telemetry_config['name']}
    Run Keyword If    ${resp['status_code']}!=200    FAIL    LE ${edit_li_telemetry_config['name']} does not exists
    Logical Interconnect Consistency Status Should Be  ${edit_li_telemetry_config['name']}    CONSISTENT
    ${response}=  Run Keyword If    ${edit_li_telemetry_config} is not ${null}  Edit Telemetry Configurations for LI  ${edit_li_telemetry_config}
    Run Keyword And Continue On Failure    Wait For Task2    ${response}    timeout=300    interval=5
    Logical Interconnect Consistency Status Should Be  ${update_logical_interconnect_from_group['name']}    NOT_CONSISTENT
    Logical Enclosure State Should Be    ${logical_enclosure_state['name']}    Inconsistent
    Run Keyword If    ${update_logical_interconnect_from_group} is not ${null}  Update Logical Interconnect from Group  ${update_logical_interconnect_from_group}   ${VERIFY}
    # Check LE state and LI consistency status
    Logical Enclosure State Should Be    ${logical_enclosure_state['name']}    Consistent
    Logical Interconnect Consistency Status Should Be  ${update_logical_interconnect_from_group['name']}    CONSISTENT