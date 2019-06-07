from FusionLibrary.libs.cli.cli_base import remote_actions
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import re
import json


class FusionCLIKeywords(object):

    def run_multi_cmd(self, appliance_ip, ssh_username, ssh_password, commands, interval='2s'):
        cli = remote_actions(host=appliance_ip, username=ssh_username, password=ssh_password)
        logger.debug("start running commands on appliance")
        out = ""
        for command in commands:
            logger.debug(command)
            rc = cli.call_cmd(command, realout=False)
            logger.debug(rc.stdout)
            out = out + rc.stdout + "\n"
            BuiltIn().sleep(interval)
        cli.close_ssh()
        return out

    def run_ssh_cmd(self, appliance_ip, ssh_username, ssh_password, command):
        cli = remote_actions(host=appliance_ip, username=ssh_username, password=ssh_password)
        logger.debug("start running commands on SSH server")
        logger.debug(command)
        rc = cli.call_cmd(command, realout=False)
        cli.close_ssh()
        return rc.stdout.strip('\n')

    def scp_local_to_remote(self, appliance_ip, ssh_username, ssh_password, local_path, remote_path):
        s = remote_actions(host=appliance_ip, username=ssh_username, password=ssh_password)
        rc = s.upload_file_from_local(local_path, remote_path)
        return rc

    def scp_remote_to_local(self, appliance_ip, ssh_username, ssh_password, remote_path, local_path):
        s = remote_actions(host=appliance_ip, username=ssh_username, password=ssh_password)
        rc = s.download_file_to_local(remote_path, local_path)
        return rc

    def check_ssh_to_console(self, ip, username, password):
        cli = remote_actions(host=ip, username=username, password=password)
        login = True if cli.connected else False
        cli.close_ssh()
        return login

    def _add_firmware_bundle(self, appliance_ip, ssh_username, ssh_password, spp_file_name, spp_file_path, spp_file_md5, auth, firmware_bundle_uri):

        cli = remote_actions(host=appliance_ip, username=ssh_username, password=ssh_password)

        # check if Firmware Bundle already added into OneView
        cmd = 'curl -m 1200 -k -X GET -H "Accept: application/json" -H "auth:%s" -H "X-API-Version:300" https://%s%s' % (auth, appliance_ip, firmware_bundle_uri)
        logger.debug("send API GET request to check if Firmware Bundle <%s - %s> already exists in OneView's Firmware Bundle repo" % (spp_file_name, firmware_bundle_uri))
        rc = cli.call_cmd(cmd, realout=False)
        output = rc.stdout

        if json.loads(output).get('uri') == firmware_bundle_uri:
            logger.warn("Firmware Bundle <%s - %s> already exists in OneView's Firmware Bundle repo, "
                        "skipped to post SPP iso file to OneView FB repo" % (spp_file_name, firmware_bundle_uri))
            cli.close_ssh()
            return True

        require_download = True
        # check if SPP iso file already exists in Appliance's local directory (not OneView FWB repo)
        cmd = 'ls | grep %s' % spp_file_name
        logger.debug("check if SPP file <%s> already exists in appliance's local directory" % spp_file_name)
        rc = cli.call_cmd(cmd, realout=True)
        output = rc.stdout
        if rc.code != 0:
            logger.debug("SPP file <%s> does not exist in appliance's local directory" % spp_file_name)
        else:
            if re.search(spp_file_name, output):
                logger.debug("SPP file <%s> already exists in appliance's local directory, will check md5 first" % spp_file_name)
                cmd = 'md5sum %s' % spp_file_name
                rc = cli.call_cmd(cmd, realout=True)
                output = rc.stdout
                if rc.code != 0:
                    logger.warn("failed to run command <%s>" % cmd)
                    cli.close_ssh()
                    return False
                else:
                    if re.search(spp_file_md5, output):
                        logger.debug("existed SPP iso file <%s> validate successfully" % spp_file_name)
                        require_download = False
                    else:
                        logger.debug("SPP iso file <%s> validate failed, need remove and download again" % spp_file_name)
                        cmd = 'rm -rf %s' % spp_file_name
                        logger.debug("try to delete SPP file <%s>" % spp_file_name)
                        rc = cli.call_cmd(cmd, realout=True)
                        if rc.code != 0:
                            logger.warn("failed to delete SPP file <%s> via command <%s>, please check or delete it manually" % (spp_file_name, cmd))
                            cli.close_ssh()
                            return False
            else:
                logger.warn("failed to search <{0}> from the output <{1}> of listing existing iso files via  <ls | grep {0}>".format(spp_file_name, output))
                cli.close_ssh()
                return False

        # download SPP iso file from shared location
        if require_download is True:
            cmd = 'wget  -q %s%s' % (spp_file_path, spp_file_name)
            logger.debug("start downloading SPP iso file <%s> ......" % spp_file_name)
            rc = cli.call_cmd(cmd, realout=True)
            if rc.code != 0:
                logger.warn("failed to run download SPP iso file command <%s>" % cmd)
                cli.close_ssh()
                return False
            else:
                cmd = 'md5sum %s' % spp_file_name
                rc = cli.call_cmd(cmd, realout=True)
                output = rc.stdout
                if rc.code != 0:
                    logger.warn("failed to run command <%s>" % cmd)
                    cli.close_ssh()
                    return False
                else:
                    if re.search(spp_file_md5, output):
                        logger.debug("successfully downloaded SPP iso file <%s>" % spp_file_name)
                    else:
                        logger.warn("failed to download SPP iso file <%s>, md5 should be <%s>, but <%s>" % (spp_file_name, spp_file_md5, output))
                        return False

        # send API POST request to pose SPP iso file into OneView FWB repo
        cmd = 'curl -m 1200 -k -X POST -H "Accept: application/json" -H "auth:%s" -H "uploadfilename:%s" -H "X-API-Version:300" -F file="@/root/%s" https://%s/rest/firmware-bundles' % (auth, spp_file_name, spp_file_name, appliance_ip)
        logger.debug("send API POST request to post SPP iso file <%s> to OneView's Firmware Bundle repo ......" % spp_file_name)
        rc = cli.call_cmd(cmd, realout=True)
        output = rc.stdout
        if rc.code != 0:
            logger.warn("failed to run cmd <%s>" % cmd)
            cli.close_ssh()
            return False
        else:
            task_uri = json.loads(output).get('uri')
            if task_uri is None:
                message = json.loads(output).get('message')
                logger.warn("an error occur when upload SPP: <%s>" % message)
                return False
            cmd = 'curl -m 1200 -k -X GET -H "Accept: application/json" -H "auth:%s" -H "X-API-Version:300" https://%s%s' % (auth, appliance_ip, task_uri)
            timeout = 300
            start = datetime.now()
            while (datetime.now() - start).total_seconds() < timeout:
                stdin, stdout, stderr = cli.ssh.exec_command(cmd)
                output = stdout.readlines()[0]
                if json.loads(output).get('errorCode') is not None:
                    msg = ' ' * 7 + '\n{}'.format(' ' * 8).join(output.split(','))
                    logger.warn("failed to run cmd <%s>, error message is: \n%s" % (cmd, msg))
                    cli.close_ssh()
                    return False
                else:
                    resp = json.loads(output)
                    if resp.get('taskState') == 'Completed' and resp.get('uri') == task_uri:
                        logger.debug("successfully posted Firmware Bundle <%s - %s> to OneView" % (spp_file_name, firmware_bundle_uri))
                        cli.close_ssh()
                        return True
                    elif resp.get('taskState') == 'Error' and resp.get('uri') == task_uri:
                        task_state = resp.get('taskState')
                        logger.warn("task of add Firmware Bundle <%s - %s> failed with (taskState: <%s>), return false ... " % (spp_file_name, firmware_bundle_uri, task_state))
                        cli.close_ssh()
                        return False
                    else:
                        task_state = resp.get('taskState')
                        logger.debug("task of add Firmware Bundle <%s - %s> still running (taskState: <%s>), keep waiting ... " % (spp_file_name, firmware_bundle_uri, task_state))
                        BuiltIn().sleep(15)
                        continue
            else:
                logger.warn("failed to wait for the task of adding Firmware Bundle <%s - %s> "
                            "completed within <%s> seconds" % (spp_file_name, firmware_bundle_uri, timeout))
                cli.close_ssh()
                return False

    def fusion_cli_add_firmware_bundle(self, appliance_ip, ssh_credentials, auth, firmware_bundles, fail_if_false=True):
        """
            This is to add Firmware Bundle(s) via CLI:
                - SSH login to OneView host,
                - download SPP iso file to local directory via wget, and validate file MD5,
                - send RESTful API POST request to post iso file to OneView's Firmware Bundle repo,
                - check the task(s) of add firmware bundle(s)
        :param appliance_ip:
        :param ssh_credentials: {'userName': 'root', 'password': 'hpvse1'}
        :param auth: auth of an logged in user session, can be retrieved by
                        ${resp}   ${auth} =     Fusion API Login Appliance    ${APPLIANCE_IP}       ${admin_credential}
        :param firmware_bundles: a list of firmware bundles to be added into OneView
        :param fail_if_false: if upload failed, not fail the test
                [Data example]
                    Firmware_Bundles = [
                        {
                            'SPPFileName': 'SPP2016020.2015_1204.63.iso',
                            'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/2016.02.0\ Gen9Snap5/Released/',
                            'SPPFileMD5': 'f8eb9835e5698b9daaea4e66eaa964db',
                            'FirmwareBundleURI': '/rest/firmware-drivers/SPP2016020_2015_1204_63',
                        },
                        {
                            'SPPFileName': 'SPPgen9snap6.2016_0510.105.iso',
                            'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
                            'SPPFileMD5': 'c2e3d4bc2290619041fe0ceeb8364c34',
                            'FirmwareBundleURI': '/rest/firmware-drivers/SPPgen9snap6_2016_0510_105',
                        },
                    ]
        :return:

            [Example]
            ${status} = Fusion CLI Add Firmware Bundle | <applianec_ip> | <ssh_credentials> | <auth> | <firmware_bundles> | <fail_if_false>
        """

        ssh_username = ssh_credentials['userName']
        ssh_password = ssh_credentials['password']
        for fb in firmware_bundles:
            spp_file_name = fb['SPPFileName']
            spp_file_path = fb['SPPFilePath']
            spp_file_md5 = fb['SPPFileMD5']
            firmware_bundle_uri = fb['FirmwareBundleURI']
            if not self._add_firmware_bundle(appliance_ip, ssh_username, ssh_password, spp_file_name, spp_file_path, spp_file_md5, auth, firmware_bundle_uri):
                msg = "failed to add Firmware Bundle from SPP file <%s>" % spp_file_name
                logger.warn(msg)
                if fail_if_false is True:
                    BuiltIn.fail(msg)
                    raise AssertionError
                return False
            else:
                logger.debug("successfully added Firmware Bundle from SPP file <%s>" % spp_file_name)

        return True

    def _get_feature_toggles_by_features(self, features, featureTogglesMapping):
        """
        This is used to get feature toggles from datafile by feature name
        Args:
            features: features need to be tested
            featureTogglesMapping: Dictionary with key-feature and value-toggles

        Returns: Toggles
        """
        toggles = []
        features = features.strip().split(",")
        for feature in features:
            if feature in featureTogglesMapping:
                logger.info("Adding %s feature toggles to list." % feature)
                toggles.extend(featureTogglesMapping[feature])
            else:
                logger.info("No feature toggles found for %s" % feature)
        logger.info("Deleting the duplicate toggles.")
        toggles = list(set(toggles))
        return toggles

    def fusion_cli_enable_feature_toggles(self, appliance_ip, features, featureTogglesMapping, ssh_credentials):
        """
        This is used to enable feature toggles for features to be tested
        Returns:

        """
        cmds = []
        ssh_username = ssh_credentials['userName']
        ssh_password = ssh_credentials['password']
        toggles = self._get_feature_toggles_by_features(features, featureTogglesMapping)
        if not toggles:
            logger.info("No toggles need to be enabled.")
            return False
        else:
            logger.info("Setting feature toggles: Starting")
            cmds.append("/ci/bin/set-feature-toggles -n -e %s" % " -e ".join(toggles))
            self.run_multi_cmd(appliance_ip, ssh_username, ssh_password, cmds, interval="2s")
            logger.info("Setting feature toggles: Done. Need to reboot the appliance")

        return True

    def populate_role_flag(self, features, populates):
        """This flag is used to control whether to populate the role"""
        for populate in populates:
            if populate in features:
                logger.info("%s needs to populate the role." % populate)
                return True
        return False
