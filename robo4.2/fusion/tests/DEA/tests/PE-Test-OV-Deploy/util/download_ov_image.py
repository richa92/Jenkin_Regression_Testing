'''
Created on Apr 11, 2017

@author: AndTran
'''

import argparse
from sgmllib import SGMLParser
import urllib
import logging
import urllib2
import os
import time
import sys

logger = logging.getLogger(__file__)
format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)


class URLLister(SGMLParser):

    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)


def download_file(url, download_location):
    """ Downloading file in chunnks
        Required input:
            url - complete download url. ie. http://myserver/myfile.zip
            download_location - save file location; i.e. /temp
    """
    base_file = os.path.basename(url)
    os.umask(0o002)
    temp_path = download_location

    try:
        file = os.path.join(temp_path, base_file)
        req = urllib2.urlopen(url)
        total_size = int(req.info().getheader('Content-Length').strip())
        logger.info("Total file size %s" % str(total_size))
        downloaded = 0
        CHUNK = 256 * 10240
        logger.info("Downloading file % s" % file)
        start = time.clock()
        with open(file, 'wb') as fp:
            while True:
                chunk = req.read(CHUNK)
                downloaded += len(chunk)
                if(downloaded % 52428800 == 0):
                    logger.info("Downloading %s MB\n" % str(downloaded / (1024 * 1024)))
                if not chunk:
                    break
                fp.write(chunk)
        elapsed_time = time.clock() - start
        logger.info("Downloading file completed in %0.3f Minutes" % (elapsed_time / 60))
    except urllib2.HTTPError as e:
        logger.info(e.code)
        return False
    except urllib2.URLError as e:
        logger.info(e.reason)
        return False
    return file


def get_file_url(base_url, look_for_pass=True, fixed_url=None):
    """
        Required input:
            base_url = "http://ci-nexus.vse.rdlabs.hpecorp.net/Fusion/rel/3.10/DDImage/SSH/"
    """
    if fixed_url is not None:
        return fixed_url

    usock = urllib.urlopen(base_url)
    parser = URLLister()
    parser.feed(usock.read())
    parser.close()
    usock.close()
    myFileList = []
    myBuildNumbers = []
    latestURL = ""
    try:
        for url in parser.urls:
            logger.debug(url)
            if url[-3:] == "zip":
                myStringArray = url.split("_")
                for myString in myStringArray:
                    if look_for_pass:
                        if myString[:4] == "PASS":
                            myFileList.append(url)
                            myBuildNumbers.append(int(myString.replace("PASS", "").replace(".zip", "")))
                    else:
                        if myString[:2] == "RC":
                            myFileList.append(url)
                            myBuildNumbers.append(int(myString.replace("RC", "").replace(".zip", "")))
            elif url[-3:] == "ova":
                myStringArray = url.split("_")
                for myString in myStringArray:
                    if look_for_pass:
                        if myString[:4] == "PASS":
                            myFileList.append(url)
                            myBuildNumbers.append(int(myString.replace("PASS", "").replace(".ova", "")))
                    else:
                        if myString[:3] == "RC":
                            myFileList.append(url)
                            myBuildNumbers.append(int(myString.replace("RC", "").replace(".ova", "")))

        latest_build_number = (max(myBuildNumbers))
        for myFile in myFileList:
            if str(latest_build_number) in myFile:
                latestURL = base_url + myFile
        if not latestURL:
            logger.error("Found no OV image")
            sys.exit(1)
        logger.info("Found latest OV image %s \n" % latestURL)
        return latestURL

    except:
        raise AssertionError("Error getting latest OV image URL")


def get_args():
    parser = argparse.ArgumentParser(description='Script downloads OneView daily build image from a given source.')
    parser.add_argument('-s', '--source_url', type=str, help='Base URL of the source which stores OneView daily build images')
    parser.add_argument('-rc', '--rc_build', action='store_true', default=False, help='Download FC build; default is False and will download pass build')
    parser.add_argument('-d', '--dest', type=str, help='Download location. Location where to store the downloaded image')
    parser.add_argument('-fu', '--fixedurl', type=str, help='Download location. Location where to store the downloaded image')

    '''
    -s http://ci-nexus.vse.rdlabs.hpecorp.net/Fusion/rel/3.10/DDImage/SSH/
    -d /tmp for Linux or -d c:\\temp for Windows
    '''
    args = parser.parse_args()

    if args.fixedurl:
        fixed_url = args.fixedurl
        destination = args.dest
        source_url = ""
        rc_build = False
    else:
        source_url = args.source_url
        destination = args.dest
        rc_build = args.rc_build
        fixed_url = ""
    return source_url, destination, rc_build, fixed_url


def main():
    base_url, destination, rc_build, fixed_url = get_args()
    if fixed_url:
        download_file(fixed_url, destination)
        sys.exit(0)
    if rc_build:
        latest_image_url = get_file_url(base_url, look_for_pass=False)
    else:
        latest_image_url = get_file_url(base_url)
    download_file(latest_image_url, destination)
    sys.exit(0)


if __name__ == "__main__":
    main()
