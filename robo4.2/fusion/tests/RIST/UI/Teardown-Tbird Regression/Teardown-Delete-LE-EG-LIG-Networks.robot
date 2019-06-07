*** Settings ***
Resource        ../resource.txt
Resource        ../../../../Resources/ui/common/setup.txt


Test Setup      Run Keywords        Load Test Data and Open Browser
...             AND                 Log into Fusion appliance as Administrator
Test Teardown   Logout and close all browsers

*** Variables ***
${DataFile}                            	F176/Regression_data.xml         # Data File Location
${APPLIANCE_IP}                         16.114.209.223               # Appliance IP
${ApplianceUrl}                         https://${APPLIANCE_IP}         # Appliance Url

*** Test Cases ***
Delete LE EG LIG Networks and Users
    ${Status1}=  fusion ui delete tbird logical enclosure  @{TestData.logicalenclosures_consistent}
   	Should Be True  ${Status1}   msg=Failed to delete le
    ${Status2}=  fusion ui delete enclosure group  @{TestData.encgroups}
    Should Be True  ${Status2}   msg=Failed to delete eg
    ${Status3}=  fusion ui delete logical interconnect group  @{TestData.ligs}
    Should Be True  ${Status3}   msg=Failed to delete lig
    ${Status4}=  fusion ui delete network set  @{TestData.networkSets}
    Should Be True  ${Status4}   msg=Failed to delete network sets
   	${Status5}=  fusion ui delete all appliance networks
   	Should Be True  ${Status5}   msg=Failed to delete networks
    ${Status6}=  fusion ui remove user		@{TestData.users}
    Should Be True  ${Status6}   msg=Failed to delete users