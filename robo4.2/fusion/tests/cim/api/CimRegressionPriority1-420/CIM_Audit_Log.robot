*** Settings ***
Documentation     Create AuditLog for OneView

Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Library           json
Force Tags         Critical
Resource          ../Resource1-42/CIM_Common_Resource.txt
Resource          ../Resource1-42/CIM_Audit_Log_Keyword.txt

*** Variables ***
${filename}    audit_log.zip

*** Test Cases ***

Download Audit Log
    [Documentation]    Download Audit Log for Appliance
    Download AuditLog
    Log To Console    ${filename} has been downloaded succesfully to ${DownloadPath}