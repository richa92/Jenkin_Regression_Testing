# import imp
# types = imp.load_source('module.name', '../../../../Resources/api/types.py')

encR6 = {
    "type": "EnclosureV7"
}

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

ris_node_profile1_no_iscsi = [{
    "server": "CN754406XL, bay 7",
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/rest/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Description": "This is the Server iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
        ],
    }
}]
