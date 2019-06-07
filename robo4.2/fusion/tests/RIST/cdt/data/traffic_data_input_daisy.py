# Appliance/OneView IPv4 & its login credentials
oneview = {
    'ip': '16.114.208.62',
    'cred': {
        'userName': 'Administrator',
        'password': 'hpvse123',
    },
}

# Server/GuestOS reachable IP & other login input
serversAndCredentials = {
    'le:LE1/encl:1/bay:3': {  # P2
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.33',
        'platform': 'Linux',
    },
    'le:LE1/encl:1/bay:5': {  # P13
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.28',
        'platform': 'Linux',
    },
    'le:LE1/encl:2/bay:4': {  # P14
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.54',
        'platform': 'Linux',
    },
    'le:LE1/encl:2/bay:5': {  # P6
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.3',
        'platform': 'Linux',
    },
    # 'le:LE1/encl:1/bay:4': { #P3
    # 'osUserLoginCredentials': {
    # 'user_name': 'root',
    # 'password': 'HPvse123$'
    # },
    # 'reachableIp': '10.100.0.14',
    # 'platform': 'Linux',
    # },
    'le:LE1/encl:2/bay:3': {  # P5
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.2',
        'platform': 'Linux',
    },
    'le:LE1/encl:3/bay:4': {  # P9
        'osUserLoginCredentials': {
            'user_name': 'root',
            'password': 'HPvse123$'
        },
        'reachableIp': '10.100.0.17',
        'platform': 'Linux',
    },
}

# Extra session options like interval, size, ttl
trafficProfileOptionsForFping = {
    'trafficgen': 'fping',
    'interval': 100,
}
trafficProfileOptionsForPing = {
    'trafficgen': 'ping',
}

