Execution Procedure OVF1136:

Below are the changes to be done in “ovf_1136_me_data.py” file to execute OVF1136

1 Change the networks, egs and servers tags according to your respective appliance data
Networks:
Iscsi: ISCSI network name
Mgmt: Management network name
private_nw: Private network name added

egs: Enclosure Group Name

servers: server hardware name and server hardware type
        While entering the data in servers field for hardware please make sure to have the same hardware type(SHT) for server1 and server2
        In the servers field for hardware please have a different server hardware type(SHT) for server3 than server1 and server2
        Eg: if SHT is 480 in server1 and server2 please have 660 in server3

2.token_names: This field is mandatory to run token related test case number TC43
The data must be entered according to the hardware you are using, bay no and serverprofile name
Example: “MXQ64801LT1ovf1136_sp.com”
Here: MXQ64801LT is the server name, 1 is the bay number and ovf1136_sp.com is the server profile name used.

3.Create one DP having no NIC CA and use it in the osdps tag2

Make the below changes in "environment_data.py" file of OVF1136
1.Change the networks, egs and server tag according to your respective appliance data
Networks:
Iscsi: ISCSI network name
Mgmt: Management network name
private_nw: Private network name added

egs: Enclosure Group Name

servers: server hardware name and server hardware type
