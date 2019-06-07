*** Settings ***
Documentation    Backup and Restore of OV appliance
Resource                        ../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test cases ***
Backup and Restore
   [Tags]      PRE-BR
   [Documentation]     Backup and Restore OV appliance
   Create Backup from OV
   Restore From Backup from OV