"""
helper.py

Helper functions
"""
import sys
import os
import re
import webbrowser
from pprint import pprint
from random import shuffle
from operator import itemgetter


def launch_browser(path, url):
    """
        Launch a browser provided in the path to open a url.
        Arguments:
            path: path to browser executable
            url: url to open with the browser
    """
    webbrowser.get(path).open(url)


def order_icms(icms, order='random'):
    """ takes a list of interconnects and returns them sorted based on the given order
    random:    random order  # empty/invalid choice default
    alpha:     by enclosure, by interconnect bay number
    ibsmaster: by stackingDomainId, then stackingDomainRole, master first, then slave
    ibsslave:  by stackingDomainId, then by stackingDomainRole, slave first, then master
    """
    if not icms:
        return
    if order == 'alpha':
        icms.sort(key=itemgetter('name'))
    elif order == 'ibsmaster':
        icms = sorted(icms, key=itemgetter('stackingDomainId', 'stackingDomainRole'))
    elif order == 'ibsslave':
        icms = sorted(icms, key=itemgetter('stackingDomainId', 'stackingDomainRole'), reverse=True)
    else:
        shuffle(icms)
    return icms


def string_to_dictionary(string):
    """ Takes string in key=value comma separated and return a dictionary.
    Example:
    string = EnclosureSN=CN744502FG,Bay=3,User=OneView,Password=gLFSub12wFHeP7Gl
    dict = string_to_dictionary(string)
    dict is {"EnclosureSN":"CN744502FG","Bay":"3","User":"OneView","Password":"gLFSub12wFHeP7Gl"
    """
    return dict((n, v) for n, v in (a.split('=') for a in string.split(",")))


def get_argv():
    """ Pybot arguments is not exposed so we are using to get them
    """
    return sys.argv


def variable_file_should_be_passed(num=1):
    """ Test that a variablefile argument was used in the pybot command line
    and that variable file exists.
    """
    clList = get_argv()
    # There is an open issue in RF than when fixed can give us flexibilty of changing data variable file on the fly.
    # https://github.com/robotframework/robotframework/issues/2101
    # dataFiles = []
    f = {}
    i = 0
    try:
        for cmdl in clList:
            i += 1
            if cmdl == '-V':
                f[str(i)] = clList[i]
            elif re.match('-V\S*', cmdl):
                f[str(i)] = re.sub('-V', '', cmdl)
        if not f:
            errMsg = "A required argument was not found in your pybot command. Please use -V <variablefile> to specify your data variable file!"
            raise RuntimeError(errMsg)
        elif len(f) != num:
            errMsg = "The script expects %d data variable file(s) but %d was/were given!" % (num, len(f))
            raise RuntimeError(errMsg)
        else:
            errMsg = ""
            for v in f.itervalues():
                if not os.path.isfile(v):
                    errMsg = errMsg + "%s " % v
                # else:
                #    dataFiles.append(v)
            if errMsg:
                errMsg = "Variable file(s) you specified in your pybot command does not exist: " + errMsg
                raise RuntimeError(errMsg)
    except Exception as e:
        raise Exception("Data variable file check failed", e)
    # return dataFiles


def is_tag_present(tag='QuickMinimal'):
    """ Parses the command-line arguments for a robot framework tag and returns boolean.
     Argument:
          tag: RF test suite tag name
     Return:
          True: tag was found
          False: tag not found
"""
    pybot_ags = get_argv()
    i = 0
    found = False
    f = []
    try:
        for cmd in pybot_ags:
            i += 1
            if cmd == '-i':
                ele = pybot_ags[i]
                f.append(ele)
        for x in f:
            if x == tag:
                found = True
            else:
                continue
    except Exception as e:
        raise Exception("Unable to perform search for tag name %s" % tag, e)
    return found


