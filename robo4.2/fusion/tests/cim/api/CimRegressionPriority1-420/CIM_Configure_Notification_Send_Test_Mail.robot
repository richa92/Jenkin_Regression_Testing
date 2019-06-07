*** Settings ***
Documentation     Edit Notifications and Send Test mail
Library           RoboGalaxyLibrary
Library           FusionLibrary
Library           SSHLibrary
Library           OperatingSystem
Library           String
Library           Collections
Library           XML
Library           Dialogs
Library           json

Resource          ../Resource1-42/CIM_Common_Resource.txt
Resource          ../Resource1-42/CIM_Email_Keyword.txt

*** Test Cases ***
Email Configuration
    [Documentation]    Email Configuration
    Configure email notification

Verify Error messages while configuring E-mail Notification
   [Documentation]     Error messages while configuring E-mail Notification
   Error messages while configuring E-mail Notification

To send Test Mail
    [Documentation]    Send Test Mail after configuring Email
    Send Test Mail
