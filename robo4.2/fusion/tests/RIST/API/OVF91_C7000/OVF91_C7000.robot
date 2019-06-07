*** Settings ***
Documentation       OVF91 C7000 Validate acceptance of new OA certificates
Suite Setup         OVF91 C7000 Setup
Suite Teardown      OVF91 C7000 Teardown
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'
${APPLIANCE_ADMIN_PASSWORD}		wpsthpvse1

*** Test Cases ***
OVF2161 Synergy TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF91 C7000 PTS1 Add CA Certificates
    ${headers}=     Fusion APi Get Headers
    set to Dictionary       ${headers}      forceSaveLeaf=True
    ${add_leafcert}=        Fusion Api Import Server Certificate   ${OVF91_ADD_CA_CERTIFICATES}       headers=${headers}
    Should be equal    '${add_leafcert['status_code']}'    '202'    msg=Fail to add self signed leaf cert

OVF7000 PTS1 Add Enclosure
	Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
	Add Enclosures from variable	${enclosures}

OVF7000 PTS1 Verify Enclosure
    Verify Enclosures from list  ${enclosures_expected}  state=Configured

*** Keywords ***
Remove Enclosure Group
    [Documentation]  Remove the enclosure group by name
    [Arguments]     ${name}
    ${uri} =  Get Enclosure Group URI    ${name}
    ${resp} =  Fusion Api Delete Enclosure Group  uri=${uri}
    Wait For Task2  ${resp}  timeout=600  interval=10

Remove LIG
    [Documentation]  Remove the LIG by name
    [Arguments]     ${name}
    ${uri} =  Get LIG URI    ${name}
    ${resp} =  Fusion Api Delete LIG  uri=${uri}
    Wait For Task2  ${resp}  timeout=600  interval=10

OVF91 C7000 Setup
    [Documentation]  OVF91 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF91 C7000
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Create the LIG and EG
    Log    ${feature} Suite Setup: Start create the LIG and EG.    console=true
	Add LIG from list	${ligs}
	Add Enclosure Group from list	${enc_groups}
	Log    ${feature} Suite Setup: Finish create the LIG and EG.    console=true

OVF91 C7000 Teardown
    [Documentation]  OVF91 C7000 Teardown
    Set Log Level	TRACE
    ${feature} =  set variable  OVF91 C7000
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Remove the enclosure, EG, LIG, and certificate
    Log    ${feature} Suite Teardown: Start remove the enclosure, EG, LIG, and certificate.    console=true
    ${resp} =  Fusion Api Delete Server Certificate    ${OVF91_ENC_OA1_CA_ROOT_CERTIFICATE_NAME}
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove self signed leaf cert
    Wait For Task2    ${resp}    2min    5
    Remove Enclosure  ${OVF91_ENC}  param=?force=True
    Remove Enclosure Group  ${OVF91_EG}
    Remove LIG  ${OVF91_LIG}
    Log    ${feature} Suite Teardown: Finish remove the enclosure, EG, LIG, and certificate.    console=true


