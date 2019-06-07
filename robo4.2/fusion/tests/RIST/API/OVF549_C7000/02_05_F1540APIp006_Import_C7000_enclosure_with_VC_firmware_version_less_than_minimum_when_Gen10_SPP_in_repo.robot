*** Settings ***
Documentation        Import C7000 enclosure with VC firmware version less than minimum when Gen10 SPP in repo(Firmware should be updated)
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
Import C7000 enclosure with VC firmware version less than minimum when Gen10 SPP in repo(Firmware should be updated)
    Log    \nTest to downgrade C7000 VC firmware and add it to appliance    console=true
    Remove All Enclosures
    Clear Multi OA VC Mode  ${WPST32Encls}
    Run VCSU to Update VC Firmware   ${WPST32Encls}
    ${tasks} =   Add Enclosures from variable      ${Managed32WithSPP}  30min
    Verify Task Result  ${tasks}
	:FOR    ${vc}  IN  @{verify_interconnect}
	\       Wait Until Keyword Succeeds    30s    5s    Verify Interconnect Status    ${vc}  ${vc_managed_state}

