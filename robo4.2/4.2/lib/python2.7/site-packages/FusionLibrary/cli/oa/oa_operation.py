from FusionLibrary.libs.cli.cli_base import remote_actions
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import re


class OACLIKeywords(object):

    def _reset_blade(self, encl):
        timeout = 180  # timeout for each bay's RESET operation to complete
        cli = remote_actions(host=encl.oa1hostname, username=encl.oa1username, password=encl.oa1password)

        for bay in encl.bays.bay:
            out = cli.call_cmd("RESET SERVER %s" % bay.number, realout=True)
            output = out.stdout

            if out.code != 0:
                logger.warn("Failed to run 'RESET SERVER %s' on enclosure '%s' bay '%s'" % (bay.number, encl.name, bay.number))
                return False
            else:
                if re.search(r'Successfully reset the E-Fuse for device bay %s' % bay.number, output):
                    logger.info("'RESET SERVER %s' successfully performed on enclosure '%s' bay '%s'" % (bay.number, encl.name, bay.number), also_console=True)
                    # wait 10 seconds for the response of SHOW SERVER INFO <bay number> to really show the blade is being reset, otherwise the response still the old
                    # this is kind of like the response has been delayed for some seconds, which is not acting as the same as SSH to the OA and run the command via PUTTY
                    BuiltIn().sleep(10)
                    start = datetime.now()
                    while (datetime.now() - start).total_seconds() < timeout:
                        out = cli.call_cmd("SHOW SERVER INFO %s" % bay.number, realout=True)
                        output = out.stdout
                        if out.code != 0:
                            logger.warn("Failed to run 'SHOW SERVER INFO %s' on enclosure '%s' bay '%s'" % (bay.number, encl.name, bay.number))
                            return False
                        else:
                            if re.search(r'Product Name: %s' % bay.ProductName, output):
                                logger.info("'SHOW SERVER INFO %s' successfully got 'Product Name: %s' on enclosure '%s' bay '%s'" % (bay.number, bay.ProductName, encl.name, bay.number), also_console=True)
                                break
                            else:
                                logger.info("'Product Name: %s' not found from command 'SHOW SERVER INFO %s' on enclosure '%s' bay '%s', retrying ..." % (bay.ProductName, bay.number, encl.name, bay.number), also_console=True)
                                BuiltIn().sleep(0.5)
                                continue
                else:
                    logger.warn("Failed to perform 'RESET SERVER %s' on enclosure '%s' bay '%s'!" % (bay.number, encl.name, bay.number))
                    return False

        return True

    def update_oa_firmware(self, encl, timeout=300):
        if isinstance(encl, dict):
            encl = self.obj_dic(encl)
        logger.debug("Update OA [%s] firmware to [%s]" % (encl.hostname, encl.firmware_url))

        cli = remote_actions(host=encl.hostname, username=encl.username, password=encl.password)
        is_force = getattr(encl, "force_update", "").upper()
        cli.call_cmd("UPDATE IMAGE " + is_force + " " + encl.firmware_url)
        BuiltIn().sleep(timeout)

        return True

    def update_multi_oa_firmware(self, encls, timeout=300):
        logger.debug("Updating OA Firmwares")
        for n, encl in enumerate(encls):
            self.update_oa_firmware(encl, timeout)

        return True

    def clear_oa_vc_mode(self, encl, timeout=60):
        if isinstance(encl, dict):
            encl = self.obj_dic(encl)
        logger.debug("Clear OA [%s] VC Mode" % encl.hostname)

        cli = remote_actions(host=encl.hostname, username=encl.username, password=encl.password)
        vc = cli.call_cmd("CLEAR VCMODE")
        BuiltIn().sleep(timeout)

        return vc

    def restart_oa(self, encl, timeout=180):
        if isinstance(encl, dict):
            encl = self.obj_dic(encl)
        logger.debug("Restart OA [%s] VC Mode" % encl.hostname)

        cli = remote_actions(host=encl.hostname, username=encl.username, password=encl.password)
        res = cli.call_cmd("restart oa")
        BuiltIn().sleep(timeout)

        return res

    def power_off_all_blades(self, encl, timeout=100):
        if isinstance(encl, dict):
            encl = self.obj_dic(encl)
        cli = remote_actions(host=encl.hostname, username=encl.username, password=encl.password)
        pow = cli.call_cmd("poweroff server all")
        BuiltIn().sleep(timeout)

        return pow

    def clear_multi_oa_vc_mode(self, encls, timeout=60):
        logger.debug("Clear OA VC Modes")
        for n, encl in enumerate(encls):
            self.clear_oa_vc_mode(encl, timeout)

        return True

    def oa_cli_reset_blade(self, encl):
        if self._reset_blade(encl) is False:
            logger.warn("Failed to reset blade(s) on enclosure '%s'" % encl.oa1hostname)
            raise AssertionError
        else:
            logger.info("Successfully reset blade(s) on enclosure '%s'" % encl.oa1hostname)

    def remove_all_sso_certificates_blade(self, ilo):
        timeout = 20
        if isinstance(ilo, dict):
            ilo = self.obj_dic(ilo)
        cli = remote_actions(host=ilo.ilo, username=ilo.username, password=ilo.password)
        cli.call_cmd("cd /map1/oemhp_ssocfg1")
        out = cli.call_cmd("show")
        output = out.stdout
        index = re.findall("Record\[\d+\]", output)
        count = 0
        print len(index)
        for i in range(len(index)):
            ind = re.findall("\[\d+\]", index[i])
            ind1 = str(ind)
            ind2 = ind1.strip('[\'[]\']')
            out2 = cli.call_cmd("delete %s" % ind2)
            output2 = out2.stdout
            if re.findall("SSO Server record deleted", output2):
                logger.debug("Successfully deleted the certificate")
                BuiltIn().sleep(timeout)
                count += 1
        if count == len(index):
            return True
        else:
            return False

    def obj_dic(self, d):
        top = type('new', (object,), d)
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                setattr(top, i, self.obj_dic(j))
            elif isinstance(j, seqs):
                setattr(top, i, type(j)(self.obj_dic(sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                setattr(top, i, j)
        return top