def is_string_number(string):
    """
        Attempts conversion of string to float to decide if the passed argument (string) is numeric or not.
        Arguments:
            string: string to test
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def convert_ether_summary_to_dictionary(ether_summary_list):
    """ Convert list of space separated string like this:
    2      Po2(U)[AU,OU]   LACP       Ten-GigabitEthernet0/0/1:1(P),Ten-GigabitEthernet0/0/1:2(P)
                                      Ten-GigabitEthernet1/0/1:1(P),Ten-GigabitEthernet1/0/1:2(P)
    3      Po3(U)[AU,OU]   LACP       Ten-GigabitEthernet0/0/1:3(P),Ten-GigabitEthernet0/0/1:4(P)
                                      Ten-GigabitEthernet1/0/1:3(P),Ten-GigabitEthernet1/0/1:4(P)
    To something like this and return it:
    {'2': { 'lagId': 2, 'portChannel': 'Po2(U)[AU,OU]', 'protocol': 'LACPP', 'ports': ['Ten-GigabitEthernet0/0/1:1(P)','Ten-GigabitEthernet0/0/1:2(P)','Ten-GigabitEthernet1/0/1:1(P)','Ten-GigabitEthernet1/0/1:2(P)']},
    '3': {'blah': blah'}
    """
    ethSummary = {}
    j = 0
    for i in xrange(len(ether_summary_list)):
        if ether_summary_list[i] == '' or 'OneView' in ether_summary_list[i]:
            continue
        lsplit = ether_summary_list[i].split()
        if is_string_number(lsplit[0]):
            if lsplit[2] == 'Disabled':
                continue
            ethSummary[lsplit[0]] = {'lagId': int(lsplit[0]), 'portChannel': lsplit[1], 'protocol': lsplit[2], 'ports': [lsplit[3]]}
            j = i
        else:
            ethSummary[ether_summary_list[j].split()[0]]['ports'].append(lsplit[0])
    return ethSummary


def check_ping(host, extra='>/dev/null 2>&1'):
    """
        Check Ping
        Argument:
        host - hostname/ip to ping
        extra - intended for extra stuff like redirections, etc
        Return:
        return value of 0 on success or non-zero on failure
    """
    retval = os.system("ping -c 1 " + host + extra)
    return retval


def get_server_reachable_ip(haFile, server_profile=None):
    """
        Get Server Reachable IP
        Argument:
        haFile - path to your HA file.
        server_profile - filter by server profile name.
        Return:
        Dictionary of profile to reachable IP key-value pair
    """
    with open(haFile, 'r') as h:
        reachableIP = {}
        prev_profile = None
        for line in h:
            ha = line.split()
            if ha[7] == 'None':
                continue
            curr_profile = ha[0]
            if prev_profile and prev_profile != curr_profile and not reachableIP:
                raise AssertionError('Unable to find a pingable IP for server profile: %s' % prev_profile)
            if ha[0] in reachableIP.keys():
                continue
            if server_profile and ha[0] != server_profile:
                continue
            if check_ping(ha[7]) != 0:
                continue
            elif server_profile:
                return ha[7]
            else:
                reachableIP[ha[0]] = ha[7]
            prev_profile = curr_profile

    if not reachableIP:
        raise AssertionError('Unable to find a pingable IP for server profile: %s' % prev_profile)
    return reachableIP


def split_port_id(connPortId):
    """
        Splits the connection portId to determine the port type, device slot, physical port and virtual port.

        Argument:
            connPortId (string)  : Port ID string that looks like Lom 1:1-a, Flb 2:2-d, or Mezz 3:1-b

        Return:
            portId (dict)  : Port ID dict that includes port type, device slot, physical port and virtual port
    """

    portId = dict()

    # Split the connection port id to get the port type (Flb, Lom, Mezz) and port map (1:1-a)
    connPortIdData = connPortId.split(" ", 2)
    if len(connPortIdData) != 2:
        errMsg = "Connection port id is not what's expected: portId %s." % connPortId
        raise RuntimeError(errMsg)
    else:
        portId['portType'] = connPortIdData[0]
        connPortMap = connPortIdData[1]

    # Split the connection port map (1:1-a) to get the device slot (1,2,3) and the Flex10/20 map (1-a)
    connPortMapData = connPortMap.split(":", 2)
    if len(connPortMapData) != 2:
        errMsg = "Connection port map is not what's expected: Port map %s." % connPortMapData
        raise RuntimeError(errMsg)
    else:
        portId['devSlot'] = connPortMapData[0]
        flexMap = connPortMapData[1]

    # Split the flexMap (1-a) to get phy and virt port
    flexMapData = flexMap.split("-", 2)
    if len(flexMapData) != 2:
        errMsg = "Flex10/20 map is not what's expected: Flex10/20 map %s." % flexMap
        raise RuntimeError(errMsg)
    else:
        portId['phyPort'] = flexMapData[0]
        portId['virtPort'] = flexMapData[1]

    return portId


def get_bond_interface_data(profile, mac, speed, status, haFile, sameLI):
    """
        Get root bonding interface data using mac address.
        Argument:
            profile - server profile
            mac - mac address of the profile connection to acquire data.
            speed - profile connection maxBandwidth
            status - profile connection status: up|down|bothUp
            haFile - path to your HA file
            sameLI - boolean indicating both sides of connection is the same LI as the offline interconnect
        Returns:
            tuple of root bond interface and dictionary of profile connection data
    """
    invert_status = {'up': 'down', 'down': 'up'}
    with open(haFile, 'r') as h:
        # sort HA by side-a MAC address
        sortedByMac = sorted(h.readlines(), key=lambda item: item.strip().split()[3])
        bond = -1
        prev_mac = 0
        data = {}
        for line in sortedByMac:
            ha = line.split()
            curr_mac = ha[3]
            if ha[0] == profile and prev_mac != curr_mac:
                bond += 1
            if ha[7] == 'None':
                prev_mac = curr_mac
                continue
            if status == 'bothUp' and mac in [ha[3], ha[5]]:
                data = {ha[3]: 'up', ha[5]: 'up', 'speed': str(speed), 'System MAC address': ha[3].lower()}
                break
            if ha[3] == mac:
                data = {mac: status, ha[5]: invert_status[status] if sameLI else status, 'speed': str(speed), 'System MAC address': ha[3].lower()}
                break
            elif ha[5] == mac:
                data = {mac: status, ha[3]: invert_status[status] if sameLI else status, 'speed': str(speed), 'System MAC address': ha[3].lower()}
                break
            prev_mac = curr_mac
    return 'bond' + str(bond), data


def generate_server_profiles_ha_files(haFile, sp_ha_dir='./profiles_ha_files'):
    """
        Generate server profiles HA files for north-south, east-west ping.
        Argument:
            haFile - path to HA File
            sp_ha_dir - directory to save the generated server profiles HA files.
    """
    # building networks dictionary
    network_data = {}
    with open(haFile, 'r') as ha_file:
        for ha_line in ha_file:
            profile = "".join(ha_line.split(' ')[0])
            ipAddr = "".join(ha_line.split(' ')[-2])
            vlanId = "".join(ha_line.split(' ')[-3])
            network = ".".join(ipAddr.split('.')[:3])
            if network in network_data:
                network_data[network]['data'].append(ha_line)
                network_data[network]['profiles'].append(profile)
            else:
                network_data[network] = {'data': ['TCS N/A N/A N/A N/A N/A %s %s N/A\n' % (vlanId, network + '.1'), ha_line], 'profiles': [profile]}
    # building profiles ha files
    for net_value in network_data.values():
        for subj_profile in net_value['profiles']:
            try:
                with open(sp_ha_dir + '/' + subj_profile, 'a+') as filehandle:
                    for net_data in net_value['data']:
                        profile_name = "".join(net_data.split(' ')[0])
                        if profile_name != subj_profile:
                            filehandle.writelines(net_data)
            except IOError:
                raise AssertionError('Error while creating HA file for profile: %s' % subj_profile)


def file_should_exist(file_to_test):
    """
        Fail if file does not exist.
        Argument:
        file_to_test - path to your file to check.
    """
    if not os.path.exists(file_to_test):
        raise AssertionError('File does not exist: %s' % file_to_test)


def save_obj(filename, varname, obj):
    """
        Save an object to a file. Create a file based on filename arg that contains varname=obj.
        Arguments:
            filename - name of file to save object to.
            varname - variable name to hold the object to be saved.
            obj - object to be saved.
    """
    try:
        with open(filename, 'wb') as f:
            f.write(varname + '=')
            pprint(obj, stream=f)
    except IOError:
        raise AssertionError('Error while writing to file: %s' % filename)


def save_list_values_to_file(filename, listdata):
    """
        Save to filename the listdata values.
        Arguments:
            filename - filename to save to
            listdata - list of data to save
    """
    try:
        with open(filename, 'w') as filehandle:
            filehandle.writelines(["%s" % hadata for hadata in listdata])
    except IOError:
        raise AssertionError('Error while writing to file: %s' % filename)
