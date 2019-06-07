*** Settings ***
Documentation       This suite is used to perform E-Fuse action on all blades and interconnects
...                 in a given C7000 enclosure
...
...                 The data variable file should contain a variable 'ENCLOSURES' that holds a
...                 list of dictionaries containing OA information. Example
...
...                     ENCLOSURES = [{ 'oa': '192.168.20.10',
...                                     'user': 'Administrator',
...                                     'password': 'iwf01help'}]
...
...                 Usage:
...                     1. Perform E-fuse using a python data file
...                         pybot -V /path/data.py C7000_efuse_all_blades_and_interconnects.robot
...
...                     2. Perform E-fuse using a yaml data file
...                        pybot -V /path/data.yaml C7000_efuse_all_blades_and_interconnects.robot
...
Library             FusionLibrary
Resource            ../../Resources/api/oa/oa_cli.txt

*** Test Cases ***
Perform E-Fuse
    :FOR    ${enc}    IN    @{ENCLOSURES}
    \    Log    E-fuse is performed on ${enc['oa']}
    \    OA CLI EFUSE All Server Bays    ${enc['oa']}    ${enc['user']}    ${enc['password']}
    \    OA CLI EFUSE All Interconnects    ${enc['oa']}    ${enc['user']}    ${enc['password']}