# Traffic session as entity input
input = {
    'fusion': oneview,
    'serversAndCredentials': serversAndCredentials,
    'entities': [

        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['100'],
            'source': 'le:LE1/encl:1/bay:3/port:3:1-a',
            'destination': [
                '10.100.0.24',

            ],
            'description': 'North-South',
        },

        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['100'],
            'source': 'le:LE1/encl:2/bay:4/port:3:1-a',
            'destination': [
                '10.100.0.24',
            ],
            'description': 'North-South',
        },

        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['100'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-a',
            'destination': [
                '10.100.0.24',

            ],
            'description': 'North-South',
        },
        # Starting from here P2 to P13
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['162-165'],
            'source': 'le:LE1/encl:1/bay:3/port:3:1-b',
            'destination': [
                'le:LE1/encl:1/bay:5/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P13 to P2
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['166-168'],
            'source': 'le:LE1/encl:1/bay:5/port:3:1-c',
            'destination': [
                'le:LE1/encl:1/bay:3/port:3:1-b'

            ],
            'description': 'East-West',
        },
        # P14 to P6
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['169-172'],
            'source': 'le:LE1/encl:2/bay:4/port:3:1-c',
            'destination': [
                'le:LE1/encl:2/bay:5/port:3:1-b'

            ],
            'description': 'East-West',
        },
        # P6 to P14
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['173-175'],
            'source': 'le:LE1/encl:2/bay:5/port:3:1-b',
            'destination': [
                'le:LE1/encl:2/bay:4/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # p13-P6
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['215-218'],
            'source': 'le:LE1/encl:1/bay:5/port:3:1-c',
            'destination': [
                'le:LE1/encl:2/bay:5/port:3:1-b'

            ],
            'description': 'East-West',
        },
        # p6-P13
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['219-221'],
            'source': 'le:LE1/encl:2/bay:5/port:3:1-b',
            'destination': [
                'le:LE1/encl:1/bay:5/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P2-P6
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['223-225'],
            'source': 'le:LE1/encl:1/bay:3/port:3:1-c',
            'destination': [
                'le:LE1/encl:2/bay:5/port:3:1-c'
            ],
            'description': 'East-West',
        },
        # P6-P2
        {
            'profile': trafficProfileOptionsForPing,
            'vlan': ['226-229'],
            'source': 'le:LE1/encl:2/bay:5/port:3:1-c',
            'destination': [
                'le:LE1/encl:1/bay:3/port:3:1-c'
            ],
            'description': 'East-West',
        },
        # P13 to P14
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['250-253'],
            'source': 'le:LE1/encl:1/bay:5/port:3:1-d',
            'destination': [
                'le:LE1/encl:2/bay:4/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P14 to P13
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['254-256'],
            'source': 'le:LE1/encl:2/bay:4/port:3:1-d',
            'destination': [
                'le:LE1/encl:1/bay:5/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P14 to P6
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['262-265'],
            'source': 'le:LE1/encl:2/bay:4/port:3:1-d',
            'destination': [
                'le:LE1/encl:2/bay:5/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P6 to P14
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['266-268'],
            'source': 'le:LE1/encl:2/bay:5/port:3:1-c',
            'destination': [
                'le:LE1/encl:2/bay:4/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P6 to P2
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['284-287'],
            'source': 'le:LE1/encl:2/bay:5/port:3:1-d',
            'destination': [
                'le:LE1/encl:1/bay:3/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P2 to P6
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['288-290'],
            'source': 'le:LE1/encl:1/bay:3/port:3:1-d',
            'destination': [
                'le:LE1/encl:2/bay:5/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P5-P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['460-462'],
            'source': 'le:LE1/encl:2/bay:3/port:3:1-b',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:1-b'

            ],
            'description': 'East-West',
        },
        # P9-P5
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['463-466'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-b',
            'destination': [
                'le:LE1/encl:2/bay:3/port:3:1-b'

            ],
            'description': 'East-West',
        },
        # P3-P5
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['467-470'],
        # 'source': 'le:LE1/encl:1/bay:4/port:3:1-c',
        # 'destination': [
        # 'le:LE1/encl:2/bay:3/port:3:1-c'

        # ],
        # 'description': 'East-West',
        # },
        # P5-P3
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['471-473'],
        # 'source': 'le:LE1/encl:2/bay:3/port:3:1-c',
        # 'destination': [
        # 'le:LE1/encl:1/bay:4/port:3:1-c'

        # ],
        # 'description': 'East-West',
        # },
        # P9-P3
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['496-499'],
        # 'source': 'le:LE1/encl:3/bay:4/port:3:1-c',
        # 'destination': [
        # 'le:LE1/encl:1/bay:4/port:3:1-c'

        # ],
        # 'description': 'East-West',
        # },
        # P3-P9
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['500-502'],
        # 'source': 'le:LE1/encl:1/bay:4/port:3:1-c',
        # 'destination': [
        # 'le:LE1/encl:3/bay:4/port:3:1-c'

        # ],
        # 'description': 'East-West',
        # },
        # P5-P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['521-524'],
            'source': 'le:LE1/encl:2/bay:3/port:3:1-c',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P9-P5
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['525-527'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-c',
            'destination': [
                'le:LE1/encl:2/bay:3/port:3:1-c'

            ],
            'description': 'East-West',
        },
        # P3-P5
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['528-530'],
        # 'source': 'le:LE1/encl:1/bay:4/port:3:1-d',
        # 'destination': [
        # 'le:LE1/encl:2/bay:3/port:3:1-d'

        # ],
        # 'description': 'East-West',
        # },
        # P5-P3
        # {
        # 'profile': trafficProfileOptionsForPing,
        # 'vlan': ['531-535'],
        # 'source': 'le:LE1/encl:2/bay:3/port:3:1-d',
        # 'destination': [
        # 'le:LE1/encl:1/bay:4/port:3:1-d'

        # ],
        # 'description': 'East-West',
        # },
        # P5-P9
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['582-584'],
            'source': 'le:LE1/encl:2/bay:3/port:3:1-d',
            'destination': [
                'le:LE1/encl:3/bay:4/port:3:1-d'

            ],
            'description': 'East-West',
        },
        # P9-P5
        {
            'profile': trafficProfileOptionsForFping,
            'vlan': ['585-588'],
            'source': 'le:LE1/encl:3/bay:4/port:3:1-d',
            'destination': [
                'le:LE1/encl:2/bay:3/port:3:1-d'

            ],
            'description': 'East-West',
        },

    ]
}

# Threshold to make test case PASS/FAIL
threshold = {
    'ping': {
        'numberOfAllowedFailures': 40,
    },
    'fping': {
        'numberOfAllowedFailures': 40,
        'numberOfContinuousAllowedFailures': 30,
    },
}
