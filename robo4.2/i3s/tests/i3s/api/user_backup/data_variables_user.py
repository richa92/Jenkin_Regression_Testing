#from winnt import NULL
from requests.api import patch

users = [
    {'userName': 'Backupadmin', 'password': 'admin123', 'fullName': 'Backupadmin', "permissions": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            }],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'admin123', 'fullName': 'Networkadmin',
     "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": None
            }], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Noprivlege', 'password': 'admin123', 'fullName': 'Noprivledge', "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Serveradmin', 'password': 'admin123', 'fullName': 'Serveradmin', "permissions": [
            {
                "roleName": "Server administrator",
                "scopeUri": None
            }],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Storageadmin', 'password': 'admin123', 'fullName': 'Storageadmin', "permissions": [
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Softwareadmin', 'password': 'admin123', 'fullName': 'Softwareadmin', "permissions": [
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

artifact_bundle = 'HPE_Support_Artifacts-5_00'

backup_file_name = '/root/Goldenimage/backup_download.zip'
