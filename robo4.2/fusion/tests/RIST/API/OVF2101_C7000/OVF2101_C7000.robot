*** Settings ***
Documentation       OVF2101 array controller inventory
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Suite Setup         OVF2101 C7000 Setup
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
OVF2101 C7000 TS0 Initialize the Variables and Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF2101 C7000 NTS1 Negative Test
    Get Local Storage on Gen9

OVF2101 C7000 PTS1 Verify Server Hardware Local Storage
    Server Hardware Local Storage Should Match RIS  ${server}

OVF2101 C7000 PTS1 Refresh the Server
    ${resp} =  Refresh Server Hardware  ${server}
    Wait for Task2  ${resp}  timeout=1200  interval=10

OVF2101 C7000 PTS1 Verify Server Hardware Local Storage after Refresh
    Server Hardware Local Storage Should Match RIS  ${server}

OVF2101 C7000 PTS2 Create the profile
    Power off Servers in Profiles  ${pts2_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts2_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF2101 C7000 PTS2 Verify Server Hardware Local Storage after Create
    Server Hardware Local Storage Should Match RIS  ${server}

OVF2101 C7000 PTS2 Refresh the Server
    ${resp} =  Refresh Server Hardware  ${server}
    Wait for Task2  ${resp}  timeout=1200  interval=10

OVF2101 C7000 PTS2 Verify Server Hardware Local Storage after Refresh
    Server Hardware Local Storage Should Match RIS  ${server}

OVF2101 C7000 PTS2 Delete the Profiles
    ${resp}=  Remove Server Profile  ${pts2_profile_create}
    Wait for Task2  ${resp}    timeout=60    interval=10

OVF2101 C7000 PTS2 Verify Server Hardware Local Storage after Delete
    Server Hardware Local Storage Should Match RIS  ${server}


*** Keywords ***
OVF2101 C7000 Setup
    [Documentation]  OVF2101 C7000 Setup
    ${feature} =  set variable  OVF2101 C7000
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    
    # Clean up the profiles
    Log  ${feature} Suite Setup: Cleanup the profiles  console=True
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist} =  Remove Server Profiles from variable  ${suite_setup_profiles}
    Wait for task2  ${resplist}  timeout=3600  interval=10

    # Create the profiles to initialze the controllers
    Log  ${feature} Suite Setup: Create profiles to initialize the controllers  console=True
    Power off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=1800  interval=10

    # Remove the profiles
    Log  ${feature} Suite Setup: Remove the profiles  console=True
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=900  interval=10

Get Local Storage on Gen9
    [Documentation]  OVF2101 negative test
    ${gen9_sh_uri} =  Get Server Hardware URI  ${gen9_server}
    ${resp} =  Fusion Api Get Resource  uri=${gen9_sh_uri}/localStorage
    Should be equal  '${resp['status_code']}'  '404'  msg=Get Server Hardware Local Storage on Gen9 Status Code Should Return 404
    Should be equal  '${resp['errorCode']}'  'RESOURCE_NOT_FOUND'  msg=Get Server Hardware Local Storage on Gen9 Should Return Error RESOURCE_NOT_FOUND