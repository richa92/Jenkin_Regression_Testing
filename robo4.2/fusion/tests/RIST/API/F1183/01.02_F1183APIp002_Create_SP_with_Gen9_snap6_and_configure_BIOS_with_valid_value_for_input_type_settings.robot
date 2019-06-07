*** Settings ***
Documentation                   F1183 BIOS Configuration By HPSUT
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library  			String
Resource            ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables 		    ./Regression_Data.py

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'
${TARGET}		    'C7000'
#C7000 or TBird
${DATA_FILE}         Regression_Data.py

*** Test Cases ***
F1183APIp002_Create SP with Gen 9 snap 6 and configure BIOS input value
    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    #power off all server and delete all server profile
    Clear Test Environtment
    Update BIOS input value when create profile