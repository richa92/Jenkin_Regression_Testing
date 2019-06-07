*** Settings ***
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    SSHLibrary
Library    OperatingSystem
Library    XML
Library    String
Variables   variables_expmsg.py


*** Variables ***
${DataFile}    firmware_data_tbird.xml

${ApplianceUrl}    https://10.10.0.91
${Browser}    FireFox
#${Browser}    Chrome
#${Browser}    IE
${SeleniumSpeed}    0.1
${IP}    10.10.6.89
${USER1}    root
${PASSWORD}    wpsthpvse1
${PROMPT}    [root@wpstciscodemo ~]


*** Keywords ***

Load Test Data and Open Browser
    Set Log Level    TRACE
    Load Test Data    ${DataFile}
    Log Variables
    #Open Browser    ${ApplianceUrl}    ${Browser}    ff_profile_dir=C:\\swathi\\firefox_profile
    Open Browser    ${ApplianceUrl}    ${Browser}
    Maximize Browser Window
    # Run Keyword if "{Browser}" == "IE" Go To javascript:Document.getElementById('overridelink').click()
    Set Selenium Speed    ${SeleniumSpeed}

Logout and Close All Browsers
    Fusion UI Logout of Appliance
    Close All Browsers

Log into Fusion appliance as Administrator
    ${user}=    Get Data By Property    ${TestData.users}   name    Administrator
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As BackupAdmin
    Maximize Browser Window
    ${user}=    Get Data By Property    ${TestData.users}   name    BackupAdminT
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As ReadOnly
    Maximize Browser Window
    ${user} =    Get Data By Property    ${TestData.users}   name    ReadOnly
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As StorageAdmin
    Maximize Browser Window
    ${user}=    Get Data By Property    ${TestData.users}   name    StorageAdmin
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As NetworkAdmin
    Maximize Browser Window
    ${user}=    Get Data By Property    ${TestData.users}   name    NetworkAdminT
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As ServerAdmin
    Maximize Browser Window
    ${user}=    Get Data By Property    ${TestData.users}   name    ServerAdminT
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As SoftwareAdmin
    Maximize Browser Window
    ${user} =    Get Data By Property    ${TestData.users}   name    SoftwareAdmin
    Fusion UI Login to Appliance    ${user[0].name}

Log into Fusion Appliance As specified user
    [Arguments]    ${specifieduser}
    Maximize Browser Window
    ${user} =    Get Data By Property    ${TestData.users}   name    ${specifieduser}
    Fusion UI Login to Appliance    ${user[0].name}

Perform SSH connection test
    [Arguments]    ${IP}    ${USER1}    ${PASSWORD}
    Set Default Configuration   prompt=${PROMPT}    timeout=1 minute
    ${id}=    Open Connection    ${IP}
    ${ssh_status}    ${output}=    Run Keyword And Ignore Error    Login   ${USER1}    ${PASSWORD}
    Run keyword if    '${ssh_status}'=='FAIL'    Log to Console    "SSH to Server: Failed"
    Run keyword if    '${ssh_status}'=='PASS'    Log to Console    "SSH to Server: Passed"
    Close Connection
    Log to Console    "Closed SSH channel"
    Log to Console    "SSH_status"
    Log to Console    ${ssh_status}
    [return]    ${ssh_status}
