from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.libs.cli.cli_base import remote_actions
import re


def get_oa_snmp_engine_id(oa, oa_username, oa_password):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :return engine_id: '0x8000000b0434343a31653a61313a35373a61333a6532'
    """
    engine_id = ''
    command = 'show snmp'
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        if 'Engine ID' in rtn.stdout:
            for line in rtn.stdout.split('\n'):
                if 'Engine ID' in line:
                    (str1, engine_id) = line.split(':')
                    engine_id = engine_id.strip()
                    break
        else:
            logger._debug("Engine ID not found")

    BuiltIn().should_not_be_empty(engine_id, msg=('Engine ID not found on oa %s' % oa))
    BuiltIn().log('PASS: Get OA SNMP engine ID %s on OA %s' % (engine_id, oa), console=True)

    return engine_id


def get_oa_snmp_users(oa, oa_username, oa_password):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :return snmp_users: [u'fvttest', u'fvttest1', u'fvttest2', u'oneview_5262356e31584d5a57645249']
    Example show snmp user list output:
    wpst16-oa1 [SCRIPT MODE]&gt; show snmp users list


     SNMPv3 User                      Local  Access   Security   EngineID
     -------------------------------- ------ ------ ------------ -----------
     fvttest1                         local  ro     authNoPriv   0x8000000b0434343a31653a61313a35373a61333a6532
     oneview_575436624162484a4c4d6a7a local  ro     authPriv     0x8000000b0434343a31653a61313a35373a61333a6532
    """
    snmp_users = []
    command = 'show snmp users list'
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        if 'No SNMPv3 users created' not in rtn.stdout:
            start = rtn.stdout.index('-----------')
            output_string = rtn.stdout[start + 12:-1]
            for line in output_string.split('\n'):
                if re.search('0x', line):
                    fields = line.split()
                    snmp_users.append(fields[0])
        else:
            logger._debug("No SNMPv3 users created")

    BuiltIn().log('PASS: Get OA SNMP users %s on OA %s' % (snmp_users, oa), console=True)
    return snmp_users


def check_oa_snmp_user_presence(oa, oa_username, oa_password, user='oneview', expected=False):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param user: 'oneview', 'fvttest1'
    :param expected: expected presence
    """
    check = False
    snmp_users = get_oa_snmp_users(oa, oa_username, oa_password)
    for snmp_user in snmp_users:
        if re.search(user, snmp_user):
            check = True
            break

    BuiltIn().should_be_equal(check.__str__(), expected.__str__(), msg=('Check OA SNMP user %s presence on OA %s should match expected' % (user, oa)))
    BuiltIn().log('PASS: Check OA SNMP user %s on OA %s' % (user, oa), console=True)


def remove_oa_snmp_user(oa, oa_username, oa_password, snmp_user):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param snmp_user:  'fvttest1'
    """
    command = 'remove snmp user %s' % snmp_user
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        BuiltIn().should_match_regexp(rtn.stdout, 'was removed', msg='remove oa snmp user output should match')
        BuiltIn().log('PASS: Remove OA SNMP user %s on OA %s' % (snmp_user, oa), console=True)


def remove_oa_snmp_users(oa, oa_username, oa_password):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    """
    snmp_users = get_oa_snmp_users(oa, oa_username, oa_password)
    if snmp_users:
        for snmp_user in snmp_users:
            remove_oa_snmp_user(oa, oa_username, oa_password, snmp_user)
    else:
        logger._debug("No SNMPv3 users created")


def add_oa_snmp_user(oa, oa_username, oa_password, snmp_user):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param snmp_user: ['fvttest', 'SHA1', 'wpsthpvse1', 'AES128', 'wpsthpvse1']
    """
    command = 'add snmp user %s %s %s %s %s' % (snmp_user[0], snmp_user[1], snmp_user[2], snmp_user[3], snmp_user[4])
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        BuiltIn().should_match_regexp(rtn.stdout, 'was created', msg='add oa snmp user output should match')
        BuiltIn().log('PASS: Add OA SNMP user %s on OA %s' % (snmp_user, oa), console=True)


def get_oa_snmp_trapreceivers(oa, oa_username, oa_password):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :return snmp_trapreceivers: [u'16.114.220.143 public', u'16.114.220.248 oneview_5262356e31584d5a57645249']
    Example show snmp output:
        SNMP Configuration:
            Status: Enabled
            System Name: wpst16
            System Location:
            System Contact:
            Read Community Name: vQWOiJ
            Write Community Name:
            Engine ID: 0x8000000b0434343a31653a61313a35373a61333a6532
            Trap Receiver host: 16.114.218.215 abcabc
                                16.114.218.215 fvttest1 0x8000000b0434343a31653a61313a35373a61333a6532 authNoPriv  v3
                                16.114.218.206 oneview_575436624162484a4c4d6a7a 0x8000000b0434343a31653a61313a35373a61333a6532 authPriv  v3
    """
    snmp_trapreceivers = []
    command = 'show snmp'
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        if 'No trap receivers specified' not in rtn.stdout:
            start = rtn.stdout.index('Trap Receiver host:')
            output_string = rtn.stdout[start + 19:-1]
            for line in output_string.split('\n'):
                line = line.strip()
                if re.search('^[\d\w-]*\\.[\d\w-]*\\.', line):
                    fields = line.split()
                    snmp_trapreceivers.append("%s %s" % (fields[0], fields[1]))
        else:
            logger._debug("No trap receivers specified")

    return snmp_trapreceivers


def check_oa_snmp_trapreceiver(oa, oa_username, oa_password, destination, community='', user=''):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param destination: '16.114.218.215'
    :param community for SNMPv1:'public'
    :param user for SNMPv3: 'fvttest1'
    community and user are mutually exclusive.
    Example show snmp output:
        SNMP Configuration:
            Status: Enabled
            System Name: wpst16
            System Location:
            System Contact:
            Read Community Name: vQWOiJ
            Write Community Name:
            Engine ID: 0x8000000b0434343a31653a61313a35373a61333a6532
            Trap Receiver host: 16.114.218.215 abcabc
                                16.114.218.215 fvttest1 0x8000000b0434343a31653a61313a35373a61333a6532 authNoPriv  v3
                                16.114.218.206 oneview_575436624162484a4c4d6a7a 0x8000000b0434343a31653a61313a35373a61333a6532 authPriv  v3

    """
    check = False
    command = 'show snmp'
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        if 'No trap receivers specified' not in rtn.stdout:
            start = rtn.stdout.index('Trap Receiver host:')
            output_string = rtn.stdout[start + 19:-1]
            logger._debug(output_string.split('\n'))
            for line in output_string.split('\n'):
                fields = line.split()
                if len(fields) == 2:
                    if fields[0] == destination and fields[1] == community:
                        check = True
                        break
                else:
                    if fields[0] == destination and re.search(user, fields[1]):
                        check = True
                        break
        else:
            logger._debug("No trap receivers specified")

    BuiltIn().should_be_equal(check.__str__(), True.__str__(), msg='Check OA SNMP trapreceiver should match True')
    BuiltIn().log('PASS: Check OA SNMP trapreceiver destination %s community %s user %s on OA %s' % (destination, community, user, oa), console=True)


