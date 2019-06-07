*** Settings ***
Documentation     OVF806: i3S - Profile - Changing Server Profile OS Deployment Plan should preserve settings common to both plans

Resource          resource.robot
Suite Setup       Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${serveradmin}
Test Setup        OVF806 Test Setup
Suite Teardown    I3S Suite Teardown


*** Test Cases ***
OVTC53178
    [Documentation]    As a server administrator, I would like to chose a different deployment plan
    ...    for a SPT that has associated SPs. The deployment plan has removed few CA's and added two more CA's
    [Tags]    OVF806_TC08

    ${tc08_spt} =    copy.deepcopy    ${spt}
    ${tc08_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc08_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc08_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc08_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc08_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc08_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc08_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc08_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVTC53179
    [Documentation]    As a server administrator, I want to Update from Template
    ...    when a SP using SPT has its deployment plan changed. Both the deployment plans have the same set of custom attributes.
    [Tags]    OVF806_TC09

    ${tc09_spt} =    copy.deepcopy    ${spt}
    ${tc09_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc09_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc09_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc09_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc09_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc09_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc09_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc09_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'=='NonCompliant'    Fail    Profile is NonCompliant even after updating its SPT

OVTC53180
    [Documentation]    ver administrator, I want to 'Update from Template' when a SP using SPT has its deployment plan
    ...    modified. Both the deployment plans dont have the same set of custom attributes.
    [Tags]    OVF806_TC10

    ${tc08_spt} =    copy.deepcopy    ${spt}
    ${tc08_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc08_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc08_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc08_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc08_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc08_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc08_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc08_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVTC53181
    [Documentation]    As a server administrator, I want to 'Update from Template'
    ...    when a SP using SPT has its deployment plan modified. The deployment plans have the same set of custom attributes
    ...    but their default values are different (SP was deployed using default values).
    [Tags]    OVF806_TC11

    ${tc11_spt} =    copy.deepcopy    ${spt}
    ${tc11_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc11_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc11_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc11_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc11_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc11_editSpt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Check profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc11_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc11_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc11_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'=='NonCompliant'    Fail    Profile is NonCompliant even after updating its SPT

OVTC53182
    [Documentation]    As a server administrator, I want to 'Update from Template' when a SP using SPT has its
    ...    deployment plan modified. The deployment plans have few CA's that are different.
    [Tags]    OVF806_TC12

    ${tc08_spt} =    copy.deepcopy    ${spt}
    ${tc08_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc08_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc08_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc08_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc08_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc08_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc08_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc08_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVTC53184
    [Documentation]    As a server administrator, I want to modify a SP that is non-complaint with its SPT.
    ...    The deployment plan is modified to one that is not part of the current SP nor the SPT.
    [Tags]    OVF806_TC14

    ${tc14_spt} =    copy.deepcopy    ${spt}
    ${tc14_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc14_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc14_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc14_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc14_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc14_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${tc14_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc14_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc14_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc14_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53185
    [Documentation]    As a server administrator, I want to change the deployment plan for a particular SP that is assigned.
    ...    However, I would like to use the default values that are set in the new deployment plan.
    [Tags]    OVF806_TC15

    ${tc15_spt} =    copy.deepcopy    ${spt}
    ${tc15_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc15_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc15_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc15_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc15_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc15_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf} =    Edit I3S Server Profile    ${tc15_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc15_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc15_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc15_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53186
    [Documentation]    As a server administrator, I want to change a SP to a different SPT that has a different deployment plan.
    [Tags]    OVF806_TC16

    ${tc16_spt1} =    copy.deepcopy    ${spt}
    ${tc16_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc16_spt1}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc16_spt1['name']}'

    ${tc16_spt2} =    copy.deepcopy    ${spt}
    Set To Dictionary    ${tc16_spt2}    name=OVF806_SPT2
    Set To Dictionary    ${tc16_spt2['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnCreateSPT} =    Create I3S SPT    ${tc16_spt2}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc16_spt2['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc16_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc16_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc16_sp['name']}

    # Edit Sp and Change DP
    ${tc16_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc16_editSp}    serverProfileTemplateUri=${tc16_spt2['name']}
    ${blnEditProf}=  Edit I3S Server Profile  ${tc16_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc16_editSp['name']}' with different DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc16_sp['name']}

    # Verifying default values of custom attributes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    Remove SPT And Server Profiles by SPT    OVF806_SPT2

OVTC53187
    [Documentation]    As a server administrator, I want to change the SP from a
    ...    single NIC model to a NIC team model as configured by a different deployment plan
    [Tags]    OVF806_TC17

    ${tc17_spt} =    copy.deepcopy    ${spt}
    ${tc17_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc17_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc17_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc17_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc17_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${sp_resp} =    Get Server Profile    ${tc17_sp['name']}
    ${attributes} =    Create List    ipaddress
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_resp}    ${attributes}
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc17_sp['name']}

    # Edit Sp and Change DP
    ${editSp} =    copy.deepcopy    ${tc17_editSp}
    ${blnEditProf}=  Edit I3S Server Profile  ${editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${editSp['name']}' with different DP

    # Get Deafult Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc17_sp['name']}
    ${attributes1} =    Create List    ipaddress1
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc17_sp['name']}

    # Verifying default values of custom attributes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53188
    [Documentation]    As a server administrator, I want to change the SPTs deployment plan
    ...    from a single NIC model to NIC team model. It has no associated SPs
    [Tags]    OVF806_TC18

    ${tc18_spt} =    copy.deepcopy    ${sptWithTeamedNicDp}
    ${tc18_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc18_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc18_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc18_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc18_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${sp_resp} =    Get Server Profile    ${tc18_sp['name']}
    ${attributes} =    Create List    ipaddress1
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_resp}    ${attributes}
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc18_sp['name']}

    # Edit Sp and Change DP
    ${editSp} =    copy.deepcopy    ${tc15_editSp}
    ${blnEditProf}=  Edit I3S Server Profile  ${editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc18_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc18_sp['name']}
    ${attributes1} =    Create List    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc18_sp['name']}

    # Verifying default values of custom attributes
    # Should Not Be Equal As String    '${attrib_values[0]}'    '${attrib_values1[0]}'    Host NIC values not changed
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53189
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan from a single NIC model to NIC team model. It has no associated SPs
    [Tags]    OVF806_TC19

    ${tc19_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc19_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc19_spt['name']}'

    ${tc19_editSpt}=    copy.deepcopy    ${sptWithTeamedNicDp}
    ${blnupdateProf}=    Edit I3S SPT    ${tc19_editSpt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${tc19_editSpt['name']}'

OVTC53190
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan from a single NIC model to NIC team model. It has associated SPs
    [Tags]    OVF806_TC20

    ${tc20_spt} =    copy.deepcopy    ${spt}
    ${tc20_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc20_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc20_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc20_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc20_sp['name']}'

    ${tc20_editSpt}=    copy.deepcopy    ${sptWithTeamedNicDp}
    ${blnupdateProf}=    Edit I3S SPT    ${tc20_editSpt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${tc20_editSpt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc20_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVTC53191
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan from a NIC team model to a single NIC model. It has associated SPs
    [Tags]    OVF806_TC21

    ${tc21_spt} =    copy.deepcopy    ${sptWithTeamedNicDp}
    ${tc21_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc21_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc21_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc21_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc21_sp['name']}'

    ${tc21_editSpt}=    copy.deepcopy    ${spt}
    ${blnupdateProf}=    Edit I3S SPT    ${tc21_editSpt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${tc21_editSpt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc21_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVTC53192
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan to a new one with a different golden image.  Build plan reamins the same. It has no associated server profiles.
    [Tags]    OVF806_TC22

    ${tc22_spt} =    copy.deepcopy    ${spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc22_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc22_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

OVTC53193
    [Documentation]    As a server administrator, I want to change a SPs
    ...    deployment plan to a newer with that has a different golden image. Build plan remains the same.
    [Tags]    OVF806_TC23

    ${tc23_spt} =    copy.deepcopy    ${spt}
    ${tc23_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc23_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc23_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc23_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc23_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    # Edit Sp and Change DP
    ${tc23_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc23_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc23_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc23_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53194
    [Documentation]    As a server administrator, I want to change a SPTs
    ...    deployment plan to the one with a newer golden image. It has server profiles associated.
    [Tags]    OVF806_TC24

    ${tc24_spt} =    copy.deepcopy    ${spt}
    ${tc24_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc24_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc24_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc24_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc24_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc24_sp['name']}

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc24_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVTC53195
    [Documentation]    As a server administrator, I want to change a SP to a newer deployment plan.
    ...    The SP was created from a SPT that is using a older Golden image. Edit profile of this system.
    [Tags]    OVF806_TC25

    ${tc23_spt} =    copy.deepcopy    ${spt}
    ${tc23_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc23_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc23_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc23_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc23_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    # Edit Sp and Change DP
    ${tc23_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc23_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc23_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc23_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53196
    [Documentation]    As a server administrator, I want to change a SP to a newer deployment plan.
    ...    The SP was created from a SPT that is using a older Golden image. Update from profile template.
    [Tags]    OVF806_TC26

    ${tc23_spt} =    copy.deepcopy    ${spt}
    ${tc23_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc23_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc23_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc23_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc23_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    # Edit Sp and Change DP
    ${tc23_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc23_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc23_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc23_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc23_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc23_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVTC53197
    [Documentation]    As a server administrator, I want to revert the SPT
    ...    to its former Deployment plan. There are no associated server profiles
    [Tags]    OVF806_TC27

    ${tc27_spt} =    copy.deepcopy    ${spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc27_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc27_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    ${edit_spt1}=    copy.deepcopy    ${spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt1}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt1['name']}'

OVTC53198
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan.
    ...    It is associated to a SPT. The plan is to update the SPT also
    [Tags]    OVF806_TC28    OVF806_TC29

    ${tc29_spt} =    copy.deepcopy    ${spt}
    ${tc29_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc29_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc29_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc29_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc29_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc29_sp['name']}

    # Edit Sp and Change DP
    ${tc29_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc29_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc29_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc29_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSp} =    Get Server Profile    ${tc29_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSp['templateCompliance']}'!='NonCompliant'    Fail    Profile is consistent with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc29_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

OVTC53199
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan. It is
    ...    associated to a SPT. The plan is to update the SPT also
    [Tags]    OVF806_TC29

    ${tc29_spt} =    copy.deepcopy    ${spt}
    ${tc29_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc29_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc29_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc29_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc29_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc29_sp['name']}

    # Edit Sp and Change DP
    ${tc29_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc29_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc29_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc29_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSp} =    Get Server Profile    ${tc29_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSp['templateCompliance']}'!='NonCompliant'    Fail    Profile is consistent with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc29_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

OVTC53200
    [Documentation]    As a server administrator, I want to revert the SPT to its
    ...    former Deployment plan. It has associated server profiles.
    [Tags]    OVF806_TC30

    ${tc30_spt} =    copy.deepcopy    ${spt}
    ${tc30_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc30_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc30_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc30_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc30_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc30_sp['name']}

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSp} =    Get Server Profile    ${tc30_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSp['templateCompliance']}'!='NonCompliant'    Fail    Profile is consistent with SPT after updating DP

    # Edit Sp and Change DP
    ${tc30_editSp} =    copy.deepcopy    ${tc15_editSp}
    Set To Dictionary    ${tc30_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc30_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc30_editSp['name']}' with different DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc30_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVTC53201
    [Documentation]    As a server administrator, I want to revert the SPT to its former Deployment plan.
    ...    There are no associated server profiles. There are changes to the custom attributes - older deployment plan reduces the number of Cas
    [Tags]    OVF806_TC31    OVF806_TC33

    ${spt} =    copy.deepcopy    ${tc31_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc31_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc31_spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Get Deafult Custom attributes from profile DP
    ${cas_afterSptUpdate} =    Get Default custom Attributes From DP    SPT:${tc31_spt['name']}

    Log    Verifying spt does not have 'User Name' ca    console=True
    ${caList_afterSptUpdate} =    Get Dictionary keys    ${cas_afterSptUpdate}
    List Should Not Contain Value   ${caList_afterSptUpdate}    UserName    SPT '${tc31_spt['name']}' contains CA 'UserName'

OVTC53202
    [Documentation]    As a server administrator, I want to revert the STP to
    ...    its former deployment plan. There are no associated server profiles. The older deployment plan has additional CAs
    [Tags]    OVF806_TC32

    ${tc32_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc32_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc31_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Get Deafult Custom attributes from profile DP
    ${cas_afterSptUpdate} =    Get Default custom Attributes From DP    SPT:${tc32_spt['name']}

    Log    Verifying spt contains 'User Name' ca    console=True
    ${caList_afterSptUpdate} =    Get Dictionary keys    ${cas_afterSptUpdate}
    List Should Contain Value   ${caList_afterSptUpdate}    UserName    SPT '${tc32_spt['name']}' does not contains CA 'UserName'

OVTC53203
    [Documentation]    As a server administrator, I want to revert the SPT to its former Deployment plan.
    ...    There are no associated server profiles. There are changes to the custom attributes - older deployment plan reduces the number of Cas
    [Tags]    OVF806_TC33

    ${spt} =    copy.deepcopy    ${tc31_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc31_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc31_spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile tempalte '${edit_spt['name']}'

    # Get Deafult Custom attributes from profile DP
    ${cas_afterSptUpdate} =    Get Default custom Attributes From DP    SPT:${tc31_spt['name']}

    Log    Verifying spt does not have 'User Name' ca    console=True
    ${caList_afterSptUpdate} =    Get Dictionary keys    ${cas_afterSptUpdate}
    List Should Not Contain Value   ${caList_afterSptUpdate}    UserName    SPT '${tc31_spt['name']}' contains CA 'UserName'

OVTC53204
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan.
    ...    It is not associated to a SPT. The older deployment plan has more CA's than the current plan.
    [Tags]    OVF806_TC34

    ${sp_body} =    copy.deepcopy    ${tc34_sp}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${edit_sp} =    copy.deepcopy    ${tc34_sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWithUserName['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'

OVTC53205
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan.
    ...    It is associated to a SPT. The older deployment has more CAs than the current plan.
    [Tags]    OVF806_TC35

    ${tc35_spt} =    copy.deepcopy    ${spt}
    ${tc35_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc35_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc35_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc35_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc35_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc35_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc35_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc35_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc35_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc35_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc35_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVTC53206
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan.
    ...    It is associated to a SPT. The older deployment has more CA's than the current plan. Update the profile via the SPT
    [Tags]    OVF806_TC36

    ${tc36_spt} =    copy.deepcopy    ${spt}
    ${tc36_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc36_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc36_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc36_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc36_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc36_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc35_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc35_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc36_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc36_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc36_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc36_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='Compliant'    Fail    Profile is not Compliant with SPT after updating DP

OVTC53207
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan.
    ...    It is associated to a SPT. The older deployment has less CAs than the current plan. Update the profile via the SPT
    [Tags]    OVF806_TC37

    ${tc37_spt} =    copy.deepcopy    ${spt}
    ${tc37_sp} =    copy.deepcopy    ${sp_from_spt}

    Set To Dictionary    ${tc37_spt['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${tc37_spt['osDeploymentSettings']}    osCustomAttributes=${cas_dpWithUserName['osCustomAttributes']}
    ${blnCreateSPT} =    Create I3S SPT    ${tc37_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc37_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc37_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc37_sp['name']}'

    # Get Deafult Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc37_sp['name']}

    # Edit Sp and Change DP
    ${edit_tc37_sp} =    copy.deepcopy    ${edit_tc35_sp}
    Set To Dictionary    ${edit_tc37_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_tc37_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc37_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc37_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc37_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Deafult Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc37_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc37_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc37_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='Compliant'    Fail    Profile is not Compliant with SPT after updating DP
