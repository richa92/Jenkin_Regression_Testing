*** Settings ***
Documentation    Suite to test bios registry feature for C7K
Library    FusionLibrary
Library    RoboGalaxyLibrary
Library    OperatingSystem
Library    SSHLibrary
Library    BuiltIn
Library    Collections
Library    XML
Library    String
Library    json
Library    Process

Resource        ../../../../Resources/api/fusion_api_resource.txt
Resource        resources.txt
Variables        data_variables.py
Suite Setup        Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance


*** Variables ***

${APPLIANCE_IP}        16.125.76.249

*** Test Cases ***

Add C7K enclosure in monitored mode TC 01
    Add Enclosures from variable    ${c7k_enclosures_monitored}

Refresh C7K blades in monitored mode and check for bios versions TC 02
    ${servers}=    Get all enclosures from Oneview
    Set suite variable    ${servers}
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    ${resp}=    Refresh Server Hardware    ${server['name']}
    \    wait for task2    ${resp}    300    10
    \    Server Refresh Complete    ${server}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${True}    FAIL    BIOS download did not succeed

Reset and refresh C7K blades in monitored mode and check for bios versions TC 03
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Run keyword if    '${server['powerState']}'!='On'    Power on server    ${server['name']}
    \    Reset Server    ${server['name']}
    \    ${resp}=    Refresh Server Hardware    ${server['name']}
    \    wait for task2    ${resp}    300    10
    \    Server Refresh Complete    ${server}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${True}    FAIL    BIOS download did not succeed

Power off C7K blades in monitored mode and check for bios versions TC 04
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power off Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download need not succeed

Power on C7K blades in monitored mode and check for bios versions TC 05
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power on Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download need not succeed

Add C7K enclosure in managed mode TC 06
    Remove All Enclosures
    Add Enclosure Group from variable		${c7k_enc_groups}
    Add Enclosures from variable		${c7k_enclosures_managed}
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    FAIL    Log    Did not download latest bios registry files.    console=True

Refresh C7K blades in managed mode and check for bios versions TC 07
    Set suite variable    ${servers}
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    ${resp}=    Refresh Server Hardware    ${server['name']}
    \    wait for task2    ${resp}    300    10
    \    Server Refresh Complete    ${server}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${True}    FAIL    BIOS download did not succeed

Reset and refresh C7K blades in managed mode and check for bios versions TC 08
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Run keyword if    '${server['powerState']}'!='On'    Power on server    ${server['name']}
    \    Reset Server    ${server['name']}
    \    ${resp}=    Refresh Server Hardware    ${server['name']}
    \    wait for task2    ${resp}    300    10
    \    Server Refresh Complete    ${server}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${True}    FAIL    BIOS download did not succeed

Power off C7K blades in managed mode and check for bios versions TC 09
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power off Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download did not succeed

Power on C7K blades in managed mode and check for bios versions TC 10
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power on Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download did not succeed


*** Keywords ***

Get all enclosures from Oneview
    [Documentation]    Get all enclosures data from Oneview
    ${enclosures} =     Fusion Api Get Enclosures
    ${servers_list}    Create List
    :FOR    ${enclosure}    in    @{enclosures['members']}
    \    ${Gen10_servers_list}=    Get all Gen10 servers from enclosure    ${enclosure}    ${servers_list}
    [Return]    ${Gen10_servers_list}

Get all Gen10 servers from enclosure
    [Documentation]    Get all servers data from enclosure
    [Arguments]    ${enc}    ${servers_list}
    :FOR    ${server}    in    @{enc['deviceBays']}
    \    ${server_dict}    Create Dictionary
    \    ${server_bay_present}=    Run keyword if    '${server['devicePresence']}'=='Present'    Set Variable    ${True}
    \    ${server_bay}=    Run keyword if    ${server_bay_present}==${True}    Run keyword if    '${server['deviceUri']}'!='None'    Run keyword if    ${server['deviceUri'].startswith('/rest/server-hardware')} == True    Set Variable    ${server}
    \    Continue For Loop If    ${server_bay} is None
    \    ${server_details}=    Get Resource by URI    ${server['coveredByDevice']}
    \    ${server_rom_version}=    Set variable    ${server_details['romVersion']}
    \    ${server_family}=    Run keyword if    '${server_details['state']}'=='Monitored' or '${server_details['status']}'=='OK'    Fetch From Left    ${server_rom_version}    ${SPACE}
    \    ${server_family}=    Run keyword if    '${server_details['state']}'=='Monitored' or '${server_details['status']}'=='OK'    Convert To Lowercase    ${server_family}
    \    ${is_gen10}=    Run keyword if    '${server_details['generation']}'=='Gen10'    Set variable    ${True}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  name=${server_details['name']}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  uri=${server_details['uri']}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  server_family=${server_family}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  powerState=${server_details['powerState']}
    \    Run keyword if    ${is_gen10}==${True}    Append to list    ${servers_list}    ${server_dict}
    [Return]    ${servers_list}
