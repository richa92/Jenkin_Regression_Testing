import threading
import os
import time


def checkservicehealth(no, ip, name, flag):
    print "start"
    if flag == "Windows":
        print "Pinging in Windows"
        print os.system("ping -n %s %s > %s" % (no, ip, name))
        time.sleep(2)
    elif flag == "Linux":
        print "Pinging in Linux"
        print os.system("ping -c %s %s > %s" % (no, ip, name))
        time.sleep(2)
    else:
        print "Please provide valid flag value to ping"


def startthread(no, ip, name, flag):
    t1 = threading.Thread(name="checkservicehealth", target=checkservicehealth, args=(no, ip, name, flag))
    t1.start()

if __name__ == "__main__":
    startthread()
