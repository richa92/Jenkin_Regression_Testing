*** Settings ***
Resource        ../resource.txt
#Resource        ../../../../Resources/ui/servers/teardown.txt
Resource        ../../../../Resources/ui/common/setup.txt


Suite Setup  Run Keywords       Load Test Data and Open Browser
...          AND                Log into Fusion appliance as Administrator
...          AND                C7000 Enclosure Setup
...          AND                Logout and close all browsers
Suite Teardown  Run Keywords    Load Test Data and Open Browser
...             AND             Log into Fusion appliance as Administrator
...             AND             C7000 Enclosure Teardown
...             AND             Logout and close all browsers

Test Setup      Run Keywords        Load Test Data and Open Browser
...             AND                 Log into Fusion appliance as Administrator
Test Teardown   Logout and close all browsers

*** Variables ***
${DataFile}         Regression_data.xml         # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
F346 - Verify Network Sets are NOT Supported during Create Server Profile with iSCSI Function Type
    run keyword and expect error  ${networkConnectionNotVisibleErrMsg}  fusion ui create server profile  @{TestData.serverProfile.negative.netSets}

F346 - Verify Create Server Profile with iSCSI HW Boot Mode
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.add}
    should be true  ${Result1}   msg=Failed to create Server Profiles
    ${Result2} =    fusion ui delete server profile  @{TestData.serverProfile.add}
    should be true  ${Result2}   msg=Failed to delete Server Profiles

F346 - Verify Cannot Create Server Profile with only iSCSI Secondary Boot Mode
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}   ${onlyIscsiSecondaryBootErrMsg}
    run keyword and expect error   ${expectedErrorMessage}  fusion ui create server profile  @{TestData.serverProfile.negative.secondaryBoot}

F346 - Verify Cannot Create Server Profile with Multiple iSCSI Primary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}	${multipleIscsiPrimaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile	@{TestData.serverProfile.negative.multiIscsiPrimary}

F346 - Verify Cannot Create Server Profile with Multiple iSCSI Secondary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileErrMessage}   ${multipleIscsiSecondaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile  @{TestData.serverProfile.negative.multiIscsiSecondary}

F346 - Verify User Specified iSCSI Initiator Name Must Be Unique in Create Server Profile
    ${partialExpectedErrorMessage}=  catenate  SEPARATOR=  ${unableToAddProfileErrMessage}  ${nonUniqueIscsiInitiatorNameErrMsgPart1}
    ${expectedErrorMessage}=      Create Expected Error Message for Invalid iSCSI Primary/Secondary Boot Connections  ${partialExpectedErrorMessage}  ${TestData.serverProfile.negative.nonUniqueIscsiInitiatorName.profile[1].Advanced.iscsiInitiatorName}  ${nonUniqueIscsiInitiatorNameErrMsgPart2}
    ${profileData1}=  Convert Data to List  ${TestData.serverProfile.negative.nonUniqueIscsiInitiatorName.profile[0]}
    ${profileData2}=  Convert Data to List  ${TestData.serverProfile.negative.nonUniqueIscsiInitiatorName.profile[1]}
    ${Result1}=  fusion ui create server profile  @{profileData1}
    should be true  ${Result1}  msg=Failed to create Server Profile
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile  @{profileData2}
    Load Test Data and Open Browser
    Log into Fusion appliance as Administrator
    ${Result2}=  fusion ui delete server profile  @{profileData1}
    should be true  ${Result2}  msg=Failed to delete Server Profile

F346 - Verify Error Message when Invalid User Specified iSCSI Initiator Name Used in Create Server Profile
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${expectedErrorMessage}=  catenate  SEPARATOR=  ${invalidIscsiInitiatorNameErrMsgPart1}  ${TestData.serverProfile.negative.invalidIscsiInitiatorName.profile.Advanced.iscsiInitiatorName}  ${invalidIscsiInitiatorNameErrMsgPart2}
    ${profileData}=  Convert Data to List  ${TestData.serverProfile.negative.invalidIscsiInitiatorName.profile}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile  @{profileData}

F346 - Verify Edit Server Profile Connection iSCSI HW Boot
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.edit.create1}
    should be true  ${Result1}  msg=Failed to create Server Profile
    ${Result2} =  fusion ui edit server profile  @{TestData.serverProfile.edit.test1}
    should be true  ${Result2}  msg=Failed to edit Server Profile
    ${Result3} =  fusion ui verify server profile connections info   @{TestData.serverProfile.edit.test1}
    should be true  ${Result3}   msg=Failed to verify Server Proflie Connections
    ${Result4} =    fusion ui delete server profile  @{TestData.serverProfile.edit.test1}
    should be true  ${Result4}   msg=Failed to delete Server Profiles
    ${Result5} =  fusion ui create server profile  @{TestData.serverProfile.edit.create2}
    should be true  ${Result5}  msg=Failed to create Server Profile
    ${Result6} =  fusion ui edit server profile  @{TestData.serverProfile.edit.test2}
    should be true  ${Result6}  msg=Failed to edit Server Profile
    ${Result6} =  fusion ui verify server profile connections info   @{TestData.serverProfile.edit.test2}
    should be true  ${Result6}   msg=Failed to verify Server Proflie Connections
    ${Result7} =    fusion ui delete server profile  @{TestData.serverProfile.edit.test2}
    should be true  ${Result7}   msg=Failed to delete Server Profiles

