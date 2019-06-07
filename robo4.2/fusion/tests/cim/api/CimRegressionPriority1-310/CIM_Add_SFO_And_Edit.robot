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

Edit Created Server Firmware Operator and add server administrator as another role
    [Documentation]     Create SFO and edit
    Login    ${admin_credentials}
    ${userlist} =    create list
    append to list    ${userlist}    ${users[0]}
    Add User    ${userlist}
    Edit User    ${updateUser}
    Remove User
    Logout
