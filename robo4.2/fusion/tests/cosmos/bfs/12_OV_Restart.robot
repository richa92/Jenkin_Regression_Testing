*** Settings ***
Documentation    OV Restart and wait for appliance to be in OK state
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown
Resource                        ..\\..\\..\\Resources\\api\\settings\\appliance_state.txt

*** Test Cases ***
Restart OV
   [Tags]    PRE-RESTART
   [Documentation]     Restart OV

   ${resp}=  Fusion Api Appliance Shutdown    REBOOT
   Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-Task is in progress\n
   Wait For Task2  ${resp}      timeout=2000      interval=5
   # Sleep since appliance ip won't be pingable
   sleep   400s
   Wait For Appliance To Become Pingable    ${APPLIANCE_IP}    30 minutes    30 s
   Wait Until Keyword Succeeds  40min  30s  Check Appliance State  ${APPLIANCE_IP}  OK