F346 - Verify Edit iSCSI Initiator Name
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.edit.initiatorEdit.add}
    should be true  ${Result1}  msg=Failed to create Server Profile
    ${Result2} =  fusion ui verify server profile general info   @{TestData.serverProfile.edit.initiatorEdit.add}
    should be true  ${Result2}   msg=Failed to verify Server Proflie General Info
    ${Result3} =  fusion ui edit server profile  @{TestData.serverProfile.edit.initiatorEdit.edit1}
    should be true  ${Result3}  msg=Failed to edit Server Profile
    ${Result4} =  fusion ui verify server profile general info   @{TestData.serverProfile.edit.initiatorEdit.edit1}
    should be true  ${Result4}   msg=Failed to verify Server Proflie General Info
    ${Result5} =  fusion ui edit server profile  @{TestData.serverProfile.edit.initiatorEdit.edit2}
    should be true  ${Result5}  msg=Failed to edit Server Profile
    ${Result6} =  fusion ui verify server profile general info   @{TestData.serverProfile.edit.initiatorEdit.edit2}
    should be true  ${Result6}   msg=Failed to verify Server Proflie General Info
    ${Result7} =    fusion ui delete server profile  @{TestData.serverProfile.edit.initiatorEdit.edit2}
    should be true  ${Result7}   msg=Failed to delete Server Profiles

F346 - Verify Server Profile Overview and Details Views includes iSCSI Function and iSCSI HW Boot Settings
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.verify}
    should be true  ${Result1}  msg=Failed to create Server Profile
    ${Result2} =  fusion ui verify server profile general info   @{TestData.serverProfile.verify}
    should be true  ${Result2}  msg=Failed to verify Server Profile General info
    ${Result3} =  fusion ui verify server profile connections info   @{TestData.serverProfile.verify}
    should be true  ${Result3}  msg=Failed to verify Server Profile Connections info
    ${Result4} =  fusion ui verify server profile advanced info   @{TestData.serverProfile.verify}
    should be true  ${Result4}  msg=Failed to verify Server Profile Advanced info
    ${Result5} =    fusion ui delete server profile  @{TestData.serverProfile.verify}
    should be true  ${Result5}   msg=Failed to delete Server Profiles

F346 - Verify Server Hardware Type Adapters View when Configured with iSCSI Function
    fusion ui validate server hardware types page  @{TestData.serverHardwareType}

F346 - Verify Cannot Copy Server Profile with iSCSI HW Boot Without Editing Connection
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.copy.create}
    run keyword and expect error  ${failedWaitInvisibleCopySpErrMsg}  fusion ui copy server profile  @{TestData.serverProfile.negative.cannotCopy}

F346 - Verify Copy Server Profile with iSCSI HW Boot
    ${Result1}=  fusion ui copy server profile  @{TestData.serverProfile.copy.test}
    should be true  ${Result1}   msg=Failed to copy Server Profile

F346 & F1174 - Verify Required Fields for Create Server Profile with iSCSI HW Boot
    fusion ui verify create server profile required fields for connection with iscsi boot  @{TestData.serverProfile.requiredFields}

