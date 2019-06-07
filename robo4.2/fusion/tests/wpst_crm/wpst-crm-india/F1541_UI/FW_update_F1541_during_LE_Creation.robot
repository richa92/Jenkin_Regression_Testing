*** Settings ***
Documentation      Continuous Integration Tests for RoboGalaxy dev Branch
Resource           lig-config.txt
Force Tags         Buildup
Suite Setup         Load Test Data and Open Browser
Suite Teardown      Logout And Close All Browsers
Library             Dialogs
Library             Collections

*** Variables ***
${expected_build_version}    2.00.00-0210744
${li_list} =    SGH420HHYA-LIG_B1
${Encname} =        SGH420HHYA

*** Keywords ***


*** Test Cases ***

Login to appliance
		Set Log Level    TRACE
    	Log Variables

 		${user}=    Get Data By Property	${TestData.users}	name	Administrator
		Fusion UI Login to Appliance   ${user[0].name}
		${li_list} =   Create list     ${li_list}
###############  FIRMWARE UPDATE DURING LE CREATION with flag Downgrade ############ 	
TC01 Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation with force flag (Downgrade)
	Log To Console   "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation with force flag (Downgrade)"
	Log to Console       "Testcase_ID: F1541_UI_46: Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation with force flag (Downgrade)"
	
	####### CREATIG LIG, EG and Add enclosure  ################

#TC01 Create FC network1 FC_NW_1
	Log to Console      Create FC network1 FC_NW_1
    Fusion UI Create FC Network         @{TestData.fcnetworks_uplink}[0]


#TC02 Create FC network1 FC_NW_2
	Log to Console      Create FC network1 FC_NW_2
    Fusion UI Create FC Network         @{TestData.fcnetworks_uplink}[1]



#TC04 Create Logical Interconnect Group

    Log to Console    "Create Logical Interconnect Group"
    Fusion UI Create Logical Interconnect Group         @{TestData.ligs}



#TC05 Edit Create Logical Interconnect Group
	Log to Console      Edit Create Logical Interconnect Group
    fusion_ui_edit_logical_interconnect_group     @{TestData.LigEditB}

#TC06 Create Enclosure Group
    Log to Console     Create Enclosure Group

    Fusion UI Create Enclosure Group    @{TestData.encgroups}



#TC07 Add Enclosure along with firmware bundle
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_RPM_Downgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen


###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC02 Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation without force flag (upgrade)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation without force flag (upgrade)"
	Log to Console       "Testcase_ID: F1541_UI_44: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation without force flag (upgrade)"
	

	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_RPM_Upgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen
 
 
 ###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC03 Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation with force flag (Downgrade)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation with force flag (Downgrade)"
	Log to Console       "Testcase_ID: F1541_UI_40: Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation with force flag (Downgrade)"

	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_RPM_Downgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen

###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC04 Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation without force flag (upgrade)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation without force flag (upgrade)"
	Log to Console       "Testcase_ID: F1541_UI_45: Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version during LE creation without force flag (upgrade)"

	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_RPM_Upgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen
 
###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC05 Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation with force flag (Downgrade)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation with force flag (Downgrade)"
	Log to Console       "Testcase_ID: F1541_UI_43: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version during LE creation with force flag (Downgrade)"

	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_SCEXES_Downgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen

###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC06 Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version during LE creation with force flag (same version)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version during LE creation with force flag (same version)"
	Log to Console       "Testcase_ID: F1541_UI_42: Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version during LE creation with force flag (same version)"

	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_SCEXES_Downgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen
  
  
    
###############  FIRMWARE UPDATE DURING LE CREATION without flag Upgrade############ 	
TC07 Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation without force flag (upgrade)
	Log To Console        "###############  FW Update operation (Stage + Activate) of VC modules during LE creation  without force flag ############" 
	[Documentation]       "FW Update During LE creation : Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation without force flag (upgrade)"
	Log to Console       "Testcase_ID: F1541_UI_41: Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version during LE creation without force flag (upgrade)"
	###### Delete LIG and EG #####
	
	${status}=    Fusion UI delete Server Profile  @{TestData.profiles}
    Should be True    ${status}    msg=Failed to delete Server profile
    
    ${status}=	Fusion UI Delete Enclosure    @{TestData.enclosures}
 	Should Be True	${status}	Failed to delete enclosures
 	
    Log to Console  "Add Enclosure along with firmware bundle"
#    Fusion UI Add Enclosure    @{TestData.enclosures}

    Fusion UI Add Enclosure    @{TestData.FWenclosures_RPM_Upgrade_force}


    Sleep	35 minutes 1 seconds
	Log To Console    Validation of ENC activities
    #${Status}=    fusion_ui_validate_enc_messages    ${Encname}
    ${Status}=    fusion_ui_validate_enc_messages    @{TestData.LE_Testupdate_le_firmware}[1]
    Log to Console    ${Status}
	Run Keyword and Continue on Failure	   Should Contain		'${Status}'		${Enc_same_version_error_messageenc} 	Expected Error Message Not seen
  
   	
	
 	
 	
 		    