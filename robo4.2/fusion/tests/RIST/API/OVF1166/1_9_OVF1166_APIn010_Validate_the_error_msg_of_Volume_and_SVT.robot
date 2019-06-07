*** Settings ***
Documentation        OVF1166     APIn010 Validate The Error Message Of Volume and Volume Template which is not in same scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF1166.txt


Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1166_API_n010_Validate_The_Error_Message_Of_Volume_And_Volumes_Template_Which_Is_Not_In_Same_Scope
    [Documentation]    OVF1166_API_n010_Validate_The_Error_Message_Of_Volume_And_Volumes_Template_Which_Is_Not_In_Same_Scope
    Log To Console    \n- Test Case: OVF1166_API_n010_Validate_The_Error_Message_Of_Volume_And_Volumes_Template_Which_Is_Not_In_Same_Scope
    credential Login     ${credentials_list}
    ${index} =     Set Variable      ${0}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Validate Volume Error Message With Scope Limited User Session   ${n010_volume_profile[${index}]}
    \        ${index} =     Set Variable      ${index+1}
    Log To Console    \n- Test Case: Successfully: OVF1166_API_n010_Validate_The_Error_Message_Of_Volume_And_Volumes_Template_Which_Is_Not_In_Same_Scope
