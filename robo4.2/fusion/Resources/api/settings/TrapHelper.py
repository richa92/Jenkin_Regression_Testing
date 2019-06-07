from RoboGalaxyLibrary.utilitylib import logging as logger
import paramiko


def start_trap_listener(testhead, username, password, validate_string, trap_listener='/root/trap_forwarding/TrapListener.py',
                        buffer_size=1024, data_size=0, listen_port=1162,
                        status_file='/root/trap_forwarding/status_file', log_file='/root/trap_forwarding/log_file'):
    """
    :param testhead:
    :param username:
    :param password:
    :param validate_string: 'Remote Insight Test Trap' or fvttest3
    :param trap_listener: default to TrapListener.py
    :param buffer_size: default to 1024
    :param data_size: default to 0
    :param listen_port: default to 1162
    :param status_file: default to /root/trap_forwarding/status_file
    :param log_file: default to /root/trap_forwarding/log_file
    start_trap_listener(testhead='linux-testhead.vse.rdlabs.hpecorp.net', username='root', password='wpsthpvse1', validate_string='fvttest3', data_size=300, listener_port=1162, trap_listener='TrapListener.py', status_file='/root/trap_forwarding/status_file')
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(testhead, username=username, password=password)
        command = "%s -v %s -b %s -d %s -p %s -s %s -l %s &" % (
            trap_listener, validate_string, buffer_size, data_size, listen_port, status_file, log_file)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        command = "ps -ef |grep %s |head -1 |awk '{print $2}'" % trap_listener
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.readlines()
        pid = ''.join(output)
        logger._debug("The pid for trap listener is %s" % pid)
        ssh_client.close()
    except (paramiko.BadHostKeyException,
            paramiko.AuthenticationException,
            paramiko.SSHException) as e:
        raise AssertionError("SSH exception %s" % e.message)


def get_trap_listener_status(
        testhead, username, password, status_file='/root/trap_forwarding/status_file'):
    """
    :param testhead:
    :param username:
    :param password:
    :param status_file: default to /root/trap_forwarding/status_file
    :return: START, PASS, STOP, or PURGE
    get_trap_listener_status(testhead='linux-testhead.vse.rdlabs.hpecorp.net', username='root', password='wpsthpvse1', status_file='/root/trap_forwarding/status_file')
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(testhead, username=username, password=password)
        command = 'cat %s' % status_file
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.readlines()
        ssh_client.close()
        return ''.join(output)
    except (paramiko.BadHostKeyException,
            paramiko.AuthenticationException,
            paramiko.SSHException) as e:
        raise AssertionError("SSH exception %s" % e.message)


def stop_trap_listener(testhead, username, password,
                       trap_listener='/root/trap_forwarding/TrapListener.py', status_file='/root/trap_forwarding/status_file'):
    """
    :param testhead:
    :param username:
    :param password:
    :param trap_listener: default to TrapListener.py
    :param status_file: default to /root/trap_forwarding/status_file
    stop_trap_listener(testhead='linux-testhead.vse.rdlabs.hpecorp.net', username='root', password='wpsthpvse1', trap_listener='TrapListener.py', status_file='/root/trap_forwarding/status_file')
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(testhead, username=username, password=password)
        command = "ps -ef |grep %s |head -1 |awk '{print $2}'" % trap_listener
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.readlines()
        pid = ''.join(output)
        logger._debug("The pid for trap listener is %s" % pid)
        ssh_client.exec_command(command)
        command = 'kill %s' % pid
        ssh_client.exec_command(command)
        command = 'echo STOP > %s' % status_file
        ssh_client.exec_command(command)
        ssh_client.close()
    except (paramiko.BadHostKeyException,
            paramiko.AuthenticationException,
            paramiko.SSHException) as e:
        raise AssertionError("SSH exception %s" % e.message)


def purge_trap_listeners(testhead, username, password, script='PurgeTrapListener.sh',
                         trap_listener='/root/trap_forwarding/TrapListener.py', status_file='/root/trap_forwarding/status_file'):
    """
    :param testhead:
    :param username:
    :param password:
    :param script: default to PurgeTrapListener.sh
    :param trap_listener: default to TrapListener.py
    :param status_file: default to /root/trap_forwarding/status_file
    purge_trap_listeners(testhead='linux-testhead.vse.rdlabs.hpecorp.net', username='root', password='wpsthpvse1', trap_listener='TrapListener.py', status_file='/root/trap_forwarding/status_file')
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(testhead, username=username, password=password)
        command = "%s -v -t %s -s %s" % (script, trap_listener, status_file)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.readlines()
        logger._debug("The command output is %s" % ''.join(output))
        ssh_client.close()
    except (paramiko.BadHostKeyException,
            paramiko.AuthenticationException,
            paramiko.SSHException) as e:
        raise AssertionError("SSH exception %s" % e.message)
