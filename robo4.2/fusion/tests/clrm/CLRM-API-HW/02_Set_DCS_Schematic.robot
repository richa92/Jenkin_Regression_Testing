*** Settings ***
Library    requests

Resource                        resource.txt


*** Test Cases ***
Start DCS
	  [Documentation]	Starts the DCS schema based on the user selection
      Run Keyword IF		'${OV_TYPE}' == 'DCS' and '${DCS_TYPE}' == 'C7000'		C7000 DCS Set Schematic to Demo
      ...	ELSE IF		'${OV_TYPE}' == 'DCS' and '${DCS_TYPE}' == 'TBIRD'  		Tbird DCS Discover Hardware
      ...	ELSE		Log to Console		OV type is SSH so not starting DCS

*** keywords ***
Tbird DCS Discover Hardware
    [Tags]    HWSETUP    DCS    TBIRD
    [Documentation]     Invoke Hardware Discovery
    Open Connection    ${APPLIANCE_IP}
    Login    ${FUSION_SSH_USERNAME}    ${FUSION_SSH_PASSWORD}
    ${stdout}=  Execute Command    dcs status
    Log    ${stdout}    console=True
    Set Global Variable  ${FUSION_IP}  ${APPLIANCE_IP}
    Log       X-API-Ver: ${X-API-VERSION}   console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${ADMIN_CREDENTIALS}
    Invoke Hardware Setup       timeout=720
    Sleep    60s
    Wait For ALL Enclosures In OK Status    timeout=1200
    Fusion Api Logout Appliance

C7000 DCS Set Schematic to Demo
    [Tags]   DCS    C7000
    [Documentation]     Change DCS Schematics to demo
    Open Connection    ${APPLIANCE_IP}
    Login    ${FUSION_SSH_USERNAME}    ${FUSION_SSH_PASSWORD}
    ${stdout}=  Execute Command    dcs stop
    Should Contain    ${stdout}    DCS is Stopped
    ${cmd}=  Set Variable  /dcs/bin/schematic-gen.sh /dcs/schematic/demo /dcs/schematic/demo_conf.xml
    ${stdout}=  Execute Command    ${cmd}
    Should Contain    ${stdout}    Generating demo Schema...
    ${stdout}=  Execute Command    dcs start /dcs/schematic/demo cold
    Should Contain    ${stdout}    Data Center Simulator started
    ${stdout}=  Execute Command    dcs status
    Log    ${stdout}    console=True
