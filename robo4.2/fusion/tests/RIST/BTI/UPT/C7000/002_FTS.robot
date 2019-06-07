*** Settings ***
Documentation   First Time Setup
Resource        resource.txt

*** Test Cases ***
C7000 UPT FTS First Time Setup
    [Documentation]    First Time Setup
    set to dictionary  ${appliance['applianceNetworks'][0]}  app1Ipv4Addr  ${APPLIANCE_IP}
    First Time Setup  password=${admin_credentials['password']}
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}



