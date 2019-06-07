admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
task_states = ['Warning', 'Completed']

iloUserName = 'Administrator'
iloPassword = 'hpvse123'

Gen10SYIP = '16.114.218.190'
Gen10SYName = 'CN75440444, bay 8'

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

GEN10SYInventory = [
    {
        "componentName": "agentless management service",
        "componentVersion": "1.30.0.0"
    },
    {
        "componentName": "System ROM",
        "componentVersion": "I42"
    },
]
