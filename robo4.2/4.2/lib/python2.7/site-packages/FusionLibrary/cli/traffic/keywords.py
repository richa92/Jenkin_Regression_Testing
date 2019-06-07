import json
import traceback
import platform
import subprocess
from vsp import VspLibrary
from ping import PingLibrary
from iperf import IPerfLibrary
from iometer import IOMeterLibrary
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class TrafficLibraryKeywords(object):

    def __init__(self):
        class TrafficClass:
            pass
        self.traffic = TrafficClass()
        self.traffic.data = None

    def _get_component_by_uri(self, uri, input):
        for block in input:
            if block['uri'] == uri:
                return block
        else:
            return False

    def _search_and_set_to_input_dictionary(self, source, key, value):
        for server in self.traffic.data['serversAndCredentials']:
            if server == source:
                self.traffic.data['serversAndCredentials'][server][key] = value
                break
        else:
            # BuiltIn().fail("Input data error: Server:'{}' not present in input".format(source))
            logger.warn("Input data error: Server:'{}' not present in input".format(source))

        return True

    def map_ov_data_and_given_data(self, input_traffic_data, ov_data):

        self.traffic.data = input_traffic_data
        logger.info(json.dumps(self.traffic.data['serversAndCredentials'], indent=4, separators=(',', ': ')), also_console=True)
        try:
            logger.debug("get_server_profile_information_from_ov entered")

            le_map = list()
            if 'members' in ov_data['ilts'] and len(ov_data['ilts']['members']) > 0:
                for ilt in ov_data['ilts']['members']:
                    le_data = dict()
                    le_data['enclosures'] = list()

                    if 'enclosureMembers' in ilt and len(ilt['enclosureMembers']) > 0:
                        encl_count = 0
                        for encl in ilt['enclosureMembers']:
                            encl_count += 1
                            en_data = dict()

                            enclosure = self._get_component_by_uri(uri=encl['enclosureUri'], input=ov_data['enclosures']['members'])
                            en_data['uri'] = enclosure['uri']
                            en_data['name'] = enclosure['name']
                            en_data['serialNumber'] = enclosure['serialNumber']
                            if encl_count == 1:
                                if enclosure['logicalEnclosureUri'] is None:
                                    raise AssertionError(
                                        "To generate traffic OV must have atleast one LE; seems LE not created in OneView")

                                leres = self._get_component_by_uri(uri=enclosure['logicalEnclosureUri'], input=ov_data['les']['members'])
                                le_data['name'] = leres['name']
                                le_data['uri'] = leres['uri']

                            en_data['deviceBays'] = list()

                            bay_count = 0
                            for dev in enclosure['deviceBays']:
                                bay_count += 1
                                if 'devicePresence' in dev and dev['devicePresence'] == 'Present' and dev['deviceUri'].find('server-hardware') > 0:
                                    device_data = dict()
                                    device = self._get_component_by_uri(uri=dev['deviceUri'], input=ov_data['serverhardwares']['members'])
                                    device_data['name'] = device['name']
                                    device_data['source'] = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=leres['name'],
                                                                                                   encl=encl_count,
                                                                                                   bay=bay_count)
                                    device_data['uri'] = device['uri']
                                    device_data['serialNumber'] = device['serialNumber']
                                    device_data['powerState'] = device['powerState']
                                    device_data['status'] = device['status']
                                    device_data['iLO'] = dict()
                                    device_data['iLO']['mpHostName'] = device['mpHostInfo']['mpHostName']
                                    for address in device['mpHostInfo']['mpIpAddresses']:
                                        if address['type'] == 'LinkLocal':
                                            device_data['iLO']['IPv6'] = address['address']
                                        elif address['type'] in ('DHCP', 'Undefined'):
                                            device_data['iLO']['IPv4'] = address['address']
                                        else:
                                            device_data['iLO']['OtherAddress'] = address['address']

                                    self._search_and_set_to_input_dictionary(device_data['source'], 'iLO', device_data['iLO'])

                                    if device['serverProfileUri'] is not None:
                                        profile = self._get_component_by_uri(uri=device['serverProfileUri'], input=ov_data['serverprofiles']['members'])
                                        device_data['spName'] = profile['name']
                                        device_data['spUri'] = profile['uri']
                                        device_data['sanStorage'] = profile['sanStorage']

                                        device_data['connections'] = list()
                                        for net in profile['connections']:
                                            connection = net
                                            if net['networkUri'].find('ethernet-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], input=ov_data['ethernet_networks']['members'])
                                            elif net['networkUri'].find('fc-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], input=ov_data['fc_networks']['members'])
                                            elif net['networkUri'].find('fcoe-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], input=ov_data['fcoe_networks']['members'])
                                            elif net['networkUri'].find('network-sets') > 0:
                                                netset = self._get_component_by_uri(uri=net['networkUri'], input=ov_data['network_sets']['members'])
                                                network = dict()
                                                network['networks'] = list()
                                                for netUri in netset['networkUris']:
                                                    eth = self._get_component_by_uri(uri=netUri, input=ov_data['ethernet_networks']['members'])
                                                    network['networks'].append(eth)

                                            else:
                                                pass
                                            connection['network'] = network
                                            device_data['connections'].append(connection)

                                        self._search_and_set_to_input_dictionary(device_data['source'], 'connections', device_data['connections'])
                                    else:
                                        device_data['spName'] = None
                                        device_data['spUri'] = None
                                        device_data['sanStorage'] = None
                                        device_data['connections'] = None

                                    en_data['deviceBays'].append(device_data)
                            le_data['enclosures'].append(en_data)
                        le_map.append(le_data)
                    else:
                        logger.warn("There is no enclosure member for '{}'".format(le_data['name']))
            else:
                pass
                raise AssertionError("There is no ILT connection in OneView API responce, Please check")

            logger.info(json.dumps(le_map, indent=4, separators=(',', ': ')))
            logger.info(json.dumps(self.traffic.data, indent=4, separators=(',', ': ')))

            return True

        except:
            BuiltIn().fail(traceback.format_exc())

        finally:
            logger.debug("get_server_profile_information_from_ov exited")

    def log_server_interface_data(self, server='all'):
        try:
            if server == 'all':
                for server, data in self.traffic.data['serversAndCredentials'].iteritems():
                    logger.info("Interface detail of server '{}'".format(server), also_console=True)
                    logger.info(json.dumps(self.traffic.data['serversAndCredentials'][server]['interfaces'], indent=4, separators=(',', ': ')), also_console=True)
            else:
                logger.info("Interface detail of server '{}'".format(server), also_console=True)
                logger.info(json.dumps(self.traffic.data['serversAndCredentials'][server]['interfaces'], indent=4, separators=(',', ': ')), also_console=True)

        except:
            logger.debug(traceback.format_exc())
            raise AssertionError()

        finally:
            pass

    def check_ip_reachability(self, host):
        ''' Returns if IP is reachable from our platform '''
        logger.info("\ncheck_ip_reachability entered..", also_console=1)
        try:
            logger.debug("Trying to ping: '%s'" % host)
            ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
            command = "ping " + ping_str + " " + host
            logger.info(command.split(), also_console=True)
            try:
                output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, universal_newlines=True)
                logger.info(output, also_console=True)
                if 'TTL' in output:
                    return True
                else:
                    return False

            except subprocess.CalledProcessError:
                logger.debug(traceback.format_exc())
                logger.info("Getting CalledProcessError", also_console=True)
                return False
        except:
            logger.debug(traceback.format_exc())
            return False
        finally:
            logger.info("check_ip_reachability exited..\n", also_console=True)

    def find_reachable_ip_for_each_server(self):

        reachable_ip = dict()
        for server, data in self.traffic.data['serversAndCredentials'].iteritems():

            for port, portBlock in data['interfaces'].iteritems():

                flag = 0
                for ipBlock in portBlock['ipAddress']:
                    if 'functionType' in ipBlock and ipBlock['functionType'].lower() == 'fibrechannel':
                        continue
                    else:
                        if self.check_ip_reachability(ipBlock['ip']):
                            flag = 1
                            logger.info("For Server : '{0}' IP: '{1}' is reachable".format(server, ipBlock['ip']), also_console=True)
                            self.traffic.data['serversAndCredentials'][server]['reachable_ip'] = ipBlock['ip']
                            reachable_ip[server] = ipBlock['ip']
                            break
                if flag == 1:
                    break

        return reachable_ip

    def report_traffic(self):
        """
        Finalize all traffic analysis and report status
        :return:
        """

        pass

    class VspLibraryKeywords(object):

        def __init__(self):
            self.vsp = VspLibrary(self.traffic)

        def login_to_server_ilo(self):
            pass

        def logout_server_ilo(self):
            pass

        def login_to_ilo_vsp_console(self):
            pass

        def logout_ilo_vsp_console(self):
            pass

        def get_server_ip_addresses(self):
            pass

        def get_server_mac_addresses(self):
            pass

        def get_server_os_platform(self):
            pass

        def run_command_in_server(self):
            pass

        def get_all_server_interface_through_ilo_vsp_console(self):
            """
            Fetching datas through iLO VSP console

            :return:
            """

            return self.vsp.get_all_server_interface_through_ilo_vsp_console()

    class PingTrafficLibraryKeywords(object):

        def __init__(self):
            self.ping = PingLibrary(self.traffic)

        def start_ping_traffic(self):
            """
            Establishing ping traffic in servers with iLO VSP console
            :return:
            """

            return self.ping.start_traffic()

        def stop_ping_traffic(self):
            """
            Killing all running ping traffics in the server.
            :return:
            """

            return self.ping.stop_traffic()

        def analyse_ping_traffic(self):
            """
            Gets all ping log data and analyse its status
            :return:
            """
            pids = dict()
            pids = self.ping.analyse_traffic()
            return pids

        def generate_ping_commands(self):
            """
            Generating command based on given input or strea
            :return:
            """

            return self.ping.generate_commands_to_execute()

    class IPerfTrafficLibraryKeywords(object):

        def __init__(self):
            self.iperf = IPerfLibrary(self.traffic)

        def start_iperf_traffic(self):
            return self.iperf.start_traffic()

        def stop_iperf_traffic(self):
            return self.iperf.stop_traffic()

        def analyse_iperf_traffic(self):
            return self.iperf.analyse_traffic()

        def generate_iperf_commands(self):
            return self.iperf.generate_commands_to_execute()

    class IOMeterLibraryKeywords(object):

        def __init__(self):
            self.iometer = IOMeterLibrary(self.traffic)

        def start_iometer_traffic(self):
            return self.iometer.start_traffic()

        def stop_iometer_traffic(self):
            return self.iometer.stop_traffic()

        def analyse_iometer_traffic(self):
            return self.iometer.analyse_traffic()

        def generate_iometer_commands(self):
            return self.iometer.generate_commands_to_execute()
