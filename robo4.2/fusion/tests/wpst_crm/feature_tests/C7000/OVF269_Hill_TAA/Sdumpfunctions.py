import sys
#import variables
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
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import platform
#import remotelogin

version_list = []

class SupportDump:

	def __init__(self):	
		pass
		
def decrypt_and_extract_the_dump_file(src_dir, decryptor_path):
	logger.console('Extracting the support dump file')
	i = 1
	for filename in os.listdir(src_dir):
		while filename.endswith(".part"):
			logger.console("waiting %s seconds for the download to complete" % (i*30))
			time.sleep(30)
			i = i+1
			if i >= 240:
				logger.error("Took more than 2 hours to download , so failing the test case")
			if not os.path.isfile(src_dir + "//" + filename):
				logger.console("Download completed")
				break
	if (platform.system() == 'Windows'):
		decryptor_extractor(r"decrypt-support-dump.bat", src_dir, decryptor_path)
	else: #(platform.system() == 'Linux'):
		decryptor_extractor(r"decrypt-support-dump.sh", src_dir, decryptor_path, "linux")


def decryptor(filename, src_dir, decryptor_path, platform):
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
			logger.error("Exception occured during decryption in Windows platform")
			return False


def decryptor_extractor(filename, src_dir, decryptor_path, platform = None):
	if not (decryptor_path == ""):
		decryptor(filename, src_dir, decryptor_path, platform)
		gzip_files = [filename for filename in os.listdir(src_dir) if filename.endswith('.tar.gz')]
	else:
		gzip_files = [filename for filename in os.listdir(src_dir) if filename.endswith('.sdmp')]
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
			i = i+1
	if (i == 0):
		logger.error("No files found under %s " % src_dir)
		return False
	logger.info("Total no. of files found under %s is %s" % (src_dir, i), also_console=True)


def combinations(List, repeat_val):
	LIG_Combinations = itertools.product(List, repeat=repeat_val)
	LIG_LIST = list(LIG_Combinations)
	return LIG_LIST


def createegxml(EgName, Ligs_List_xml, Bay_list):
	enclosures = str(len(Ligs_List_xml))
	enclosuregroup = Element('enclosuregroup', name=EgName, enclosure_count=enclosures, ipv4_addresses="use dhcp")
	for eachLigIndex in range(0, len(Ligs_List_xml)):
		enclosure = SubElement(enclosuregroup, 'enclosure', no=str(eachLigIndex+1))
		for eachBay in Bay_list[eachLigIndex]:
			SubElement(enclosure, 'switch', bay=str(eachBay), lig=Ligs_List_xml[eachLigIndex])
	return (ElementTree.tostring(enclosuregroup))


def fetch_the_filename_and_return_version(dict):    
	if len(version_list) > 2 :
		del version_list[0:2]
		logger.console("Initialized the version list")
	if re.match("Smart Component for HPE Synergy 12Gb SAS Connection Module Firmware|Smart Component for HPE Synergy  D3940 Storage Module firmware", dict['name']):
		logger.console(dict['name'])
		version_list.append(dict['componentVersion'])
	return version_list

def change_the_natasha_properties_in_dcs(host,switchFW,encFW,firmware_timeout=90):
	dcs_properties_file = r'/dcs/conf/natasha_firmware_history_samples.properties'
	sshlogin = remotelogin.SSHUtils(host=host,user=r'root',password=r'hpvse1')
	sshlogin.remote_ssh(r"sed -i.bak 's/^\(%s=\).*/\1%s/' %s"%('switchFW', switchFW, dcs_properties_file))
	sshlogin.remote_ssh(r"sed -i.bak 's/^\(%s=\).*/\1%s/' %s"%('encFW', encFW, dcs_properties_file))
	sshlogin.remote_ssh(r"sed -i.bak 's/^\(%s=\).*/\1%s/' %s"%('time', firmware_timeout, dcs_properties_file))
	output = sshlogin.remote_ssh_output("cat %s"% dcs_properties_file )
	logger.console("The changed %s file \n %s"%(dcs_properties_file, output))

if __name__ == '__main__':
	src_dir = "C:\\Sandbox\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137-Hill\\Backup 3&6\\support_dump\\"
	decryptor_path = "C:\\Sandbox\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137-Hill\\Backup 3&6\\"
	s = decrypt_and_extract_the_dump_file(src_dir, decryptor_path)
	print s