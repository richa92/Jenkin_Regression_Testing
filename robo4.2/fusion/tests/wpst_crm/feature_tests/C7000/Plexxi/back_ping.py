import threading
import os
import time


def checkservicehealth1(no, ip, name):
    print "dddddd start"
    print os.system("ping -n %s %s > %s" % (no, ip, name))
    time.sleep(2)


def startthread1(no, ip, name):
    t1 = threading.Thread(name="checkservicehealth1", target=checkservicehealth1, args=(no, ip, name))
    # name=logger1.txt
    t1.start()


if __name__ == "__main__":
    startthread()
