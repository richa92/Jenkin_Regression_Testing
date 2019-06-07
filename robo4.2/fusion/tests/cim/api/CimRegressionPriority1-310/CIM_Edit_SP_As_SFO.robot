*** Settings ***
Documentation     Server Firmware Operator Tests


Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Force Tags         Critical
Resource          ../Resource/CIM_SFO_Keywords.txt


*** Test Cases ***

Add SFO Edit Server Profile as SFO and delete SFO
    [Documentation]     Create SFO and Edit Server Profile
    Login    ${admin_credentials}
    ${userlist} =    create list
    append to list    ${userlist}    ${users[0]}
    Add User    ${userlist}
    Power Off Server To Create Server Profile
    Create Server profile for Test
    #Editing Server Hardware only as SFO
    Get Server Profile Server Hardwares details and Edit Server Profile    ${sfo_credentials}    ${editSP}
    #Editing Firmware only as SFO
    Get Server Profile Server Hardwares details and Edit Server Profile    ${sfo_credentials}    ${edit_SP_Fr}
    Login    ${admin_credentials}
    Remove User
    Remove ServerProfile for cleanup

