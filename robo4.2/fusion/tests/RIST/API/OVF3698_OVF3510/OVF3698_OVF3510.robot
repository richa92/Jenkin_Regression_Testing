*** Settings ***
Documentation                   Verify enclosure with BI
...                               - Do GET on Enclosure verify BI data did not change
Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
TestCase Get on Enclosure
   [Tags]    ovs29857-enc
   Verify Enclosures from list  ${verify_enc}

TestCase Get on Server
    [Tags]    Performance    server_hardware-condition-single
    Run Keyword If	${verify_servers} is not ${null}		Verify Resources For list	${verify_servers}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
