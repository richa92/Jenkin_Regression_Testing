from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re
import subprocess
import platform
import xml.etree.ElementTree as ET
from base64 import b64decode
from distutils.spawn import find_executable  # pylint: disable=import-error


def run_cpqlocfg(command):
    '''
    :param command: cpqlocfg.exe command line string with any parameters
    :return:  tuple of cpqlocfg.exe output or error message and PASS or FAIL

    cpqlocfg.exe is a 32 bit Windows app.  It can be run natively on Windows or via the 32 bit wine emulator on Linux.
    Note that not all Linux distributions include 32 bit wine, it may have to be built from source.
    '''
    os = platform.system()
    if os == 'Windows' or os == 'Linux':
        if os == 'Linux':
            wine_path = find_executable('wine')
            if wine_path is None:
                return 'Cannot find wine to run cpqlocfg.exe on Linux', 'FAIL'
            command = wine_path + ' ' + command.replace('\\', '/')
            command = command.split(' ')
        try:
            logger._debug("The command is %s " % command)
            output = subprocess.check_output(command)
            logger._debug("The output is %s" % output)
            if 'Script succeeded' in output:
                start = output.index('<?xml')
                end = output.rindex('>')
                output = output[start:end + 1]
                output = re.sub('\n|\r', '', output)
                str = '<?xml version=\"1.0\"?>'
                output = output.replace(str, '')
                str = "<RIBCL VERSION=\"2.23\"><RESPONSE    STATUS=\"0x0000\"    MESSAGE='No error'     /></RIBCL>"
                output = output.replace(str, '')
                str = "<RESPONSE    STATUS=\"0x0000\"    MESSAGE='No error'     />"
                output = output.replace(str, '')
                return output, 'PASS'
            else:
                return output, 'FAIL'
        except subprocess.CalledProcessError, e:
            return e.output, 'FAIL'
    else:
        return 'cpqlocfg.exe only runs on Windows or on Linux with 32 bit wine emulator', 'FAIL'


def get_ilo_snmp_engine_id(snmp_settings):
    '''
    :param snmp_settings:
        <GET_SNMP_IM_SETTINGS>
            <SNMP_ACCESS VALUE="Enable"/>
            <SNMP_ADDRESS_1 VALUE="16.114.220.248"/>
            <SNMP_ADDRESS_1_ROCOMMUNITY VALUE="abcabc"/>
            <SNMP_ADDRESS_1_TRAPCOMMUNITY VERSION="" VALUE=""/>
            <SNMP_ADDRESS_2 VALUE=""/>
            <SNMP_ADDRESS_2_ROCOMMUNITY VALUE=""/>
            <SNMP_ADDRESS_2_TRAPCOMMUNITY VERSION="" VALUE=""/>
            <SNMP_ADDRESS_3 VALUE=""/>
            <SNMP_ADDRESS_3_ROCOMMUNITY VALUE=""/>
            <SNMP_ADDRESS_3_TRAPCOMMUNITY VERSION="" VALUE=""/>
            <SNMP_V3_ENGINE_ID VALUE="0x6367754b374277644659565561716b68"/>
            <SNMP_PORT VALUE="161"/>
            <SNMP_TRAP_PORT VALUE="162"/>
            <TRAP_SOURCE_IDENTIFIER VALUE="iLO Hostname"/>
            <RIB_TRAPS VALUE="Y"/>
            <OS_TRAPS VALUE="Y"/>
            <COLD_START_TRAP_BROADCAST VALUE="Y"/>
            <SNMP_V1_TRAPS VALUE="Y"/>
            <SNMP_PASSTHROUGH_STATUS VALUE="N"/>
            <WEB_AGENT_IP_ADDRESS VALUE="WIN-U4P4HQNNRIO"/>
            <CIM_SECURITY_MASK VALUE="3"/>
            <SNMP_SYS_CONTACT VALUE=""/>
            <SNMP_SYS_LOCATION VALUE=""/>
            <AGENTLESS_MANAGEMENT_ENABLE VALUE="Y"/>
            <SNMP_SYSTEM_ROLE VALUE=""/>
            <SNMP_SYSTEM_ROLE_DETAIL VALUE=""/>
            <SNMP_USER_PROFILE INDEX="1">
                <SECURITY_NAME VALUE="fvttest1"/>
                <AUTHN_PROTOCOL VALUE="1"/>
                <AUTHN_PASSPHRASE VALUE="**********"/>
                <PRIVACY_PROTOCOL VALUE="1"/>
                <PRIVACY_PASSPHRASE VALUE="**********"/>
            </SNMP_USER_PROFILE>
            <SNMP_USER_PROFILE INDEX="2">
                <SECURITY_NAME VALUE="fvttest2"/>
                <AUTHN_PROTOCOL VALUE="1"/>
                <AUTHN_PASSPHRASE VALUE="**********"/>
                <PRIVACY_PROTOCOL VALUE="1"/>
                <PRIVACY_PASSPHRASE VALUE="**********"/>
            </SNMP_USER_PROFILE>
            <SNMP_USER_PROFILE INDEX="3">
                <SECURITY_NAME VALUE="oneview_353578734c7a5057444e7046"/>
                <AUTHN_PROTOCOL VALUE="1"/>
                <AUTHN_PASSPHRASE VALUE="**********"/>
                <PRIVACY_PROTOCOL VALUE="1"/>
                <PRIVACY_PASSPHRASE VALUE="**********"/>
            </SNMP_USER_PROFILE>
        </GET_SNMP_IM_SETTINGS>
    :return engine_id: '0x6367754b374277644659565561716b68'
    '''
    engine_id = ''
    tree = ET.fromstring(snmp_settings)
    e = tree.find('SNMP_V3_ENGINE_ID')
    engine_id = e.attrib['VALUE']
    BuiltIn().should_not_be_empty(engine_id, msg='Engine ID not found')
    BuiltIn().log('PASS: Get iLO SNMP engine ID %s' % engine_id, console=True)
    return engine_id


