""" Claimed Enclosure Scanner

Usage:  python scanForEnclosures.py

This script makes Fusion API queries to determine how many enclosures have been
claimed.  It also reads the Fusion version file through SSH so you can
determine if a system is worth reserving based on its claim _and_ CIM firmware
status.  Each system's status is printed to the console, and will come up in
varying order each time because the queries are multithreaded (to minimize wait
time for all this glorious info).

This can facilitate development & test development work if claims are
proving problematic, or can help find machines that are old or not working.  It
could also be expanded to show system information similar to Avast for
SD2/Hawks, as well as to run "lldpcli show neighbors" over SSH in order to see
if a claim is even easily possible.

"""

import urllib2       # for making REST requests
import json          # for converting REST responses to dictionaries
import paramiko      # for SSH into the appliance to discover Fusion version
import threading     # for running all queries at once
from threading import Thread        # less expensive than threading
from Queue import Queue         # for making the output print nicer
import time          # Cheap way to wait before join


# This class contains the queries that'll run on each enclosure
class queryThread (threading.Thread):
    def __init__(self, systemName):
        """
        Contains logic to initialize the thread instance.
        Not called directly; instead, use "t = queryThread(args)" to initialize a new object.
        In this case, args is systemName, consisting of the hostname or IP to the CIM you wish to query.

        Example:
            t = queryThread("stella-cim1.rsn.hp.com")
        """
        threading.Thread.__init__(self)
        self.systemName = systemName

    def run(self):
        """
        Contains the code this thread shall run.
        In particular, this makes the Fusion API & SSH requests to pull the desired info,
        and present it to the user.

        This function is not called directly; instead, use
        "t.start()"
        on your new QueryThread object called t.
        """
        # Import the queue
        global q
        # Define a new SSH client & make sure it always accepts unknown keys
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        rsrc = ""
        infoString = ("%s" % self.systemName).ljust(28)
        # Define common HTTP request headers here
        hdrs = {
            "Accept-Language": "en",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        # Form a request to get a login session ID for this particular system
        req = urllib2.Request(url=('https://%s/rest/login-sessions' % self.systemName), data='{"userName": "Administrator", "password":"hpvse123"}', headers=hdrs)
        # Submit the request, and stand by for any errors
        try:
            rsrc = urllib2.urlopen(req)
        except urllib2.URLError as u:
            if "503" in u.__str__():
                # If HTTP 503 is returned, the system is unavailable
                print "%s: The system is down or rebooting; try again later.  (HTTP 503)" % infoString
            elif "400" in u.__str__():
                # If HTTP 400 is returned, the system deemed the request to be malformed somehow
                print "%s: The system deemed the login-sessions request to be malformed.  (HTTP 400)" % infoString
            else:
                # Print the exception out since an uncommon status was returned
                print infoString, u
            return
        except Exception as e:
            print "%s ERROR getting sessionID: %s %s" % (e.__str__(), e.__class__())
            return
        # Load the response into a JSON object & pull out the desired data (the sessionID)
        authData = json.loads(rsrc.read())
        sessionID = authData["sessionID"]

        # Use the sessionID token to query for how many enclosures have been added to Fusion
        req = urllib2.Request(url=('https://%s/rest/enclosures' % self.systemName), headers=hdrs)
        # Add additional headers specific to this particular call
        req.add_header('auth', sessionID)
        req.add_header('X-API-Version', "200")
        try:
            rsrc = urllib2.urlopen(req)
        except Exception as e:
            print "%s ERROR getting enclosure info: %s" % (infoString, e.__str__)
            return
        # Parse the result & report how many enclosures are added into this system
        enclData = json.loads(rsrc.read())
        enclTotal = enclData["total"]
        infoString += "|" + ("%d" % enclTotal).rjust(4)

        # Also query for server hardware from Fusion
        # TODO: this section is now copypasta... see if we can function-ize most of this
        #       OR better yet, use a function from fusion_api.py
        req = urllib2.Request(url=('https://%s/rest/server-hardware' % self.systemName), headers=hdrs)
        # Add additional headers specific to this particular call
        req.add_header('auth', sessionID)
        req.add_header('X-API-Version', "200")
        try:
            rsrc = urllib2.urlopen(req)
        except Exception as e:
            print "%s ERROR getting enclosure info: %s" % (infoString, e.__str__)
            return
        # Parse the result & report how many enclosures are added into this system
        enclData = json.loads(rsrc.read())
        enclTotal = enclData["total"]
        infoString += "|" + ("%d" % enclTotal).rjust(4)

        # Find out what Fusion version this system is running
        try:
            ssh.connect(self.systemName, username='root', password='hpvse1')
        except:
            print "%s ERROR finding Fusion version over SSH" % infoString
            return
        stdin, stdout, stderr = ssh.exec_command("more /ci/etc/version")
        stdin.flush()
        stdin.channel.shutdown_write()
        # Now we have the Fusion version; strip down the extraneous text and print all the information about this system
        fusionVersion = stdout.readlines()[3][8:15]
        ssh.close()
        # Write the output on-screen through the queue
        print "%s| %d" % (infoString, int(fusionVersion))


# Systems to check (hostnames or IPs):
systems = [
    "trippel-cim1.fcux.usa.hp.com",
    "tesla-cim1.rsn.hp.com",
    "stella-cim1.rsn.hp.com",
    "odell-cim1.fcux.usa.hp.com",
    "mustang-cim1.rsn.hp.com",
    "leffe-cim1.rsn.hp.com",
    "ipa-cim1.rsn.hp.com",
    "innis-cim1.rsn.hp.com",
    "fattire-cim1.fcux.usa.hp.com",
    "duvel-cim1.rsn.hp.com",
    "dp2proto2-cim1.rsn.hp.com",
    "dp2proto1-cim1.rsn.hp.com",
    "cobra-cim1.rsn.hp.com",
    "bock-cim1.fcux.usa.hp.com",
    "amstel-cim1.rsn.hp.com"
]

# Print column headings
print "Hostname                    |Encs|SHw |Build"
# Make a list of threads and populate it with one thread per system we want to check
threads = []
for system in systems:
    threads.append(queryThread(system))
# Kick off all these threads so we can check systems simultaneously
[t.start() for t in threads]

# TODO: Write a timer that checks the status of these threads after 15 seconds,
# and stops them if they have exceeded this timeout amount.
# The list of threads above makes it easier to track all these objects.
# However, threads staying open too long has not been a problem; nevertheless,
# if it becomes such, then this should facilitate writing such a timer.
