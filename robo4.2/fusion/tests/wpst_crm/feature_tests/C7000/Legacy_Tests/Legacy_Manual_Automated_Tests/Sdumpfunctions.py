import sys
import itertools
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import logging
from robot.api import logger
import logging as _logging
import smtplib
import os
import tarfile
import time
import re
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders as Encoders
import platform

version_list = []


class SupportDump:

    def __init__(self):
        pass


def decrypt_and_extract_the_dump_file(src_dir, decryptor_path):
    logger.console('Extracting the support dump file')
    i = 1
    for filename in os.listdir(src_dir):
        while filename.endswith(".part"):
            logger.console("waiting %s seconds for the download to complete" % (i * 30))
            time.sleep(30)
            i = i + 1
            if i >= 240:
                logger.error("Took more than 2 hours to download , so failing the test case")
            if not os.path.isfile(src_dir + "//" + filename):
                logger.console("Download completed")
                break
    if (platform.system() == 'Windows'):
        extracting_decryted_file(r"decrypt-support-dump.bat", src_dir, decryptor_path)
    else:  # (platform.system() == 'Linux'): for linux
        extracting_decryted_file(r"decrypt-support-dump.sh", src_dir, decryptor_path, "linux")


def decryptor(filename, src_dir, decryptor_path, platform):
    privatekey = "private.key"
    executable_filename = os.path.join(decryptor_path, filename)
    print executable_filename
    privatekey = os.path.join(decryptor_path, privatekey)
    print privatekey
    dump_files = [filename for filename in os.listdir(src_dir) if filename.startswith("ci") and filename.endswith(".sdmp")]
    print dump_files
    logger.console("The length of dump_files is :%s" % len(dump_files))
    if len(dump_files) > 1 or len(dump_files) == 0:
        logger.error("No files or More than one dump files found ")
        return False
    src_file = os.path.join(src_dir, dump_files[0])
    print src_file
    if (platform == "linux"):
        logger.console("Entered into linux")
        if (os.system("sh " + executable_filename + " -f " + src_file + " -k " + privatekey)):
            logger.error("Exception occured during decryption in Linux platform")
            return False
    else:
        logger.console("Entered into Windows")
        decryption_without_private_key(src_file, executable_filename, platform)
        decryption_with_private_key(src_file, executable_filename, platform)
        if (os.system(executable_filename + " -f " + src_file + " -k " + privatekey)):
            logger.error("Exception occured during decryption in Windows platform")
            return False


def decryptor_error(filename, src_dir, decryptor_path, platform=None):
    privatekey = "private.key"
    executable_filename = os.path.join(decryptor_path, filename)
    privatekey = os.path.join(decryptor_path, privatekey)
    dump_files = [filename for filename in os.listdir(src_dir) if filename.startswith("ci") and filename.endswith(".sdmp")]
    logger.console("The length is :%s" % len(dump_files))
    if len(dump_files) > 1 or len(dump_files) == 0:
        logger.error("No files or More than one dump files found ")
        return False
    src_file = os.path.join(src_dir, dump_files[0])
    if (platform == "linux"):
        logger.console("Entered into linux")
        if (os.system("sh " + executable_filename + " -f " + src_file + " -k " + privatekey)):
            logger.error("Exception occured during decryption in Linux platform")
            return False
    else:
        if (os.system(executable_filename + " -f " + src_file + " -k " + privatekey)):
            logger.error("Decryption Error")
            return False


def decryption_without_private_key(src_file, executable_filename, platform):
    if (platform == "linux"):
        logger.console("Entered into linux")
        if (os.system("sh " + executable_filename + " -f " + src_file)):
            logger.info("valid command")
            return False
        else:
            logger.error("Invalid command")
            return False
    else:
        logger.console("Entered into Windows")
        if (os.system(executable_filename + " -f " + src_file)):
            logger.info("valid command")
            return False
        else:
            logger.error("Invalid command")
            return False


def decryption_with_private_key(src_file, executable_filename, platform):
    if (platform == "linux"):
        logger.console("Entered into linux")
        if (os.system("sh " + executable_filename + " -f " + src_file + " -k ")):
            logger.info("Private key is found")
            return False
        else:
            logger.error("Private key file is not found")
            return False
    else:
        logger.console("Entered into Windows")
        if (os.system(executable_filename + " -f " + src_file + " -k ")):
            logger.info("Private key is found")
            return False
        else:
            logger.error("Private key file is not found")
            return False


def appending_line(file):
    appendNew = '\nThis is the new line = "BE CONFIDENT OF WHO YOU ARE"'
    appendFile = open(file, 'a')
    appendFile.write(appendNew)
    appendFile.close()


def extracting_decryted_file(filename, src_dir, decryptor_path, platform=None):
    if not (decryptor_path == ""):
        decryptor(filename, src_dir, decryptor_path, platform)
        gzip_files = [filename for filename in os.listdir(src_dir) if filename.endswith('.tar.gz')]
    else:
        gzip_files = [filename for filename in os.listdir(src_dir) if filename.endswith('.sdmp')]
    logger.console("The length of gzip_files is :%s" % len(gzip_files))
    if len(gzip_files) > 1 or len(gzip_files) == 0:
        logger.error("No files or More than one gunzip files are found ")
    path = os.path.join(src_dir, gzip_files[0])
    opener, mode = tarfile.open, 'r:gz'
    logger.console("Extracting the file to :%s" % src_dir)
    os.chdir(src_dir)
    try:
        file = opener(path, mode)
        try:
            file.extractall()
        finally:
            file.close()
    finally:
        os.chdir(os.getcwd())


def validating_le_dump_files(src_dir):
    logger.console("Below are the support dump files found for logical enclosure")
    src_dir = os.path.join(src_dir, 'logical-enclosure')
    i = 0
    for subdir, dirs, files in os.walk(src_dir):
        for file in files:
            logger.info(os.path.join(subdir, file), also_console=True)
            i = i + 1
    if (i == 0):
        logger.error("No files found under %s " % src_dir)
        return False
    logger.info("Total number of files found under %s is %s" % (src_dir, i), also_console=True)


def readfile(filename):
    dump_file = open(filename, 'r')
    print dump_file.read()
    dump_file.close()


def rename(old_name, new_name):
    os.rename(old_name, new_name)
    print "The file renamed successfully"
    return new_name


def getSize(filename):
    sizeinfo = os.stat(filename)
    return sizeinfo.st_size

if __name__ == '__main__':
    src_dir = "C:\\Sandbox\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137-Hill\\Backup 3&6\\support_dump\\"
    decryptor_path = "C:\\Sandbox\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137-Hill\\Backup 3&6\\"
    s = decrypt_and_extract_the_dump_file(src_dir, decryptor_path)
    print s