F1174 - Verify Create Server Profile with User-Entered CHAP/MCHAP for iSCSI Boot
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.addChap}
    should be true  ${Result1}   msg=Failed to create Server Profiles
    ${Result2} =    fusion ui delete server profile  @{TestData.serverProfile.addChap}
    should be true  ${Result2}   msg=Failed to delete Server Profiles

F1174 - Verify CHAP/MCHAP Configuration Retained when Changing EG/SHT
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.editChap.egShtTest}
    should be true  ${Result1}   msg=Failed to create Server Profiles
    ${Result2} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.changeEg}
    should be true  ${Result2}  msg=Failed to edit EG in Server Profile
    ${Result3} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.changeSht}
    should be true  ${Result3}  msg=Failed to edit SHT in Server Profile
    ${Result4} =    fusion ui delete server profile  @{TestData.serverProfile.editChap.changeSht}
    should be true  ${Result4}   msg=Failed to delete Server Profiles

F1174 - Verify Edit Server Profile with CHAP/MCHAP for iSCSI boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${CreateResult} =  fusion ui create server profile  @{TestData.serverProfile.editChap.createNoChap}
    should be true  ${CreateResult}   msg=Failed to create Server Profiles
    ${Result1} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.chap}
    should be true  ${Result1}  msg=Failed to edit iSCSI connection from No CHAP -> CHAP
    ${Result2} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.chap}
    should be true  ${Result2}  msg=Failed to verify Server Profile Connections info after editing SP from No CHAP -> CHAP
    ${Result3} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result3}  msg=Failed to edit iSCSI connection from CHAP -> MCHAP
    ${Result4} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result4}  msg=Failed to verify Server Profile Connections info after editing SP from CHAP -> MCHAP
    ${Result5} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.chap}
    should be true  ${Result5}  msg=Failed to edit iSCSI connection from MCHAP -> CHAP
    ${Result6} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.chap}
    should be true  ${Result6}  msg=Failed to verify Server Profile Connections info after editing SP from MCHAP -> CHAP
    ${Result7} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.noChap}
    should be true  ${Result7}  msg=Failed to edit iSCSI connection from CHAP -> No CHAP
    ${Result8} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.noChap}
    should be true  ${Result8}  msg=Failed to verify Server Profile Connections info after editing SP from CHAP -> No CHAP
    ${Result9} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result9}  msg=Failed to edit iSCSI connection from No CHAP -> MCHAP
    ${Result10} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result10}  msg=Failed to verify Server Profile Connections info after editing SP from No CHAP -> MCHAP
    ${Result11} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.noChap}
    should be true  ${Result11}  msg=Failed to edit iSCSI connection from MCHAP -> No CHAP
    ${Result12} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.noChap}
    should be true  ${Result12}  msg=Failed to verify Server Profile Connections info after editing SP from MCHAP -> No CHAP
    ${DeleteResult2} =  fusion ui delete server profile  @{TestData.serverProfile.editChap.noChap}
    should be true  ${DeleteResult2}   msg=Failed to delete Server Profiles

F1174 - Verify Server Profile Overview and Details Views includes CHAP/MCHAP Settings
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.verifyChap}
    should be true  ${Result1}  msg=Failed to create Server Profile
    ${Result2} =  fusion ui verify server profile general info   @{TestData.serverProfile.verifyChap}
    should be true  ${Result2}  msg=Failed to verify Server Profile General info
    ${Result3} =  fusion ui verify server profile connections info   @{TestData.serverProfile.verifyChap}
    should be true  ${Result3}  msg=Failed to verify Server Profile Connections info
    ${Result4} =  fusion ui verify server profile advanced info   @{TestData.serverProfile.verifyChap}
    should be true  ${Result4}  msg=Failed to verify Server Profile Advanced info
    ${Result5} =    fusion ui delete server profile  @{TestData.serverProfile.verifyChap}
    should be true  ${Result5}   msg=Failed to delete Server Profiles

F1174 - Verify Copy Server Profile with CHAP/MCHAP for iSCSI Boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.copyChap.create}
    should be true  ${Result1}  msg=Failed to create Server Profiles
    ${Result2}=  fusion ui copy server profile  @{TestData.serverProfile.copyChap.test}
    should be true  ${Result2}   msg=Failed to copy Server Profiles
    ${Result3} =    fusion ui delete server profile  @{TestData.serverProfile.copyChap.create}
    should be true  ${Result3}   msg=Failed to delete Server Profiles

