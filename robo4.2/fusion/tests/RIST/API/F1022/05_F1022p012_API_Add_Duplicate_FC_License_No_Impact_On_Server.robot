*** Settings ***
Documentation        F1022p012_API_Add_Duplicate_FC_License_No_Impact_On_Server

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
Validate Duplicate FC License No Impact On Server License
    [Documentation]   F1022p012_API_Add_Duplicate_FC_License_No_Impact_On_Server
    ...               Add duplicate FC upgrade license, check its status and and check no impact on server license

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \nChecking the new license need to be added is existing in license pool    console=true
    Validate Exist Valid Licenses In License Pool But Unassigned To ICM  ${newLicenses}

    Log    Adding new licenses and validating results    console=true
    ${validLicenses}=     Get From Dictionary  ${newLicenses}  license
    :FOR    ${validLicense}  IN    @{validLicenses}
    \       ${addLicResp}=      Fusion Api Add License    ${validLicense["key"]}
    \       ${valDict}=    Create Dictionary    status_code=${412}
    \       Validate Response    ${addLicResp}  ${valDict}
    \       ${valDict} = 	Create Dictionary    message=License key already exists
    \       Validate Response Regex    ${addLicResp}  ${valDict}

    Log    Checking FC license did not be applied to serve hardware    console=true
    Validate FC Licenses Didn't Impact Server Hardware

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
