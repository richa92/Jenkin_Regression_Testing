*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt

Suite Setup       Precondition Setup For F353
Suite Teardown    Clear F353 Server Profiles


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird14
${Add_LE}                       true
${Add_Storage}                  false
${DataFile}                     F353/Regression_data.xml  # Data File Location
${ApplianceUrl}                 https://${APPLIANCE_IP}    # Appliance Url

*** Keywords ***
Precondition Setup For F353
    Set Log Level	TRACE
	Fusion Api Login Appliance 		     ${APPLIANCE_IP}		            ${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}

Clear F353 Server Profiles
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles