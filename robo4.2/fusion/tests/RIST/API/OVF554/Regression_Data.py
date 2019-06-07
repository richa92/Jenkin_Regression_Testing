admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']

iloUserName = 'Administrator'
iloPassword = 'hpvse1-ilo'

Gen10SYName = 'tbird15, bay 8'
Gen10BLName = 'wpst22, bay 16'
Gen10DLIP = '16.114.212.43'
Gen10BLIP = '16.125.78.225'
Gen10SYIP = '16.114.218.197'

# Server Hardware
GEN10SYServer = [
    {
        'hostname': Gen10SYIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]
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
