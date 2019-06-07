##############################################################

# These conditions are based on resource manager and are predefined by the users.
# Example below: name- would be the name of OneView's resource, then followed by
# the conditions. For server profile resource, it has a few conditions such as
# applying a profile with no connections(connectionless) takes about 30000 milliseconds(30 seconds)
# to complete, while a profile with firmware takes 400000 milliseconds. Listener will use
# these predefined conditions to determine the asynchronous performance results.

# {name: <resource>, <conditions>: <time_to_complete_async_task>}
##############################################################


conditions = [
    {
        'name': 'server profile',
        'connectionless': 30000,
        'gen8_connections_only': 30000,
        'connections_only': 30000,
        'local_storage': 400000,
        'firmware': 1200000,
        'everything': 1200000,
        'jbod': 1200000,
        'BIOS': 1200000,
        '4eth': 1200000
    },
    {
        'name': 'enclosure',
        'single': 24000
    },
    {
        'name': 'server hardware',
        'single': 6000
    },
    {
        'name': 'ligs',
        'single': 6000
    },
    {
        'name': 'logical enclosure',
        'single': 240000
    }
]
