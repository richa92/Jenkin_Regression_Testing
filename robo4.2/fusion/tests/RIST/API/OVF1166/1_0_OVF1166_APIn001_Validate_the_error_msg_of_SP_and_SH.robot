*** Settings ***
Documentation        OVF1166     APIn001 Validate The Error Message Of SP and SH which is not in same scope

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
Test Setup           Pre Test


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF1166_API_n001_Validate_The_Error_Message_Of_SP_And_SH_Which_Is_Not_In_Same_Scope
    [Documentation]    OVF1166_API_n001_Validate_The_Error_Message_Of_SP_And_SH_Which_Is_Not_In_Same_Scope
    Log To Console    \n- Test Case: OVF1166_API_n001_Validate_The_Error_Message_Of_SP_And_SH_Which_Is_Not_In_Same_Scope
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Validate Server Profile Error Message With Scope Limted User Session   server_profile_body=${n001_server_profile}
    Log To Console    \n- Test Case: Successfully: OVF1166_API_n001_Validate_The_Error_Message_Of_SP_And_SH_Which_Is_Not_In_Same_Scope
