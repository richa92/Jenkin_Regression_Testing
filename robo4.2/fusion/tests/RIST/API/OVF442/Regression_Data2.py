ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

cim1_name = "CN75120D7B, appliance bay 1"

MAINTENANCE_CREDENTIALS = {"host": {"active": "16.114.210.229",
                                    "standby": "16.114.210.230"
                                    },
                           "username": "root",
                           "password": "hpvse1"
                           }

MAINTENANCE_CREDENTIALS_BAK = {"host": {"active": "16.114.210.230",
                                        "standby": "16.114.210.229"
                                        },
                               "username": "maintenance",
                               "password": "hpvse1"
                               }

CIM_HOSTS = {"active": "16.114.209.229",
             "standby": "16.114.211.59"
             }

CIM_HOSTS_BAK = {"active": "16.114.211.59",
                 "standby": "16.114.209.229"
                 }

ilo_credentials = {'username': 'Administrator1', 'password': 'hpvse123'}

disable_ssh_body = {"allowSshAccess": False,
                    "type": "SshAccess"
                    }

enable_ssh_body = {"allowSshAccess": True,
                   "type": "SshAccess"
                   }
