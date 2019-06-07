*** Settings ***
Documentation    Run First Time Setup on newly deployed DCS VM
Resource         resource.txt



*** Test Cases ***

First Time Setup
    [Documentation]     Configure First time setup for OneView Appliance
    Log to Console	${APPLIANCE_IP}
	Log to console	\nWiating for Appliance to startup it takes 12 min
	Log to console		Get Current Date
    Sleep   12 minutes
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}
    Wait For Appliance To Be Ready		${APPLIANCE_IP}
    ${eula}=    Fusion Api Save EULA    ${APPLIANCE_IP}
    Log to Console 	${eula}
    Return From Keyword If    ${eula['status_code']}!=200    FAIL   msg=EULA is not saved
    ${req} = 		Create Dictionary		newPassword=admin123
	...						oldPassword=admin
	...						userName=Administrator
    ${password}=   Fusion Api Change Administrator password	  host=${APPLIANCE_IP}		body=${req}
    Run Keyword If  ${password['status_code']}==400  Log   Password is already set  WARN
    Run Keyword If    ${password['status_code']}==200    Log   Password is set
    ${admin_credentials} =            Create Dictionary		password=admin123
        ...                                             	userName=Administrator
    Log to Console 	\nLogging in to the appliance after change password
    ${response}		${session_id}=			Fusion Api Login Appliance		${APPLIANCE_IP} 		${admin_credentials}
    ${Network_response}=	Fusion Api Get Appliance Interfaces	    
    Run Keyword If    ${Network_response['status_code']}!=200	
    ...		Fatal Error    Unable to fetch Appliance Interfaces Dictionary: ${Network_response['message']}
    ${body} =    Convert To Dictionary    ${Network_response}    
    Remove from dictionary	${body}		headers		
    Remove from dictionary      ${body}         status_code   
    ${hostname} = 	get from dictionary	${body['applianceNetworks'][0]} 	hostname    
    Set to dictionary	${body['applianceNetworks'][0]}		hostname=${hostname}.hpe.com
    Set to dictionary   ${body['applianceNetworks'][0]}		app1Ipv4Addr=
    Set to dictionary   ${body['applianceNetworks'][0]}		ipv4Type=STATIC
    Set to dictionary   ${body['applianceNetworks'][0]}		overrideIpv4DhcpDnsServers=false
    Log to Console     ${body}		
    ${resp}= 	Fusion Api Configure Appliance Interfaces		${body}	
    Log to Console	${resp}
    Run Keyword If  ${resp['status_code']!=202}   FAIL  msg=Unable to set the network interfaces	
    Wait For Task	${resp}		timeout=500s		interval=5s


*** Keywords ***

Wait For Appliance To Be Ready
	[Documentation]	Waits for an appliance reach a the ready state
	[Arguments]		${appliance}	${timeout}=20 min	${interval}=30 s
	Wait Until Keyword Succeeds		${timeout}	${interval}	Appliance Reached Ready State	${appliance}


Appliance Reached Ready State
	[Documentation]	Waits for an appliance reach OK state
	[Arguments]		${appliance}
	${state} = 	Fusion Api Get Resource		${appliance}/controller-state.json
	Log 	-Appliance state: ${state['state']}    console=True
	Should Match Regexp	${state['state']}	((?i)OK)
