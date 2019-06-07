*** Settings ***
Documentation     OVF806: i3S - Profile - Changing Server Profile OS Deployment Plan should preserve settings common to both plans

Resource          resource.robot
Suite Setup       Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Test Setup        OVF806 Test Setup
Suite Teardown    I3S Suite Teardown


*** Test Cases ***
OVF806_TC11 Change DP of SPT which has associated SP, New DP has changed CA
    [Documentation]    As a server administrator, I would like to choose a different deployment plan
    ...    for a SPT that has associated SPs. The deployment plan has removed few CA's and added two more CA's
    [Tags]    TC11    OVF806

    ${tc11_spt} =    copy.deepcopy    ${spt}
    ${tc11_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc11_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc11_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc11_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc11_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc11_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc11_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc11_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVF806_TC12 Perform "Update from Template" when DP of the SP has changes , new DP has same CA
    [Documentation]    As a server administrator, I want to 'Update from Template'
    ...    when a SP using SPT has its deployment plan modified. The deployment plans have the same set of custom attributes
    ...    but their default values are different (SP was deployed using default values)
    [Tags]    TC12    OVF806

    ${tc12_spt} =    copy.deepcopy    ${spt}
    ${tc12_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc12_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc12_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc12_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc12_sp['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc12_editSpt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Check profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${tc12_sp['name']}
    Run Keyword If    '${sp_resp_after_updating_spt['templateCompliance']}'!='NonCompliant'    Fail    Profile is not NonCompliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${tc12_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc12_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'=='NonCompliant'    Fail    Profile is NonCompliant even after updating its SPT

OVF806_TC15 Modify a SP that is non-complaint with its SPT. The deployment plan is modified to one that is not part of the current SP nor the SPT
    [Documentation]    As a server administrator, I want to modify a SP that is non-complaint with its SPT
    ...    The deployment plan is modified to one that is not part of the current SP nor the SPT
    [Tags]    TC15    OVF806

    ${tc15_spt} =    copy.deepcopy    ${spt}
    ${tc15_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc15_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc15_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc15_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc15_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc15_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${tc15_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc15_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc15_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc15_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC16 Change the deployment plan for a particular SP that is assigned
    [Documentation]    As a server administrator, I want to change the deployment plan for a particular SP that is assigned
    ...    However, I would like to use the default values that are set in the new deployment plan
    [Tags]    TC16    OVF806

    ${tc16_spt} =    copy.deepcopy    ${spt}
    ${tc16_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc16_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc16_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc16_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc16_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc16_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf} =    Edit I3S Server Profile    ${tc16_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc16_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc16_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc16_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC17 Change a SP to a different SPT that has a different deployment plan
    [Documentation]    As a server administrator, I want to change a SP to a different SPT that has a different deployment plan
    [Tags]    TC17    OVF806

    ${tc17_spt1} =    copy.deepcopy    ${spt}
    ${tc17_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc17_spt1}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc17_spt1['name']}'

    ${tc17_spt2} =    copy.deepcopy    ${spt}
    Set To Dictionary    ${tc17_spt2}    name=OVF806_SPT2
    Set To Dictionary    ${tc17_spt2['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnCreateSPT} =    Create I3S SPT    ${tc17_spt2}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc17_spt2['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc17_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc17_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc17_sp['name']}

    # Edit Sp and Change DP
    ${tc17_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc17_editSp}    serverProfileTemplateUri=${tc17_editSp['name']}
    ${blnEditProf}=  Edit I3S Server Profile  ${tc17_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc17_editSp['name']}' with different DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc17_sp['name']}

    # Verifying default values of custom attributes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    Remove SPT And Server Profiles by SPT    OVF806_SPT2

OVF806_TC18 Change the SP from a single NIC model to a NIC team model as configured by a different deployment plan
    [Documentation]    As a server administrator, I want to change the SP from a
    ...    single NIC model to a NIC team model as configured by a different deployment plan
    [Tags]    TC18    OVF806

    ${tc18_spt} =    copy.deepcopy    ${spt}
    ${tc18_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc18_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc18_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc18_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc18_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${sp_resp} =    Get Server Profile    ${tc18_sp['name']}
    ${attributes} =    Create List    ipaddress
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_resp}    ${attributes}
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc18_sp['name']}

    # Edit Sp and Change DP
    ${editSp} =    copy.deepcopy    ${tc18_editSp}
    ${blnEditProf}=  Edit I3S Server Profile  ${editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${editSp['name']}' with different DP

    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc18_sp['name']}
    ${attributes1} =    Create List    ipaddress1
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc18_sp['name']}

    # Verifying default values of custom attributes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC20 Change the SPT's deployment plan from a single NIC model to NIC team model, It has no associated SPs
    [Documentation]    As a server administrator, I want to change the SPTs deployment plan
    ...    from a single NIC model to NIC team model. It has no associated SPs
    [Tags]    TC20    OVF806

    ${tc20_spt} =    copy.deepcopy    ${sptWithTeamedNicDp}
    ${tc20_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc20_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc20_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc20_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc20_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${sp_resp} =    Get Server Profile    ${tc20_sp['name']}
    ${attributes} =    Create List    ipaddress1
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_resp}    ${attributes}
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc20_sp['name']}

    # Edit Sp and Change DP
    ${editSp} =    copy.deepcopy    ${tc16_editSp}
    ${blnEditProf}=  Edit I3S Server Profile  ${editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc20_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc20_sp['name']}
    ${attributes1} =    Create List    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc20_sp['name']}

    # Verifying default values of custom attributes
    # Should Not Be Equal As String    '${attrib_values[0]}'    '${attrib_values1[0]}'    Host NIC values not changed
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC21 Change the SPT's deployment plan from a single NIC model to NIC team model, It has associated SPs
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan from a single NIC model to NIC team model. It has associated SPs
    [Tags]    TC21    OVF806

    ${tc21_spt} =    copy.deepcopy    ${spt}
    ${tc21_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc21_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc21_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc21_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc21_sp['name']}'

    ${tc21_editSpt}=    copy.deepcopy    ${sptWithTeamedNicDp}
    ${blnupdateProf}=    Edit I3S SPT    ${tc21_editSpt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${tc21_editSpt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc21_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVF806_TC22 Change the SPT's deployment plan from a NIC team model to a single NIC model, It has associated SPs
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan from a NIC team model to a single NIC model. It has associated SPs
    [Tags]    TC22    OVF806

    ${tc22_spt} =    copy.deepcopy    ${sptWithTeamedNicDp}
    ${tc22_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc22_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc22_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc22_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc22_sp['name']}'

    ${tc22_editSpt}=    copy.deepcopy    ${spt}
    ${blnupdateProf}=    Edit I3S SPT    ${tc22_editSpt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${tc22_editSpt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc22_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVF806_TC23 Change the SPT's deployment plan to a new one with a different golden image,Build plan remains the same, It has no associated server profiles
    [Documentation]    As a server administrator, I want to change the SPTs
    ...    deployment plan to a new one with a different golden image.  Build plan remains the same. It has no associated server profiles
    [Tags]    TC23    OVF806

    ${tc23_spt} =    copy.deepcopy    ${spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc23_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc23_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

OVF806_TC24 Change a SP's deployment plan to a newer with that has a different golden image, Build plan remains the same
    [Documentation]    As a server administrator, I want to change a SPs
    ...    deployment plan to a newer with that has a different golden image. Build plan remains the same
    [Tags]    TC24    OVF806

    ${tc24_spt} =    copy.deepcopy    ${spt}
    ${tc24_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc24_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc24_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc24_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc24_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc24_sp['name']}

    # Edit Sp and Change DP
    ${tc24_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc24_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc24_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc24_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc24_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC25 Change a SPT's deployment plan to the one with a newer golden image,It has server profiles associated
    [Documentation]    As a server administrator, I want to change a SPTs
    ...    deployment plan to the one with a newer golden image. It has server profiles associated
    [Tags]    TC25    OVF806

    ${tc25_spt} =    copy.deepcopy    ${spt}
    ${tc25_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc25_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc25_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc25_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc25_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc25_sp['name']}

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc25_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

OVF806_TC26 Change a SP to a newer deployment plan,The SP was created from a SPT that is using a older Golden image
    [Documentation]    As a server administrator, I want to change a SP to a newer deployment plan
    ...    The SP was created from a SPT that is using a older Golden image. Edit profile of this system
    [Tags]    TC26    OVF806

    ${tc26_spt} =    copy.deepcopy    ${spt}
    ${tc26_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc26_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc26_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc26_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc26_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc26_sp['name']}

    # Edit Sp and Change DP
    ${tc26_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc23_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc26_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc26_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc26_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC27 Change a SP to a newer deployment plan, SP was created from a SPT that is using a older Golden image
    [Documentation]    As a server administrator, I want to change a SP to a newer deployment plan
    ...    The SP was created from a SPT that is using a older Golden image. Update from profile template
    [Tags]    TC27    OVF806

    ${tc27_spt} =    copy.deepcopy    ${spt}
    ${tc27_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc27_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc27_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc27_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc27_sp['name']}'
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc27_sp['name']}

    # Edit Sp and Change DP
    ${tc27_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc27_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc27_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc27_editSp['name']}' with different DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc27_sp['name']}

    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc27_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVF806_TC28 Revert the SPT to its former Deployment plan, There are no associated SPs
    [Documentation]    As a server administrator, I want to revert the SPT
    ...    to its former Deployment plan. There are no associated server profiles
    [Tags]    TC28    OVF806

    ${tc28_spt} =    copy.deepcopy    ${spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc28_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc28_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    ${edit_spt1}=    copy.deepcopy    ${spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt1}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt1['name']}'

OVF806_TC31 revert the SP to its former deployment plan, It is associated to a SPT, update the SPT also
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan
    ...    It is associated to a SPT. The plan is to update the SPT also
    [Tags]    TC31    OVF806

    ${tc31_spt} =    copy.deepcopy    ${spt}
    ${tc31_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc31_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc31_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc31_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc31_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc31_sp['name']}

    # Edit Sp and Change DP
    ${tc31_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc31_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc31_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc31_editSp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSp} =    Get Server Profile    ${tc31_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSp['templateCompliance']}'!='NonCompliant'    Fail    Profile is consistent with SPT after updating DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc31_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

OVF806_TC32 Revert the SPT to its former Deployment plan, It has associated SPs
    [Documentation]    As a server administrator, I want to revert the SPT to its
    ...    former Deployment plan. It has associated server profiles
    [Tags]    TC32    OVF806

    ${tc32_spt} =    copy.deepcopy    ${spt}
    ${tc32_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc32_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc32_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc32_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc32_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc32_sp['name']}

    ${edit_spt}=    copy.deepcopy    ${spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSp} =    Get Server Profile    ${tc32_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSp['templateCompliance']}'!='NonCompliant'    Fail    Profile is consistent with SPT after updating DP

    # Edit Sp and Change DP
    ${tc32_editSp} =    copy.deepcopy    ${tc16_editSp}
    Set To Dictionary    ${tc32_editSp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditProf}=    Edit I3S Server Profile    ${tc32_editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${tc32_editSp['name']}' with different DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc32_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC33 Revert the SPT to its former Deployment plan, There are no associated SPs
    [Documentation]    As a server administrator, I want to revert the SPT to its former Deployment plan
    ...    There are no associated server profiles. There are changes to the custom attributes - older deployment plan reduces the number of Cas
    [Tags]    TC33    OVF806

    ${spt} =    copy.deepcopy    ${tc33_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc33_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc33_spt}
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_spt['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Get Default Custom attributes from profile DP
    ${cas_afterSptUpdate} =    Get Default custom Attributes From DP    SPT:${tc33_spt['name']}

    Log    Verifying spt does not have 'User Name' ca    console=True
    ${caList_afterSptUpdate} =    Get Dictionary keys    ${cas_afterSptUpdate}
    List Should Not Contain Value   ${caList_afterSptUpdate}    UserName    SPT '${tc33_spt['name']}' contains CA 'UserName'

OVF806_TC34 Revert the STP to its former deployment plan, There are no associated SP, The older DP has additional CA's
    [Documentation]    As a server administrator, I want to revert the STP to
    ...    its former deployment plan. There are no associated server profiles. The older deployment plan has additional CAs
    [Tags]    TC34    OVF806

    ${tc34_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc34_spt['name']}'

    ${edit_spt}=    copy.deepcopy    ${tc34_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'

    # Get Default Custom attributes from profile DP
    ${cas_afterSptUpdate} =    Get Default custom Attributes From DP    SPT:${edit_spt['name']}

    Log    Verifying spt contains 'User Name' ca    console=True
    ${caList_afterSptUpdate} =    Get Dictionary keys    ${cas_afterSptUpdate}
    List Should Contain Value    ${caList_afterSptUpdate}    UserName    SPT '${edit_spt['name']}' does not contains CA 'UserName'

OVF806_TC36 Revert the SP to its former DP. It is not associated to a STP. The older deployment plan has more CA's than the current plan
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan
    ...    It is not associated to a SPT. The older deployment plan has more CA's than the current plan
    [Tags]    TC36    OVF806

    ${sp_body} =    copy.deepcopy    ${tc36_sp}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${edit_sp} =    copy.deepcopy    ${tc36_sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWithUserName['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'

OVF806_TC38 Revert the SP to its former DP. It is associated to a SPT. The older deployment has more CA's than the current plan
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan
    ...    It is associated to a SPT. The older deployment has more CAs than the current plan
    [Tags]    TC38    OVF806

    ${tc38_spt} =    copy.deepcopy    ${spt}
    ${tc38_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc38_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc38_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc38_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc38_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc38_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc38_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc38_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc38_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc38_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc38_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

OVF806_TC40 Revert the SP to its former DP,It is associated to a SPT, The older deployment has more CA's than the current plan. Update the profile via the SPT
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan
    ...    It is associated to a SPT. The older deployment has more CA's than the current plan. Update the profile via the SPT
    [Tags]    TC40    OVF806

    ${tc40_spt} =    copy.deepcopy    ${spt}
    ${tc40_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${tc40_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc40_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc40_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc40_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc40_sp['name']}

    # Edit Sp and Change DP
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc38_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc38_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc40_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc40_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc40_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc40_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='Compliant'    Fail    Profile is not Compliant with SPT after updating DP

OVF806_TC41 Revert the SP to its former deployment plan. It is associated to a SPT. The older deployment has less CA's than the current plan. Update the profile via the SPT
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan
    ...    It is associated to a SPT. The older deployment has less CAs than the current plan. Update the profile via the SPT
    [Tags]    TC41    OVF806

    ${tc41_spt} =    copy.deepcopy    ${spt}
    ${tc41_sp} =    copy.deepcopy    ${sp_from_spt}

    Set To Dictionary    ${tc41_spt['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${tc41_spt['osDeploymentSettings']}    osCustomAttributes=${cas_dpWithUserName['osCustomAttributes']}
    ${blnCreateSPT} =    Create I3S SPT    ${tc41_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc41_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc41_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc41_sp['name']}'

    # Get Default Custom attributes from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc41_sp['name']}

    # Edit Sp and Change DP
    ${edit_tc41_sp} =    copy.deepcopy    ${edit_tc38_sp}
    Set To Dictionary    ${edit_tc41_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_tc41_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnEditProf}=  Edit I3S Server Profile  ${edit_tc41_sp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${edit_tc41_sp['name']}' with different DP

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc41_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='NonCompliant'    Fail    Profile is NonCompliant with SPT after updating DP

    # Get Default Custom attributes from profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc41_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

    ${blnUpdateSp} =    Update SP From SPT    ${tc41_sp['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Check SP compliance with SPT
    ${sp_resp_afterUpdatingFromSpt} =    Get Server Profile    ${tc41_sp['name']}
    Run Keyword If    '${sp_resp_afterUpdatingFromSpt['templateCompliance']}'!='Compliant'    Fail    Profile is not Compliant with SPT after updating DP

OVF806_TC01 Re-deploy SP with new DP with no additional CA
    [Documentation]    As a server administrator, I would like to re-deploy a server profile with a new deployment plan. It has no additional custom attribute
    [Tags]    TC01    OVF806
    ${sp_body} =    copy.deepcopy    ${tc01_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc01_Sp['name']}
    ${attributes1} =    Create List    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc01_Sp['name']}

    #Edit server profile
    ${edit_sp} =    copy.deepcopy    ${tc01_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    #Get Default Custom attributes from edit profile DP1
    ${sp_resp2} =    Get Server Profile    ${edit_sp['name']}
    ${attributes2} =    Create List    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    #Comparing CA values and OS volume
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=Custom attribute values are not same after changing profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC02 Re-deploy SP with new DP with additional CA
    [Documentation]    As a server administrator, I would like to re-deploy a server profile with a new deployment plan. It has few additional custom attributes
    [Tags]    TC02    OVF806
    ${sp_body} =    copy.deepcopy    ${tc01_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc01_Sp['name']}
    ${attributes1} =    Create List    UserName
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc01_Sp['name']}

    #Edit server profile
    ${edit_sp} =    copy.deepcopy    ${tc01_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWithUserName['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    #Get Default Custom attributes from edit profile DP1
    ${sp_resp2} =    Get Server Profile    ${edit_sp['name']}
    ${attributes2} =    Create List    UserName
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    #Comparing CA values and OS volume
    Should Not Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=Custom attribute values are not same after changing profile DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC04 Re-deploy SP with new DP with changed CA values and additional CA
    [Documentation]    As a server administrator, I would like to re-deploy a server profile with a new deployment plan. Some of the custom attributes default values have been modified. It has one additional custom attributes
    [Tags]    TC03    TC04    OVF806
    ${sp_body} =    copy.deepcopy    ${tc01_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc01_Sp['name']}
    ${attributes1} =    Create List    HostName
    ${attributes2} =    Create List    DomainName
    ${attributes3} =    Create List    UserName
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes2}
    ${attrib_values3} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes3}

    #Edit server profile
    ${edit_sp} =    copy.deepcopy    ${tc01_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWithUserName
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_differentcavalue_WithUserName['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    #Get Default Custom attributes from edit profile DP1
    ${sp_resp2} =    Get Server Profile    ${edit_sp['name']}
    ${attributes4} =    Create List    HostName
    ${attributes5} =    Create List    DomainName
    ${attributes6} =    Create List    UserName
    ${attrib_values4} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes4}
    ${attrib_values5} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes5}
    ${attrib_values6} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes6}
    #Comparing CA values
    Should Not Be Equal as Strings    ${attrib_values1}    ${attrib_values4}    msg=CA not changed after changing profile DP
    Should Not Be Equal as Strings    ${attrib_values2}    ${attrib_values5}    msg=CA not changed after changing profile DP
    Should Not Be Equal as Strings    ${attrib_values3}    ${attrib_values6}    msg=CA not changed after changing profile DP

OVF806_TC05 Re-deploy SP with new DP with changed CA types
    [Documentation]    As a server administrator, I would like to re-deploy a server profile with a new deployment plan. Some of the custom attributes types have been modified
    [Tags]    TC05    OVF806
    ${sp_body} =    copy.deepcopy    ${tc05_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc05_Sp['name']}

    # Edit server profile DP
    ${edit_sp} =    copy.deepcopy    ${tc05_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    #Get OS volume from Edit server profile
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    #Comparing OS volumes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC08 Re-deploy SP with a new DP, SP is associated to a SPT
    [Documentation]    As a server administrator, I would like to re-deploy a server profile with a new deployment plan. However, the SP is associated to a SPT
    [Tags]    TC08    OVF806
    ${tc08_spt} =    copy.deepcopy    ${spt}
    ${tc08_sp} =    copy.deepcopy    ${sp_from_spt}
    #Create Server profile template
    ${blnCreateSPT} =    Create I3S SPT    ${tc08_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc08_spt['name']}'
    #Create SP from SPT
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc08_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc08_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc08_sp['name']}

    # Edit server profile DP
    ${osdp_uri} =    Get OSDP URI    dp1With1Nic_StaticAndDhcpNic
    ${tc08_sp} =    Get Server Profile    ${tc08_sp['name']}
    Set To Dictionary    ${tc08_sp['osDeploymentSettings']}    osDeploymentPlanUri=${osdp_uri}
    ${sp_uri} =    Get from dictionary    ${tc08_sp}    uri
    ${blnEditPorf} =    Fusion API Edit Server Profile    ${tc08_sp}    ${sp_uri}
    ${blnStatus} =    Capture Task Status    ${blnEditPorf}    1200
    Should Be True    ${blnStatus}    Failed to update SP DP
    #Get OS volume from Edit server profile
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc08_sp['name']}
    #Comparing OS volumes
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    #Verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc08_sp}

OVF806_TC09 Change DP of SPT which has no associated SP, new DP has changed CA
    [Documentation]    As a server administrator, I would like to chose a different deployment plan for a SPT that has no associated SP's created. The deployment plan has removed some custom attributes and added a few additional Cas
    [Tags]    TC09    OVF806
    ${tc09_spt} =    copy.deepcopy    ${spt}
    #Create Server profile Template
    ${blnCreateSPT} =    Create I3S SPT    ${tc09_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc09_spt['name']}'
    # Get Default Custom attributes from template DP
    ${spt_resp1} =    Get Server Profile Template    ${tc09_spt['name']}
    ${attributes1} =    Create List    UserName
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${spt_resp1}    ${attributes1}

    #Edit server profile template
    ${edit_spt}=    copy.deepcopy    ${tc09_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'
    #Get Default Custom attributes from template DP1
    ${spt_resp2} =    Get Server Profile Template    ${edit_spt['name']}
    ${attributes2} =    Create List    UserName
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${spt_resp2}    ${attributes2}
    #comparing CA values of SPT
    Should Not Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=Custom attribute values are not same after changing profile DP

OVF806_TC10 Change DP of SPT which has associated SP, New DP has same CA
    [Documentation]    As a server administrator, I would like to chose a different deployment plan for a SPT that has associated SPs. The deployment plan has no changes to the custom attributes. Modifications are related to script executio
    [Tags]    TC10    OVF806
    #Create server profile template
    ${tc10_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc10_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc10_spt['name']}'
    #Create SP from SPT
    ${tc10_sp} =    copy.deepcopy    ${sp_from_spt}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc10_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc10_sp['name']}'
    #Edit Server Profile template
    ${tc10edit_spt} =    copy.deepcopy    ${tc10edit_spt}
    ${blnupdateProf} =    Edit I3S SPT    ${tc10edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'
    #Verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc10_sp}

OVF806_TC19 Change the SP from a NIC team to a single NIC model by changing its deployment plan
    [Documentation]    As a server administrator, I want to change the SP from a NIC team to a single NIC model by changing its deployment plan
    [Tags]    TC19    OVF806
    #Create server profile
    ${tc19_sp} =    copy.deepcopy    ${tc19_Sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${tc19_sp}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${tc19_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc19_sp['name']}
    # Get Default Custom attributes from profile DP
    ${sp_resp} =    Get Server Profile    ${tc19_sp['name']}
    ${attributes} =    Create List    ipaddress
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_resp}    ${attributes}

    # Edit Sp and Change DP
    ${editSp} =    copy.deepcopy    ${tc19_editSp}
    ${blnEditProf}=  Edit I3S Server Profile  ${editSp}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${editSp['name']}' with different DP
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${editSp['name']}
    ${attributes1} =    Create List    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    #Get Os volume from Edit SP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${editSp['name']}
    # Verifying/comparing default values of custom attributes and OS volume
    Should Be Equal as Strings    ${attrib_values}    ${attrib_values1}    msg=HostNIC values are same
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP

OVF806_TC29 Revert the SP to its former deployment plan. There are no associated SPTs
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan. There are no associated SPTs
    [Tags]    TC29    OVF806
    ${sp_body} =    copy.deepcopy    ${tc01_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${sp_body['name']}
    ${attributes1} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${sp_body['name']}

    #Edit Server profile
    ${edit_sp} =    copy.deepcopy    ${tc01_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic_diffGI
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPEdit} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    #Edit the server profile to revert back the DP
    ${blnEditformer}=    Edit I3S Server Profile    ${tc01_Sp}
    Run Keyword If    '${blnEditformer}'!='True'    Fail    Failed to update server profile '${tc01_Sp['name']}'
    #Get Default Custom attributes from profile DP after reverting the DP
    ${sp_resp2} =    Get Server Profile    ${tc01_Sp['name']}
    ${attributes2} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    #Get OS volume after reverting the DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${tc01_Sp['name']}
    #Comparing the CA values and OS volume with initial DP and after Edit and reverting the DP
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_beforeSPEdit}    msg=OS Volume not changed after changing profile DP
    Should Not Be Equal as Strings    ${vol_beforeSPEdit}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    # Comparing default values of custom attributes
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=values are same

OVF806_TC30 Revert the SP to its former deployment plan, It is associated to a SPT
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan. It is associated to a SPT. The plan is to update only this SP
    [Tags]    TC30    OVF806
    #Create Server profile template
    ${tc30_spt} =    copy.deepcopy    ${spt}
    ${tc30_sp} =    copy.deepcopy    ${sp_from_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc30_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc30_spt['name']}'
    #Create Server profile from SPT
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc30_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc30_sp['name']}'
    #Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc30_sp['name']}
    ${attributes1} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc30_sp['name']}

    #Edit Server profile
    ${edit_sp} =    copy.deepcopy    ${tc30_editSp}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPEdit} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${edit_sp}
    #Edit server profile to revert back the DP
    ${edit_sp30} =    copy.deepcopy    ${tc30_editSp}
    Set To Dictionary    ${edit_sp30['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp30}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp30['name']}'
    #Get Default custom attributes from profile DP after reverting the DP
    ${sp_resp2} =    Get Server Profile    ${edit_sp30['name']}
    ${attributes2} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    #Get OS volume after reverting the DP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${edit_sp30['name']}
    #Comparing the CA values and OS volume with initial DP and after edit and revert DP
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_beforeSPEdit}    msg=OS Volume not changed after changing profile DP
    Should Not Be Equal as Strings    ${vol_beforeSPEdit}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    #comparing default values of custom attributes
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=values are same

OVF806_TC35 revert the SPT to its former DP. There are no associated SPs. The older DP has a reduced number of CA's
    [Documentation]    As a server administrator, I want to revert the STP to its former deployment plan. There are no associated server profiles. The older deployment plan has a reduced number of CA's
    [Tags]    TC35    OVF806
    #Creating Server profile template
    ${tc35_spt} =    copy.deepcopy    ${tc08_edit_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc35_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc35_spt['name']}'
    #Get Default Custom attributes from template DP1
    ${spt_resp1} =    Get Server Profile Template    ${tc35_spt['name']}
    ${attributes1} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${spt_resp1}    ${attributes1}

    #Edit server profile template
    ${edit_spt}=    copy.deepcopy    ${spt}
    ${blnupdateProf}=    Edit I3S SPT    ${edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${edit_spt['name']}'
    #Revert server profile template DP
    ${revert_edit_spt}=    copy.deepcopy    ${tc08_edit_spt}
    ${blnupdateProf}=    Edit I3S SPT    ${revert_edit_spt}
    Run Keyword If    '${blnupdateProf}'!='True'    Fail    Failed to update server profile template '${revert_edit_spt['name']}'
    #Get Default Custom attributes from template DP1
    ${spt_resp2} =    Get Server Profile Template    ${revert_edit_spt['name']}
    ${attributes2} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${spt_resp2}    ${attributes2}
    #comparing the server profile template CA values before and after reverting back the DP
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=values are same

OVF806_TC37 Revert the SP to its former DP. It is not associated to a SPT. The older deployment plan has less CA's to the current plan
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan. It is not associated to a STP. The older deployment plan has less CA's to the current plan
    [Tags]    TC37    OVF806
    ${sp_body} =    copy.deepcopy    ${tc37_Sp}
    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${sp_body['name']}
    ${attributes1} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${sp_body['name']}

    #Edit server profile
    ${edit_sp} =    copy.deepcopy    ${tc37_Sp}
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Set To Dictionary    ${edit_sp['osDeploymentSettings']}    osCustomAttributes=${cas_dpWith1Nic_StaticNic['osCustomAttributes']}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPEdit} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    #Revert server profile DP
    ${sp_revert} =    copy.deepcopy    ${tc37_Sp}
    ${blnEditformer}=    Edit I3S Server Profile    ${sp_revert}
    Run Keyword If    '${blnEditformer}'!='True'    Fail    Failed to update server profile '${sp_revert['name']}'
    #Get Default custom attribute values
    ${sp_resp2} =    Get Server Profile    ${sp_revert['name']}
    ${attributes2} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    #Get OS volume from SP
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${sp_revert['name']}
    #Comparing OS volume with initial SP and after edit and revert
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_beforeSPEdit}    msg=OS Volume not changed after changing profile DP
    Should Not Be Equal as Strings    ${vol_beforeSPEdit}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    # comparing default values of custom attributes
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=values are same

OVF806_TC39 Revert the SP to its former DP, It is associated to a SPT. The older deployment has less CA's than the current plan
    [Documentation]    As a server administrator, I want to revert the SP to its former deployment plan. It is associated to a STP. The older deployment has less CA's than the current plan
    [Tags]    TC39    OVF806
    #Create Server profile template
    ${tc39_spt} =    copy.deepcopy    ${tc08_edit_spt}
    ${tc39_sp} =    copy.deepcopy    ${sp39_from_spt39}
    ${blnCreateSPT} =    Create I3S SPT    ${tc39_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${tc39_spt['name']}'
    #create server profile from SPT
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc39_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc39_sp['name']}'
    # Get Default Custom attributes from profile DP
    ${sp_resp1} =    Get Server Profile    ${tc39_sp['name']}
    ${attributes1} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values1} =    Get OS Attribute Values from Profile Response    ${sp_resp1}    ${attributes1}
    # Get OS Volume from profile DP
    ${vol_beforeSPUpdate} =    Get OS Volume From Server Profile    ${tc39_sp['name']}
    #Edit Server profile
    ${edit_sp} =    copy.deepcopy    ${tc39_editSp}
    ${blnEditPorf}=    Edit I3S Server Profile    ${edit_sp}
    Run Keyword If    '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${edit_sp['name']}'
    # Get OS Volume from profile DP
    ${vol_beforeSPEdit} =    Get OS Volume From Server Profile    ${edit_sp['name']}
    #Revert server profile DP
    ${sp_revert} =    copy.deepcopy    ${tc39_editSp}
    Set To Dictionary    ${sp_revert['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticAndDhcpNic_noPswd
    Set To Dictionary    ${sp_revert['osDeploymentSettings']}    osCustomAttributes=${cas_Withnopassword['osCustomAttributes']}
    ${blnEditformer}=    Edit I3S Server Profile    ${sp_revert}
    Run Keyword If    '${blnEditformer}'!='True'    Fail    Failed to update server profile '${sp_revert['name']}'
    #Get Default custom attribute values
    ${sp_resp2} =    Get Server Profile    ${sp_revert['name']}
    ${attributes2} =    Create List    DomainName    Hostname    ipaddress
    ${attrib_values2} =    Get OS Attribute Values from Profile Response    ${sp_resp2}    ${attributes2}
    ${vol_afterSPUpdate} =    Get OS Volume From Server Profile    ${sp_revert['name']}
    #Comparing OS volume with initial SP, after Edit and after reverting SP.
    Should Not Be Equal as Strings    ${vol_beforeSPUpdate}    ${vol_beforeSPEdit}    msg=OS Volume not changed after changing profile DP
    Should Not Be Equal as Strings    ${vol_beforeSPEdit}    ${vol_afterSPUpdate}    msg=OS Volume not changed after changing profile DP
    # comparing default values of custom attributes
    Should Be Equal as Strings    ${attrib_values1}    ${attrib_values2}    msg=values are same