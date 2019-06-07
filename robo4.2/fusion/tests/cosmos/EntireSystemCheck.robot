***Setting***
Documentation    Entire System Check (ESC)
...              Tests to verify all resources status and state without providing any data file
...              Tests to verify Active alerts
...              Tests to verify Active tasks
...              Tests to verify License and template compliance.
...              Test Plan - CST System Restart MAThttps
...              Link - https://ea2013.sharepoint.hpe.com/teams/theCosmos/_layouts/15/WopiFrame2.aspx?sourcedoc=%2Fteams%2FtheCosmos%2FGrenoble%2FTest%20Module%2FCST%20System%20Restart%20MAT%2Edocx&action=view&wdparaid=160C0273

Library          FusionLibrary
Library          RoboGalaxyLibrary
Resource        ../../Resources/api/fusion_api_resource.txt
Suite Setup      Login
Suite Teardown   Logout
Resource                        ../../Resources/api/fusion_api_resource.txt

***Variables***
${password}               Cosmos123
&{admin_credentials}      userName=Administrator    password=${password}
${APPLIANCE_IP}           10.141.1.15

***Test Case***
Servers Hardware Refresh Test
    [Tags]    Refresh  C7K  TBIRD
    Wait For Appliance State To Be Expected State  OK
    Sleep  60s  Waiting for Enclosure refresh to be started
    Wait For ALL Enclosures Complete Refresh
    Servers Refresh Should be completed

One View Alerts Test
    [Tags]    AlertsOV  C7K  TBIRD
    Should Not Have Active Alerts With Severity Other Than  OK

One View Task Test
    [Documentation]    Wait for all tasks in OV and timeout
    ...  default timeout is 10 mins
    ...  Filter on “Tasks” state not completed and cleared with Status not equal to OK
    [TAGS]  OVT  C7K  TBIRD
    Wait For All Tasks IN One View
    Should not have task state other than Completed and Cleared with Status other than OK

Server Hardware State Test
    [Tags]    SH-State  C7K  TBIRD
    Server Hardwares State Should Not Be  Unmanaged

Server Hardware Status Test
    [Tags]    SH-Status  C7K  TBIRD
    Server Hardwares Status Should Be  OK

San Manager Status Test
    [Tags]    SM-Status  C7K  TBIRD
    San Manager Attribute status Should Have Value OK

San Manager State Test
    [Tags]    SM-State  C7K  TBIRD
    San Manager Attribute state Should Have Value Managed

SANs Status Test
    [Tags]    San-Status  C7K  TBIRD
    SANs Attribute status Should Have Value OK

SANs State Test
    [Tags]    San-State  C7K  TBIRD
    SANs Attribute state Should Have Value Managed

Storage Systems Status Test
    [Tags]    SS-Status  C7K  TBIRD
    Storage Systems Attribute status Should Have Value OK

Storage Systems State Test
    [Tags]    SS-State  C7K  TBIRD
    Storage Systems Attribute state Should Have Value Managed

Storage Systems Actual And Expected Port Test
    [Tags]  SS-P  C7K  TBIRD
    Storage Systems Actual and Expected Port Should Be Consistent

Storage Volumes Status Test
    [Tags]    SV-Status  C7K  TBIRD
    Storage Volumes Attribute status Should Have Value OK

Storage Volumes State Test
    [Tags]    SV-State  C7K  TBIRD
    Storage Volumes Attribute state Should Have Value Managed

Server Profiles State Test
    [Documentation]    Verify status of all profiles in OV
    [TAGS]    SP-State  C7K  TBIRD
    Server Profiles Attribute state should Have Value Normal

Server Profiles Status Test
    [Documentation]    Verify state of all profiles in OV
    [TAGS]    SP-Status  C7K  TBIRD
    Server Profiles Attribute status Should Have Value OK

Server Profile Templates State Test
    [Documentation]    Verify status of all profile templates in OV
    [TAGS]    SPT-State  C7K    TBIRD
    Server Profile Templates Attribute state should Have Value Normal

Server Profile Template Status Test
    [Documentation]    Verify state of all profile templates in OV
    [TAGS]    SPT-Status  C7K    TBIRD
    Server Profile Templates Attribute status Should Have Value OK

Server Profile Template Compliance Test
    [Documentation]    Verify compliance for Server Profile Template
    [TAGS]    SPTC  C7K    TBIRD
    Server Profile Template Should be Compliant

Hypervisor Cluster Profiles State Test
    [Documentation]    Verify status of all profiles in OV
    [TAGS]    HCP-State  C7K    TBIRD
    Hypervisor Cluster Profiles Attribute state should Have Value Active

Hypervisor Cluster Profiles Status Test
    [Documentation]    Verify state of all profiles in OV
    [TAGS]    HCP-Status  C7K    TBIRD
    Hypervisor Cluster Profiles Attribute status Should Have Value OK

