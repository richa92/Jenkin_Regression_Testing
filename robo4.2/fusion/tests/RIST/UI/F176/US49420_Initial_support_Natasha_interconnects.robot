*** Settings ***
Resource        ../resource.txt

Test Setup      Run Keywords    Load Test Data and Open Browser
...             AND             Log into Fusion appliance as Administrator
Test Teardown   Logout and close all browsers


*** Variables ***
${user}                         Administrator
${DataFile}                     F176/Regression_data.xml 	# Data File Location
${APPLIANCE_IP}                 16.114.209.223               # Appliance IP
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url
${FUSION_IP}                    ${APPLIANCE_IP}             # Fusion Appliance IP

*** Test Cases ***
Add And Edit Natasha Interconnects
    Fusion UI Validate Interconnect    @{TestData.natasha_interconnects_monitored}

Create Networks, Network Sets, LIG, and EG
    Fusion UI create ethernet network   @{TestData.networks}
	Fusion UI create network set    @{TestData.networkSets}
    Fusion UI Create Tbird Logical Interconnect Group    @{TestData.ligs}
    Fusion UI Create Tbird Enclosure Group    @{TestData.encgroups}

Create A Logical Enclosure without Natasha LIG   
   	Fusion UI Create Tbird Logical Enclosure    @{TestData.logicalenclosures_consistent}
    Fusion UI validate tbird enclosure configuration	@{TestData.configured_enclosures}

Verify Interconnect State
    Fusion UI Validate Interconnect    @{TestData.natasha_interconnects_monitored}
    Fusion UI Validate Interconnect    @{TestData.interconnects_configured}

Create A Natasha LIG
    fusion ui create natasha logical interconnect group    @{TestData.natasha_lig_1}
    fusion ui edit natasha logical interconnect group    @{TestData.natasha_lig_1}

Add Natasha LIG to Enclosure Group
    Fusion UI Edit Tbird Enclosure Group    @{TestData.encgroups_natasha}

Verify Logical Enclosure Inconsistent with Enclosure Group
    Fusion UI Verify Logical Enclosure Consistency State    @{TestData.logicalenclosures_inconsistent}

Update Logical Enclosure from Group
    Fusion UI Logical Enclosure Update From Group    @{TestData.logicalenclosures_inconsistent}
    Fusion UI Verify Logical Interconnects Status    @{TestData.natasha_li}
    Fusion UI Verify Logical Enclosure Consistency State    @{TestData.logicalenclosures_consistent}

Edit Natasha LIG to Add Interconnect
    fusion ui edit natasha logical interconnect group    @{TestData.natasha_lig_2}

Update Logical Interconnect From Group
    Fusion UI Update Logical Interconnect From Group    @{TestData.natasha_li}

Verify Natasha Interconnect in Configured State
    Fusion UI Validate Interconnect     @{TestData.natasha_interconnects_configured}
    Fusion UI Validate Interconnect    @{TestData.interconnects_configured}