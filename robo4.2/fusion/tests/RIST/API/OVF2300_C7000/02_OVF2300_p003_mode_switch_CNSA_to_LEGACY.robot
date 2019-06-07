*** Settings ***
Documentation      Switch From CNSA To LEGACY And Do The Check Point

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ./keywords.txt
Variables            ./Regression_Data.py


*** Variables ***
${APPLIANCE_IP}         unknown

*** Test Cases ***
C3Switch From CNSA To LEGACY And Do The Check Point
    Security Mode Check Current Mode Is  CNSA
    Switch Security Mode To  LEGACY
    Login By IA User
    Security Mode Check Current Mode Is  LEGACY
    SSH Check For Mode  LEGACY  ${APPLIANCE_IP}
