*** Settings ***
Documentation    Deploy Fusion ISO onto CIM using Atlas USB Key
...    = Usage =
...    pybot |-v ENCLOSURE:tesla |-v ISO_URL:<Fusion ISO Image> Deploy_CIM_Fusion.txt
...    = Variables =
...    | ENCLOSURE | (required) Name of the enclosure to Deploy upon. (values from variables.py) |
...    | ISO_URL | (optional) URL of Fusion ISO Image To Install (defaulted) |
...
...     --Prepare for Firmware Update [Get Firmware Versions and Get Enclosure Manager Credentials]
...     --Stop cluster service on Standby and Active CIM
...     --Reset all EM's in the ring
...     --Deploy Firmware Updates [Initiate DD Image Update, Wait For Fusion Install and Startup and Assign Administrator Password]

Resource          ./resource_dd.txt
#Resource          ../../../../Resources/api/fusion_api_resource.txt
#Variables         ./variables_tbird.py    ${ENCLSOURE}
#Resource          ./resource_tbird.txt
#Variables         ./data_variables_tbird.py

*** Variables ***


*** Test Cases ***
Prepare for DD Image
    [Tags]    DEPLOY    Pre-Deploy
    [Documentation]  Pre Deploy DD Image by getting firmware versions
    Log Variables
    Set Log Level   TRACE
    #Console    \nDeploying from: ${DD_URL} onto: ${ENCLOSURE}
    Get Firmware Versions

Get the enclosure(For multi-enclosure environments)credentials
    [Tags]  DEPLOY    GETENCCREDENTIALS
    [Documentation]  Get Enclosure Manager credentials and verify claimed enclosure
    ${Enclosure_Credentials}    Get Enclosure Manager Credentials
    Run Keyword and Ignore Error
    ...    Verify Claimed Enclosure

Reset all EM's in the ring
    [Tags]    DEPLOY    Factory-Reset-EM
    [Documentation]  Reset all EM's
    Set Log Level   TRACE
    EM Factory Reset

Deploy DD Image
    [Tags]    DEPLOY    Deploy-DD-Image
    [Documentation]  Deploy DD Image
    Initiate DD Image Update
    Wait For Fusion Install and Startup
    Assign Administrator Password

Setup Fusion after Deploy
    [Tags]    DEPLOY    Post-Deploy
    [Documentation]  Set Fusion appliance after Deploy
    Appliance Login
    Set Fusion Version Metadata
    # Write Fusion Properties
    Get Firmware Versions
    # This should be "Run Keyword and Continue on Failure" to fail the Test case if enclosure is not claimed.
    Run Keyword and Ignore Error
    ...    Verify Claimed Enclosure
    #Prevent CIM iLo Reset From Fusion Factory Reset
    Generate Fusion Dump and Log After Network Initialization

Refresh Enclosure
    [Tags]      DEPLOY    REFRESH
    [Documentation]  Refresh Enclosure
    ${responses}=  Refresh Enclosure Async   ${encs_monitor}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}  timeout=1000    interval=20
