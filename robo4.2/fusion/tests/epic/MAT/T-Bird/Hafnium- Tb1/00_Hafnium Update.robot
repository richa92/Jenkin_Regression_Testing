*** Settings ***
Documentation
...     This Test Suite Download Hafnium build, rename it, send it to OV root and update the firmware.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource.txt
Library                         robot.api.logger
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***
Update Hafnium
    [Tags]              HAFNIUM
    [Documentation]     This Test is to update Hafnium firmware on interconnects
    Set Log Level   TRACE
    # Open a connection to Jenkins (the destination) and retrieve the last build Id
    Set Default Configuration   prompt=\#        timeout=500
    Open Connection    ${APPLIANCE_IP}
    Login    ${ssh_username}    ${ssh_password}

    # Get a copy of the file onto the destination machine
    Console    \nCopying ${potash_pkg} .....
    ${STDOUT}    ${STDERR}=    Execute Command
    ...    wget ${potash_url}
    ...    return_stderr=yes
    Should Contain    ${STDERR}    100%    msg=Couldnt transfer ${potash_pkg}
    Console    \nRenaming pkg file
    ${STDOUT}    ${STDERR}=    Execute Command
    ...    /bin/mv ${potash_pkg} hpe_icm.pkg
    ...    return_stderr=yes
    Should Not Contain    ${STDERR}    Failure    msg=Couldnt rename ${potash_pkg}
    Console    \nUpdating Firmware
    :FOR    ${icm}  IN  @{interconnects}
    \   SSHLibrary.Write   scp hpe_icm.pkg ${firmwareupdate_password}@${icm['ipAddress']}:.
    \   Read Until  ${firmwareupdate_password}@${icm['ipAddress']}'s password:
    \   SSHLibrary.Write   ${firmwareupdate_password}
    \   Read Until  hpe_icm.pkg
    \   Console    \nApplying Update on ${icm['name']}
    \   SSHLibrary.Write   ssh ${firmwareupdate_password}@${icm['ipAddress']} apply.update
    \   Read Until  ${firmwareupdate_password}@${icm['ipAddress']}'s password:
    \   SSHLibrary.Write   ${firmwareupdate_password}
    \   Read Until  flash.update: Completed flashing uImage to
    \   Console    \nActivating Update on ${icm['name']}
    \   SSHLibrary.Write   ssh ${firmwareupdate_password}@${icm['ipAddress']} activate.update
    \   Read Until  ${firmwareupdate_password}@${icm['ipAddress']}'s password:
    \   SSHLibrary.Write   ${firmwareupdate_password}
    \   Read Until  activate.update: Initiating a Reboot
    Close Connection
    Sleep   120s
    :FOR    ${icm}  IN  @{interconnects}
    \   ${fw} =     Get Interconnect Firmware Version   ${icm['name']}
    \   Run Keyword Unless  '${fw}'=='${expected_fw}'    Run Keyword and Continue on Failure    Fail     Installed firmware version on ${icm['name']} is ${fw} however expected firmware version is ${expected_fw}
