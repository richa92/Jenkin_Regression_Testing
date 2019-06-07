from winnt import NULL
from requests.api import patch


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

storage_admin = {'userName': 'storage', 'password': 'storageadmin'}

network_admin = {'userName': 'network', 'password': 'networkadmin'}

server_admin = {'userName': 'server', 'password': 'serveradmin'}

readonly_admin = {'userName': 'readonly', 'password': 'readonly'}

backup_admin = {'userName': 'backup', 'password': 'backupadmin'}


subnet = [{'type': 'Subnet',
           'gateway': '10.10.10.1',
           'networkId': '10.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'testsub.com'},

          {'type': 'Subnet',
           'gateway': '20.20.20.1',
           'networkId': '20.20.20.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test20.com'},

          {'type': 'Subnet',
           'gateway': '30.30.30.1',
           'networkId': '30.30.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test30.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.1',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test40.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '50.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test540.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test543.com'},

          {'type': 'Subnet',
           'gateway': ' ',
           'networkId': '80.80.80.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'NoGateway.com'},

          {'type': 'Subnet',
           'gateway': '90.90.90.1 ',
           'networkId': '90.90.90.0',
           'subnetmask': ' ',
           'dnsServers': [],
           'domain': 'NoSubnet.com'},

          {'type': 'Subnet',
           'gateway': '91.91.91.1',
           'networkId': '91.91.91.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': ''},

          {'type': 'Subnet',
           'gateway': '80.80.80.0',
           'networkId': '127.0.0.1',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Loopback.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '258.890.1.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': 'a.b.c',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '1234.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '10. .10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'test543.com.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.255',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'test543.com.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'testsubEdit.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.2',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'testsubEdit.com'},

          {'type': 'Subnet',
           'gateway': '10.10.10.2',
           'networkId': '10.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['10.10.10.254'],
           'domain': 'EditSubnetWithRange.com'},

          {'type': 'Subnet',
           'gateway': '224.0.0.2',
           'networkId': '224.0.0.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Multicast.com'},

          {'type': 'Subnet',
           'gateway': '1.1.1.1',
           'networkId': '1.1.1.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubnetMaskAllCheck.com'},

          {'type': 'Subnet',
           'gateway': '15.15.15.1',
           'networkId': '15.15.15.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet15.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet1516.com'},

          {'type': 'Subnet',
           'gateway': '127.0.0.1',
           'networkId': '17.17.17.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'GatewayLoopback.com'},

          {'type': 'Subnet',
           'gateway': '19.19.19.1',
           'networkId': '19.19.19.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['19.19.19.2'],
           'domain': 'OneDNS.com'},

          {'type': 'Subnet',
           'gateway': '18.18.18.1',
           'networkId': '18.18.18.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['127.0.0.1'],
           'domain': 'DNSLoopBack.com'},

          {'type': 'Subnet',
           'gateway': '21.21.21.1',
           'networkId': '21.21.21.0',
           'subnetmask': '127.0.0.1',
           'dnsServers': [],
           'domain': 'DNSLoopBack.com'},

          {'type': 'Subnet',
           'gateway': '224.0.0.0',
           'networkId': '24.24.24.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'GatewayMulticast.com'},

          {'type': 'Subnet',
           'gateway': '24.24.24.1',
           'networkId': '24.24.24.0',
           'subnetmask': '224.0.0.0',
           'dnsServers': [],
           'domain': 'SubnetmaskMulticast.com'},

          {'type': 'Subnet',
           'gateway': '24.24.24.1',
           'networkId': '24.24.24.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['224.0.0.0'],
           'domain': 'DNSMulticast.com'},

          {'type': 'Subnet',
           'gateway': '100.100.100.1',
           'networkId': '100.100.100.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['100.100.100.2'],
           'domain': 'AssociateTestCase.com'},

          {'type': 'Subnet',
           'gateway': '200.200.200.1',
           'networkId': '200.200.200.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['200.200.200.2'],
           'domain': 'SubnetAllocateTestCase.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet16.com'},

          {'type': 'Subnet',
           'gateway': '210.210.210.1',
           'networkId': '210.210.210.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['210.210.210.2'],
           'domain': 'Subnet210.com'},

          {'type': 'Subnet',
           'gateway': '125.125.125.1',
           'networkId': '125.125.125.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['125.125.125.2'],
           'domain': 'Subnet125.com'},

          {'type': 'Subnet',
           'gateway': '126.126.126.1',
           'networkId': '126.126.126.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['126.126.126.2'],
           'domain': 'Subnet126.com'},

          {'type': 'Subnet',
           'gateway': '5.5.5.1',
           'networkId': '5.5.5.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['5.5.5.2'],
           'domain': 'SubnetDiffUsers.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.3',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['40.40.40.4'],
           'domain': 'SubnetServerUsersEdit.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.7',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['40.40.40.8'],
           'domain': 'SubnetNetworkUsersEdit.com'},

          {'type': 'Subnet',
           'gateway': '50.40.50.1',
           'networkId': '50.40.50.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.50.2',
               '50.40.50.3',
               '50.40.50.4'],
           'domain': 'TestEditSubAssociated.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.16.0',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.65',
           'networkId': '16.16.16.64',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.193',
           'networkId': '16.16.16.192',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '50.40.41.1',
           'networkId': '50.40.41.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test5041.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.193',
           'networkId': '192.168.1.192',
           'subnetmask': '255.255.255.224',
           'dnsServers': [],
           'domain': 'vlsm1.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.1',
           'networkId': '192.168.1.0',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'vlsm2.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.129',
           'networkId': '192.168.1.128',
           'subnetmask': '255.255.255.192',
           'dnsServers': [],
           'domain': 'vlsm3.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.225',
           'networkId': '192.168.1.224',
           'subnetmask': '255.255.255.252',
           'dnsServers': [],
           'domain': 'vlsm4.com'},

          {'type': 'Subnet',
           'gateway': '150.150.150.1',
           'networkId': '150.150.150.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet150.com'},

          {'type': 'Subnet',
           'gateway': '60.60.60.1',
           'networkId': '60.60.60.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubAllocateLE.com'},

          {'type': 'Subnet',
           'gateway': '61.61.61.1',
           'networkId': '61.61.61.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubAllocateLE2.com'},

          {'type': 'Subnet',
           'gateway': '130.130.130.1',
           'networkId': '130.130.130.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet130.com'},

          {'type': 'Subnet',
           'gateway': '131.131.131.1',
           'networkId': '131.131.131.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain':'`~!@#$%^&*()_+={}|[]\:";<>?,/'},

          {'type': 'Subnet',
           'gateway': '132.132.132.1',
           'networkId': '132.132.132.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Check-name.com'},

          {'type': 'Subnet',
           'gateway': '175.175.175.1',
           'networkId': '175.175.175.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubnetPatch.com'}

          ]

edit_subnet = [{'type': 'Subnet',
                'gateway': '50.40.30.1',
                'networkId': '50.40.30.0',
                'subnetmask': '255.255.255.0',
                'dnsServers': [
                    '50.40.40.2',
                        '50.40.40.3',
                        '50.40.40.4'],
                'domain': 'testsubEdit.com'},

               {'type': 'Subnet',
                'gateway': '20.20.20.1',
                'networkId': '20.20.20.0',
                'subnetmask': '255.255.255.0',
                'dnsServers': [],
                'domain': 'test20.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.128',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.224',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.240',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.248',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.252',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.192',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'}
               ]

range_enable = [{'type': 'Range',
                 'enabled': 'true'}
                ]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}
                 ]

ipv4ranges = [{'type': 'Range',
               'startAddress': '10.10.11.2',
               'endAddress': '10.10.11.100',
               'name': 'test',
               'subnetUri': ' '},

              {'type': 'Range',
               'startAddress': '10.10.10.3',
               'endAddress': '10.10.10.252',
               'name': 'test1',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '10.10.11.101',
               'endAddress': '10.10.11.200',
               'name': 'test2',
               'subnetUri': ' '},

              {'type': 'Range',
               'endAddress': '30.30.30.200',
               'startAddress': '30.30.30.2',
               'name': 'test13',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.2',
               'startAddress': '30.30.30.254',
               'name': 'OverLapRange',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.5',
               'name': 'SameSubnetIdStartAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '300.3O..5',
               'name': 'InvalidEndAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '127.0.0.1',
               'name': 'LoopbackEndAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.2',
               'name': 'LoopbackStartAddress',
               'startAddress': '127.0.0.1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': ' ',
               'name': 'EmptyAddress',
               'startAddress': ' ',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.2',
               'endAddress': '15.15.15.100',
               'name': 'test151',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.101',
               'endAddress': '15.15.15.200',
               'name': 'test152',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.201',
               'endAddress': '15.15.15.254',
               'name': 'test153',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test1330',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test1330',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '100.100.100.100',
               'startAddress': '100.100.100.5',
               'name': 'Range100AssiciateTestCase',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '200.200.200.100',
               'startAddress': '200.200.200.5',
               'name': 'RangeAllocateTestCase',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.201',
               'endAddress': '15.15.15.220',
               'name': 'test15R3',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '16.16.16.201',
               'endAddress': '16.16.16.220',
               'name': 'Range16',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '20.20.20.20',
               'endAddress': '20.20.20.30',
               'name': 'RangeSub20',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '210.210.210.10',
               'endAddress': '210.210.210.20',
               'name': 'RangeSub210',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '125.125.125.10',
               'endAddress': '125.125.125.20',
               'name': 'Range125A',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '40.40.40.40',
               'endAddress': '40.40.40.50',
               'name': 'Range40Users',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.30.30',
               'endAddress': '50.40.30.40',
               'name': 'Range1Sub504030',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.30.50',
               'endAddress': '50.40.30.60',
               'name': 'Range2Sub504030',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.40.10',
               'endAddress': '50.40.40.20',
               'name': 'Range1Sub504040',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.41.10',
               'endAddress': '50.40.41.20',
               'name': 'Range1Sub504041',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test13Duplicate',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.222',
               'startAddress': '192.168.1.194',
               'name': 'RangeVlsm1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.3',
               'startAddress': '192.168.1.2',
               'name': 'RangeVlsm2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.190',
               'startAddress': '192.168.1.130',
               'name': 'RangeVlsm3',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.226',
               'startAddress': '192.168.1.226',
               'name': 'RangeVlsm4',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.252',
               'startAddress': '30.30.30.252',
               'name': 'RangeSameFirstEndIp',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.252',
               'startAddress': '30.30.30.250',
               'name': 'RangeReAssignIpAfterDelete',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '150.150.150.50',
               'startAddress': '150.150.150.40',
               'name': 'Range150Allocate',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '60.60.60.60',
               'startAddress': '60.60.60.10',
               'name': 'RangeAllocateLE',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '61.61.61.60',
               'startAddress': '61.61.61.10',
               'name': 'RangeAllocateLE2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.10',
               'startAddress': '130.130.130.4',
               'name': '33character33character33character',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.10',
               'startAddress': '130.130.130.4',
               'name': '32character32character32characte',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.40',
               'startAddress': '224.130.130.30',
               'name': 'RangeFirstMulticast',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '224.130.130.50',
               'startAddress': '130.130.130.20',
               'name': 'RangeLastMulticast',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '1.1.1.20',
               'startAddress': '1.1.1.10',
               'name': 'Range1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '1.1.1.30',
               'startAddress': '1.1.1.25',
               'name': 'Range2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '175.175.175.20',
               'startAddress': '175.175.175.10',
               'name': 'RangePatch',
               'subnetUri': ''}

              ]

ipv4ranges_edit = [

    {'type': 'Range',
     'endAddress': '30.30.30.254',
     'startAddress': '30.30.30.251',
     'name': 'test13',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.39',
     'name': 'Range150ExpandFirstIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.39',
     'name': 'Range150ExpandLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.52',
     'startAddress': '150.150.150.38',
     'name': 'Range150ExpandFirstLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.52',
     'startAddress': '150.150.150.39',
     'name': 'Range150ShrinkFirstIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.39',
     'name': 'Range150ShrinkLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.40',
     'name': 'Range150ShrinkFirstLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.41',
     'name': 'Range150ShrinkExpandIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.40',
     'name': 'Range150Allocate',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.40',
     'name': 'Range150ExpandLastIpAllocated',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.41',
     'name': 'Range150ShrinkFirstIpAllocated',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.56',
     'startAddress': '150.150.150.40',
     'name': 'Range150DisExpLastIpAllocat',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '1.1.1.30',
     'startAddress': '1.1.1.10',
     'name': 'Range1',
     'subnetUri': ''}

]

Ethernet_network_1 = [
    {'name': 'eth-100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},

    {'vlanId': '17',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET30',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '10',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET10',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '100',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET100',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '200',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetAssociateSub200',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'Network16A',
     'type': 'ethernet-networkV300',
     'vlanId': '102',
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'BlankSubnetUri',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'NoSubnetSelection',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '15',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK15',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'NETWORK40',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '16',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK16',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '20',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK20',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NoUri',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': '',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '210',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK210',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '125',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK125',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '126',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK126Untagged',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub40',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '30',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504030',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504040',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '41',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504041',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '150',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK150',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'NetworkPatch',
     'type': 'ethernet-networkV300',
     'vlanId': '75',
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}

]

edit_network = [
    {'vlanId': '125',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK125',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}

]

bulk_networks_dict = {
    'vlanIdRange': '5,6,7,8',
    'namePrefix': 'bulk',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-network',
    'bandwidth': {
        'maximumBandwidth': 20000,
        'typicalBandwidth': 2500}
}
network_sets = [
    {'name': 'NetSet100', 'type': 'network-setV300', 'networkUris': ['NET100'], 'nativeNetworkUri': None},
    {'name': 'NetSetHappy', 'type': 'network-setV300', 'networkUris': ['nethappy'], 'nativeNetworkUri': None},
    {'name': 'NetSet15', 'type': 'network-setV300', 'networkUris': ['NETWORK15'], 'nativeNetworkUri': None},
    {'name': 'NetSet4015', 'type': 'network-setV300', 'networkUris': ['NETWORK15', 'NETWORK40'], 'nativeNetworkUri': None},
    {'name': 'NetSet16', 'type': 'network-setV300', 'networkUris': ['NETWORK16'], 'nativeNetworkUri': None},
    {'name': 'NetSet16A', 'type': 'network-setV300', 'networkUris': [], 'nativeNetworkUri': None}
]

network_sets_working = [
    {'name': 'NetSet100', 'type': 'network-setV300', 'networkUris': ['NET100'], 'nativeNetworkUri': None},
    {'name': 'NetSetHappy', 'type': 'network-setV300', 'networkUris': ['nethappy'], 'nativeNetworkUri': None}
]
Ethernet_Network_Set = [{
                        'name': 'NetSet100',
                        'networkUris': ['/rest/ethernet-networks/43f49f6f-f31d-4ca1-b240-9ea0e0a25c3f'],
                        'connectionTemplateUri':None,
                        'type':'network-setV300',
                        'nativeNetworkUri':None},

                        {
                        'name': 'NetSet200',
                        'networkUris': '',
                        'connectionTemplateUri': None,
                        'type': 'network-setV300',
                        'nativeNetworkUri': None}
                        ]
subnet_allocate = [
    {'idList': ['200.200.200.11']},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']},
    {'idList': ['210.210.210.200']},
    {'idList': ['210.210.210.10', '210.210.210.11']},
    {'idList': ['210.210.210.255']},
    {'idList': ['210.210.210.2']},
    {'idList': ['210.210.210.1']},
    {'idList': ['210.210.210.10', '210.210.210.12', '210.210.210.15', '210.210.210.19']},
    {'idList': ['50.40.30.30']},
    {'idList': ['50.40.40.15']},
    {'idList': ['50.40.41.15']},
    {'idList': ['50.40.40.16', '50.40.40.17', '50.40.40.19']},
    {'idList': ['50.40.40.12', '50.40.40.16', '50.40.40.17', '50.41.41.18', '50.40.40.19']},
    {'idList': ['550.A.30.30']},
    {'idList': ['50.40.40.10', '50.40.40.11', '50.40.40.12', '50.40.40.13', '50.40.40.14', '50.40.40.15', '50.40.40.16', '50.40.40.17', '50.40.40.18', '50.40.40.19', '50.40.40.20']},
    {'idList': ['50.40.41.10', '50.40.41.11', '50.40.41.12', '50.40.41.13', '50.40.41.14', '50.40.41.15', '50.40.41.16', '50.40.41.17', '50.40.41.18', '50.40.41.19', '50.40.41.20']},
    {'idList': ['150.150.150.40', '150.150.150.41', '150.150.150.42', '150.150.150.43', '150.150.150.44', '150.150.150.45']},
    {'idList': ['50.40.40.12', '50.40.40.16', '50.40.40.17', '50.40.40.19']}
]

subnet_collect = [
    {'idList': ['200.200.200.11']},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']},
    {'idList': ['210.210.210.10', '210.210.210.11', '210.210.210.12', '210.210.210.13', '210.210.210.14', '210.210.210.15', '210.210.210.16', '210.210.210.17', '210.210.210.18', '210.210.210.19', '210.210.210.20']}
]

subnet_allocate_count = [
    {'count': 6},
    {'count': 15},
    {'count': 1},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']}

]

lig_tbird_2enc = {"type": "logical-interconnect-groupV300",
                  "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "lig_tbird21",
                  "interconnectMapTemplate":
                  {"interconnectMapEntryTemplates": [
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 2},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 2}]},
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1, 2],
                  "interconnectBaySet": "3",
                  "redundancyType": "HighlyAvailable",
                  "internalNetworkUris": [],
                  "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                  "qosConfiguration": None,
                  "uplinkSets": []
                  }

lig_tbird_1enc_dcs = {"type": "logical-interconnect-groupV300",
                      "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                      "description": None,
                      "name": "lig_1_Encl_dcs",
                      "interconnectMapTemplate":
                      {"interconnectMapEntryTemplates": [
                          {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                          {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                      "enclosureType": "SY12000",
                      "enclosureIndexes": [1],
                      "interconnectBaySet": "3",
                      "redundancyType": "Redundant",
                      "internalNetworkUris": [],
                      "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                      "qosConfiguration": None,
                      "uplinkSets": []
                      }


lig_demo_3enc = {"type": "logical-interconnect-groupV300",
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                 "description": None,
                 "name": "lig_demo_pools",
                 "interconnectMapTemplate":
                 {"interconnectMapEntryTemplates": [
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 2},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 1},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 2},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 3}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 3},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 3}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 3}]},

                 "enclosureType": "SY12000",
                 "enclosureIndexes": [1, 2, 3],
                 "interconnectBaySet": "3",
                 "redundancyType": "HighlyAvailable",
                 "internalNetworkUris": [],
                 "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                 "qosConfiguration": None,
                 "uplinkSets": []
                 }


