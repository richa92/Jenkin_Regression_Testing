*** Settings ***
Documentation		C7000 Fusion Appliance deployment and common resources setup (users, networks, SAN manager, etc.)
Resource            ./keywords.txt
Resource            ./utils.txt

*** Variables ***
${APPLIANCE_IP}                 ${None}             # leave it as ${None} if you want this test to create a new one
${SSH_PASS}                     hpvse1
${Team_Name}                    SHQA
${settings}                     ${C7000EnvSetup.${Team_Name}}
${admin_credentials}            ${settings.Common.admin_credentials}


*** Test Cases ***
Teardown Fusion Environment - remove/delete all resources
    Remove All Resources For C7000      ${APPLIANCE_IP}