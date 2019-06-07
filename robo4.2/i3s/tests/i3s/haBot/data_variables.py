from winnt import NULL
from requests.api import patch


fusion_IP = '15.212.164.150'
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
leToTestHA     = "LE"

curl1          = "7.19.7"  
curl2          = "7.54.1"				


IOFlag         = 0
loops          = 1
mgmtCases      = 1
linkCases      = 1
icmCases       = 1
cimPCases      = 1
cimRmCases     = 0
cimRmCasesUI   = 0
StopToDebug    = 0


sdmp_body = {"errorCode": "CI", "encrypt": False}
LE_SupportDump_Payload = {"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": True} 
rediscover_appliance_Payload = {"description": None, "cimEnclosureName": None}
#rediscover_appliance_Payload = {"description": NULL, "cimEnclosureName": null}


### not required unless you want to recover your i3S appliances from some failure
repair1       = 'fe80::9eb6:54ff:fe97:9d18'
repair2       = 'fe80::1602:ecff:fe46:b1f0'
powerFailRuns  = 2
rmInsertRuns   = 2
mgmtCableRuns  = 2


##########################################################################################



