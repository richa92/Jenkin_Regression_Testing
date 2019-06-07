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
F1183APIn006_Edit SP, update BIOS with invalid parameter
    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    #power off all server and delete all server profile
    Clear Test Environtment
    Create empty server profile  ${editinvalidnbiosProfiles }
    Log to console and logfile  Edit SP and Configure BIOS, with invalid BIOS value
    ${profilelist} =    Generate Profile Body  ${editinvalidnbiosProfiles }    ${True}
	${resps} =   Edit Server Profiles from variable   ${profilelist}
	Validate SP BIOS Invalid Task  ${resps}