F346 & F1174 - Delete All Server Profiles
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles

F1162 - Verify Network Sets are NOT Supported during Create Server Profile Template with iSCSI HW Boot
    run keyword and expect error  ${networkConnectionNotVisibleErrMsg}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.netSets}

F1162 - Verify Create Server Profile Template with iSCSI HW Boot
    ${Result} =  fusion ui create server profile template  @{TestData.serverProfileTemplate.add}
    should be true  ${Result}   msg=Failed to create Server Profile Templates

F1162 - Verify Create Server Profile From Template with iSCSI HW Boot
    ${Result} =  fusion ui create server profile from template  @{TestData.serverProfileTemplate.createFromTemplate}
    should be true  ${Result}  msg=Failed to create Server Profile from Template

F1162 - Verify Cannot Create Server Profile Template with only iSCSI Secondary Boot Mode
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileTemplateErrMessage}   ${onlyIscsiSecondaryBootErrMsg}
    run keyword and expect error   ${expectedErrorMessage}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.secondaryBoot}

F1162 - Verify Cannot Create Server Profile Template with Multiple iSCSI Primary HW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileTemplateErrMessage}	${multipleIscsiPrimaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile template	 @{TestData.serverProfileTemplate.negative.multiIscsiPrimary}

F1162 - Verify Cannot Create Server Profile Template with Multiple iSCSI Secondary HW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileTemplateErrMessage}   ${multipleIscsiSecondaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.multiIscsiSecondary}

F1162 - Verify Required Fields for Create Server Profile Template with iSCSI HW Boot
    fusion ui verify create server profile template required fields for connection with iscsi boot  @{TestData.serverProfileTemplate.requiredFields}

F1162 - Verify Edit Unassociated Server Profile Template with iSCSI HW Boot Connection
    ${Result} =  fusion ui create server profile template  @{TestData.serverProfileTemplate.edit.create}
    should be true  ${Result}   msg=Failed to create Server Profile Templates
    ${Result2} =  fusion ui edit server profile template  @{TestData.serverProfileTemplate.edit.test}
    should be true  ${Result2}  msg=Failed to edit Server Profile Template
    fusion ui verify server profile template connections info  @{TestData.serverProfileTemplate.edit.test}
    fusion ui verify server profile template advanced info   @{TestData.serverProfileTemplate.edit.test}
    ${Result3} =    fusion ui delete server profile template  @{TestData.serverProfileTemplate.edit.test}
    should be true  ${Result3}   msg=Failed to delete Server Profile Templates

F1162 - Verify Server Profile Template Overview and Details Views includes iSCSI HW Boot Settings
    ${Result1} =  fusion ui create server profile template  @{TestData.serverProfileTemplate.verify}
    should be true  ${Result1}  msg=Failed to create Server Profile Template
    fusion ui verify server profile template connections info   @{TestData.serverProfileTemplate.verify}
    fusion ui verify server profile template advanced info   @{TestData.serverProfileTemplate.verify}
    ${Result2} =    fusion ui delete server profile template  @{TestData.serverProfileTemplate.verify}
    should be true  ${Result2}   msg=Failed to delete Server Profile Templates

F1162 - Verify Copy Server Profile Template with iSCSI HW Boot
    ${Result1} =  fusion ui copy server profile template  @{TestData.serverProfileTemplate.copy}
    should be true  ${Result1}   msg=Failed to copy Server Profile Templates
    ${Result2} =    fusion ui delete server profile template  @{TestData.serverProfileTemplate.copy}
    should be true  ${Result2}   msg=Failed to delete Server Profile Templates

F1162 - Verify Delete Assigned Server Profile Template with iSCSI HW Boot Connections
    ${Result} =  fusion ui validate server profile template in use cannot be deleted  @{TestData.serverProfileTemplate.deleteAssigned}
    should be true  ${Result}  msg=Failed to verify that assigned Server Profile Template could not be deleted

F1162 - Verify Delete Unassigned Server Profile Template with iSCSI HW Boot Connections
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${DeleteResult2} =  fusion ui delete all server profile templates
    should be true  ${DeleteResult2}   msg=Failed to delete Server Profile Templates
