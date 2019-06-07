"""
    Function on Etherchannel parameter
"""
import paramiko
import time


def get_etherchannel_loadbalance_from_icm(hostname, username, password, command):
    """
    Get the Etherchannel load balance parameter
    """
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    channel = ssh.invoke_shell(term='vt100', width=200, height=1000000, width_pixels=0, height_pixels=0)
    while channel.recv_ready() is False:
        time.sleep(10)
        print channel.recv_ready()
    results = ''
    results += channel.recv(50000)
    channel.send(command)
    results = ''
    while channel.recv_ready() is False:
        time.sleep(2)
        print "Recv Ready: ", channel.recv_ready()
    results += channel.recv(50000)
    print "Results After show etherchannel Command: \n", results
    table = "\n".join(results.split("\n")[6:-1])
    print "Table After splitting \n", table
    ssh.close()
    return table


def get_etherchannel_port_counter_from_icm(hostname, username, password, command):
    """
    Clear the Port counter in icm
    """
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    channel = ssh.invoke_shell(term='vt100', width=200, height=1000000, width_pixels=0, height_pixels=0)
    while channel.recv_ready() is False:
        time.sleep(10)
        print channel.recv_ready()
    results = ''
    results += channel.recv(50000)
    print channel.send('no pagination\n')
    channel.send(command)
    results = ''
    while channel.recv_ready() is False:
        time.sleep(2)
        print "Recv Ready: ", channel.recv_ready()
    results += channel.recv(50000)
    print "Results After show port counter Command: \n", results
    ssh.close()
    return results
