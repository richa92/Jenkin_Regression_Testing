import sys
import os
import select
import paramiko
import errno
import shutil
import re
from RoboGalaxyLibrary.data.test_data import DataObj
from RoboGalaxyLibrary.utilitylib.logging import logger


class local_actions(object):
    def __init__(self):
        pass

    def create_folder(self, path, remove_old=False):
        path = path.strip().rstrip(os.path.sep)
        if os.path.exists(path):
            if remove_old is True:
                shutil.rmtree(path)
            else:
                return False, {'except_obj': 'Target folder "%s" is existing' % path, 'line': sys._getframe().f_lineno}
        os.makedirs(path)
        return True, None

    def list_all_files(self, path):
        files = []
        path = path.strip().rstrip(os.path.sep)
        if os.path.exists(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    files.append(os.path.join(dirpath, filename))
                if '.git' in dirnames:
                    dirnames.remove('.git')
        else:
            return False, {'except_obj': 'Target folder "%s" is not existing' % path, 'line': sys._getframe().f_lineno}
        return True, files

    def list_folder(self, path):
        content = []
        path = path.strip().rstrip(os.path.sep)
        if os.path.exists(path):
            for dirpath, dirnames, filenames in os.walk(path):
                if dirpath == path:
                    for dirname in dirnames:
                        dir = os.path.join(dirpath, dirname)
                        content.append({'name': dir, 'attr': 'd'})
                    for filename in filenames:
                        file = os.path.join(dirpath, filename)
                        content.append({'name': file, 'attr': 'f'})
                    break
        else:
            return False, {'except_obj': 'Target folder "%s" is not existing' % path, 'line': sys._getframe().f_lineno}
        return True, content

    def call_cmd(self):
        raise NotImplementedError()


class remote_actions(object):

    def __init__(self, host=None, username=None, password=None):
        self.connected = False

        if host and username and password:
            self.open_ssh(host, username, password)

    def open_ssh(self, host, username, password):
        # if call this method again when connection is keeping.
        # suppose we want to disconnect current SSH connection then connect to another host
        if self.connected is False:
            try:
                self.ssh = paramiko.SSHClient()
                self.sftp = None
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(host, username=username, password=password, look_for_keys=False)
                self.connected = True
                logger.debug("Connected to %s" % host)
            except Exception as e:
                self.connected = False
                logger.debug("Connected to %s failed with the exception %s" % (host, e.message))
        # close current connect & connect to another host
        else:
            self.close_ssh()
            self.open_ssh(host, username, password)

    def close_ssh(self):
        if self.connected is True:
            self._close_sftp()
            self.ssh.close()
            self.connected = False

    def _open_sftp(self):
        if self.sftp is None:
            self.sftp = self.ssh.open_sftp()

    def _close_sftp(self):
        if self.sftp is not None:
            self.sftp.close()
            self.sftp = None

    def call_cmd(self, cmd, realout=False):
        out = DataObj()
        out.add_property('stdout', None)
        out.add_property('stderr', None)
        out.add_property('code', 1)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        if realout is False:
            out.add_property('stdout', stdout.read())
            out.add_property('stderr', stdout.read())
        else:
            outputs = []
            while not stdout.channel.exit_status_ready():
                # Only print data if there is data to read in the channel
                if stdout.channel.recv_ready():
                    rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
                    if len(rl) > 0:
                        # Print data from stdout
                        data = stdout.channel.recv(1024)
                        outputs.append(data)
                        # logger.debug(data, also_console=True, newline=False, time_prefix=False)
                        logger.debug(data)
            else:
                data = stdout.channel.recv(1024)
                outputs.append(data)
                # logger._debug(data, also_console=True, newline=False, time_prefix=False)
                logger.debug(data)
            out.add_property('stdout', ''.join(outputs))
            out.add_property('stderr', stderr.read())
            # logger._debug('', time_prefix=False)
            logger.debug('')
        out.code = stdout.channel.recv_exit_status()
        return out

    def list_folder(self, folder_path):
        self._open_sftp()
        result = None
        try:
            result = self.sftp.listdir(folder_path)
        except IOError as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}

        return result, None

    def create_folder(self, path):
        self._open_sftp()
        path_list = path.split('/')
        for i in xrange(1, len(path_list)):
            path_to_create = '/'.join(path_list[0:i + 1])
            try:
                self.sftp.stat(path_to_create)
            except IOError as ex:
                if ex.errno == errno.ENOENT:
                    # create folder which not exist
                    self.sftp.mkdir(path_to_create)
                else:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}
        return True, None

    def download_file_to_local(self, remote_path, local_path):
        self._open_sftp()
        try:
            self.sftp.get(remote_path, local_path)
        except IOError as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}

        return True, None

    def download_folder_to_local(self, local_path, remote_path):
        local_path = local_path.strip().rstrip(os.path.sep)
        self._open_sftp()
        try:
            item_list = self.sftp.listdir(remote_path)
        except IOError as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}
        if not os.path.exists(local_path):
            local_actions().create_folder(local_path)

        for item in item_list:
            remote_file_path = "%s/%s" % (remote_path, item)
            local_file_path = "%s/%s" % (local_path, item)
            stat = self.sftp.stat(remote_file_path)
            if re.match('^dr.*', str(stat)):
                self.download_folder_to_local(local_file_path, remote_file_path)
            else:
                self.sftp.get(remote_file_path, local_file_path)
        return True, None

    def upload_file_from_local(self, local_path, remote_path):
        # check if local_path exists
        if not os.path.isfile(local_path):
            return False, {'except_obj': IOError("Specified :local_path '%s' not exist or not a file!" % local_path), 'line': sys._getframe().f_lineno}

        self._open_sftp()
        try:
            self.sftp.put(local_path, remote_path)
        except IOError as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}

        return True, None

    def upload_folder_from_local(self, local_path, remote_path):
        # check if local_path is a folder
        if not os.path.isdir(local_path):
            return False, {'except_obj': IOError("Specified :local_path '%s' not exist or not a folder!" % local_path), 'line': sys._getframe().f_lineno}

        self._open_sftp()

        # firstly create remote_path is not exist
        self.create_folder(remote_path)

        for dirpath, dirnames, filenames in os.walk(local_path):
            if dirnames:
                # create folder on remote
                for dirname in dirnames:
                    folder_to_create = os.path.join(remote_path, dirname).replace(os.path.sep, '/')
                    # create if not exist
                    try:
                        self.sftp.listdir(folder_to_create)
                    except IOError as ex:
                        if ex.errno == errno.ENOENT:
                            logger.debug("Creating folder '%s' on remote" % folder_to_create)
                            self.sftp.mkdir(folder_to_create)
                        else:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            return False, {'except_obj': ex, 'line': exc_tb.tb_lineno}

            if filenames:
                # do single upload
                for filename in filenames:
                    local_file_path = os.path.join(dirpath, filename).replace(os.path.sep, '/')
                    remote_file_path = os.path.join(remote_path, local_file_path.replace(os.path.sep, '/').replace(local_path.replace(os.path.sep, '/'), '').lstrip('/')).replace(os.path.sep, '/')
                    logger.debug("Uploading file on remote: '%s' => '%s'" % (local_file_path, remote_file_path))
                    self.sftp.put(local_file_path, remote_file_path)

        return True, None
