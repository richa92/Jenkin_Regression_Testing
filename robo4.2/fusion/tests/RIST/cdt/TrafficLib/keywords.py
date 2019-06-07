"""Module contains keyword for Traffic."""
import os
import re
import json
import traceback
import platform
import subprocess
import tempfile
import requests
from glob import glob1
from vsp import VspLibrary
from ping import PingLibrary
from fping import FpingLibrary
from iperf import IPerfLibrary
from iometer import IOMeterLibrary
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class TrafficLibraryKeywords(object):

    """Module contains keyword for Traffic."""

    def __init__(self):
        """Initialize."""
        class TrafficClass:

            """Traffic class."""
            pass
        self.traffic = TrafficClass()
        self.traffic.data = None
        self.support_files = 'https://rg.us.rdlabs.hpecorp.net/util/traffic_keyword_support_tools/'

    def _get_component_by_uri(self, uri, iput):
        """Private method."""
        for block in iput:
            if block['uri'] == uri:
                return block
        else:
            return False

    def _search_and_set_to_input_dictionary(self, source, key, value):
        """Private method."""
        for server in self.traffic.data['serversAndCredentials']:
            if server == source:
                self.traffic.data['serversAndCredentials'][server][key] = value
                break
        else:
            # BuiltIn().fail("Input data error: Server:'{}' not present in input".format(source))
            # logger.warn("Input data warning: Server:'{}' not present in input".format(source))
            pass

        return True

    def _format_vlan_key(self, vlan_list):
        """Private method."""
        fail = 0
        values = list()

        for val in vlan_list:

            match = re.match(r'\s*([\d]+)\s*(?:\-([\d]+))?\s*', str(val))
            if match:
                if match.group(2) and int(match.group(2)) > int(match.group(1)):
                    values.extend(range(int(match.group(1)), int(match.group(2)) + 1))

                elif match.group(1) and match.group(2) is None:
                    values.extend([int(match.group(1))])

                else:
                    logger.trace("Failed to format vlan value. Given input: {val}, All values: {lis}".format(val=val, lis=vlan_list))
                    fail += 1

            else:
                fail += 1

        if fail > 0:
            logger.trace("Failed to format vlan list. Given input: {}".format(vlan_list))
            return vlan_list
        else:
            return [str(v) for v in values]

    def _download_traffic_support_tool_binaries(self, remote_path, local_path):
        """Private method."""
        logger.trace("_download_traffic_support_tool_binaries entered")

        try:
            if local_path:
                logger.info("Local binary location given, skipping automated download of binaries.")
                return local_path

            if not remote_path:
                raise Exception("Please give valid value for _download_traffic_support_tool_binaries")

            logger.trace("Started downloading support binaries from remote location: {path}".format(path=remote_path))

            temp_location = tempfile.gettempdir()
            folder_name = 'traffic_keyword_support_tools'
            abs_path = os.path.join(temp_location, folder_name)

            if len(glob1(abs_path, '*')) >= 3:   # Minimum three files should be there fping.exe, psexec.exe, fping*.rpm
                logger.trace("Folder exists in test head temporary location, skipping automated download of binaries.")
                return abs_path

            else:
                if not os.path.exists(abs_path):
                    os.mkdir(abs_path)

                # Download file and keep it in this temporary location..
                res = requests.get(remote_path, verify=False)
                logger.trace(res)

                if res.status_code != 200:
                    logger.error("Failed to fetch/download support binaries; Please configure environment proxy and also make sure all management networks are added in exception list in internet settings")
                    raise Exception("Failed to fetch/download support binaries; Please configure environment proxy and also make sure all management networks are added in exception list in internet settings")

                match = list()
                try:
                    # match = re.findall(r'<a\s*href=[\'|\"]\s*(?P<LINK1>\/util\/traffic_keyword_support_tools\/(?P<LINK2>.+?))\s*[\'|\"]\s*>\s*(?P<NAME>.+?)\s*<\/a>', res.content, re.I)
                    link1 = "<a\s*href=[\'|\"]\s*(Fping\.exe)[\'|\"]>\s*Fping\.exe<\/a>"
                    link2 = "<a\s*href=[\'|\"]\s*(Fping-.*\.rpm)[\'|\"]>\s*fping-.*\.rpm<\/a>"
                    link3 = "<a\s*href=[\'|\"]\s*(psExec\.exe)[\'|\"]>\s*psExec\.exe<\/a>"
                    match = re.findall(r".*" + link1 + r".*\n.*" + link2 + r".*\n.*" + link3, res.content, re.I)
                except:
                    raise Exception("Error in regular expression, Please check res content")

                # Download each binary
                for tool_link in match[0]:
                    link = self.support_files + str(tool_link)
                    logger.info("Started downloading support binary: {link}".format(link=link), also_console=True)

                    response = requests.get(link, verify=False)
                    if response.status_code == 200:
                        local_file = os.path.join(abs_path, tool_link)
                        with open(local_file, 'wb') as f:
                            f.write(response.content)
                        del response
                    else:
                        raise Exception("Failed to download binary : {}".format(link))

            return abs_path

        except:
            logger.trace(traceback.format_exc())
            return False

        finally:
            logger.trace("_download_traffic_support_tool_binaries exited")

    def download_support_binaries(self, local_path=None):
        """Checks 'traffic_keyword_support_tools' folder exists in temp folder. If support binary exists then download gets skipped. If not all needed binaries downloaded from self.support_files location.

        Example:
        | Download Support Binaries |.
        """
        remote_path = self.support_files

        tools_location = self._download_traffic_support_tool_binaries(remote_path, local_path)
        if not tools_location:
            raise Exception("Failed to download and configure traffic_support_tool_binaries from '{remote_path}'. Please check reachability and re-run script".format(remote_path=remote_path))

        self.traffic.data['tools'] = tools_location
        return tools_location

    def set_traffic_input(self, iput):
        """ Assign all given traffic data input into this class instance.

        Example:
        | Set Traffic Input | @{iput} |.
        """
        self.traffic.data = iput

        # Format 'vlan' key in entity list
        for index in xrange(len(self.traffic.data['entities'])):
            if 'vlan' in self.traffic.data['entities'][index]:
                self.traffic.data['entities'][index]['vlan'] = self._format_vlan_key(
                    self.traffic.data['entities'][index]['vlan'])

        logger.trace(json.dumps(self.traffic.data['serversAndCredentials'], indent=4, separators=(',', ': ')))

        return True

    def map_ov_data_and_given_data(self, ov_data):
        """ Validate against OneView information and given input

        Example:
        | Map OV Data And Given Data | @{input} |.
        """

        try:
            logger.debug("map_ov_data_and_given_data entered")

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

                            enclosure = self._get_component_by_uri(uri=encl['enclosureUri'], iput=ov_data['enclosures']['members'])
                            en_data['uri'] = enclosure['uri']
                            en_data['name'] = enclosure['name']
                            en_data['serialNumber'] = enclosure['serialNumber']
                            if encl_count == 1:
                                if enclosure['logicalEnclosureUri'] is None:
                                    raise AssertionError(
                                        "To generate traffic OV must have atleast one LE; seems LE not created in OneView")

                                leres = self._get_component_by_uri(uri=enclosure['logicalEnclosureUri'], iput=ov_data['les']['members'])
                                le_data['name'] = leres['name']
                                le_data['uri'] = leres['uri']

                            en_data['deviceBays'] = list()

                            bay_count = 0
                            for dev in enclosure['deviceBays']:
                                bay_count += 1
                                if 'devicePresence' in dev and dev['devicePresence'] == 'Present' and dev['deviceUri'] is not None and dev['deviceUri'].find('server-hardware') > 0:
                                    device_data = dict()
                                    device = self._get_component_by_uri(uri=dev['deviceUri'], iput=ov_data['serverhardwares']['members'])
                                    device_data['name'] = device['name']
                                    device_data['source'] = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=leres['name'],
                                                                                                   encl=encl_count,
                                                                                                   bay=bay_count)

                                    # Next Run: Skip if sever data already collected from OV
                                    if device_data['source'] in self.traffic.data['serversAndCredentials'] and 'connections' in self.traffic.data['serversAndCredentials']:
                                        logger.debug("Server '{}' data already been collected".format(device['source']))
                                        continue

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
                                        profile = self._get_component_by_uri(uri=device['serverProfileUri'], iput=ov_data['serverprofiles']['members'])
                                        device_data['spName'] = profile['name']
                                        device_data['spUri'] = profile['uri']
                                        device_data['sanStorage'] = profile['sanStorage']

                                        device_data['connections'] = list()
                                        for net in profile['connectionSettings']['connections']:
                                            connection = net
                                            if net['networkUri'].find('ethernet-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], iput=ov_data['ethernet_networks']['members'])
                                            elif net['networkUri'].find('fc-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], iput=ov_data['fc_networks']['members'])
                                            elif net['networkUri'].find('fcoe-networks') > 0:
                                                network = self._get_component_by_uri(uri=net['networkUri'], iput=ov_data['fcoe_networks']['members'])
                                            elif net['networkUri'].find('network-sets') > 0:
                                                netset = self._get_component_by_uri(uri=net['networkUri'], iput=ov_data['network_sets']['members'])
                                                network = dict()
                                                network['networks'] = list()
                                                for netUri in netset['networkUris']:
                                                    eth = self._get_component_by_uri(uri=netUri, iput=ov_data['ethernet_networks']['members'])
                                                    if netset['nativeNetworkUri'] == eth['uri']:
                                                        eth['nativeNetwork'] = True
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

            logger.trace(json.dumps(le_map, indent=4, separators=(',', ': ')))
            logger.trace(json.dumps(self.traffic.data, indent=4, separators=(',', ': ')))

            return True

        except:
            BuiltIn().fail(traceback.format_exc())

        finally:
            logger.debug("map_ov_data_and_given_data exited")

    def log_server_interface_data(self, server='all'):
        """ Prints all server Or Guest OS information in to the report.

        Example:
        | Log Server Interface Data | ${server}='all' |.
        """
        try:
            if server == 'all':
                for server, data in self.traffic.data['serversAndCredentials'].iteritems():

                    if 'current_host' in server.lower():
                        continue
                    logger.info(data)
                    logger.info('=' * 50)
                    logger.info("<h2>Interface configuration for server <b>'{}'</b></h2>".format(server), html=True)
                    logger.info(json.dumps(self.traffic.data['serversAndCredentials'][server]['interfaces'], indent=4, separators=(',', ': ')))
                    logger.info('=' * 50)
            else:
                logger.info('=' * 50)
                logger.info("<h2>Interface configuration for server <b>'{}'</b></h2>".format(server), html=True)
                logger.info(json.dumps(self.traffic.data['serversAndCredentials'][server]['interfaces'], indent=4, separators=(',', ': ')))
                logger.info('=' * 50)

        except:
            logger.debug(traceback.format_exc())
            raise AssertionError()

        finally:
            pass

    def check_ip_reachability(self, host):
        """ Returns if IP is reachable from our platform.

        Example:
        | Check Ip Reachability |.
        """
        logger.info("\ncheck_ip_reachability entered..", also_console=1)
        try:
            logger.debug("Trying to ping: '%s'" % host)
            ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
            command = "ping " + ping_str + " " + host
            logger.info(command.split(), also_console=True)
            try:
                output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, universal_newlines=True)
                logger.info(output, also_console=True)
                if 'ttl' in output.lower():
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

    class VspLibraryKeywords(object):

        """Module to deal with Virtual Serial Ports."""

        def __init__(self):
            """Initialize Method."""
            self.vsp = VspLibrary(self.traffic)

        def login_to_server_ilo(self):
            """Not Implemented."""
            pass

        def logout_server_ilo(self):
            """Not Implemented."""
            pass

        def login_to_ilo_vsp_console(self):
            """Not Implemented."""
            pass

        def logout_ilo_vsp_console(self):
            """Not Implemented."""
            pass

        def get_server_ip_addresses(self):
            """Not Implemented."""
            pass

        def get_server_mac_addresses(self):
            """Not Implemented."""
            pass

        def get_server_os_platform(self):
            """Not Implemented."""
            pass

        def run_command_in_server(self):
            """Not Implemented."""
            pass

        def get_all_host_os_interface_configurations(self):
            """
            Get All Host OS Interface Configurations
            If 'reachableIp' and 'platform' not given in server dict, then trying to collect
            data through iLO VSP console. For this user needs to enable VSP property in System Utility and also
            needs to confirm serial console sessio is enabled on the server host OS.
            """
            return self.vsp.get_all_host_os_interface_configurations()

    class PingTrafficLibraryKeywords(object):

        """ This module implements Ping traffic related keywords."""

        def __init__(self):
            """Initialize method."""
            self.ping = PingLibrary(self.traffic)

        def start_ping_traffic(self):
            """
            Connect to the server/GuestOS and run all session in background and STDOUT will be redirectedto an file.
            """
            return self.ping.start_traffic()

        def stop_ping_traffic(self):
            """
            Kills all running fping traffics in the server.
            """

            return self.ping.stop_traffic()

        def analyse_ping_traffic(self, threshold):
            """
            Gets all fping log data and analyse its status. If threshold limit exceeds then fails the test case
            Or else returns True
            | Analyse Ping Traffic | ${threshold} |.
            """
            return self.ping.analyse_traffic(threshold)

        def generate_ping_commands(self):
            """
            Generating command based on given input.
            """
            return self.ping.generate_commands_to_execute()

        def report_ping_traffic_statistics(self):
            """
            Reports all sessions log in JSON format. User also gets output in table format under
            'Rebort Traffic' keyword.
            """

            return self.ping.report_traffic_statistics()

    class FpingTrafficLibraryKeywords(object):

        """ Implements FPing traffic Library keywords."""

        def __init__(self):
            """ Initialize Method."""
            self.fping = FpingLibrary(self.traffic)

        def start_fping_traffic(self):
            """
            Connect to the server/GuestOS and run all session in background and STDOUT will be redirectedto an file.
            """

            return self.fping.start_traffic()

        def stop_fping_traffic(self):
            """
            Kills all running fping traffics in the server.
            """

            return self.fping.stop_traffic()

        def analyse_fping_traffic(self, threshold):
            """
            Gets all fping log data and analyse its status. If threshold limit exceeds then fails the test case
            Or else returns True
            | Analyse Fping Traffic | ${threshold} |.
            """
            return self.fping.analyse_traffic(threshold)

        def generate_fping_commands(self):
            """
            Generating command based on given input.
            """

            return self.fping.generate_commands_to_execute()

        def report_fping_traffic_statistics(self):
            """
            Reports all sessions log in JSON format. User also gets output in table format under
            'Rebort Traffic' keyword.
            """

            return self.fping.report_traffic_statistics()

    class IPerfTrafficLibraryKeywords(object):

        """Implements IPerf Traffic library keywords."""

        def __init__(self):
            """ Initialize Method."""
            self.iperf = IPerfLibrary(self.traffic)

        def start_iperf_traffic(self):
            """Starts the iPerf traffic session."""
            return self.iperf.start_traffic()

        def stop_iperf_traffic(self):
            """Stops the iperf traffic session."""
            return self.iperf.stop_traffic()

        def analyse_iperf_traffic(self):
            """ Analyze the iperf traffic output for failures if any."""
            return self.iperf.analyse_traffic()

        def generate_iperf_commands(self):
            """ Generates the iperf commands to initiate traffic."""
            return self.iperf.generate_commands_to_execute()

    class IOMeterLibraryKeywords(object):

        """ Traffic passing keywords using IOMeter."""

        def __init__(self):
            """ Initialize Method."""
            self.iometer = IOMeterLibrary(self.traffic)

        def start_iometer_traffic(self):
            """Starts the IOMeter Traffic."""
            return self.iometer.start_traffic()

        def stop_iometer_traffic(self):
            """Stops the IOMeter Traffic."""
            return self.iometer.stop_traffic()

        def analyse_iometer_traffic(self):
            """Analyse the IOMeter Traffic result for errors."""
            return self.iometer.analyse_traffic()

        def generate_iometer_commands(self):
            """Generate the IOMeter commands to initiate traffic."""
            return self.iometer.generate_commands_to_execute()
