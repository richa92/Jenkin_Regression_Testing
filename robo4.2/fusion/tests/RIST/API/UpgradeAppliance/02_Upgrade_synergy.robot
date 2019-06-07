*** Settings ***
Documentation             Download Update Bin File, Upload it into Appliance, and Update Appliance with it.
Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   BuiltIn
Library                   robot.api.logger
Library                   Collections
Library                   OperatingSystem
Resource                  ./../../../../Resources/api/fusion_api_resource.txt
Resource                  ./keywords.txt
Variables                 ./Regression_Data.py

Test Setup                Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown             Fusion Api Logout Appliance
Suite Teardown            Remove Upgrade BIN File

*** Variables ***
${APPLIANCE_IP}           'DCS APPLIANCE IP'
${Team_Name}              SHQA
${RELEASE}                UNDEFINED
${PASS_BUILD}             UNDEFINED

*** Test Cases ***
Set Api Version
    Set Appliance Version Variable
    Set Data Version Variable

Upgrade OneView Appliance
    Set log level  TRACE
    Log     \nDownloading the upgrade bin file: ${update_bin_filename} ...    console=True
    Fusion Api Download Upgrade File
    ...         ${update_bin_file_url}
    ...         ${update_bin_filename}
    OperatingSystem.File Should Exist    ${EXECDIR}\\${update_bin_filename}
    ...               msg=Upgrade file ${update_bin_filename} is not existing in folder ${EXECDIR}

    Log    Uploading the upgrade bin file: ${update_bin_filename} ...  console=True
    ${Response}=                    Fusion Api Upload Appliance Firmware
    ...                             ${update_bin_filename}
    Log    ${Response}

    Log    Upgrading Appliance to ${PASS_BUILD}...    console=True
    ${Response}=                    Fusion Api Upgrade Appliance Firmware
    ...                             ${update_bin_filename}
    Log to console and logfile      \n${Response}

    Log    Waiting for OneView state to change to "UPGRADE"    console=True
    Wait For Appliance State To Be Expected State    ExpectedState=UPGRADE    timeout=20 mins      interval=5 s

    Log    Waiting for OneView state to change to "OK""  console=True
    Wait For Appliance State To Be Expected State    ExpectedState=OK    timeout=150 mins    interval=60 s
