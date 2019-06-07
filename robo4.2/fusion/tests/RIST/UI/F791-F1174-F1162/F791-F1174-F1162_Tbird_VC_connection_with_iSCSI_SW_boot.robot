*** Settings ***
Resource        ../resource.txt
Resource        ../../../../Resources/ui/common/setup.txt
Resource        ../../../../Resources/ui/servers/teardown.txt

Suite Teardown  Run Keywords    Load Test Data and Open Browser
...          AND                Log into Fusion appliance as Administrator
...          AND                Remove all Server Profiles and Server Profile Templates
...          AND                Logout and close all browsers

Test Setup      Run Keywords        Load Test Data and Open Browser
...             AND                 Log into Fusion appliance as Administrator
Test Teardown   Logout and close all browsers

*** Variables ***
${DataFile}                            	F791-F1174-F1162/Regression_data.xml         # Data File Location
${APPLIANCE_IP}                         16.114.209.223               # Appliance IP
${ApplianceUrl}                         https://${APPLIANCE_IP}         # Appliance Url

*** Test Cases ***
F791 - Verify Network Sets are NOT Supported during Create Server Profile with iSCSI SW Boot
    run keyword and expect error  ${iscsiBootNotFound}  fusion ui create server profile  @{TestData.serverProfile.negative.netSets}

F791 - Verify Cannot Create Server Profile with only iSCSI Secondary Boot Mode
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}   ${onlyIscsiSecondaryBootErrMsg}
    run keyword and expect error   ${expectedErrorMessage}  fusion ui create server profile  @{TestData.serverProfile.negative.secondaryBoot}

F791 - Verify Cannot Create Server Profile with Multiple iSCSI Primary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}	${multipleIscsiPrimaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile	@{TestData.serverProfile.negative.multiIscsiPrimary}

F791 - Verify Cannot Create Server Profile with Multiple iSCSI Secondary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileErrMessage}   ${multipleIscsiSecondaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile  @{TestData.serverProfile.negative.multiIscsiSecondary}

F791 & F1174 - Verify Required Fields for Create Server Profile with iSCSI SW Boot
    fusion ui verify create server profile required fields for connection with iscsi boot  @{TestData.serverProfile.requiredFields}

F791 - Verify Create Server Proflie with iSCSI SW Boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result} =  fusion ui create server profile  @{TestData.serverProfile.add}
    should be true  ${Result}   msg=Failed to create Server Profiles

F791 - Verify Edit Server Profile Connection iSCSI SW Boot
    ${Result1} =  fusion ui edit server profile  @{TestData.serverProfile.edit}
    should be true  ${Result1}  msg=Failed to edit Server Profile
    ${Result2} =  fusion ui verify server profile general info   @{TestData.serverProfile.edit}
    should be true  ${Result2}  msg=Failed to verify Server Profile General info
    ${Result3} =  fusion ui verify server profile connections info   @{TestData.serverProfile.edit}
    should be true  ${Result3}   msg=Failed to verify Server Profile Connections

F791 - Verify Cannot Copy Server Profile with iSCSI SW Boot Without Editing Connection
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.editCreateNoChap}
    should be true  ${Result1}  msg=Failed to create Server Profile
    run keyword and expect error  ${failedWaitInvisibleCopySpErrMsg}  fusion ui copy server profile  @{TestData.serverProfile.negative.cannotCopy}

F791 - Verify Copy Server Profile with iSCSI SW Boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${Result1} =  fusion ui create server profile  @{TestData.serverProfile.editCreateNoChap}
    should be true  ${Result1}  msg=Failed to create Server Profile
    ${Result1}=  fusion ui copy server profile  @{TestData.serverProfile.copy}
    should be true  ${Result1}   msg=Failed to copy Server Profile

F791 - Verify Server Profile Overview and Details Views includes iSCSI SW Boot Settings
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

F1174 - Verify Create Server Profile with User-Entered CHAP/MCHAP for iSCSI Boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
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
    ${CreateResult} =  fusion ui create server profile  @{TestData.serverProfile.editCreateNoChap}
    should be true  ${CreateResult}  msg=Failed to create Server Profile with iSCSI connection without No CHAP
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
    ${Result7} =  fusion ui edit server profile  @{TestData.serverProfile.edit}
    should be true  ${Result7}  msg=Failed to edit iSCSI connection from CHAP -> No CHAP
    ${Result8} =  fusion ui verify server profile connections info   @{TestData.serverProfile.edit}
    should be true  ${Result8}  msg=Failed to verify Server Profile Connections info after editing SP from CHAP -> No CHAP
    ${Result9} =  fusion ui edit server profile  @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result9}  msg=Failed to edit iSCSI connection from No CHAP -> MCHAP
    ${Result10} =  fusion ui verify server profile connections info   @{TestData.serverProfile.editChap.mchap}
    should be true  ${Result10}  msg=Failed to verify Server Profile Connections info after editing SP from No CHAP -> MCHAP
    ${Result11} =  fusion ui edit server profile  @{TestData.serverProfile.edit}
    should be true  ${Result11}  msg=Failed to edit iSCSI connection from MCHAP -> No CHAP
    ${Result12} =  fusion ui verify server profile connections info   @{TestData.serverProfile.edit}
    should be true  ${Result12}  msg=Failed to verify Server Profile Connections info after editing SP from MCHAP -> No CHAP

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
    ${Result2}=  fusion ui copy server profile  @{TestData.serverProfile.copyChap.copy}
    should be true  ${Result2}   msg=Failed to copy Server Profiles

