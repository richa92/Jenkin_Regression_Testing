"""
   Data File for API Regression Test cases
"""

ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'hpvse123'}
USERS = [{"emailAddress": "Read-Only@users.com",
          "enabled": "true",
          "fullName": "ReadOnly",
          "mobilePhone": "555-2121",
          "officePhone": "555-1212",
          "password": "hpvse123",
          "permissions": [{"roleName": "Read only"}],
          "type": "UserAndPermissions",
          "userName": "ReadOnlyUser"},
         {"emailAddress": "Backup-Admin@users.com",
          "enabled": "true",
          "fullName": "BackupAdmin",
          "mobilePhone": "555-2121",
          "officePhone": "555-1212",
          "password": "hpvse123",
          "permissions": [{"roleName": "Backup administrator"}],
          "type": "UserAndPermissions",
          "userName": "BackupAdminUser"}]
NEWLICENSES = {
    'license': [{"key": "YCDC B9MA H9PA 8HU2 U7B5 HWW5 Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 FQD6 GFN4 KJVT D5KM AFVW TT5J 57HK NXGW BPSM YF26 28JS EWTZ X36Q M5G7 WZJL HH5Q L975 SNJT 288F ADT2 LK44 56UG V8MC 2K9X 7KG2 F6AD EMVA 9GEB 95Y6 XBM3 HVDY LBSS PU24 KEWY JSJC FPZC 2JJE ZLAB \"MB_TEST_E5Y39A KEY-E5Y39A#FUSION HP_OV_w/o_iLO_w/_3yr_24x7_Phys_Flex_Lic UUCAJUTE69E6\"", "type": "License"}],
    'NewLicense': [{"key": "9CYE BQ9A H9PA 8HU3 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 5U6Y XYVM KJVT D5KM AFVW TT5J ND7J 6Q2K JMTK 9GW8 C9QE XUNR NW89 45BT BS2Z X4YU WP7Y HNEH FRWE 4DGC KX2F BDB5 V8MC 2K9X V862 F6ED 7ZAW JUK2 FF2F MKKE 5NM4 BGP8 58KE Z2TX DSB4 5GT9 W8RL WVDR XSSU 9Y39 LQAC YMFZ VGGE A7EJ \"IPP20150406103202 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic UYY6JUHTYH46\"_3MKHV-XQTSN-STRJH-4GQ9T-WSJS6", "type": "License"}],
    'invalidLicense': [{'key': 'YYYY D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]}
NODEID = {"product": "HPE OneView Advanced w/o iLO", "nodes": [""], "type": "License"}
NODELIST = [{"nodes": [{"nodeId": "1", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "2", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "3", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "4", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "5", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "6", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "7", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "8", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "9", "nodeUri": "/rest/node1.usa.hp.com/"}]}, {"nodes": [{"nodeId": "10", "nodeUri": "/rest/node1.usa.hp.com/"}]}]
EMAIL_CONFIGURATION = {
    "alertEmailDisabled": "false",
    "alertEmailFilters": [
        {
            "disabled": "false",
            "displayFilter": "status:warning status:critical",
            "emails": ["vinay.kumar2@hpe.com", "vinay.kumar2@hpe.com"],
            "filter": "status:'warning' or status:'critical'",
            "userQueryFilter": "CPU",
            "limit": 5,
            "limitDuration": "minute",
            "filterName": "Critical Alerts"
        }],
    "password": "",
    "senderEmailAddress": "",
    "smtpPort": 25,
    "smtpProtocol": "",
    "smtpServer": "",
    "type": "EmailNotificationV3"}

TEST_EMAIL = {
    "htmlMessageBody": "Html alert message with html and css content",
    "subject": "Critical alert generated",
    "textMessageBody": "Plain text mail content",
    "toAddress": ["vinay.kumar2@hpe.com", "krithika.m@hpe.com"],
    "type": "Email"}

HTML_NOTIFICATION = {
    "htmlMessageBody": "Html alert message with html and css content",
    "subject": "Critical alert generated",
    "textMessageBody": "Plain text mail content",
    "toAddress": ["vinay.kumar2@hpe.com", "vinay.kumar2@hpe.com"],
    "type": "Email"}
