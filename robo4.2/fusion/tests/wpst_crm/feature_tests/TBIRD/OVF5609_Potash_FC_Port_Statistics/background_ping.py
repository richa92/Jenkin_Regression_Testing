import time
import re
import os
import threading
from robot.libraries.BuiltIn import BuiltIn


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute any windows commands
    '''
    try:
        build_cmd = "paexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
        print build_cmd
        output = os.system(build_cmd)
        return output
    except Exception as e:
        return e


def execute_traffic(ip, username, passwd, wcmd):
    io_thread = threading.Thread(target=execute_windows_commands, args=(ip, username, passwd, wcmd))
    io_thread.start()


def get_interconnect_statistics(ic_uri, ic_port):
    print ic_port
    uri = ic_uri + '/statistics/' + ic_port
    print uri
    fz = BuiltIn().get_library_instance('FusionLibrary')
    output = fz.fusion_api_get_interconnect(uri)
    return output
