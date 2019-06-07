"""
    Elk helper class

    (C) Copyright 2018 Hewlett-Packard Development Company, L.P.
"""
from datetime import datetime
from Queue import Queue
from threading import Thread
import json
import os
import unittest
import requests
from robot.libraries.BuiltIn import RobotNotRunningError
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger


class ElkQueueWriter(Thread):

    """
    This class is the Elk queue writer thread.
    It performs a blocking read on the activity queue and writes the data
    to the Elk index when it is added to the queue by the listeners.
    It does this to avoid interfering with test execution times since latency
    would be introduced if every suite, test, and keyword had to write to Elk
    when it completed.
    """

    PROXIES = {
        "http": "web-proxy.corp.hpecorp.net:8080",
        "https": "web-proxy.corp.hpecorp.net:8080"
    }
    MAX_RETRIES = 5

    def __init__(self, host, index, queue):
        """
        Initialize the host and index vars
        """
        self.queue = queue
        self.session = None
        self.host = host
        self.index = index.lower()
        self.connected = self.get_elk_version() is not None
        Thread.__init__(self, name="ElkWriterThread")
        self.setDaemon(1)

    def is_connected(self):
        """
        Is the server connected
        """
        self.connected = self.get_elk_version() is not None
        return self.connected

    def get_elk_version(self):
        """
        Get the Elk version
        """
        try:
            resp = requests.get(self.host, proxies=self.PROXIES)
            if resp.status_code != 200:
                return None
            else:
                return json.loads(resp.text).get('version').get('number')
        except requests.exceptions.ConnectionError:
            self.connected = False
        return None

    def run(self):
        """ Entry point for the queue writer thread """
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/x-ndjson"})
        self.session.mount(self.host, requests.adapters.HTTPAdapter(max_retries=self.MAX_RETRIES))

        retry = self.MAX_RETRIES
        while retry:
            # retrieve an item from the queue.  If there's nothing then this
            # will block the thread until something is available.
            item = self.queue.get(block=True)
            uri = "{}/{}/{}".format(self.host, self.index, item.obj_type)

            try:
                # post the item to Elk using the standard proxy
                resp = self.session.post(
                    uri,
                    data=json.dumps(item.data),
                    proxies=self.PROXIES
                )
            except:
                resp = None
            # handle any issues
            if not resp or resp.status_code != 201:
                if retry == self.MAX_RETRIES:
                    print('{}: Failed to post results to {}\n'.format(str(datetime.now()), uri))
                retry -= 1


class UnitTests(unittest.TestCase):

    """
    Unit test class
    """

    def test_connection(self):
        """
        Test Elk Connectivity by polling version
        """
        queue = Queue()
        writer = ElkQueueWriter('http://rist-elk.vse.rdlabs.hpecorp.net:9200/', 'testindex', queue)
        version = writer.get_elk_version()
        print('Elk version: {}'.format(version))
        self.assertIsNotNone(version)


if __name__ == '__main__':
    unittest.main()
