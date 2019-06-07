*** Settings ***
Library    RoboGalaxyLibrary
Library    FusionLibrary
Variables   expected_messages.py

*** Variables ***
${DataFile}    ./TestData.xml
${ApplianceUrl}    https://15.212.136.117
${Browser}    Firefox
#${Browser}    IE
${SeleniumSpeed}    0.2

*** Keywords ***

Load Test Data and Open Browser
    Set Log Level    TRACE
    Load Test Data  ${DataFile}
    Log Variables
    Open Browser  ${ApplianceUrl}  ${Browser}
    Set Selenium Speed  ${SeleniumSpeed}

Logout and Close All Browsers
    Fusion UI Logout of Appliance
    Close All Browsers

Close Tutorial Dialog
    ${tutorial}=  Is Element Visible    id=hp-tutorial-step
    Run Keyword If    ${tutorial}==True    Click Element    id=hp-tutorial-close
    Element Should Not Be Visible    id=hp-tutorial-step

Login to Fusion appliance as Administrator
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  Administrator
    Fusion UI Login to Appliance   ${user[0].name}
    Close Tutorial Dialog

Login to Fusion Appliance As BackupAdmin
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  BackupAdmin
    Fusion UI Login to Appliance   BackupAdmin
    Close Tutorial Dialog

Login to Fusion Appliance As ReadOnly
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  ReadOnly
    Fusion UI Login to Appliance   ReadOnly
    Close Tutorial Dialog

Login to Fusion Appliance As StorageAdmin
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  StorageAdmin
    Fusion UI Login to Appliance   StorageAdmin
    Close Tutorial Dialog

Login to Fusion Appliance As NetworkAdmin
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  NetworkAdmin
    Fusion UI Login to Appliance   NetworkAdmin
    Close Tutorial Dialog

Login to Fusion Appliance As ServerAdmin
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  ServerAdmin
    Fusion UI Login to Appliance   ServerAdmin
    Close Tutorial Dialog

Login to Fusion Appliance As SoftwareAdmin
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  SoftwareAdmin
    Fusion UI Login to Appliance   ${user[0].name}
    Close Tutorial Dialog

Login to Fusion Appliance As specified user
    [Arguments]    ${specifieduser}
    Maximize Browser Window
    ${user} =  Get Data By Property  ${TestData.users}  name  ${specifieduser}
    Fusion UI Login to Appliance   ${user[0].name}
    Close Tutorial Dialog