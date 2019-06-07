import multiprocessing
import time
import os
import paramiko


def checkServerHealth(no, ip):
    print ip
    print os.system("ping -n %s %s > logger1.txt" % (no, ip))
    time.sleep(2)


def Services(no, ip):
    w1 = multiprocessing.Process(name='checkserver', target=checkServerHealth(no, ip))
    w1.daemon = True
    w1.start()

if __name__ == '__main__':
    Services('6', '10.142.245.190')


def sshto_server():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22
    ssh.connect(hostname="192.168.147.221", port=port, username="root", password="hpvse1")
    sftp = ssh.open_sftp()
    try:
        print "ssh to Linux"
    except IOError:
        pass
    f = sftp.open("/etc/sysconfig/network-scripts/ifcfg-bond-bond1", 'a')
    f.write("\nIPADDR=195.168.140.80\n")
    f.write("NETMASK=255.255.255.0\n")
    f.write("GATEWAY=195.168.140.1\n")
    f.close()
    input, output, error = ssh.exec_command("service bond1 restart\n")
    print "Outputis : ", output.readlines()
    ssh.close()
