*** Settings ***
Documentation        Uplink Sets Associated with ethernet Create a new uplink set  for LI which in the active scope with a ethernet which in another active scope
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
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Uplink Sets Associated with ethernet Create a new uplink set for LI which in the active scope with a ethernet which in another active scope
    Log  Can not add eth3 to LI2
    ${resps}=   Add Uplinkset from variable Async    ${add_Uplinksets2}
    Wait For Task2   ${resps}   timeout=240   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
