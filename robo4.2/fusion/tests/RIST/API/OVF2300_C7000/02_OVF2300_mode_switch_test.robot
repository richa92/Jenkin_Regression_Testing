*** Settings ***
Documentation      02_OVF2300_p002_mode_switch_test.robot

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Login By IA User


*** Variables ***
${APPLIANCE_IP}         unknown

*** Test Cases ***
C1:Switch From LEGACY To FIPS And Do The Check Point
    Security Mode Check: Current Mode Is:  LEGACY
    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS
    Security Mode Check: Current Mode By Mode List Is:  FIPS
    SSH Check For Mode:  FIPS  ${APPLIANCE_IP}
    Create Compatibility Report And Do The Basic Check Point

C2:Switch From FIPS To CNSA And Do The Check Point
    Security Mode Check: Current Mode Is:  FIPS
    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    Security Mode Check: Current Mode By Mode List Is:  CNSA
    SSH Check For Mode:  CNSA  ${APPLIANCE_IP}

C3:Switch From CNSA To LEGACY And Do The Check Point
    Security Mode Check: Current Mode Is:  CNSA
    Switch Security Mode To:  LEGACY
    Login By IA User
    Security Mode Check: Current Mode Is:  LEGACY
    Security Mode Check: Current Mode By Mode List Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}

C4:Switch From LEGACY To CNSA And Do The Check Point
    Security Mode Check: Current Mode Is:  LEGACY
    Switch Security Mode To:  CNSA
    Login By IA User
    Security Mode Check: Current Mode Is:  CNSA
    Security Mode Check: Current Mode By Mode List Is:  CNSA
    SSH Check For Mode:  CNSA  ${APPLIANCE_IP}
    Create Compatibility Report And Do The Basic Check Point

C5:Switch From CNSA To FIPS And Do The Check Point
    Security Mode Check: Current Mode Is:  CNSA
    Switch Security Mode To:  FIPS
    Login By IA User
    Security Mode Check: Current Mode Is:  FIPS
    Security Mode Check: Current Mode By Mode List Is:  FIPS
    SSH Check For Mode:  FIPS  ${APPLIANCE_IP}

C6:Switch From FIPS To LEGACY And Do The Check Point
    Security Mode Check: Current Mode Is:  FIPS
    Switch Security Mode To:  LEGACY
    Login By IA User
    Security Mode Check: Current Mode Is:  LEGACY
    Security Mode Check: Current Mode By Mode List Is:  LEGACY
    SSH Check For Mode:  LEGACY  ${APPLIANCE_IP}
