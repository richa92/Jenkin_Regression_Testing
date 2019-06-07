"""
   Data File for API Regression Test cases
"""

ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'hpvse123'}

SFO_CREDENTIALS = {'userName': 'SFO', 'password': 'hpvse123'}

USERS = [{'userName': 'SFO',
          'password': 'hpvse123',
          'fullName': 'ServerFirmware',
          'roles': ['Server firmware operator'],
          'emailAddress': 'sarah@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndRoles'},
         {'userName': 'SFadmin',
          'password': 'hpvse123',
          'fullName': 'ServerFirmwareadmin',
          'roles': ['Server administrator'],
          'emailAddress': 'saraha@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndRoles'},
         {'userName': 'ReadOnlyUser',
          'password': 'hpvse123',
          'fullName': 'ReadonlyUser',
          'roles': ['Read only'],
          'emailAddress': 'sarah@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndRoles'}]


UPDATEUSER = [{'userName': 'SFO',
               'replaceRoles': 'false',
               'roles': ['Server administrator'],
               'type': 'UserAndRoles'}]


# Enclosures
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'

EG1 = 'GRP-%s' % ENC1

# Server Hardware
SH1 = '%s, bay 6' % ENC1
SH2 = '%s, bay 3' % ENC2
SH3 = '%s, bay 6' % ENC1

EB = '6'
EB1 = '6'

# Create empty Server profile
EMPTYPROFILE = [{
    "name": "EMPTY_SP2",
    "type": "ServerProfileV7",
    "serverHardwareUri": SH1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "connections": [],
    "boot":
        {
            "manageBoot": False},
    "bootMode": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}]

EDIT_SP = [
    {
        "type": "ServerProfileV7",
        "uri": "",
        "name": "EMPTY_SP2",
        "description": "",
        "serialNumber": "",
        "uuid": "",
        "iscsiInitiatorName": "",
        "iscsiInitiatorNameType": "",
        "serverProfileTemplateUri": "",
        "templateCompliance": "Unknown",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": ENC1,
        "enclosureBay": EB1,
        "affinity": "Bay",
        "associatedServer": None,
        "hideUnusedFlexNics": True,
        "firmware": {
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None},
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "category": "server-profiles",
        "created": "",
        "modified": "",
        "status": "OK",
        "state": "Normal",
        "inProgress": False,
        "connections": [],
        "bootMode":{
            "mode": None,
            "pxeBootPolicy": None,
            "manageMode": False},
        "boot": {
            "order": [],
            "manageBoot": False},
        "bios":{
            "manageBios": False,
            "overriddenSettings": []},
        "localStorage":{
            "sasLogicalJBODs": [],
            "controllers":[]},
        "sanStorage":{
            "volumeAttachments": [],
            "manageSanStorage": False},
        "osDeploymentSettings": None,
        "refreshState": "NotRefreshing",
        "eTag": ""}]

EDIT_SP_FR = [
    {
        "type": "ServerProfileV7",
        "uri": "",
        "name": "EMPTY_SP2",
        "description": "",
        "serialNumber": "",
        "uuid": "",
        "iscsiInitiatorName": "",
        "iscsiInitiatorNameType": "",
        "serverProfileTemplateUri": "",
        "templateCompliance": "Unknown",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": ENC1,
        "enclosureBay": EB1,
        "affinity": "Bay",
        "associatedServer": None,
        "hideUnusedFlexNics": True,
        "firmware": {
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": "NotScheduled",
            "firmwareInstallType": "FirmwareAndOSDrivers",
            "forceInstallFirmware": False,
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/Custom_Car_10104_incom_Productionbp-2016-07-23-05"},
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "category": "server-profiles",
        "created": "",
        "modified": "",
        "status": "OK",
        "state": "Normal",
        "inProgress": False,
        "connections": [],
        "bootMode":{
            "mode": None,
            "pxeBootPolicy": None,
            "manageMode": False},
        "boot": {
            "order": [],
            "manageBoot": False},
        "bios":{
            "manageBios": False,
            "overriddenSettings": []},
        "localStorage":{
            "sasLogicalJBODs": [],
            "controllers":[]},
        "sanStorage":{
            "volumeAttachments": [],
            "sanSystemCredentials":[],
            "manageSanStorage": False},
        "osDeploymentSettings": None,
        "refreshState": "NotRefreshing",
        "eTag": ""}]


SUPPORT_DUMP = {
    "encrypt": True,
    "errorCode": "CI",
}

NEWLICENSES = {'licenseType': 'LicenseV500',
               'license': [{'key': 'QCDG C9MA H9PA KHU2 U7B5 HWW5 Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 RMDZ XENY KJVT D5KM EFVW TSNJ 37H8 PXGW BPSM YF26 28JS EWTZ X36Q M5G7 WZJL HH5Q L975 SNJT 288F ADT2 LK44 56UG V8MC 2K9X 7KG2 F6AD EMVA 9GEB 95Y6 XBM3 HVDY LBSS PU24 KEWY JSJC FPZC 2JJE ZLAB "MB_TEST_E5Y39A KEY-E5Y39A#FUSION HP_OV_w/o_iLO_w/_3yr_24x7_Phys_Flex_Lic UUCAJUTE69E6"'},
                           {'key': 'AC3C C9MA H9P9 8HX2 U7B5 HWW5 Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 EQHY UENM KJVT D5KM EFVW TSNJ D77K MXWW BPSM YF26 28JS EWTZ X36Q M5G7 WZJL HH5Q L975 SNJT 288F ADT2 LK44 56UG V8MC 2K9X 7KG2 F6AD EMVA 9GEB 95Y6 XBM3 HVDY LBSS PU24 KEWY JSJC FPZC 2JJE ZLAB "MB_TEST_E5Y39A KEY-E5Y39A#FUSION HP_OV_w/o_iLO_w/_3yr_24x7_Phys_Flex_Lic UUCAJUTE69E6"'}],
               'invalidLicense': [{'key': 'YYYY D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]}
