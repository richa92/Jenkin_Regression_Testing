Execution Procedure OVF1134:

Below are the changes to be done in “environment_data.py file” file to execute OVF1134

1. Change the networks, egs and servers tags according to your respective appliance data

Networks:
Iscsi: ISCSI network name
Mgmt: Management network name
private_nw: Private network name added

egs: Enclosure Group Name
le: Logical Enclosure name

servers: server hardware name and server hardware type

Here: 1st and 2nd are different server hardware of same SHT from same enclosure
      3rd server hardware of same SHT from different enclosure in same LE
      Last server hardware is of different SHT in same LE
