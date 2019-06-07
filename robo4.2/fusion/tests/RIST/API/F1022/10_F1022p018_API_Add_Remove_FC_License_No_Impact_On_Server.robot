*** Settings ***
Documentation        F1022p018_API_Add_Remove_FC_License_No_Impact_On_Server

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Validate Add & Remove FC Licenses 10 Times And No Impact On Server License
    [Documentation]  F1022p018_API_Add_Remove_FC_License_No_Impact_On_Server
    ...              Add and remove FC Licenses at least 10 times. Verify it has no impact on server license status

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nRemoving FC license before test    console=true
    Remove All FC Licenses

    ${times}=    Set Variable  10
    :FOR    ${index}   IN RANGE  ${times}
    \       ${time}=   Evaluate    ${index} + 1
    \       Log    The ${time} times loop for testing .....    console=true
    \       Log    ----------------------------------    console=true

    \       Log    Adding fc uplinkset for LI if not existing.    console=true
    \       ${us_uri}=    Get Uplinkset URI    ${US_name}
    \       ${sourceFcUplinset}=   Deepcopy    ${fc_uplinkset}
    \       Should Be Equal As Strings  ${us_uri}  '/bad_uplinkset_uri'
    \       ${task}=  Add Uplinkset From Variable   ${sourceFcUplinset}
    \       Should Not Be Equal As Strings    ${task['taskState']}    Error   msg=LE grant license should be failed due to no FC licenses

    \       Log    Sleep 60 seconds, waiting for the fc licenses applied    console=true
    \       Sleep    60s

    \       Log    Checking logical interconnect need licenses.    console=true
    \       ${li_resp}=    Validate Logical Interconnect FC License Consumption  ${LI_name}  ${0}  YesWillBeApplied

    \       Log    Adding new licenses    console=true
    \       ${validLicenses}=     Get From Dictionary  ${newLicenses}  license
    \       Add Licenses From Variable    ${validLicenses}

    \       Log    Sleep 1 min, waiting for the fc licenses applied    console=true
    \       Sleep    60s

    \       Log    Checking logical interconnect has been licensed.    console=true
    \       ${li_resp}=    Validate Logical Interconnect FC License Consumption  ${LI_name}  ${2}  Yes

    \       Log    Checking license nodes is licensed to interconnects correctly.    console=true
    \       Validate Exist Valid Licenses In License Pool And Assigned To ICM  ${newLicenses}  ${li_resp}

    \       Log    Checking FC license did not impact serve hardware    console=true
    \       Validate FC Licenses Didn't Impact Server Hardware

    \       Log    Removing fc uplinkset from LI.    console=true
    \       ${us_uri}=    Get Uplinkset URI    ${US_name}
    \       Should Not Be Equal As Strings  ${us_uri}  '/bad_uplinkset_uri'  msg=The fc uplinkset has been removed previously.
    \       ${resp}    Remove Uplinkset By Uri  ${us_uri}
    \       Wait For Task2   ${resp}    6min    5

    \       Log    Sleep 60 seconds, waiting for the fc licenses applied    console=true
    \       Sleep    60s

    \       Log    \nRemoving FC license.    console=true
    \       Remove All FC Licenses

    \       Log    Checking all FC licenses are deleted from license pool    console=true
    \       Validate Not Exist FC Licenses In License Pool    ${newLicenses}

    \       Log    Checking licenses has been released from interconnect.    console=true
    \       Validate Logical Interconnect FC License Consumption  ${LI_name}  ${0}  No

    \       Log    Checking FC license did not impact serve hardware    console=true
    \       Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
