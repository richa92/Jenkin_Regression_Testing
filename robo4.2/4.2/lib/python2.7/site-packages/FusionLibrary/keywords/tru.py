# pylint: disable=line-too-long
"""
tru.py

robotframework accessible keywords to execute T-Bird Recipe Utility (TRU) on CIM

(C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
from functools import wraps
from os import path, remove
import re
import unittest
from robot.api.deco import keyword
from SSHLibrary import SSHLibrary
from RoboGalaxyLibrary.common import exceptions
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.keywords.github import GitHubKeywords


TRU_REPO_URL = 'OneView-TestTools/tru'
TRU_LOCAL_FILENAME = 'tru.zip'


def ssh_request_should_succeed(decorated):
    """
    Decorator which ensures that the ssh request does not contain any failure strings in the output,
    throws NonFatalError if failure signatures are found
    :param decorated:
    :return:
    """
    @wraps(decorated)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for ssh connection request
        """
        output = decorated(self, *args, **kwargs)
        failures = re.compile('(?i)error|fail')
        if output and failures.search(output):
            raise exceptions.NonFatalError(
                'SSH command(s) failed. {}'.format(output))
    return wrapper


def connected(decorated):
    """
    Decorator which ensures that the SSH connection has been established
    """
    @wraps(decorated)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to ensure connection has been established """
        if not self.ssh or not self.connection_index:
            raise AssertionError('No SSH connection to host')
        return decorated(self, *args, **kwargs)
    return wrapper


class TRUKeywords(object):

    """
    TRU Keywords which abstract execution of TRU (T-Bird Recipe Utility) on the CIM
    """

    def __init__(self):
        self.host = None
        self.connection_index = None
        self.ssh = None
        self.tru_filename = TRU_LOCAL_FILENAME

    def __del__(self):
        if self.connection_index and self.ssh:
            self.ssh.close_all_connections()
            self.ssh = None
            self.connection_index = None
            self.host = None

    @ssh_request_should_succeed
    def _create_and_login(self, host, username='root', password='hpvse1'):
        """ Create a connection and login """
        self.host = host
        try:
            self.ssh = SSHLibrary()
            self.ssh.set_default_configuration(timeout='30 seconds')
            self.connection_index = self.ssh.open_connection(self.host)
            return self.ssh.login(username, password)
        except:
            raise exceptions.NonFatalError("Failed to successfully login via ssh to %s" % host)

    @staticmethod
    @keyword("Download TRU")
    def download_tru(version='master', file_name=None, file_type='zipball'):
        """
        Retrieve the TRU zip from GitHub - default is latest\n
        :param: version - the version to download.\n

        Examples:

            | =Keyword= | =Version= | =File Name= | =File Type= |
            | Download TRU |
            | Download TRU | 2.1.1.20 |
            | Download TRU | 2.1.1.24 | tru.zip | zipball |
            | Download TRU | 2.1.1.24 | tru.tgz | tarball |
        """
        file_path = GitHubKeywords.download_release(repo=TRU_REPO_URL, file_name=file_name, version=version, file_type=file_type)
        logger.debug('Downloaded TRU {} to {}'.format(version, file_path))
        return file_path

    @ssh_request_should_succeed
    @connected
    def _copy_tru_to_host(self, file_name, destination_file_name=TRU_LOCAL_FILENAME):
        """ Copy the TRU zip file to the host """
        return self.ssh.put_file(file_name, destination_file_name)

    @ssh_request_should_succeed
    @connected
    def _unzip_tru_on_host(self):
        """ Unzip the TRU zipfile on the host """
        self.ssh.execute_command("""unzip -o {} && mv OneView-TestTools-tru* tru""".format(TRU_LOCAL_FILENAME))

    @connected
    def _run_tru_on_host(self, oneview_admin_password=None, recipe_file=None):
        """ Execute TRU on the host with the -c -d -e parameters """
        if not oneview_admin_password:
            raise exceptions.NonFatalError('No OneView admin password provided.')

        # write an informational message
        msg = 'Running TRU on {}'.format(self.host)
        if recipe_file:
            msg += ' with recipe file {}'.format(recipe_file)
        logger.info(msg)

        # build the command (need to account for -c option if no recipe file is provided)
        command = """cd tru && python3 tbrUtility.py {} -d -e -op {}""".format(
            '-c' if recipe_file is None else '',
            oneview_admin_password
        )

        # add the recipe file if necessary
        if recipe_file:
            command += ' recipes/{}'.format(recipe_file)
        else:
            command += ' && find -maxdepth 1 -type d -name "tru_report*" -printf "%f" | xargs -I{{}} mv {{}} {}_{{}}'

        # run tru
        logger.debug(command)
        return self.ssh.execute_command(
            command,
            return_rc=True,
            return_stdout=True,
            return_stderr=True
        )

    @connected
    def _retrieve_tru_results(self):
        """
        Download the TRU results folder(s) from the host
        """
        files = []
        for folder in self.ssh.list_directories_in_directory('tru', pattern='*tru_report*'):
            zipfile = '{}.zip'.format(folder)
            self.ssh.execute_command('cd tru && zip -r {} {}'.format(zipfile, folder))
            self.ssh.get_file(source='tru/{}'.format(zipfile), destination='.')
            if not path.exists(zipfile):
                raise exceptions.NonFatalError('Failed to download {} from {}'.format(zipfile, self.host))
            self.ssh.execute_command('rm -f {}'.format(zipfile))
            logger.debug('Retreived {}'.format(zipfile))
            files.append(zipfile)
        return files

    @keyword(name='Run TRU and Retrieve Results')
    def run_tru_and_retrieve_results(self, host=None, username='root', password='hpvse1', oneview_admin_password='hpvse123', tru_version='master', recipe_file=None, log_stdout=True):  # pylint: disable=too-many-arguments
        """
        Execute TRU on the remote CIM and retrieve the results\n
        :param host: The CIM IP or hostname\n
        :param username: [optional] The CIM username (defaults to root)\n
        :param password: [optional] The CIM password\n (defaults to hpvse1)\n
        :param oneview_admin_password: [optional The OneView Administrator password (defaults to hpvse123)\n
        :param tru_version: [optional] The version of TRU to use (defaults to latest)\n
        :param log_stdout: [optional] Log the TRU output (defaults to True)\n

        Examples:

            | =Keyword= | =Host= | =CIM Username= | =CIM Password= | =OV Administrator Password= | =TRU Version= | =Recipe File= | =Log to stdout= |
            | Run TRU and Retrieve Results | 16.45.23.22 |
            | Run TRU and Retrieve Results | 16.45.23.22 | root | hpvse1 | hpvse123 |
            | Run TRU and Retrieve Results | 16.45.23.22 | root | hpvse1 | hpvse123 | 2.1.1.24 | RecipeF4.rcp |
            | Run TRU and Retrieve Results | 16.45.23.22 | root | hpvse1 | hpvse123 | 2.1.1.24 | RecipeF4.rcp | True |
        """
        self.host = host

        # get TRU from GHE
        file_name = self.download_tru(version=tru_version)

        # copy the zipball to the CIM
        self._create_and_login(host, username, password)
        self._copy_tru_to_host(file_name)

        # remove up the local copy
        remove(file_name)

        # unzip and run
        self._unzip_tru_on_host()
        stdout, stderr, return_code = self._run_tru_on_host(oneview_admin_password, recipe_file)

        # process output
        if log_stdout:
            logger.info(stdout)
        if re.match('(?i)warn', stdout):
            logger.warn("TRU encountered warnings.  Please see results for more information.")
        if re.match('(?i)error', stdout):
            logger.warn("TRU encountered errors.  Please see results for more information.")
        if stderr:
            logger.warn("TRU had stderr output.  Please see results for more information.")
        if return_code != 0:
            logger.warn("TRU had non-zero exit status.  Please see results for more information.")
        return self._retrieve_tru_results()


class TruTests(unittest.TestCase):

    """ Unit tests for TRUKeywords """

    def test_download_latest(self):
        """ Test latest versions """
        # all defaults
        filename = TRUKeywords.download_tru()
        self.assertTrue(path.exists(filename))
        remove(filename)

        # explicitly named
        filename = TRUKeywords.download_tru(file_name='tru.zip')
        self.assertTrue(path.exists('tru.zip'))
        remove(filename)

        # latest tar version
        ret_file_path = TRUKeywords.download_tru(file_type='tarball')
        self.assertTrue(path.exists(ret_file_path))
        if path.exists(ret_file_path):
            remove(ret_file_path)

        # latest zip version
        file_path = TRUKeywords.download_tru()
        self.assertTrue(path.exists(file_path))
        if path.exists(file_path):
            remove(file_path)

    def test_download_specific(self):
        """ Test specific versions """
        # specific zip version
        version = '2.1.1.20'
        file_name = 'tru-{}.zip'.format(version)
        if path.exists(file_name):
            remove(file_name)
        ret_fn = TRUKeywords.download_tru(version=version, file_name=file_name)
        self.assertEqual(path.basename(ret_fn), file_name)
        self.assertTrue(path.exists(file_name))
        if path.exists(file_name):
            remove(file_name)

        # specific tar version
        version = '2.1.1.22'
        file_name = 'tru-{}.tar'.format(version)
        if path.exists(file_name):
            remove(file_name)
        ret_file_path = TRUKeywords.download_tru(version=version, file_name=file_name, file_type='tarball')
        self.assertEqual(path.abspath(file_name), ret_file_path)
        self.assertTrue(path.exists(file_name))
        if path.exists(file_name):
            remove(file_name)

    def test_run_tru(self):
        """ Test full run and retrieval """
        tru_kw = TRUKeywords()
        tru_kw.run_tru_and_retrieve_results(host='16.114.208.62', username='root', password='hpvse1', oneview_admin_password='hpvse123')
        for zipfile in tru_kw._retrieve_tru_results():  # pylint: disable=protected-access
            self.assertTrue(path.exists(zipfile))
            remove(zipfile)


if __name__ == '__main__':
    unittest.main()
