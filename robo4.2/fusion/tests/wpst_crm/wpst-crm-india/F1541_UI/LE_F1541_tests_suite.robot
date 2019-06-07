*** Settings ***

Resource			firmware_config.txt
Force Tags			Buildup
Suite Setup			Load Test Data and Open Browser
Suite Teardown		Logout And Close All Browsers
Library             Collections


*** Variables ***

${Permissible_IC_STATES_BeforeUpdate}=    ['configured','unmanaged']
${Permissible_IC_STATES_AfterUpdate}=    ['configured']
${expected_build_version}    2.00.00-0210744

*** Test Cases ***

FW Update operation (Stage + Activate) Oneview Login
		Set Log Level    TRACE
    	Log Variables

 		${user}=	Get Data By Property	${TestData.users}	name	Administrator
		Fusion UI Login to Appliance   ${user[0].name}
		
TC01 Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure and profile mode with force flag(downgrade)
		[Documentation]     "Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure and profile mode with force flag(downgrade)"
		Log to Console     "Testcase_ID:F1541_UI_TC35--> Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure and profile mode with force flag(downgrade)"
	
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_DOWNGRADE_SHARED_INFRA_PROFILE_RPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmwarebb1}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_DOWNGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'      Error during Firmware Version and IC activity Messages Validation

TC02 Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure mode with force flag(downgrade)
		[Documentation]	"Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure mode with force flag(downgrade)"
		Log to Console	"Testcase_ID: UI Test Cases F1541_UI_TC31 --> Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure mode with force flag(downgrade)"
		
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_DOWNGRADE_SHARED_INFRA_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmwarebb1}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_DOWNGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation

TC03 Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure mode without force flag( upgrade )
		[Documentation]	"Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure mode without force flag( upgrade )"
		Log to Console	"Testcase_ID: UI Test Cases F1541_UI_TC30 --> Verify the LE FW Update operation (Stage + Activate) from scexes to RPM firmware version using shared infrastructure mode without force flag( upgrade )"
		
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =    Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_FIRMWARE_SH_INFRA_UPGARDE_RPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmwarebb1}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure     Should Be Equal    '${Status}'   'True'    Error during Firmware Version and IC activity Messages Validation

TC04 Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure mode with force flag(downgrade)
		[Documentation]	"Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure mode with force flag(downgrade)"
		Log to Console	"Testcase_ID: F1541_UI_TC34 --> Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure mode with force flag(downgrade)"

		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_FIRMWARE_SH_INFRA_DOWNGARDE_RPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_DOWNGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

	
	
