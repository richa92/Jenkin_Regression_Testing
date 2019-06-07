from robot.api import logger
import os
import tarfile
import time
import platform

version_list = []


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
        decryptor_extractor(r"decrypt-support-dump.bat", src_dir, decryptor_path)
    else:  # (platform.system() == 'Linux'):
        decryptor_extractor(r"decrypt-support-dump.sh", src_dir, decryptor_path, "linux")


def decryptor(filename, src_dir, decryptor_path, platform):
    privatekey = "private.key"
    executable_filename = os.path.join(decryptor_path, filename)
    privatekey = os.path.join(decryptor_path, privatekey)
    dump_files = [filename for filename in os.listdir(src_dir) if filename.startswith("fusion") and filename.endswith(".sdmp")]
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


def decryptor_extractor(filename, src_dir, decryptor_path, platform=None):
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
        dumpfile = opener(path, mode)
        try:
            dumpfile.extractall()
        finally:
            dumpfile.close()
    finally:
            os.chdir(os.getcwd())
