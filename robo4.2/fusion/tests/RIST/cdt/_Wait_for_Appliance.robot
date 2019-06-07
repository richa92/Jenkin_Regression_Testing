*** Settings ***
Resource    resource.txt

*** Test Cases ***
Wait for Appliance
    Wait For Appliance To Become Pingable   appliance=${APPLIANCE_IP}  timeout=150 min  interval=30 sec
    Wait For Appliance To Be Ready  appliance=${APPLIANCE_IP}  timeout=150 min  interval=30 sec
