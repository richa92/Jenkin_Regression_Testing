admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
bl_password = "hpvse123"
dl_password = "hpvse123"
task_states = ['Warning', 'Completed']

iloUserName = 'Administrator'
iloPassword = 'hpvse123'
iloPasswordDL = 'hpvse123'

Gen10BLName = 'wpst32, bay 10'
Gen10RHDLIP = '16.114.212.92'
Gen10WinDLIP = '16.114.212.49'
Gen10WinBLIP = '16.114.220.96'

# Server Hardware
GEN10DLServer = [
    {
        'hostname': Gen10RHDLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPasswordDL,
        'force': True,
        'configurationState': 'Managed'
    }
]

GEN10DLServerMonitored = [
    {
        'hostname': Gen10RHDLIP,
        'licensingIntent': 'OneViewStandard',
        'username': iloUserName,
        'password': iloPasswordDL,
        'force': False,
        'configurationState': 'Monitored'
    }
]

GEN10DLInventory = [
    {
        "componentName": "agentless management service",
        "componentVersion": "1.30.0.0"
    },
    {
        "componentName": "System ROM",
        "componentVersion": "U31"
    },
]

GEN10BLServer = [
    {
        'hostname': Gen10WinBLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]

GEN10BLInventory = [
    {
        "componentName": "agentless management service",
        "componentVersion": "1.30.0.0"
    },
    {
        "componentName": "System ROM",
        "componentVersion": "I41"
    },
]

wpst32Encls = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView'
    }
]

Managed32 = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView'
    }
]

Monitored32 = [
    {"hostname": "wpst32-oa1.vse.rdlabs.hpecorp.net",
     "username": "Administrator",
     "password": "hpvse14",
     "enclosureGroupUri": None,
     "force": False,
     "licensingIntent": "OneViewStandard",
     "initialScopeUris": [],
     "state": "Monitored"
     }
]
