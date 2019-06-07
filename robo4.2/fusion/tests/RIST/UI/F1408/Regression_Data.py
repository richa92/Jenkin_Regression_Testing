admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

Volumes = [
           {'storageSystemVolumeName': 'Tbird_FC_Private_OS_NO_Delete',
            'storageSystemUri': 'wpst3par-7200-7-srv',
            'provisioningParameters': {'shareable': 'false'}
            },
           ]

headers = {'exportOnly':'true', 'Content-Type': 'application/json', 'Accept-language': 'en_US', 'Accept': 'application/json, */*', 'X-Api-Version': 300}

deleteVolumes = {'storageSystemVolumeName': 'Tbird_FC_Private_OS_NO_Delete',
            'storageSystemUri': 'wpst3par-7200-7-srv',
            'provisioningParameters': {'shareable': 'false'}
            }