*** Settings ***
Library				RoboGalaxyLibrary
Library				FusionLibrary
Library				OperatingSystem
Library				BuiltIn
Library				Collections
Library				XML
Library		        SSHLibrary
Library				String
Library				Dialogs

*** Variables ***
${PauseWhenFailed}      False
${SendMailWhenPaused}   False
${Sender}       wpst-jenkins@hp.com
${Receiver}     Receiver email list, split using ","
${BUILD_URL}    Jenkins built-in variable
${NODE_NAME}    Jenkins slave node name
${Subject}      Error encounter when running test
${Content}

*** Keywords ***
Pause When Test Failed
	[Documentation]    Popup a dialog to pause the execution if \${PauseWhenFailed} is set to True. Finally close the browser
	Run Keyword If Test Failed		Pause Test Execution

Pause Test Execution
	[Documentation]    Pause test execution
    Return From Keyword If   '${PauseWhenFailed.lower()}'=='false'

	LOG     Encounter failure, pausing test execution, if job is launch from jenkins, please log on jenkins slave server to get job continue       level=WARN
	Send Mail Notification
	Pause Execution

Send Mail Notification
    Return From Keyword If   '${SendMailWhenPaused.lower()}'=='false'    Skipped Send Mail Notification (\${SendMailWhenPaused}=${SendMailWhenPaused})

    LOG     Sending mail notification   level=WARN
    @{receiver_lst}=    Split String	${Receiver}     ,

    Run Keyword If  '${Content}' == ''  Set Suite Variable
    ...             ${Content}
    ...             Build URL: \n${BUILD_URL}\n\nSlave Node: \n${NODE_NAME}\n\nTest case file: \n${SUITE SOURCE}\n\nTest case name: \n${TEST NAME}\n

    Connect To SMTP Server          smtp3.hpe.com  True
    Send Email      ${Sender}    ${receiver_lst}      ${Subject}      ${Content}
    Disconnect From SMTP Server