*** Settings ***
Resource        ../resource.txt
Resource        ../../../../Resources/api/fusion_api_resource.txt

Variables       API_Hardware_Setup_Data.py

Suite Setup     Run Keywords       Load Test Data and Open Browser
...             AND             	Log into Fusion appliance as Administrator
Suite Teardown  Logout and close all browsers

*** Variables ***
${DataFile}                     F175/Regression_data.xml             # Data File Location
${APPLIANCE_IP}                 16.114.213.40               # Appliance IP
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url
${X-API-VERSION}                300                         # X-API-VERSION
${FUSION_IP}                    ${APPLIANCE_IP}             # Fusion Appliance IP
${FUSION_SSH_USERNAME}          root                        # Fusion SSH Username
${FUSION_SSH_PASSWORD}          hponeview                   # Fusion SSH Password
${FUSION_PROMPT}                \#                          # Fusion Appliance Prompt
${FUSION_TIMEOUT}               300                         # Timeout

*** Test Cases ***

Verify Natasha Interconnects represented in Enclosure Overview and Detials views
    ${status}=                      Fusion Ui Validate TBird Enclosure Configuration     @{TestData.enclosures_configured}
    Should Be True                  ${status}                   msg=Failed to verify tbird Configured Enclosures


Verify Natasha Interconnects represented in Interconnects view
    fusion ui validate interconnect     @{TestData.natasha_interconnects}


Validate Hyperlinks between Natasha Interconnects and Enclosures page
    fusion ui verify interconnect hyperlinks        @{TestData.natasha_interconnects}


Verify Power Off Action for Natasha Interconnects
    fusion ui interconnect power off      @{TestData.natasha_interconnects}


Verify Power On Action for Natasha Interconnects
    fusion ui interconnect power on       @{TestData.natasha_interconnects}


Verify Turn UID On for Natasha Interconnects
    fusion ui turn on interconnect UID         @{TestData.natasha_interconnects}


Verify Turn UID Off for Natasha Interconnects
    fusion ui turn off interconnect UID        @{TestData.natasha_interconnects}


Verify Soft Reset Action for Natasha Interconnects
    fusion ui soft reset natasha interconnect       @{TestData.natasha_interconnects}


Verify Hard Reset Action for Natasha Interconnects
    fusion ui hard reset natasha interconnect       @{TestData.natasha_interconnects}


Verify Authorizations for Natasha Interconnects
    ${Status}=          fusion ui create user   @{TestData.users}
    Should Be True      ${Status}               msg= Failed to add users
    fusion ui logout of appliance
    :FOR    ${user}    IN      @{TestData.users}
        \       fusion ui login to appliance    ${user.name}
        \       fusion ui validate natasha interconnects user permissions       ${user.role}  @{TestData.natasha_interconnects}
        \       fusion ui logout of appliance
