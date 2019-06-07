*** Settings ***
Documentation    tear down

Variables        ./data_common.py

Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ./DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py


*** Test Cases ***
Teardown
    Set Log Level    TRACE
    Log    [TEARDOWN]
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Power off ALL Servers     PressAndHold
    Remove All Server Profiles
    Remove ALL LS
    Remove ALL LSGs
    Remove All LEs
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL FCoE Networks
    Remove ALL Network Sets
    Remove ALL Users
