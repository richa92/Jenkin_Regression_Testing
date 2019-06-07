*** Settings ***
Documentation             Download Update Bin File, Upload it into Appliance, and Update Appliance with it.
Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   BuiltIn
Library                   robot.api.logger
Library                   Collections
Library                   OperatingSystem
Resource                  ../Fusion_Env_Setup/keywords.txt
Resource                  ./../../../../Resources/api/fusion_api_resource.txt
Resource                  ./keywords.txt
Variables                 ./Regression_Data.py

Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}           'DCS APPLIANCE IP'
${Ring}                   TBird13
${Add_User}               true
${Add_LE}                 true
${Add_Storage}            true
${Team_Name}              SHQA
${PASS_BUILD}             UNDEFINED

*** Test Cases ***
Check The Appliance Version After Upgrade
    Log     \n-- Check the appliance version after Upgrade    console=True
    ${resp}=   Fusion Api Get Appliance Version
    Should Be Equal As Integers     ${target_build_number}  ${resp["build"]}

Check The Resources After Upgrade
    Set log level  TRACE
    Log    \nCheck resources status By Name   console=True
    :FOR   ${resource}  IN    @{${Version}.resources_names}
    \    Check Resource Attribute    ${resource}  status  (?i)OK|Warning

Validate the default mode is Legacy
    [Documentation]    Check if the current security mode is Legacy
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =    Fusion Api Get Current Security Mode
    ${modeName} =    Get From Dictionary    ${resp}    modeName
    Should Be Equal    ${modeName}    LEGACY

Login Appliance With AD user
    [Documentation]    Relogin with AD user after appliance upgrade
    ${resp} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ad_user}
    ${status} =    Get From Dictionary    ${resp[0]}    status_code
    Should Be Equal    ${status}    ${200}

Login Appliance With Ldap user
    [Documentation]    Relogin with Ldap user
    ${resp} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ldap_user}
    ${status} =    Get From Dictionary    ${resp[0]}    status_code
    Should Be Equal    ${status}    ${200}

Check repo is in good status
    [Documentation]    Check if the repo is in good status after appliance upgrade
    ${resp} =    Fusion Api Get Repository
     :FOR    ${member}    IN    @{resp['members']}
    \       ${status} =      Get From Dictionary  ${member}  status
    \       should be true  '${status}' == 'OK'

Check ipdu is in good status
    [Documentation]    Check if the ipdu is in good status after appliance upgrade
    ${resp} =    Fusion Api Get Power Device
     :FOR    ${member}    IN    @{resp['members']}
    \       ${status} =      Get From Dictionary  ${member}  status
    \       should be true  '${status}' == 'OK' or '${status}' == 'Warning'

Blade removal and insertion
    Set Log Level    TRACE
    Log     \nBlade removal and insertion    console=True
    Remove All Server Profiles  force=${TRUE}
    ${shs}=  Fusion Api Get Server Hardware
    :FOR    ${sh}    IN    @{shs["members"]}
    \    ${position}=    Set Variable   ${sh["position"]}
    \    ${resp}=  Patch Enclosure  name=${ENC1}  op=replace  path=/deviceBays/${position}/bayPowerState  value=E-Fuse
    \    Wait For Task2    ${resp}    timeout=10m    interval=5
    \    Wait Until Keyword Succeeds   10 min  10 sec  Check Resource Attribute    SH:${sh["name"]}  status  (?i)OK|Warning
    \    Sleep  1m

Enclosure Refresh
    Set Log Level    TRACE
    Log    \nRefresh enclosure   console=True
    ${enc_resp}=    Get Enclosure    ${ENC1}
    ${resp}=    Refresh Enclosure    ${enc_resp}
    Wait For Task2    ${resp}    10m    5