Hypervisor Profiles State Test
    [Documentation]    Verify status of all profiles in OV
    [TAGS]    HP-State  C7K    TBIRD
    Hypervisor Host Profiles Attribute state should Have Value Active

Hypervisor Profiles Status Test
    [Documentation]    Verify state of all profiles in OV
    [TAGS]    HP-Status  C7K    TBIRD
    Hypervisor Host Profiles Attribute status Should Have Value OK

Hypervisor Managers State Test
    [Documentation]    Verify status of Hypervisor Managers in OV
    [TAGS]    HM-State  C7K    TBIRD
    Hypervisor Managers Attribute state should Have Value Connected

Hypervisor Managers Status Test
    [Documentation]    Verify state of all profiles in OV
    [TAGS]    HM-Status  C7K    TBIRD
    Hypervisor Managers Attribute status Should Have Value OK

Enclosures State Test
    [Documentation]    Verify state of all Enclosures in OV
    [TAGS]    ENC-State  C7K    TBIRD
    Enclosures Attribute state Should Have Value Configured

Enclosures Status Test
    [Documentation]    Verify status of all Enclosures in OV
    [TAGS]    ENC-Status  C7K  TBIRD
    Enclosures Attribute status Should Have Value OK

Interconnects State Test
    [Documentation]    Verify state of all Interconnects in OV
    [TAGS]    ICM-State  C7K    TBIRD
    Interconnects Attribute state Should Have Value Configured

SAS Interconnects State Test
    [Documentation]    Verify state of all SAS Interconnects in OV
    [TAGS]    SAS-State  TBIRD
    SAS Interconnects Attribute status Should Have Value Configured

Interconnects Status Test
    [Documentation]    Verify status of all Interconnects in OV
    [TAGS]    ICM-Status  C7K    TBIRD
    Interconnects Attribute status Should Have Value OK

SAS Interconnects Status Test
    [Documentation]    Verify status of all SAS Interconnects in OV
    [TAGS]    SAS-Status  TBIRD
    SAS Interconnects Attribute state Should Have Value OK

LE State Test
    [Documentation]    Verify state of all Logical Enclosures in OV
    [TAGS]    LE-State  C7K  TBIRD
    Logical Enclosures Attribute state Should Have Value Consistent

LE Status Test
    [Documentation]    Verify status of all Logical Enclosures in OV
    [TAGS]    LE-Status  C7K  TBIRD
    Logical Enclosures Attribute status Should Have Value OK

EG State Test
    [Documentation]    Verify state of all Enclosures Group in OV
    [TAGS]    EG-State  C7K  TBIRD
    Enclosure GRoup Attribute state Should Have Value Normal

EG Status Test
    [Documentation]    Verify status of all Enclosures Group in OV
    [TAGS]    EG-Status  C7K  TBIRD
    Enclosure Group Attribute status Should Have Value OK

LIG State Test
    [Documentation]    Verify state of all Logical Interconnects Group in OV
    [TAGS]    LIG-Status  C7K  TBIRD
    All Logical Interconnect Groups State Should Be  Active

One View Remote Support Test
    [Documentation]  Check Remote Support Enable Task should be completed,
    ...  Check If Remote Support enabled
    ...  True, then all dependent resources should be enabled as well
    [TAGS]  RST  C7K  TBIRD
    Run Keyword And Continue On Failure  Remote Support Enable Task Should Be  Completed
    Remote Support Should be Enabled

One View License Test
    [Documentation]  OV Advanced License with and without iLO should be 100% compliant
    [Tags]    LT  C7K  TBIRD
    License Should Be Compliant

Frame Link Topology Should Be Discovered Without Error
    [Documentation]    Verify all FLTs were discovered properly without errors
    [Tags]    FLT  TBIRD
    Frame Link Topology Should Be Discovered Without Error

Drive Enclosure State Test
    [Documentation]    Verify Drive Enclosure State
    [Tags]    DE-State  TBIRD
    Drive Enclosure Attribute state Should Have Value Configured

Drive Enclosure Status Test
    [Documentation]    Verify Drive Enclosure Status
    [Tags]    DE-Status  TBIRD
    Drive Enclosure Attribute status Should Have Value OK

Logical JBOD State Test
    [Documentation]    Verify Logical JBOD State
    [Tags]    JBOD-State  TBIRD
    Logical JBOD Attribute state Should Have Value Configured

Logical JBOD Status Test
    [Documentation]    Verify Logical JBOD Status
    [Tags]    JBOD-Status  TBIRD
    Logical JBOD Attribute status Should Have Value OK

***Keywords***
Login
    [Documentation]  Login to OV with provided credentials
    Fusion Api Login Appliance  ${APPLIANCE_IP}    ${admin_credentials}

Logout
    [Documentation]  Logout from OV
    Fusion Api Logout Appliance