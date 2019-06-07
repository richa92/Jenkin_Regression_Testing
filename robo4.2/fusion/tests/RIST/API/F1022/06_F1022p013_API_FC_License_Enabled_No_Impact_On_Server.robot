*** Settings ***
Documentation        F1022p013_API_FC_License_Enabled_No_Impact_On_Server

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
Validate Enabled FC Upgrade License Status And No Impact On Server License
    [Documentation]   F1022p013_API_FC_License_Enabled_No_Impact_On_Server
    ...               Enable FC upgrade license, check its status and check no impact on server license

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nRemoving existing FC licenses before testing    console=true
    Remove All FC Licenses

    Log    Adding new licenses    console=true
    ${validLicenses}=     Get From Dictionary  ${newLicenses}  license
    Add Licenses From Variable    ${validLicenses}

    Log    \nChecking the new licenses are existing in license pool    console=true
    Validate Exist Valid Licenses In License Pool But Unassigned To ICM  ${newLicenses}

    Log    Judge the Logical Enclosure is existing.    console=true
    ${le_uri}=    Get Logical Enclosure URI    ${LE_name}
    ${le_uri}=    Replace String    ${le_uri}  '  ${EMPTY}
    Should Not Be Equal           '${le_uri}'  '/rest/Logical_Enclosure_${LE_name}_not_found'

    Log    Adding fc uplinkset for LI if not existing.    console=true
    ${us_uri}=    Get Uplinkset URI    ${US_name}
    ${sourceFcUplinset}=   Deepcopy    ${fc_uplinkset}
    Should Be Equal As Strings  ${us_uri}  '/bad_uplinkset_uri'  msg=The fc uplinkset has exists, please remove it before rerun
    ${task}=  Add Uplinkset From Variable   ${sourceFcUplinset}
    Should Not Be Equal As Strings    ${task['taskState']}    Error  msg=Uplinkset addition failed.

    Log    Checking logical interconnect has been licensed.    console=true
    ${li_resp}=    Validate Logical Interconnect FC License Consumption  ${LI_name}  ${2}  Yes

    Log    Checking license nodes is licensed to interconnects correctly.    console=true
    Validate Exist Valid Licenses In License Pool And Assigned To ICM  ${newLicenses}  ${li_resp}

    Log    Checking FC license did not impact serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
