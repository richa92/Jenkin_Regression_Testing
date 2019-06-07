*** Settings ***
Documentation       Variables incroduction:
...                   import from jendins:  ${TBIRD_M1} ${TBIRD_M2} ${APPLIANCE_IP}
...                   import from global variable created:  ${APPLIANCE_TYPE} ${IS_HA_ENABLED}
...
...                   If test is run on TBIRD, and TBIRD has ${TBIRD_M1} ${TBIRD_M2}, ${IS_HA_ENABLED} will be set to ${True}.
...                   SSH check cases will run on both Node1 and Node2. and HA Synchronized will be checked too.
...                   If test is run on VM, such HA checks will be ignored.


Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String

Resource             ./resources_ovf2300.txt
Variables            ./Regression_Data.py

Suite Setup         Precondition ENV Setup

*** Variables ***
${APPLIANCE_IP}                 unknown
${APPLIANCE_TYPE}               unknown
${IS_HA_ENABLED}                unknown
${TBIRD_M1}                     unknown
${TBIRD_M2}                     unknown
