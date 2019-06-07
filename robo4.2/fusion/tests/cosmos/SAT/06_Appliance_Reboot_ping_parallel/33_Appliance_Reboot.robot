*** Settings ***
Documentation
...     OV Reboot and wait for appliance to be in OK state
...     Ping IP Post Reboot
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Restart OV
   [Tags]    REBOOT   C7000  T-BIRD
   [Documentation]     Reboot appliance
   Sleep    300s
   ${resp}=  Fusion Api Appliance Shutdown    REBOOT
   Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-Task is in progress\n
   Wait For Task2  ${resp}      timeout=2000      interval=5
   # Sleep since appliance ip won't be pingable
   sleep   400s
   Wait For Appliance To Become Pingable    ${APPLIANCE_IP}    30 minutes    30 s
   Wait Until Keyword Succeeds  40min  30s  Check Appliance State  ${APPLIANCE_IP}  OK

Ping IP Post Reboot, Windows Server Should Be Pinging, FC Disk Should Exist and Active
   [Tags]      POST-REBOOT   C7000
   [Documentation]     Ping IP Post Reboot, Windows Server Should Be Pinging, FC Disk Should Exist and Active
   Power On Server Profile And Wait For POST State    ${win_os_servers}
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   02

Ping IP Post Reboot, Windows Server Should Be Pinging, FC Disk Should Exist and Active - Tbird
   [Tags]      POST-REBOOT  T-BIRD
   [Documentation]     Ping IP Post Reboot, Windows Server Should Be Pinging, FC Disk Should Exist and Active - Tbird
   Power On Server Profile And Wait For POST State    ${win_os_servers}
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

Download Support Dump - Post Appliance Reboot
    [Tags]   DOWNLOAD-OVSD  T-BIRD   C7000
    [Documentation]    Get And Download Oneview Support Dump - Post Appliance Reboot
    Get Support Dump  ${support_dump}   ${TEST NAME}