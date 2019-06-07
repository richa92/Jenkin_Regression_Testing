*** Settings ***
Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot


Variables 		                ${DATA_FILE}

Suite Setup  US52081 Suite Setup

*** Variables ***
${APPLIANCE_IP}                  APPLIANCE_IP
${DATA_FILE}                     ../shareable_data_files/dcs_natasha_3encl_schematic.py
${NOT_AUTHORIZED_ERROR_MESSAGE}  Authorization error: User not authorized for this operation.

# Hardware setup user permissions must be executed manually
*** Test Cases ***
TC6545 Big Bird Actions
    # Reset
    Run Keyword as User  administrator  Reset Random Drive Enclosure
    Run Keyword as User  server  Reset Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Reset Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Reset Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Reset Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Reset Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Reset Random Drive Enclosure
    # Refresh
    Run Keyword as User  administrator  Refresh Random Drive Enclosure
    Run Keyword as User  server  Refresh Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Refresh Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Refresh Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Refresh Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Refresh Random Drive Enclosure
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Refresh Random Drive Enclosure
    # Power Off/On
    Run Keyword as User  administrator  Power Random Drive Enclosure On and Off
    Run Keyword as User  server  Power Random Drive Enclosure On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Power Random Drive Enclosure On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Power Random Drive Enclosure On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Power Random Drive Enclosure On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Power Random Drive Enclosure On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Power Random Drive Enclosure On and Off

TC6544 BigBird Read Access
    Run Keyword as User  administrator  Get Drive Enclosures and verify
    Run Keyword as User  server  Get Drive Enclosures and verify
    Run Keyword as User  backup  Get Drive Enclosures and verify
    Run Keyword as User  storage  Get Drive Enclosures and verify
    Run Keyword as User  network  Get Drive Enclosures and verify
    Run Keyword as User  software  Get Drive Enclosures and verify
    Run Keyword as User  readonly  Get Drive Enclosures and verify

TC6547 Natasha Actions
    # Power Off/On
    Run Keyword as User  administrator  Power Random SAS Interconnect On and Off
    Run Keyword as User  server  Power Random SAS Interconnect On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Power Random SAS Interconnect On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Power Random SAS Interconnect On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Power Random SAS Interconnect On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Power Random SAS Interconnect On and Off
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Power Random SAS Interconnect On and Off
    # Soft Reset
    Run Keyword as User  administrator  Soft Reset Random SAS Interconnect
    Run Keyword as User  server  Soft Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Soft Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Soft Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Soft Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Soft Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Soft Reset Random SAS Interconnect
    # Hard Reset
    Run Keyword as User  administrator  Hard Reset Random SAS Interconnect
    Run Keyword as User  server  Hard Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Hard Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Hard Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Hard Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Hard Reset Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Hard Reset Random SAS Interconnect
    # Refresh
    Run Keyword as User  administrator  Refresh Random SAS Interconnect
    Run Keyword as User  server  Refresh Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Refresh Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Refresh Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Refresh Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Refresh Random SAS Interconnect
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Refresh Random SAS Interconnect

TC6541, TC6542, TC6769, TC6770 Natasha LIG CRUD and LI Read, Update
    Run Keyword as User  administrator  Add SAS LIG  ${sas_lig}
    Add Enclosure Group and Verify  ${sas_eg}
    Add Logical Enclosure From Variable  ${sas_le}
    Run Keyword For List  ${users}  Get Logical Interconnects and Verify As User From List
    ${sas_li_name} =  Catenate  SEPARATOR=  ${sas_le["name"]}  -  ${sas_lig["name"]}  -1
    Run Keyword as User  administrator  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword as User  server  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}
    Run Keyword as User  administrator  Get All SAS LIGS and Verify
    Run Keyword as User  server  Get All SAS LIGS and Verify
    Run Keyword as User  backup  Get All SAS LIGS and Verify
    Run Keyword as User  storage  Get All SAS LIGS and Verify
    Run Keyword as User  network  Get All SAS LIGS and Verify
    Run Keyword as User  software  Get All SAS LIGS and Verify
    Run Keyword as User  readonly  Get All SAS LIGS and Verify
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Edit SAS LIG  ${edited_sas_lig}
    Remove All LEs  force=${True}
    Fusion API Delete Enclosure Group  name=${sas_eg["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Delete SAS LIG by Name and Verify  ${sas_lig["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Delete SAS LIG by Name and Verify  ${sas_lig["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Delete SAS LIG by Name and Verify  ${sas_lig["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Delete SAS LIG by Name and Verify  ${sas_lig["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Delete SAS LIG by Name and Verify  ${sas_lig["name"]}
    Run Keyword as User  administrator  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword as User  administrator  Delete SAS LIG By Name and Verify  ${sas_lig["name"]}
    Run Keyword as User  server  Add SAS LIG  ${sas_lig}
    Run Keyword as User  server  Edit SAS LIG  ${edited_sas_lig}
    Run Keyword as User  server  Delete SAS LIG By Name and Verify  ${sas_lig["name"]}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  backup  Add SAS LIG  ${sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  storage  Add SAS LIG  ${sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  network  Add SAS LIG  ${sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  software  Add SAS LIG  ${sas_lig}
    Run Keyword and Expect Error  ${NOT_AUTHORIZED_ERROR_MESSAGE}  Run Keyword as User  readonly  Add SAS LIG  ${sas_lig}

TC6546 Natasha Read Access
    Run Keyword as User  administrator  Get Sas Interconnects and verify
    Run Keyword as User  server  Get Sas Interconnects and verify
    Run Keyword as User  backup  Get Sas Interconnects and verify
    Run Keyword as User  storage  Get Sas Interconnects and verify
    Run Keyword as User  network  Get Sas Interconnects and verify
    Run Keyword as User  software  Get Sas Interconnects and verify
    Run Keyword as User  readonly  Get Sas Interconnects and verify

*** Keywords ***
US52081 Suite Setup
	Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Remove All Users  VERIFY=${True}
	Add Users from variable  ${users}
	Login All Users  ${users}
    Remove All Server Profiles  force=${True}
    Remove All LEs  force=${True}
    Fusion API Delete Enclosure Group  name=${sas_eg["name"]}
    Fusion API Delete SAS LIG  name=${sas_lig["name"]}

Get Logical Interconnects and Verify As User From List
    [Arguments]  ${user}
    ${user_name} =  Get From Dictionary  ${user}  userName
    Run Keyword as User  ${user_name}  Get Logical Interconnects and Verify

Verify Random Drive Enclosure As User From List
	[Arguments]  ${user}
	${user_name} =  Get From Dictionary  ${user}  userName
	Run Keyword as User  ${user_name}  Verify Random Drive Enclosure  ${drive_enclosures}

Verify Random SAS Interconnect As User From List
    [Arguments]  ${user}
    ${user_name} =  Get From Dictionary  ${user}  userName
    Run Keyword as User  ${user_name}  Verify Random SAS Interconnect  ${sas_interconnects}
