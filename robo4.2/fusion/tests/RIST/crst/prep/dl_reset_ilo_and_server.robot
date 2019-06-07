*** Settings ***
Documentation       This suite is used to simulate E-Fuse action on a rack server. The actions
...                 performed on the target are
...
...                 - Reset of the iLO subsystem
...                 - Power On the server
...                 - Power Off the server
...
...                 This utility supports running against a list of servers. The variable file can
...                 of type .py or .yaml.
...
...                 In case of .py, below is an example
...
...                 data.py
...
...                     servers = [{ 'host': '192.168.20.10', 'user': 'Administrator', 'password': 'iwf01help'},
...                                { 'host': '192.168.30.10', 'user': 'Administrator', 'password': 'iwf01help'}]
...
...                 data.yaml
...
...                     # List of rack servers
...                     servers:
...                       - host: '192.168.20.10'
...                         user: 'Administrator'
...                         password: 'iwf01help'
...                       - host: '192.168.30.10'
...                         user: 'User1'
...                         password: 'iwf01help'
...
...                 Script Usage:
...
...                 - pybot -V /path/to/data.py -L:TRACE dl_reset_ilo_and_server.robot
...                 - pybot -V /path/to/data.yaml -L:TRACE dl_reset_ilo_and_server.robot
...
Library             RoboGalaxyLibrary

*** Test Cases ***
Reset iLO and Server
    :FOR    ${server}    IN    @{server_hardware}
    \    Log    \nPerforming reset of ${server['hostname']}   console=True
    \    DL ILO API Login        ${server['hostname']}    ${server['username']}    ${server['password']}
    \    DL ILO API Power Off Server    ${True}
    \    DL ILO API Reset iLO Manager
    \    DL ILO API Return After POST Complete
    \    DL ILO API Power Off Server    ${True}
    \    DL ILO API Logout
