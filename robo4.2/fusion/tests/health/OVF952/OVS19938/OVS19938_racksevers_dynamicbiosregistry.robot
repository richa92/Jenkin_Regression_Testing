*** Settings ***
Documentation    Suite to test bios registry feature for rack servers
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

Add rack servers in monitored mode and check for bios versions TC 01
    ${resp}=    Add Server hardware from variable        ${servers_monitored}
    wait for task2    ${resp}    300    5

Refresh rack servers in monitored mode and check for bios versions TC 02
    ${servers}=    Get all rack servers from Oneview
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

Reset and refresh rack servers in monitored mode and check for bios versions TC 03
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

Power off rack servers in monitored mode and check for bios versions TC 04
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power off Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download need not succeed

Power on rack servers in monitored mode and check for bios versions TC 05
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power on Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download need not succeed

Add rack servers in managed mode TC 06
    :FOR    ${server}    in    @{servers}
    \    ${response}=    Fusion Api Delete Server Hardware    uri=${server['uri']}
    \    Wait For Task2      ${response}
    ${resp}=    Add Server hardware from variable        ${servers_managed}
    wait for task2    ${resp}    300    5

Refresh rack servers in managed mode and check for bios versions TC 07
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    ${resp}=    Refresh Server Hardware    ${server['name']}
    \    wait for task2    ${resp}    300    10
    \    Server Refresh Complete    ${server}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${True}    FAIL    BIOS download did not succeed

Reset and refresh rack servers in managed mode and check for bios versions TC 08
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

Power off rack servers in managed mode and check for bios versions TC 09
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power off Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download did not succeed

Power on rack servers in managed mode and check for bios versions TC 10
    :FOR    ${server}    in    @{servers}
    \    ${bios_download_status}=    Compare ILO and OV BIOS versions    ${server['name']}     ${server['server_family']}    ${ilo_credentials}
    \    Log    bios_download_status:${bios_download_status}    console=True
    \    Run keyword if    ${bios_download_status}==${True}    Log    Need to download bios registry files.    console=True
    \    Power on Server    ${server['name']}
    \    ${post_download_status}=    Run keyword if    ${bios_download_status}==${True}    Compare ILO and OV BIOS versions    ${server['name']}    ${server['server_family']}    ${ilo_credentials}
    \    Run keyword if    ${post_download_status}==${False}    FAIL    BIOS download did not succeed


*** Keywords ***

Get all rack servers from Oneview
    [Documentation]    Get all enclosures data from Oneview
    ${all_servers} =     Fusion Api Get Server Hardware
    ${servers_list}    Create List
    ${result}    Create List
    :FOR    ${server}    in    @{all_servers['members']}
    \    Run keyword if    ${server['shortModel'].startswith('BL')} == False    Append to list    ${servers_list}    ${server}
    :FOR    ${server}    in    @{servers_list}
    \    ${server_dict}    Create Dictionary
    \    ${server_rom_version}=    Set variable    ${server['romVersion']}
    \    Log    ROM Version:${server_rom_version}    console=True
    \    ${server_family}=    Fetch From Left    ${server_rom_version}    ${SPACE}
    \    ${server_family}=    Convert To Lowercase    ${server_family}
    \    Log    Server family:${server_family}    console=True
    \    ${is_gen10}=    Run keyword if    '${server['generation']}'=='Gen10'    Set variable    ${True}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  name=${server['name']}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  uri=${server['uri']}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  server_family=${server_family}
    \    Run keyword if    ${is_gen10}==${True}    Set To Dictionary  ${server_dict}  powerState=${server['powerState']}
    \    Run keyword if    ${is_gen10}==${True}    Append to list    ${result}    ${server_dict}
    Log    Gen10 servers:${result}    console=True
    [Return]    ${result}
