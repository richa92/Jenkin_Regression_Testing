*** Settings ***
Resource            ../../Resources/api/fusion_api_resource.txt
#Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'16.114.211.88'
${DATA_FILE}         dataFile.py

*** Test Cases ***
Test Case I
    [Documentation]  Test Case I
    Appliance Login
#    [Setup]  Generate Traffic From Server bay to test head  ${trafficTestData1}
    [Setup]  Generate Traffic From Test head to Server bay  ${trafficTestData2}


    # Our code
    Log To Console   Our test steps 1
    Sleep       120s
#    Reset Power Off Power ON server while pinging
#    Sleep       300s
#    Appliance Login
#    Edit profile add extra connection
#    Sleep       120s
    ${resp} =  create list
    ${resp} = 	Analyse Traffic
    log to console		${resp}
    :FOR	${res}	IN	@{resp}
    \       ${target_ip} =     Get from Dictionary     ${res}     destination_ip
    \       ${loss_count} =   Get Length    ${res['losses']]
	\       Run Keyword If   '${loss_count}'>='0'   Fail   msg=There are more Ping losses than expected
