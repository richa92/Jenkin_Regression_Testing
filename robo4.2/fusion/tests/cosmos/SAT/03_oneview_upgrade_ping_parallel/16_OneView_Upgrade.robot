*** Settings ***
Documentation
...     Upgrade of OV appliance.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Download Appliance Firmware
    [Tags]  DOWNLOAD  T-BIRD  C7000
    [Documentation]        Download Appliance Firmware bundle from HTTP server
    Log    ${WEB_URL}   console=True
    Download Specified SPP to Local Path   ${WEB_URL}    ${WEB_USERNAME}   ${WEB_PASSWORD}

Upgrade OneView
    [Tags]    UPGRADE  T-BIRD  C7000
    [Documentation]     Upgrade Oneview
    ${binfile_name} =    Fetch From Right        ${WEB_URL}      /
    ${local_binfile}=   set variable    ${binfile_local_path}/${binfile_name}
    ${resp} =    Fusion Api Upload Appliance Firmware    ${local_binfile}
    Run keyword unless  ${resp['status_code']}== 200    Fail    "Unable to Upload Appliance Firmware"
    ${upgrade_resp} =    Fusion Api Upgrade Appliance Firmware    ${binfile_name}
    Run keyword If    ${upgrade_resp['status_code']} != 202    Fail    "Unable to Upgrade Appliance"
    Wait Until Keyword Succeeds    ${ov_upgrade_timeout}   ${interval}   Appliance Upgrade Status Should Be Successful
    Sleep    600s

Active And StandBy EM Appliance Should Be Successfully Upgraded
     [Tags]    EM-UPGRADE  T-BIRD
     [Documentation]   Active And StandBy EM Appliance Should Be Successfully Upgraded
     ${binfile_name}     Fetch From Right        ${WEB_URL}      /
     ${ov_build_version}   Get Regexp Matches   ${binfile_name}  (-.\\d+)
     Wait Until Keyword Succeeds    ${em_tmieout}    ${interval}    Active And StandBy EMs Should Be Upgraded To  ${ov_build_version[0]}

Download LE Support Dump - Post OneView Upgrade
    [Tags]    LESD  C7000  T-BIRD
    [Documentation]        Create and Download LE Support Dump - Post OneView Upgrade
    Get LE Support Dump  ${le_support_dump_prebuildup}  ${TEST NAME}

Download Support Dump - Post OneView Upgrade
    [Tags]   DOWNLOAD-OVSD  T-BIRD   C7000
    [Documentation]    Get And Download Oneview Support Dump - Post OneView Upgrade
    Get Support Dump  ${support_dump}   ${TEST NAME}