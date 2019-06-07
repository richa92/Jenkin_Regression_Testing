*** Settings ***
Documentation       Web Proxy Certificate
...                 validate https web-proxy can't be added unles CA cert is added.
...                 validate that when the web-proxy is delted the CA cert is not deleted thus subsequent add of
...                 the web-proxy does not require re-add of the CA cert.

Library				FusionLibrary
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}
Suite Setup         Login and Delete Existing Web-Proxy and CA Cert For This Test's web-proxy
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py
${DO_PAUSE}         False

*** Test Cases ***
Add Web Proxy Fails due to missing CA Cert Error
    [Documentation]     Adds the Web-Proxy to OneView before CA cert, thus fails to add
    [Tags]    AWP
    Log    Adding ${WEB_PROXY[0]['server']}: ${WEB_PROXY[0]['port']} to ${APPLIANCE_IP}

    ${task} =    Add Proxy Server to OV    ${WEB_PROXY}
    Wait For Task2    ${task}   PASS=Error    errorMessage=Import_Certificate

Add Web Proxy CA Cert to OneView
    [Documentation]     Adds CA Cert to OneView
    [Tags]     ACAOV

    ${task} =    Fusion Api Import Server Certificate    ${WEB_PROXY_CERT}
    Wait For Task2   ${task}

Add Web Proxy Should Pass
    [Documentation]     Adds the Web-Proxy to OneView and accept trust
    [Tags]    AWP
    Log    Adding ${WEB_PROXY[0]['server']}: ${WEB_PROXY[0]['port']} to ${APPLIANCE_IP}

    ${task} =    Add Proxy Server to OV    ${WEB_PROXY}
    Wait For Task2    ${task}
    Run Keyword If    ${DO_PAUSE}==True    Pause Execution    CA and Proxy There?
    ${proxy} =    Get Proxy Server
    Verify Proxy Server    ${WEB_PROXY[0]}    ${proxy}

    ${certificate} =    Fusion Api Get Remote Certificate    ip=${WEB_PROXY[0]['server']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    200

Delete Web Proxy Verify CA and Remote Server Cert still there
    [Documentation]     Delete web proxy for re-add
    ${task} =    Delete Proxy Server
    Wait For Task2    ${task}

    ${proxy} =    Get Proxy Server
    Verify Proxy Server    ${NO_WEB_PROXY}    ${proxy}
    Run Keyword If    ${DO_PAUSE}==True    Pause Execution     Proxy Gone?

    ${certificate} =    Fusion Api Get CA Certificate    param=${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    200

    ${certificate} =    Fusion Api Get Remote Certificate    ip=${WEB_PROXY[0]['server']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    200

Get and Delete Server Cert by aliasname
    [Documentation]     Get then Deletes the web-proxy server cert
    ...    Currently fails due to OVD19620

    ${certificate} =    Fusion Api Get Server Certificate    aliasname=${WEB_PROXY_ALIAS_NAME}
    Log    Status: ${certificate['status_code']}    console=Yes
    #Should Be Equal as Integers    ${certificate['status_code']}    200

    ${task} =    Fusion Api Delete Server Certificate    aliasname=${WEB_PROXY_ALIAS_NAME}
    Wait For Task2    ${task}

    ${certificate} =    Fusion Api Get Server Certificate    aliasname=${WEB_PROXY_ALIAS_NAME}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    404

Add Web Proxy CA Still There Should Pass
    [Documentation]     Adds the Web-Proxy to OneView, CA still in place
    [Tags]    AWP
    Log    Adding ${WEB_PROXY[0]['server']}: ${WEB_PROXY[0]['port']} to ${APPLIANCE_IP}

    ${task} =    Add Proxy Server to OV    ${WEB_PROXY}
    Wait For Task2    ${task}
    Run Keyword If    ${DO_PAUSE}==True    Pause Execution    Proxy There?

    ${proxy} =    Get Proxy Server
    Verify Proxy Server    ${WEB_PROXY[0]}    ${proxy}

Remove CA From OneView
    [Documentation]    Remove CA, next web-proxy add should fail as CA not imported
    Remove CA By Allias Name   ${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    ${certificate} =    Fusion Api Get CA Certificate    param=${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    404
    Run Keyword If    ${DO_PAUSE}==True    Pause Execution    CA Gone?

Add Web Proxy Fails Missing CA Cert Error Again
    [Documentation]     Adds the Web-Proxy to OneView before CA cert, thus fails to add
    [Tags]    AWP
    Log    Adding ${WEB_PROXY[0]['server']}: ${WEB_PROXY[0]['port']} to ${APPLIANCE_IP}

    ${task} =    Add Proxy Server to OV   ${WEB_PROXY}
    Wait For Task2    ${task}   PASS=Error    errorMessage=Import_Certificate

*** Keywords ***
Login and Delete Existing Web-Proxy and CA Cert For This Test's web-proxy
    [Documentation]    Login to OneView and delete
    Set Log Level    DEBUG

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    ${task} =    Delete Proxy Server
    Wait For Task2    ${task}
    ${proxy} =    Get Proxy Server
    Log    Status: ${proxy['status_code']}    console=Yes
    Verify Proxy Server    ${NO_WEB_PROXY}    ${proxy}

    ${certificate} =    Fusion Api Get CA Certificate    param=${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Run Keyword If    ${certificate['status_code']} != 200    Log    ${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']} not in trust store.    console=YEs
    Run Keyword If    ${DO_PAUSE}==True    Pause Execution    Setup, CA and Proxy Gone?
    Return From Keyword If    ${certificate['status_code']} != 200

    Log    Must remove web-proxy CA Cert    console=Yes
    Remove CA By Allias Name   ${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}

    ${certificate} =    Fusion Api Get CA Certificate    param=${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Should Be Equal as Integers    ${certificate['status_code']}    404

    Run Keyword If    ${DO_PAUSE}==True    Pause Execution    Setup, CA and Proxy Gone?

Clean Up
    [Documentation]    Deletes any existing web proxy and the CA Cert for this test's web proxy and logout
    ${task} =    Delete Proxy Server
    Wait For Task2    ${task}
    ${proxy} =    Get Proxy Server
    Verify Proxy Server    ${NO_WEB_PROXY}    ${proxy}

    ${certificate} =    Fusion Api Get CA Certificate    param=${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}
    Log    Status: ${certificate['status_code']}    console=Yes
    Run Keyword If    ${certificate['status_code']}==200    Remove CA By Allias Name   ${WEB_PROXY_CA_CERT['certificateDetails']['aliasName']}

    Fusion Api Logout Appliance