def remove_oa_snmp_trapreceiver(oa, oa_username, oa_password, trapreceiver):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param trapreceiver: ['16.114.220.143 public'], ['16.114.220.143 fvttest']
    """
    fields = trapreceiver.split()
    command = 'remove snmp trapreceiver %s %s' % (fields[0], fields[1])
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        BuiltIn().should_match_regexp(rtn.stdout, 'was removed', msg='remove snmp trapreceiver output should match')
        BuiltIn().log('PASS: remove OA SNMP trapreceiver %s' % trapreceiver, console=True)


def remove_oa_snmp_trapreceivers(oa, oa_username, oa_password):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    """
    trapreceivers = get_oa_snmp_trapreceivers(oa, oa_username, oa_password)
    if trapreceivers:
        for trapreceiver in trapreceivers:
            remove_oa_snmp_trapreceiver(oa, oa_username, oa_password, trapreceiver)
    else:
        logger._debug("No trap receivers specified")


def add_oa_snmp_trapreceiver(oa, oa_username, oa_password, trapreceiver, v3=False):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :trapreceiver: ['16.114.220.143'], ['16.114.220.143', 'public'], ['16.114.220.143', 'fvttest']
    """
    engine_id = get_oa_snmp_engine_id(oa, oa_username, oa_password)
    if v3:
        command = 'add snmp trapreceiver V3 %s %s' % (trapreceiver[0], trapreceiver[1])
    else:
        if len(trapreceiver) == 1:
            command = 'add snmp trapreceiver %s' % (trapreceiver[0])

        else:
            command = 'add snmp trapreceiver %s %s' % (trapreceiver[0], trapreceiver[1])
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        BuiltIn().should_match_regexp(rtn.stdout, 'was added', msg='add oa snmp trapreceiver output should match')
        BuiltIn().log('PASS: add OA SNMP trapreceiver %s' % trapreceiver, console=True)


def get_oa_blade_ip(oa, oa_username, oa_password, bay):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param bay: 1-16
    """
    blade_ip = ''
    command = 'show server info %s' % bay
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))
        if 'No Server Blade Installed' not in rtn.stdout:
            for line in rtn.stdout.split('\n'):
                if 'IP Address' in line:
                    (str1, blade_ip) = line.split(':')
                    blade_ip = blade_ip.strip()
                    break
        else:
            logger._debug("No Server Blade Installed in bay")

    BuiltIn().should_not_be_empty(blade_ip, msg=('Blade IP not found for bay %s on oa %s' % (bay, oa)))
    BuiltIn().log('PASS: Get OA blade IP %s for bay %s on OA %s' % (blade_ip, bay, oa), console=True)

    return blade_ip


def run_oa_hponcfg(oa, oa_username, oa_password, hpconcfg):
    """
    :param oa:
    :param oa_username:
    :param oa_password:
    :param hponcfg:
    """
    command = 'HPONCFG all << %s ' % hpconcfg
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    rtn = oa_ssh.call_cmd(command, realout=True)
    oa_ssh.close_ssh()
    if rtn.code != 0:
        logger.warn("Failed to run command %s on OA %s" % (command, oa))
        return False
    else:
        logger._debug("The command %s output on oa %s is %s" % (command, oa, rtn.stdout))


def slot_populated(oa, oa_username, oa_password, device, pos):
    """
    Check if there exists a device or not
    :param oa: FQDN or IP address of C7000 enclosure
    :param oa_username: Name of the user account
    :param oa_password: Password of the specified user
    :param device: BLADE | INTERCONNECT
    :param pos: Position in the enclosure
    :return: True if device is present else false
    """
    oa_ssh = remote_actions(host=oa, username=oa_username, password=oa_password)
    cmd = 'show '
    cmd += 'server ' if device.lower() == 'blade' else 'interconnect '
    cmd += 'status {}'.format(pos)
    rtn = oa_ssh.call_cmd(cmd, realout=True)

    if rtn.code != 0:
        logger.warn('Unable to retrieve the information.')
        return False

    match = ['No Server Blade Installed', 'No Interconnect Module Installed',
             'Power: Unknown']

    if any(x in rtn.stdout for x in match):
        return False
    else:
        return True
