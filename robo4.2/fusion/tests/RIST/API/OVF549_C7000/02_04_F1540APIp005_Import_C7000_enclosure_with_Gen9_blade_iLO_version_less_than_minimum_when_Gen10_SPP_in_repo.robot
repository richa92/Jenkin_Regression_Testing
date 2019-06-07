*** Settings ***
Documentation        Import C7000 enclosure with Gen9 blade iLO version less than minimum when Gen10 SPP in repo(Firmware should be updated)
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
Import C7000 enclosure with Gen9 blade iLO version less than minimum when Gen10 SPP in repo(Firmware should be updated)
    Log    \nTest to downgrade C7000 Gen9 ILO firmware and add it to appliance    console=true
    :FOR    ${sh}  IN  @{G9BLServer}
	\		${shname}=  Get Server Hardware Name from ILO IP  ${sh['iloIP']}
	\       Wait Until Keyword Succeeds    30s    5s    Verify Server Hardware Status    ${shname}  ${ilo_managed_state}
