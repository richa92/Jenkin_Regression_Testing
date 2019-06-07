*** Settings ***
Documentation                   Tbird Regression Ring Precheck
...                               -  Power on all servers
...                               -  Power on all SAS-IC
...                               -  Refresh a servers, SAS-IC, DE, and enclosures

Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Variables  						./Regression_Data.py

*** Variables ***

${X-API-VERSION}			    300
${APPLIANCE_IP}                 16.114.209.223
${powerState_timeout}           40
${wordy}                        ${True}

*** Test Cases ***

Log into Appliance
	${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	
Power on Reg Ring all server hardware
	Power on ALL servers
	
Power on all Reg Ring SAS-IC
	Power On Sas Interconnects from list	${sasics}
	
Power on all Reg Ring Potash ICs	
	Power On Interconnects from list	${Potash_ICs}
	Power On Interconnects from list	${Other_ICs}
	
Refresh Reg Ring Drive enclosures
	Refresh Drive Enclosure		${ENC1DEBAY1}
	
Refresh Reg Ring all Tbird Enclosures
	Refresh Enclosure Async		${encs}
	
Power Reg Ring off all server hardware
	Power off ALL servers

Logout of appliance 
	Fusion Api Logout Appliance