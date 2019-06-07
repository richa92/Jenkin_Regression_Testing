admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']

iloUserName = 'Administrator'
iloPassword = 'hpvse1-ilo'

Gen10BLName = 'wpst22, bay 16'
Gen10DLIP = '16.114.212.43'
Gen10BLIP = '16.125.78.225'

# Server Hardware
GEN10DLServer = [
    {
        'hostname': Gen10DLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]

GEN10DLServerMonitored = [
    {
        'hostname': Gen10DLIP,
        'licensingIntent': 'OneViewStandard',
        'username': iloUserName,
        'password': iloPassword,
        'force': False,
        'configurationState': 'Monitored'
    }
]

GEN10BLServer = [
    {
        'hostname': Gen10BLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]

wpst20Encls = [
    {
        'hostname': 'wpst22-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst20',
        'force': True,
        'licensingIntent': 'OneView'
    }
]

Managed20 = [
    {
        'hostname': 'wpst22-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst20',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
Monitored20 = [
    {
        'hostname': 'wpst22-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst20',
        'force': False,
        'licensingIntent': 'OneViewStandard',
        'state': 'Monitored',
    }
]
