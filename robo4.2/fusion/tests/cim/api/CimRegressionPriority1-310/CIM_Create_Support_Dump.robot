*** Settings ***
Documentation     Create Support Dump and Download for One View


Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Resource          ../Resource/CIM_Common_Resource.txt

***Variables***
${filename}    supportdump.sdmp

*** Test Cases ***

Create Support Dump and Download
    [Documentation]     Create SD and download
    Login    ${admin_credentials}
    ${resp} =    Fusion Api Create Support Dump    ${support_dump}
    Should Be Equal    '${resp['status_code']}'    '200'    msg= Support dump is not created
    ${uri} =     Get from DIctionary    ${resp}    uri
    Should Contain    ${uri}    .sdmp    msg= Support dump is not created
    Log to Console And Logfile    Support dump is created for the appliance

    #Download Support Dump

    ${response} =    Fusion Api Download Support Dump    ${uri}    ${filename}
    Should Be Equal    '${resp['status_code']}'    '200'    msg= SD download failed
    Remove File    ${filename}
    Logout

