#!/usr/local/bin/python
import requests
import json
import re
import string
from requests.auth import AuthBase

# Authorization Class


class CicAuth(AuthBase):

    def __init__(self, sessionid):
        self.sessionid = sessionid

    def __call__(self, r):
        r.headers['auth'] = self.sessionid
        return r

# Get UUID Class


class GetUuid(object):

    def __init__(self, ip, uname, pw, sessionID):
        self.ip = ip
        self.uname = uname
        self.pw = pw
        self.sessionID = sessionID

    def getUuid(self):
        # test steps to pull UUID
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        uuidUrl = string.Template("https://$ip/rest/enclosures?start=0&count=-1")
        uuidUrl = uuidUrl.substitute(ip=self.ip)

        # JRT print uuidUrl
        r = requests.get(uuidUrl, auth=CicAuth(self.sessionID), headers=headers, verify=False)
        if r.status_code == 200:
            print "uuidUrl worked"
            # JRT print r.text
        else:
            print "Error calling request.post for metric URL", r.status_code
            exit(1)

        # Parse out uuid
        if r.text.find("uuid"):
            fields = r.text.split(",")
            # fields = r.text.split(":")
            encUuidPair = re.sub('[\"}]', '', fields[2])
            print "encUuidPair = ", encUuidPair
            encUUID = encUuidPair.split(":")
            encUUID = re.sub('[\"}]', '', encUUID[1])
            print "found uuid"
        else:
            print "uuid not found"

        print "encUUID = ", encUUID
        return encUUID

    # ############################# End UUID Method ###########################


class GetMetrics(object):

    def __init__(self, ip, uname, pw, sessionID, uuid, startdate, enddate, metric1):
        self.ip = ip
        self.uname = uname
        self.pw = pw
        self.sessionID = sessionID
        self.uuid = uuid
        self.startdate = startdate
        self.enddate = enddate
        self.metric1 = metric1

    def getMetric(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        # Create metric URL

        # -- date slice ALL metrics
        # JRT metricURL = string.Template("https://$ip/rest/enclosures/$encUUID/utilization?view=native&filter=startDate=$sampleStartDate&filter=endDate=$sampleEndDate")
        # JRT metricURL = metricURL.substitute(ip=self.ip, encUUID=self.uuid, sampleStartDate=self.startdate, sampleEndDate=self.enddate)

        # -- date slice for a specific metric and metric
        # JRT metricURL = string.Template("https://$ip/rest/enclosures/$encUUID/utilization?view=native&filter=startDate=$sampleStartDate&filter=endDate=$sampleEndDate&fields=$metric1")
        # JRT metricURL = metricURL.substitute(ip=self.ip, encUUID=self.uuid, sampleStartDate=self.startdate, sampleEndDate=self.enddate, metric1=self.metric1)
        # -- view (day, hour, etc) with a single metric
        # JRT metricURL = string.Template("https://$ip/rest/enclosures/$encUUID/utilization?view=$sampleSize")
        # JRT metricURL = metricURL.substitute(ip=self.ip, encUUID=self.uuid, sampleSize=sampleSize, metric1=self.metric1)
        # -- view (day, hour, etc) ALL metrics
        sampleSize = "hour"
        metricURL = string.Template("https://$ip/rest/enclosures/$encUUID/utilization?view=$sampleSize")
        metricURL = metricURL.substitute(ip=self.ip, encUUID=self.uuid, sampleSize=sampleSize)

        print "#################################################"
        print "metricURL = ", metricURL
        print "#################################################"

        # Do a get on the URL to collect metric(s)
        r = requests.get(metricURL, auth=CicAuth(self.sessionID), headers=headers, verify=False)
        # r = requests.get(metricURL, auth=FusionAuth(sessionID), headers=headers, verify=False)
        if r.status_code == 200:
            # JRT print "printing r.text"
            # JRT print r.text
            metrics = r.text
        else:
            print "Error calling request.post for metric URL", r.status_code
            exit(1)

        # ### Let's try formatting the text here: (JRT) ####

        # JRT metricdump = metrics[string.find(metrics, '{'):]

        # JRT if metricdump:
        # JRT     try:
        # JRT         dict = json.loads(metricdump)
        # JRT     except ValueError:
        # JRT 	print "Attempting to pretty up non json string..."
        # JRT 	dict = eval(metricdump)

        # JRT     import pprint
        # JRT     print pprint.PrettyPrinter().pformat(dict)
        return metrics
