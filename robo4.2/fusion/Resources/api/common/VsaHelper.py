from RoboGalaxyLibrary.utilitylib import logging as logger
import paramiko


class VsaHelper(object):
    # Helper library to run the commands on VSA.

    def get_volume_connected_sessions(self, mgmt_ip, username, password, volume_name, port=22):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh_client.connect(mgmt_ip, username=username, password=password, port=int(port))
            command = 'getVolumeInfo volumeName=%s' % volume_name
            stdin, stdout, stderr = ssh_client.exec_command(command)
            output = stdout.readlines()
            logger._debug("getVolumeInfo volumeName=%s output is %s" % (volume_name, output))
            ssh_client.close()
            output_string = ''.join(output)
            connected_sessions = ''
            if 'SESSION' in output_string:
                logger._debug("SESSION found in getVolumeInfo volumeName=%s output" % volume_name)
                start = output_string.index('SESSION')
                end = output_string.index('PERMISSION')
                sessions_string = output_string[start:end - 4]
                sessions = sessions_string.split('SESSION')
                for session in sessions:
                    print session
                    if 'connected' in session:
                        connected_sessions = connected_sessions + session
                if (connected_sessions == ''):
                    return sessions_string, 'FAIL'
                else:
                    logger._debug("connected sessions for volume %s are %s" % (volume_name, connected_sessions))
                    return connected_sessions, 'PASS'
            else:
                logger._debug("SESSION not found in getVolumeInfo volumeName=%s output" % volume_name)
                return output_string, 'FAIL'
        except (paramiko.BadHostKeyException,
                paramiko.AuthenticationException,
                paramiko.SSHException) as e:
            raise AssertionError("SSH exception %s" % e.message)

    def parse_cliq_volume_info(self, raw_vol_info):
        """
        Very rudimentary parser for a response string from a CLIQ volume query
        as returned by the CLIQ Get Volume Info keyword
        """
        ret = {}
        sub_section = None
        in_headers = True
        for l in raw_vol_info.splitlines():
            ls = l.split()
            if (len(ls) < 1):
                continue
            if (ls[0] == 'RESPONSE'):
                in_headers = False
                sub_section = {}
                ret['RESPONSE'] = sub_section
            if (in_headers):
                continue
            if (ls[0] == 'VOLUME'):
                sub_section = {}
                ret['VOLUME'] = sub_section
            elif (ls[0] == 'STATUS'):
                sub_section = {}
                ret['STATUS'] = sub_section
            elif (ls[0] == 'PERMISSION'):
                sub_section = {}
                ret['PERMISSION'] = sub_section
            elif (ls[0] == 'CLIQ>'):
                break
            else:
                sub_section[ls[0]] = ' '.join(ls[1:])
        return ret
