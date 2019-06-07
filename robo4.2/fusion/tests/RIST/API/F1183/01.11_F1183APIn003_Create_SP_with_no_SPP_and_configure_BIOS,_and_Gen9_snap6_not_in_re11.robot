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
F1183APIn003_Create SP with no SPP and configure BIOS, and Gen 9 snap 6 not in repo
    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    #power off all server and delete all server profile
    Clear Test Environtment
    Log to console and logfile  Create SP with no SPP and configure BIOS, and Gen 9 snap 6 not in repo
    Remove Firmware Bundle  ${SNAP6SPP}
    ${profilelist} =    Generate Profile Body   ${createdropdownbiosProfiles}    ${False}
	${resps} =   Add Server Profiles from variable   ${profilelist}
	Validate Server Profile Task   ${resps}    ${IP}