les_potash = {'name': 'LE_POTASH',
              # 'enclosureUris': ['ENC:HD345r'],   #REAL
              'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102', 'ENC:0000A66103'],  # DCS
              'enclosureGroupUri': 'EG:enc_groups_potash',
              'firmwareBaselineUri': None,
              'forceInstallFirmware': False
              }


les_potash_1enc = {'name': 'LE_POTASH',
                   # 'enclosureUris': ['ENC:HD345r'],   #REAL
                   'enclosureUris': ['ENC:0000A66101'],  # DCS
                   'enclosureGroupUri': 'EG:enc_groups_potash',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

les_potash_2enc = {'name': 'LE_POTASH',
                   'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102'],  # REAL
                   'enclosureGroupUri': 'EG:enc_groups_potash',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

les_demo_3enc = {'name': 'LE_DEMO',
                 'enclosureUris': ['ENC:FVTCRMENC1', 'ENC:FVTCRMENC2', 'ENC:FVTCRMENC3'],  # DEMO REAL
                 'enclosureGroupUri': 'EG:enc_groups_demo',
                 'firmwareBaselineUri': None,
                 'forceInstallFirmware': False
                 }

les_1enc = {'name': 'LE_1_Encl',
            'enclosureUris': ['ENC:0000A66101'],  # 1 ENCL
            'enclosureGroupUri': 'EG:enc_groups_1_Encl',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

enc_groups_potash_1enc1 = [{'name': 'enc_groups_1_Encl',
                            'type': 'EnclosureGroupV300',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"}
                             ]}]

enc_groups_1enc_2 = [{'name': 'enc_groups_1_Encl_2',
                      'type': 'EnclosureGroupV300',
                      'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                      'stackingMode': 'Enclosure',
                      'ipAddressingMode': 'IpPool',
                      'ipRangeUris': '',
                      'interconnectBayMappingCount': 0,
                      'enclosureCount': 1,
                      'configurationScript': None,
                      'interconnectBayMappings':
                      [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                       {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"},
                          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"}
                       ]}]

enc_groups_potash_2enc1 = [{'name': 'enc_groups_potash',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_potash_2enc2 = [{'name': 'enc_groups_potash_2',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_demo_3enc = [{'name': 'enc_groups_demo',
                         'type': 'EnclosureGroupV300',
                         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                         'stackingMode': 'Enclosure',
                         'ipAddressingMode': 'IpPool',
                         'ipRangeUris': '',
                         'interconnectBayMappingCount': 0,
                         'enclosureCount': 3,
                         'configurationScript': None,
                         'interconnectBayMappings':
                         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                          ]}]

enc_groups_demo_3enc2 = [{'name': 'enc_groups_demo_temp',
                          'type': 'EnclosureGroupV300',
                          'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                          'stackingMode': 'Enclosure',
                          'ipAddressingMode': 'IpPool',
                          'ipRangeUris': '',
                          'interconnectBayMappingCount': 0,
                          'enclosureCount': 3,
                          'configurationScript': None,
                          'interconnectBayMappings':
                          [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                           ]}]

enc_groups_demo_3enc3 = [{'name': 'enc_groups_demo_temp2',
                          'type': 'EnclosureGroupV300',
                          'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                          'stackingMode': 'Enclosure',
                          'ipAddressingMode': 'IpPool',
                          'ipRangeUris': '',
                          'interconnectBayMappingCount': 0,
                          'enclosureCount': 3,
                          'configurationScript': None,
                          'interconnectBayMappings':
                          [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                           ]}]

enc_groups_potash_2enc3 = [{'name': 'enc_groups_potash_3',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_patch = [{'name': 'enc_groups_patch',
                     'type': 'EnclosureGroupV400',
                     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'External',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 3,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                      ]}]


lig_tbird_1enc_HW_2_potash = {"type": "logical-interconnect-groupV300",
                              "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": "lig_1_Encl_2_potash",
                              "interconnectMapTemplate":
                              {"interconnectMapEntryTemplates": [
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [1],
                              "interconnectBaySet": "3",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                              "qosConfiguration": None,
                              "uplinkSets": []
                              }

enc_groups_1enc_2potash = [{'name': 'enc_groups_2_Potash',
                            'type': 'EnclosureGroupV300',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                             ]}]

enc_groups_1enc_2potash_temp = [{'name': 'enc_groups_2_Potash_temp',
                                 'type': 'EnclosureGroupV300',
                                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                 'stackingMode': 'Enclosure',
                                 'ipAddressingMode': 'IpPool',
                                 'ipRangeUris': '',
                                 'interconnectBayMappingCount': 0,
                                 'enclosureCount': 1,
                                 'configurationScript': None,
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                  ]}]

enc_groups_1enc_2potash_temp2 = [{'name': 'enc_groups_2_Potash_temp2',
                                  'type': 'EnclosureGroupV300',
                                  'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                  'stackingMode': 'Enclosure',
                                  'ipAddressingMode': 'IpPool',
                                  'ipRangeUris': '',
                                  'interconnectBayMappingCount': 0,
                                  'enclosureCount': 1,
                                  'configurationScript': None,
                                  'interconnectBayMappings':
                                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                   ]}]

les_1enc_2potash = {'name': 'LE_2_Potash',
                    'enclosureUris': ['ENC:EM1FFFF600'],  # REAL
                    'enclosureGroupUri': 'EG:enc_groups_2_Potash',
                    'firmwareBaselineUri': None,
                    'forceInstallFirmware': False
                    }

patch_add = [
    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'NetworkPatch',
                    'resourceCategory': 'ethernet-networks',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },
    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [],
        'eTag':''
    },

    {
        'operations': [
            {
                'op': ' ',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'WRONG',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    }
]

patch_remove = [
    {
        'operations': [
            {
                'op': 'remove',
                'path': '/associatedResources/0'
            }
        ],
        'eTag': ''
    }
]

lig_tbird_1enc_HW_2_potash = {"type": "logical-interconnect-groupV300",
                              "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": "lig_1_Encl_2_potash",
                              "interconnectMapTemplate":
                              {"interconnectMapEntryTemplates": [
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [1],
                              "interconnectBaySet": "3",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                              "qosConfiguration": None,
                              "uplinkSets": []
                              }

enc_groups_1enc_2potash = [{'name': 'enc_groups_2_Potash',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                             ]}]

enc_groups_1enc_2potash_temp = [{'name': 'enc_groups_2_Potash_temp',
                                 'type': 'EnclosureGroupV400',
                                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                 'stackingMode': 'Enclosure',
                                 'ipAddressingMode': 'IpPool',
                                 'ipRangeUris': '',
                                 'interconnectBayMappingCount': 0,
                                 'enclosureCount': 1,
                                 'configurationScript': None,
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                  ]}]

enc_groups_1enc_2potash_temp2 = [{'name': 'enc_groups_2_Potash_temp2',
                                  'type': 'EnclosureGroupV400',
                                  'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                  'stackingMode': 'Enclosure',
                                  'ipAddressingMode': 'IpPool',
                                  'ipRangeUris': '',
                                  'interconnectBayMappingCount': 0,
                                  'enclosureCount': 1,
                                  'configurationScript': None,
                                  'interconnectBayMappings':
                                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                   ]}]

les_1enc_2potash = {'name': 'LE_2_Potash',
                    'enclosureUris': ['ENC:EM1FFFF600'],  # REAL
                    'enclosureGroupUri': 'EG:enc_groups_2_Potash',
                    'firmwareBaselineUri': None,
                    'forceInstallFirmware': False
                    }


users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'software', 'password': 'softwareadmin', 'fullName': 'Software', 'roles': ['Software administrator'], 'emailAddress': 'software@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]