def check_ilo_snmp_user_presence(snmp_settings, user='oneview', expected=False):
    '''
    :param snmp_settings:
    :param user: 'oneview', 'fvttest1'
    :param expected: True or False
    '''
    check = False
    tree = ET.fromstring(snmp_settings)
    for e in tree.iterfind('SNMP_USER_PROFILE/SECURITY_NAME'):
        logger._debug("Security name %s" % e.attrib['VALUE'])
        if re.search(user, e.attrib['VALUE']):
            check = True
            break

    BuiltIn().should_be_equal(check.__str__(), expected.__str__(), msg=('Check iLO SNMP user %s presence should match expected' % user))
    BuiltIn().log('PASS: Check ilo SNMP user %s' % user, console=True)


def check_ilo_snmp_address(snmp_settings, address, rocommunity='', check_rocommunity=False):
    '''
    :param snmp_settings:
    :param address: '16.114.220.248'
    :param rocommunity: '', 'abcabc', 'REGEXP:\w{6}',
    '''
    tree = ET.fromstring(snmp_settings)
    laddress = []
    lcommunity = []
    for e in tree.iter():
        if re.search('SNMP_ADDRESS', e.tag):
            fields = e.tag.split('_')
            if len(fields) == 3:
                ip = e.attrib['VALUE']
                # change IPv6 address format
                if re.search(r':', ip):
                    ip = re.sub(r'(:0){2,}', ':', ip)
                laddress.append(ip)
            if len(fields) == 4 and fields[3] == 'ROCOMMUNITY':
                lcommunity.append(e.attrib['VALUE'])
    t = zip(laddress, lcommunity)

    check = False
    for item in t:
        logger._debug("address %s rocommunity %s" % (item[0], item[1]))
        if check_rocommunity:
            if re.match('REGEXP', rocommunity):
                (str, regexp) = rocommunity.split(':')
                if item[0] == address and re.match(regexp, item[1]):
                    logger._debug("address %s rocommunity %s" % (item[0], item[1]))
                    check = True
                    break
            else:
                if item[0] == address and item[1] == rocommunity:
                    logger._debug("address %s rocommunity %s" % (item[0], item[1]))
                    check = True
                    break
        else:
            if item[0] == address:
                check = True
                break

    BuiltIn().should_be_equal(check.__str__(), True.__str__(), msg='check ilo snmp address should match True')
    if check_rocommunity:
        BuiltIn().log('Pass: Check ilo snmp address %s rocommunity %s' % (address, rocommunity), console=True)
    else:
        BuiltIn().log('Pass: Check ilo snmp address %s' % address, console=True)


def get_ilo_legacy_bios_boot_controller_order(cqhord):
    '''
    :param cqhord: iLO CQHORD environment variable base64 string value
    :return: list of CQHORD dictionaries in boot controller order
    '''
    ba = bytearray(b64decode(cqhord))
    if len(ba) % 8 != 0:
        BuiltIn().log("Invalid CQHORD decoded length (%d) for %s" % (len(ba), cqhord), level='ERROR', console=True)
        return []

    bco_list = []

    # CQHORD records are 8 bytes long, sequence through them
    for i in range(0, len(ba), 8):
        e = {}
        e['vendor_id'] = (ba[i] << 8) | ba[i + 1]
        e['device_id'] = (ba[i + 2] << 8) | ba[i + 3]
        e['slot'] = ba[i + 4]
        e['bus'] = ba[i + 5]
        e['device'] = ba[i + 6] >> 3
        e['function'] = ba[i + 6] & 0x07
        e['legacy'] = ba[i + 7] >> 7
        e['bios'] = (ba[i + 7] & 0x40) >> 6
        e['reserved'] = (ba[i + 7] & 0x38) >> 3
        e['bus_type'] = ba[i + 7] & 0x07
        bco_list.append(e)

    return bco_list
