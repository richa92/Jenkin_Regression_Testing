To run the automated script for the IGMP Snooping OVF2496 Feature. Please follow the below prerequisites

================
Prerequisites :
================

1.  Keep the Multicast tools in the Server Directory : C:\Mulitcast\mk_mc
2.  Keep the Windump in the blade serers directory : C:\Multicast\mk_mc
3.  In the Jumpstation / TCS configure the multicast router
4.  Keep the Mulitcast Sender in the Jumpstation / TCS directory C:\Multicast\mcast\bin\
5.  Configure the profile connection adapter name in the blade servers as Ethernet1, Ethernet2 and Ethernet3
6.  Disable the Firewall in the blade servers and jumpstations.
7.  Install PSEXEC tool in the TCS / Jumpstation and give the pathe of the PSexec in Path environment variable.
8.  Place the bat file to get the interfaces UUID in the blade server C:\Multicast\mk_mc
9.  Make sure the ILO and blade passwords are correct in the data variables.py
10. In the DL or TCS / Jumpstation make sure the route is configured only for the vlan 10 or specific vlan which is used to send the mulitcast traffic.