TC05 Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure and profile mode without force flag( upgrade )
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure and profile  mode without force flag( upgrade )"
		Log to Console        "Testcase_ID: F1541_UI_TC38 --> Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure mode without force flag( upgrade )"
	
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =   Fusion UI Update Logical Enclosure Firmware       @{TestData.LE_UPGRADE_SHARED_INFRA_PROFILE_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=   fusion_ui_verify_le_frmware_upgrade_activity_details    ${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation
	
TC06 Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure mode without force flag(Upgrade)
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure mode without force flag(Upgrade)"
		Log to Console     "Testcase_ID:F1541_UI_TC33 --> Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure mode without force flag(Upgrade)"
		Log to Console        ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=     fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.SAME_LE_UPGRADE_SHARED_INFRA_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation

TC07 Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure and profile mode with force flag(downgrade)
		[Documentation]     "Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure and profile mode with force flag(downgrade)"
		Log to Console     "Testcase_ID:F1541_UI_TC39 --> Verify the LE FW Update operation (Stage + Activate) from scexes to scexes firmware version using shared infrastructure and profile mode with force flag(downgrade)"
	
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_DOWNGRADE_SHARED_INFRA_PROFILE_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_DOWNGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation


TC08 Verify the LE FW Update operation (Stage + Activate) from Scexe to RPM firmware version using shared infrastructure mode with force flag( same version )
		[Documentation]     "Verify the LE FW Update operation (Stage + Activate) from Scexe to RPM firmware version using shared infrastructure mode without force flag( same version )"
		Log to Console     "Testcase_ID:F1541_UI_TC32--> Verify the LE FW Update operation (Stage + Activate) from Scexe to RPM firmware version using shared infrastructure mode without force flag( same version )"
	
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_DOWNGRADE_SHARED_INFRA_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_DOWNGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation

TC09 Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure and profile mode without force flag( upgrade )
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure and profile mode without force flag( upgrade )"
		Log to Console     "Testcase_ID:F1541_UI_TC36 --> Verify the LE FW Update operation (Stage + Activate) from RPM to RPM firmware version using shared infrastructure and profile mode without force flag( upgrade )"
		
		Log to Console        ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=     fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_UPGRADE_SHARED_INFRA_PROFILE_RPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation



TC10 Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure and profile mode with force flag(same version)
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure and profile mode with force flag(same version "
		Log to Console      "Testcase_ID:F1541_UI_TC37 --> Verify the LE FW Update operation (Stage + Activate) from RPM to scexes firmware version using shared infrastructure and profile mode with force flag(same version "
		
		Log to Console        ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=     fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_UPGRADE_SHARED_INFRA_PROFILE_SAMEVERSION_SCEXES}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation


TC11 Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure mode with force flag(same version )
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure mode with force flag(same version )"
		Log to Console      "Testcase_ID:F1541_UI_TC47 --> Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure mode with force flag(same version )"
		
		Log to Console        ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=     fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =    Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_UPGRADE_SHARED_INFRA_PROFILE_SAMEVERSION_SCEXESRPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=	fusion_ui_verify_le_frmware_upgrade_activity_details 	${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure 	Should Be Equal		'${Status}'		'True'  	Error during Firmware Version and IC activity Messages Validation

TC12 Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure and profile mode with force flag(downgrade)
		[Documentation]     "Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure and profile mode with force flag(downgrade)"
		Log to Console     "Testcase_ID:F1549_UI_TC49--> Verify the LE FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using shared infrastructure and profile mode with force flag(downgrade)"
	
		Log to Console	****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =	Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_DOWNGRADE_SHARED_INFRA_PROFILE_SCEXESRPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=     fusion_ui_verify_le_frmware_upgrade_activity_details    ${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=   fusion_ui_verify_li_and_ic_firmware_versions  ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure     Should Be Equal    '${Status}'   'True'     Error during Firmware Version and IC activity Messages Validation

TC13 Verify the LE FW Update operation (Stage + Activate) from RPM to SEXERPM firmware version using shared infrastructure mode without force flag( upgrade )
		[Documentation]      "Verify the LE FW Update operation (Stage + Activate) from RPM to SEXERPM firmware version using shared infrastructure mode without force flag( upgrade )"
		Log to Console      "Testcase_ID:F1541_UI_TC48 --> Verify the LE FW Update operation (Stage + Activate) from RPM to SEXERPM firmware version using shared infrastructure mode without force flag( upgrade )"
		
		Log to Console        ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
		${Status}=     fusion_ui_verify_ic_state_of_le   ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
	
		#################### LE FIRMWARE UPDATE with shared infrastructure ######################################
		${blnupdatefirmware} =    Fusion UI Update Logical Enclosure Firmware     @{TestData.LE_UPGRADE_SHARED_INFRA_SCEXESRPM}[1]
		run keyword if    '${blnupdatefirmware}'=='False'    Fail      " Update firmware on LE failed"
	
		###################### VERIFY THE LE ACTIVITIES #############################
		Log To Console    *****Validation of LE activities******
		${Status}=    fusion_ui_verify_le_frmware_upgrade_activity_details     ${TestData.firmware_sh_profile}
		Run Keyword and Continue on Failure   Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
		
		
		Log to Console	****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
		${Status}=   fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware_sh_profile}
		Run Keyword If    '${Status}'=='True'   Log To Console  IC Sates as desired   ELSE     Fail
		
		############# VALIDATE FIRMWARE VERSION and compare to Actual IC version #############
		${Status}=     fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.LE_UPGRADE_FIRMWARE_VERSION_VALIDATION_SH_INFRA_RPM}   
		Run Keyword and Continue on Failure     Should Be Equal     ${Status}'    'True'     Error during Firmware Version and IC activity Messages Validation



						