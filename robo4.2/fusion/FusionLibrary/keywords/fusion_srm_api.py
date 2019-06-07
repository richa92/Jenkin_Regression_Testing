"""
RoboGalaxyLibrary Fusion SRM API keywords
"""

from FusionLibrary.libs.api.ilo.ilo_client import IloClient
from FusionLibrary.libs.api.oa.oa_client import OaSoapClient
from RoboGalaxyLibrary.utilitylib import logging as logger
import tempfile
import ftplib
from urlparse import urlsplit
import os


class FusionSRMOaApiKeywords(object):
    """
    Fusion SRM API keywords
    """
    def __init__(self):
        self.oa_client = None

    def fusion_srm_oa_api_user_login(self, ip_address, username, password):
        """ User login on OA
        Example:
        | Fusion Srm OA API User Login | Administrator | password |
        """
        self.oa_client = OaSoapClient(ip_address, username, password)

    def fusion_srm_oa_api_get_blade_status(self, bay_numb):
        """ Get blade status from OA system and return as dictionary
        Example:
        | Fusion Srm OA API Get Blade Status | 1 |
        """
        return self.oa_client.get_blade_status(bay_numb)

    def fusion_srm_oa_api_set_blade_power(self, bay_numb, power_cmd):
        """ Get blade status from OA system and return as dictionary
        Example:
        | Fusion Srm OA API Set Blade Power | 1 |
        """
        self.oa_client.set_blade_power(bay_numb=bay_numb, power_cmd=power_cmd)

    def fusion_srm_oa_api_remove_all_hp_sim_certificates(self):
        """ Remove all hp sim(sso) certificates
        Example:
        | Fusion Srm OA API Remove All Hp Sim Certificates |
        """
        self.oa_client.remove_all_hp_sim_certificates()

    def fusion_srm_oa_api_remove_all_snmp_trap_receiver(self):
        """ Remove all snmp trap receiver
        Example:
        | Fusion Srm OA API Remove All Snmp Trap Receiver |
        """
        self.oa_client.remove_all_snmp_trap_receiver()

    def fusion_srm_oa_api_power_on_blade(self, bay_number):
        """ Power on 1 server blade
        Example:
        | Fusion Srm OA API Power On Blade |
        """
        self.oa_client.power_on_blade(bay_number)

    def fusion_srm_oa_api_power_off_blade(self, bay_number):
        """ Power off 1 server blades
        Example:
        | Fusion Srm OA API Power Off Blade |
        """
        self.oa_client.power_off_blade(bay_number)


class FusionSRMIloApiKeywords(object):
    """ SRM iLO API Keywords """
    def __init__(self):
        self.ilo_client = None

    def fusion_srm_ilo_api_init(self, hostname, login=None, password=None, timeout=60, port=443, protocol=None, delayed=False):
        """ Instantiate a IloClient object, perform login operation by various parameters
        Example:
        | Fusion Srm iLo API Init | wpst19ilo.vse.rdlabs.hpecorp.net | Administrator | password |
        """
        self.ilo_client = IloClient(hostname, login=login, password=password, timeout=timeout, port=port, protocol=protocol, delayed=delayed)

    def fusion_srm_ilo_api_delete_sso_cert_by_index(self, sso_idx):
        """ Delete a sso certificate of current logged iLo by specific index
        Example:
        | Fusion Srm Delete SSO Cert By Index | 1 |
        """
        self.ilo_client.delete_sso_cert_by_index(sso_idx)

    def fusion_srm_ilo_api_delete_all_sso_certs(self):
        """ Delete all SSO certificates of current logged iLo
        Example:
        | Fusion Srm Delete All Sso Certs |
        """
        self.ilo_client.delete_all_sso_certs()

    def fusion_srm_ilo_api_reset_rib(self):
        """ Reset the iLO/RILOE board of current logged iLo
        Example:
        | Fusion Srm Delete All Sso Certs |
        """
        logger.info("trying to reset iLO via 'ilo_client.reset_rib() ...'")
        if self.ilo_client.reset_rib() is True:
            logger.info("iLO '%s' reset is successfully done" % self.ilo_client.hostname)
            return True
        else:
            logger.warn("iLO '%s' reset is NOT successfully done" % self.ilo_client.hostname)
            return False

    def fusion_srm_ilo_update_firmware(self, fw_url):
        """ Update the iLO Firmware
        Example:
        | Fusion SRM iLO Update Firmware | firmware URL |
        """
        assert fw_url.count("ftp://") > 0, "Only FTP URL's supported"
        # Retrieve file into a temp file
        [_, tempfwbin] = tempfile.mkstemp()
        tempfwbin = '%s.bin' % tempfwbin
        #
        # could not get urllib2 to retrieve anonymous ftp://waco.rsn.hp.com url's
        # try:
        #     response = urllib2.urlopen( fw_url )
        # except urllib2.URLError, e:
        #     print e.reason
        #     exit
        # shutil.copyfileobj( response, handle )
        #

        try:
            U = urlsplit(fw_url)
            ftp = ftplib.FTP(U.netloc)
            # Assume anonymous login
            ftp.login()
            ftp.cwd(os.path.dirname(U.path))
            ftp.retrbinary(
                "RETR " + os.path.basename(U.path), open(tempfwbin, 'wb').write)
            ftp.quit()
        except Exception as e:
            logger.warn(e)
            return False

        # self._connect()
        # self.ilo_client.connect()
        try:
            self.ilo_client.update_rib_firmware(tempfwbin, progress=logger.info)
        except Exception as e:
            logger.warn(e)
            return False

        return True
