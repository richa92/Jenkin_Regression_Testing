*** Settings ***
Documentation       This suite is used to issue an E-Fuse on all blades & interconnects in all enclosures known to a OV appliance.
...   If no enclosures are found, a tech-setup is performed.
...   usage:  pybot -vFUSION_IP:10.0.0.1 -vFUSION_ADMIN_LOGIN:Administrator -vFUSION_ADMIN_PASSWORD:hpvse123 efuse_all_blades_and_interconnects.robot
Library             json
Library             FusionLibrary
Suite Setup         Suite Setup
Suite Teardown      Fusion Api Logout Appliance
Resource            ../../Resources/api/fusion_api_resource.txt

*** Variables ***
${CREDS}                      {"userName": "${FUSION_ADMIN_LOGIN}", "password": "${FUSION_ADMIN_PASSWORD}"}
${X-API-Version}              300
${FUSION_SSH_USERNAME}        root                # Fusion SSH Username
${FUSION_SSH_PASSWORD}        hpvse1              # Fusion SSH Password
${FUSION_PROMPT}              \#                  # Fusion Appliance Prompt
${FUSION_TIMEOUT}             60

*** Test Cases ***
Issue E-Fuse for all blades
    [Tags]    all    blades
    ${encs} =    Fusion Api Get Enclosures
    ${type} =    Set Variable    deviceBays
    :FOR    ${enc}   IN     @{encs['members']}
    \    Log    \n${enc['name']} ${enc['uri']}   console=True
    \    Process Bays   ${enc['${type}']}   ${type}   ${enc['uri']}

Issue E-Fuse for all interconnects
    [Tags]    all    interconnects
    ${encs} =    Fusion Api Get Enclosures
    ${type} =    Set Variable    interconnectBays
    :FOR    ${enc}   IN     @{encs['members']}
    \    Process Bays   ${enc['${type}']}   ${type}   ${enc['uri']}

Issue Factory Reset for all Interconnects
    [Tags]  all     interconnects       factory_reset
    ${encs} =    Fusion Api Get Enclosures
    :FOR    ${enc}   IN     @{encs['members']}
    \  Factory Reset Interconnects in Enclosure  ${enc}

*** Keywords ***
Suite Setup
    [Documentation]   suite setup
    Variable should exist    ${FUSION_IP}    ERROR:Required variable 'FUSION_IP' not supplied!
	${creds} =   json.loads    ${CREDS}
    ${resp}   ${id} =    Fusion Api Login Appliance    ${FUSION_IP}    ${creds}
    Should be equal as integers   ${resp['status_code']}    200    Unable to login to appliance!
    # Check to see if hardware is discovered yet, and if not, discover it
    ${encs} =    Fusion Api Get Enclosures
    Run keyword if   ${encs['count']} == 0   Perform hardware discovery

Process Bays
   [Documentation]    issues efuse command for all bays for the given bay type
   ...                valid types are in the REST API refrerence.
   ...                ex:   deviceBays, interconnectBays
   [Arguments]   ${bays}   ${type}   ${encuri}
   :FOR   ${bay}   IN   @{bays}
   \    ${body} =    json.loads    [{"op": "replace", "path": "/${type}/${bay['bayNumber']}/bayPowerState","value":"E-Fuse"}]
   \    ${resp} =    Fusion Api Patch Enclosure   ${body}   ${encuri}
   \    Log    \nE-Fuse request status_code: ${resp['status_code']} for ${encuri} bay ${bay['bayNumber']}   console=True

Perform hardware discovery
    [Documentation]    performs hardware discovery
    Invoke Hardware Setup  timeout=600  interval=30
    ${encs} =    Fusion Api Get Enclosures
    Run keyword if   ${encs['count']} == 0    Fail    No enclosures found after running tech-setup

Factory Reset Interconnects in Enclosure
    [Documentation]  Factory reset ICMs in an enclosure
    [Arguments]  ${enc}
    Get EM IP  enc_serial=${enc['serialNumber']}
    Get EM Token  ${enc['serialNumber']}
    :FOR  ${ic}  IN  @{enc['interconnectBays']}
    \  Log  \nFactory reset ICM ${ic['bayNumber']} on ${enc['name']}  console=True
    \  Run keyword if  '${ic['interconnectModel']}'!='${None}'  Factory Reset ICM  ${ic['bayNumber']}