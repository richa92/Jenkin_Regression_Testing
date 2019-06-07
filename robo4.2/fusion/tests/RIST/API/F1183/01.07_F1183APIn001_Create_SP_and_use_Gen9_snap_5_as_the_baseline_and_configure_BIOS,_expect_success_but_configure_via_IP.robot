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
F1183APIn001_Create SP and update BIOS using Gen9 snap5 as baseline, expect update BIOS by IP
    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    #power off all server and delete all server profile
    Clear Test Environtment
    Log to console and logfile  Create SP, update BIOS using Gen 9 snap5 as the baseline and configure BIOS
    ${profilelist} =    Generate Profile Body   ${createdropdownbiosProfiles}   ${True}   ${SNAP5SPP}
	${resps} =   Add Server Profiles from variable   ${profilelist}
	Validate Server Profile Task   ${resps}    ${IP}