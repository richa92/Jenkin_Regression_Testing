*** Settings ***
Documentation        Import C7000 enclosure with OA/Gen7/Gen8/Gen9 version less than minimum as managed when Gen10 SPP in repo(Firmware should be updated)
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
Import C7000 enclosure with OA/Gen7/Gen8/Gen9 version less than minimum as managed when Gen10 SPP in repo(Firmware should be updated)
    Log    \nTest to downgrade C7000 OA/ILO/VC firmware and add it to appliance    console=true
    Clear Multi OA VC Mode  ${WPST32Encls}
    Update Multi OA Firmware     ${WPST32Encls}
    Sleep  30
    :FOR    ${SERVER}   IN  @{G8BLServer}
	\   Run Keyword And Ignore Error    Run cpqlocfg and Reset iLO      ${SERVER['iloIP']}
    \   Sleep  60
    Run Keyword And Ignore Error    Update Server ILO Firmware      ${G8BLServer}
    :FOR    ${SERVER}   IN  @{G9BLServer}
	\   Run Keyword And Ignore Error    Run cpqlocfg and Reset iLO      ${SERVER['iloIP']}
    \   Sleep  60
    Run Keyword And Ignore Error    Update Server ILO Firmware      ${G9BLServer}
    ${tasks} =   Add Enclosures from variable      ${Managed32WithSPP}  30min
    Verify Task Result  ${tasks}
    :FOR    ${encl}  IN  @{WPST32Encls}
	\       Wait Until Keyword Succeeds    30s    5s    Verify Enclosure Status    ${encl['name']}  ${enc_managed_state}
