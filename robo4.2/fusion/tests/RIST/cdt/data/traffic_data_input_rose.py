# Appliance/OneView IPv4 & its login credentials
oneview = {
    'ip': '16.114.217.122',
    'cred': {
        'userName': 'Administrator',
        'password': 'hpvse123',
    },
}

# Server/GuestOS reachable IP & other login input
serversAndCredentials = {
    'le:LE1/encl:2/bay:6': {  # P3
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.42',
        'platform': 'Linux',
    },
    'le:LE1/encl:3/bay:4': {  # P9
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'hpvse123'
        },
        'reachableIp': '10.100.0.39',
        'platform': 'Linux',
    },
    'le:LE1/encl:1/bay:5': {  # P13
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'hpvse123'
        },
        'reachableIp': '10.100.0.41',
        'platform': 'Linux',
    },
    'le:LE1/encl:3/bay:11': {  # P14
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'password'
        },
        'reachableIp': '10.100.0.43',
        'platform': 'Linux',
    },
    'le:LE1/encl:1/bay:9': {  # P16
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.44',
        'platform': 'Linux',
    },
    'le:LE1/encl:3/bay:10': {  # P21
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.45',
        'platform': 'Linux',
    },
    'le:LE1/encl:3/bay:12': {  # P22
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.46',
        'platform': 'Linux',
    },

}

# Extra session options like interval, size, ttl
trafficProfileOptionsForFping = {
    'trafficgen': 'fping',
    'interval': 500,
}
trafficProfileOptionsForPing = {
    'trafficgen': 'ping',
}

# Traffic session as entity input
input = {
    'fusion': oneview,
    'serversAndCredentials': serversAndCredentials,
    'entities': [
        # Starting from here P3 to P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['406-416'],
            'source': 'le:LE1/encl:2/bay:6/port:3:1-b',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:2-b'

            ],
            'description': 'East-West',
        },
        # Starting from here P3 to P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['467-477'],
            'source': 'le:LE1/encl:2/bay:6/port:3:2-c',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # Starting from here P3 to P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['528-533'],
            'source': 'le:LE1/encl:2/bay:6/port:3:1-d',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:2-d'

            ],
            'description': 'East-West',
        },
        # P9 to P3
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['407-417'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-b',
            'destination': [
                'le:LE1/encl:2/bay:6/port:3:2-b'

            ],
            'description': 'East-West',
        },
        # P9 to P3
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['515-525'],
            'source': 'le:LE1/encl:3/bay:4/port:3:2-c',
            'destination': [
                'le:LE1/encl:2/bay:6/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P9 to P3
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['529-539'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-d',
            'destination': [
                'le:LE1/encl:2/bay:6/port:3:2-d'

            ],
            'description': 'East-West',
        },
        # P13 to P14
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['201-211'],
            'source': 'le:LE1/encl:1/bay:5/port:3:2-c',
            'destination': [
                'le:LE1/encl:3/bay:11/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P13 to P14
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['253-263'],
            'source': 'le:LE1/encl:1/bay:5/port:3:2-d',
            'destination': [
                'le:LE1/encl:3/bay:11/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P14-P22
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['209-221'],
            'source': 'le:LE1/encl:3/bay:11/port:3:2-c',
            'destination': [
                'le:LE1/encl:3/bay:12/port:3:2-c'

            ],
            'description': 'East-West',
        },
        # P14-P22
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['243-253'],
            'source': 'le:LE1/encl:3/bay:11/port:3:2-d',
            'destination': [
                'le:LE1/encl:3/bay:12/port:3:2-d'

            ],
            'description': 'East-West',
        },
        # P16-P21
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['102-123'],
            'source': 'le:LE1/encl:1/bay:9/port:3:1-d',
            'destination': [
                'le:LE1/encl:3/bay:10/port:3:2-d'

            ],
            'description': 'East-West',
        },
        # P21-P16
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['140-161'],
            'source': 'le:LE1/encl:3/bay:10/port:3:1-d',
            'destination': [
                'le:LE1/encl:1/bay:9/port:3:2-d'

            ],
            'description': 'East-West',
        },

    ]
}

# Threshold to make test case PASS/FAIL
threshold = {
    'ping': {
        'numberOfAllowedFailures': 5,
    },
    'fping': {
        'numberOfAllowedFailures': 5,
        'numberOfContinuousAllowedFailures': 5,
    },
}
