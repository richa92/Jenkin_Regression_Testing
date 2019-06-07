*** Settings ***
Documentation        Server Hardware support SBAC_Remove an server hardware which in the active scope
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ./Regression_Data.py
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt


*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Server Hardware support SBAC_Remove an server hardware which in the active scope
  [Documentation]  Server Hardware support SBAC_Remove an server hardware which in the active scope
  log    Server Hardware support SBAC_Remove an server hardware which in the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${uri} =  Get Server Hardware URI  ${new_dl_sh_name}
  ${resp} =  Fusion Api Delete Server Hardware  uri=${uri}
  Wait For Task2    ${resp}
  log    Successfully! Test Case : OVF1592_API_p148 Server Hardware support SBAC_Remove an server hardware which in the active scope    console=true
