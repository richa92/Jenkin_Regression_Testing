*** Settings ***
Documentation        Import Gen9 DL with iLO version less than minimum when Gen10 SPP in repo(Firmware should be updated)
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
Import Gen9 DL with iLO version less than minimum when Gen10 SPP in repo(Firmware should be updated)
    Log    \nTest to downgrade DL server ilo and add it to appliance    console=true
    Reset iLO and Update Server ILO Firmware      ${G9DLServer}
    Add Server Hardware Async  ${G9DLAdd}    ${TRUE}
    :FOR    ${sh}  IN  @{G9DLAdd}
	\		${shname}=  Get Server Hardware Name from ILO IP  ${sh['hostname']}
	\       Wait Until Keyword Succeeds    30s    5s    Verify Server Hardware Status    ${shname}  ${ilo_managed_state}