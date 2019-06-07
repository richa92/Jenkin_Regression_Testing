*** Settings ***
Documentation		TBird common resources setup (users, networks, SAN manager, etc.)
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./keywords.txt
#Resource            ./deploy_c7000_appliance.txt
Variables 		    ./data_variables.py
Library				Collections
Library             json
Library             String
Library             Collections
Library             RoboGalaxyLibrary
Library             FusionLibrary
Library             robot.api.logger
Library             OperatingSystem
Library             SSHLibrary

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird14
${Add_Storage}                  false
${Add_LE}                       false
*** Test Cases ***
Setup Fusion Environment - add/create necessary resources on TBird, to be used by different test sets
	Set Log Level	TRACE
    ${APPLIANCE_IP}=        Get Variable Value                  ${APPLIANCE_IP}                 ${None}

	Fusion Api Login Appliance 		                            ${APPLIANCE_IP}		            ${admin_credentials}

    Setup Env For TBird     Ring=${Ring}                             Add_LE=${Add_LE}                    Add_Storage=${Add_Storage}


