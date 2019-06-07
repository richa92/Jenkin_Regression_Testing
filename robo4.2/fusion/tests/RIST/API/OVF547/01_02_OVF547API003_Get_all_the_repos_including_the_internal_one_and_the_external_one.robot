*** Settings ***
Documentation        Get all the repos including the internal one and the external one
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
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Get all the repos including the internal one and the external one
    Log    \n Get all the repos including the internal one and the external one    console=true
    ${resp} =    Fusion Api Get Repository
    ${count} =   Get From Dictionary     ${resp}  count
    Log    Ensure there are repos in the appliance, repo count: ${count}    console=true
    Should Not Be Equal   '${count}'   '0'
    ${repo_list} =    Create List
    :FOR   ${repo}   IN  @{resp['members']}
    \      Append To List    ${repo_list}    ${repo['name']}
    Should Contain    ${repo_list}    ${repository_name}
    Should Contain    ${repo_list}    ${internal_name}