F791 & F1174 - Verify Delete Server Profile with iSCSI SW Boot
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles

F1162 - Verify Network Sets are NOT Supported during Create Server Profile Template with iSCSI SW Boot
    run keyword and expect error  ${iscsiBootNotFound}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.netSets}

F1162 - Verify Cannot Create Server Profile Template with only iSCSI Secondary Boot Mode
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileTemplateErrMessage}   ${onlyIscsiSecondaryBootErrMsg}
    run keyword and expect error   ${expectedErrorMessage}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.secondaryBoot}

F1162 - Verify Cannot Create Server Profile Template with Multiple iSCSI Primary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileTemplateErrMessage}	${multipleIscsiPrimaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile template	 @{TestData.serverProfileTemplate.negative.multiIscsiPrimary}

F1162 - Verify Cannot Create Server Profile Template with Multiple iSCSI Secondary SW Boot Connections
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileTemplateErrMessage}   ${multipleIscsiSecondaryBootErrMsg}
    run keyword and expect error  ${expectedErrorMessage}  fusion ui create server profile template  @{TestData.serverProfileTemplate.negative.multiIscsiSecondary}

F1162 - Verify Required Fields for Create Server Profile Template with iSCSI SW Boot
    fusion ui verify create server profile template required fields for connection with iscsi boot  @{TestData.serverProfileTemplate.requiredFields}

F1162 - Verify Create Server Profile Template with iSCSI SW Boot
    ${Result} =  fusion ui create server profile template  @{TestData.serverProfileTemplate.add}
    should be true  ${Result}   msg=Failed to create Server Profile Templates

F1162 - Verify Create Server Profile From Template with iSCSI SW Boot
    ${Result} =  fusion ui create server profile from template  @{TestData.serverProfileTemplate.createFromTemplate}
    should be true  ${Result}  msg=Failed to create Server Profile from Template

F1162 - Verify Edit Unassociated Server Profile Template with iSCSI SW Boot Connection
    ${Result1} =  fusion ui edit server profile template  @{TestData.serverProfileTemplate.edit}
    should be true  ${Result1}  msg=Failed to edit Server Profile Template
    fusion ui verify server profile template connections info  @{TestData.serverProfileTemplate.edit}
    fusion ui verify server profile template advanced info   @{TestData.serverProfileTemplate.edit}

F1162 - Verify Server Profile Template Overview and Details Views includes iSCSI SW Boot Settings
    ${Result1} =  fusion ui create server profile template  @{TestData.serverProfileTemplate.verify}
    should be true  ${Result1}  msg=Failed to create Server Profile Template
    fusion ui verify server profile template connections info   @{TestData.serverProfileTemplate.verify}
    fusion ui verify server profile template advanced info   @{TestData.serverProfileTemplate.verify}
    ${Result2} =    fusion ui delete server profile template  @{TestData.serverProfileTemplate.verify}
    should be true  ${Result2}   msg=Failed to delete Server Profile Templates

F1162 - Verify Copy Server Profile Template with iSCSI SW Boot
    ${Result} =  fusion ui copy server profile template  @{TestData.serverProfileTemplate.copy}
    should be true  ${Result}   msg=Failed to copy Server Profile Templates

F1162 - Verify Delete Assigned Server Profile Template with iSCSI SW Boot Connections
    ${Result1} =  fusion ui validate server profile template in use cannot be deleted  @{TestData.serverProfileTemplate.delete.assigned}
    should be true  ${Result1}  msg=Failed to verify that assigned Server Profile Template could not be deleted

F1162 - Verify Delete Unassigned Server Profile Template with iSCSI SW Boot Connections
    ${DeleteResult} =  fusion ui delete all appliance server profiles
    should be true  ${DeleteResult}   msg=Failed to delete Server Profiles
    ${DeleteResult2} =  fusion ui delete all server profile templates
    should be true  ${DeleteResult2}   msg=Failed to delete Server Profile Templates
