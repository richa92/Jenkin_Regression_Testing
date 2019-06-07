import threading
import os
import time
import signal


def checkservicehealth(ip, no, name):
    print "ddddddd start"
    print os.system("ping -n %s %s > %s" % (no, ip, name))


def startthread(ip, no, name):
    t1 = threading.Thread(name="checkservicehealth", target=checkservicehealth, args=(ip, no, name))
    t1.start()


def getpid(process_name):
    a = [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]
    print a
    b = int(a[0])
    os.kill(b, signal.SIGTERM)


if __name__ == "__main__":
    startthread('1.1.1.3', '200', 'mmm.txt')
