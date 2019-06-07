*** Settings ***
Documentation        Test Time Shift on NTP Server
Library           	DateTime
Resource            ../Resource/CIM_CommonResource.txt
Resource            ../Resource/CIM_UsersAndGroups.txt
Resource            ../Resource/CIM_Activity.txt
Resource            ../Resource/CIM_Settings.txt
Test Setup            Load Test Data and Open Browser
Test Teardown        Logout and close all browsers
Variables         ../../../../FusionLibrary/ui/business_logic/settings/timeandlocale_elements.py
Variables           ../../../../FusionLibrary/ui/business_logic/general/activity_elements.py
Variables            ../../../../FusionLibrary/ui/business_logic/facilities/settings_elements.py

*** Variables ***
${activity_name}	The appliance could not sync with the NTP server

*** Test Cases ***
As an Administrator Change Time On NTP Server
    Log into Fusion appliance as Administrator
    ${status} =    Fusion UI Edit Time and Locale    @{TestData.edittimeonNTP}
    Should Be True		${status}	msg=Failed to edit time and locale on appliance
    
    #Verify NTP configuration on Time and Locale page
    Fusion UI Verify Time and Locale    @{TestData.edittimeonNTP}
    
    #Change time of NTP Server
    log		Changing Time on NTP server
    ${ntp_output} =    Change Time On NTP Server
    log     Time Changed to ${ntp_output} on NTP Server
    
	#Verify if an alert is generated on Time and Locale Page and a recorded activity on activity page
    Verify Alert on Time and Locale and Activity Page After Time Shift	${activity_name}
    
    #Restart appliance to allow it to sync up with the NTP server
    Fusion UI Restart   

    #Verify alert disappearance on Time and Local Page after appliance restart
    Verify Alert on Time and Locale Page After Appliance Restart