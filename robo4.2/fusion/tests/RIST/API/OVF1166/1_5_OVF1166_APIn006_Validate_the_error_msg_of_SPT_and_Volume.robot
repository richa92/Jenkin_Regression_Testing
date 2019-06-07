*** Settings ***
Documentation        OVF1166     APIn006 Validate The Error Message Of SPT and Volumes which is not in same scope

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
OVF1166_API_n006_Validate_The_Error_Message_Of_SP_And_Volumes_Which_Is_Not_In_Same_Scope
    [Documentation]    OVF1166_API_n006_Validate_The_Error_Message_Of_SPT_And_Volumes_Which_Is_Not_In_Same_Scope
    Log To Console    \n- Test Case: OVF1166_API_n006_Validate_The_Error_Message_Of_SPT_And_Volumes_Which_Is_Not_In_Same_Scope
    credential Login     ${credentials_list}
    :FOR     ${credential}     IN     @{credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Validate Server Profile Template Error Message With Scope Limited User Session   ${n006_server_profile_template}
    Log To Console    \n- Test Case: Successfully: OVF1166_API_n006_Validate_The_Error_Message_Of_SPT_And_Volumes_Which_Is_Not_In_Same_Scope
