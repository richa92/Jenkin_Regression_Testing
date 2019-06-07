from RoboGalaxyLibrary.utilitylib import logging as logger
from tests.DEA.resource.iLO.PERISClient import PERISClient
from tests.DEA.resource.iLO import PE_ilo
import json
from robot.libraries.BuiltIn import BuiltIn
import requests
import time


class ILOAPIKeywords(object):

    def __init__(self):
        pass

    def login_ilo(self, host, cred=None, headers=None, legacy=False, odata_status=True):
        self.ilo_client, resp, sessionID = PE_ilo.login_ilo(host, cred, headers, legacy, odata_status)
        return resp, sessionID

    def login_ilo_ipv4(self, host, cred=None, headers=None, legacy=False):
        self.ilo_client, resp, sessionID = PE_ilo.login_ilo_ipv4(host, cred, headers, legacy)
        return resp, sessionID

    def logout_ilo(self):
        PE_ilo.delete_ilo_session(self.ilo_client)
        self.ilo_client.close_session()

    def ilo_ris_set_server_power(self, operation):
        """
        This keyword will set the server power via iLO RIS
        Usage example: ${Set_Power}=    iLO_RIS_Set_Server_Power    ${operation}
                      Returns the return code; hence verify response to be '200'
        """
        return PE_ilo.set_server_power(self.ilo_client, operation)

    def ilo_ris_del_users(self):
        """
        This keyword will delete the ilo user
        Usage example: ${Delete_user}=    ilo_ris_del_users
        """
        return PE_ilo.delete_ilo_users(self.ilo_client)

    def ilo_ris_del_user(self, user):
        """
        This keyword will delete the ilo user
        Usage example: ${Delete_user}=    ilo_ris_del_user  <user>
        """
        return PE_ilo.delete_ilo_user(self.ilo_client, user)

    def ilo_ris_get_object(self, uri):
        """
        This keyword gets the RIS object from the provided URI
        Usage example:  ${object}=    ilo_ris_get_object  URI
        """
        return PE_ilo.get_ris_object(self.ilo_client, uri)
        
    def ilo_ris_patch_object(self,mezzslot):
        """
        This keyword sets the RIS object from the provided URI
        Usage example:  ${object}=    ilo_ris_patch_object  URI  DATA
        """
        n= int(mezzslot)
        if n == 1:
            uri = "/redfish/v1/Chassis/1/Devices/1/"  
        elif n == 2:
            uri = "/redfish/v1/Chassis/1/Devices/2/"
        elif n == 3:
            uri = "/redfish/v1/Chassis/1/Devices/3/"
        elif n == 4:
            uri = "/redfish/v1/Chassis/1/Devices/4/"
        elif n == 5:
            uri = "/redfish/v1/Chassis/1/Devices/5/"
        elif n == 6:
            uri = "/redfish/v1/Chassis/1/Devices/6/"
        else:
            print("Provide URI in argument")
        payload = {'MCTPProtocolDisabled': True}
        return PE_ilo.patch_ris_object(self.ilo_client,uri, payload)
    
    def ilo_ris_post_object(self, uri):
        """
        This keyword posts the RIS object from the provided URI
        Usage example:  ${object}=    ilo_ris_post_object  URI  DATA
        """
        payload = { }
        return PE_ilo.post_ris_object(self.ilo_client, uri, payload)
    
    def ris_get_chassis_info(self):
        """
        This keyword gets the chassis info from RIS
        Usage example:  ${object}=    ris_get_chassis_info
        """
        return PE_ilo.get_chassis_info(self.ilo_client)

    def ilo_ris_get_provider_object(self, ptype):
        """
        This keyword gets the iLO provider object
        Usage example:  ${object}=    ilo ris get provider object    <type>
        """
        return PE_ilo.get_ilo_provider_object(self.ilo_client, ptype)

    def ilo_ris_show_blade_firmware_table(self):
        """
        This keyword will get Blade Firmware table to show on log file
        Usage example: ${Delete_user}=    ilo_show_blade_firmware_table
        """
        return PE_ilo.show_blade_firmware_table(self.ilo_client)

    def ilo_ris_update_firmware(self, fwUri):
        """ ilo_ris_update_firmware(self, fwUri):
        This keyword will update the iLO Firmware.
        Example:
        | ${response}=  |  ilo_ris_update_firmware  |  <firmware URI>  |
        """
        return PE_ilo.updateFirmware(self.ilo_client, fwUri)

    def ilo_ris_get_firmware_reset_flag(self):
        """ ilo_ris_get_firmware_reset_flag(self):
        This keyword will get the reset flag status of the iLO Firmware update.
        Example:
        | ${progress}=  |  ilo_ris_get_firmware_reset_flag  |
        """
        return PE_ilo.get_updateFirmware_reset_flag(self.ilo_client)

    def ilo_ris_reset_ilo(self):
        """ ilo_ris_update_firmware(self, fwUri):
        This keyword will update the iLO Firmware.
        Example:
        | ${response}=  |  ilo_ris_update_firmware  |  <firmware URI>  |
        """
        return PE_ilo.resetiLO(self.ilo_client)

    def ilo_ris_get_firmware_update_details(self):
        """ ilo_ris_get_firmware_update_details(self):
        This keyword will check if the iLO Firmware update is successful via details message.
        Example:
        | ${result}=  |  ilo_ris_get_firmware_update_details
        """
        return PE_ilo.get_updateFirmware_details(self.ilo_client)

    def ilo_ris_get_firmware_update_state(self):
        """ ilo_ris_get_firmware_update_state(self):
        This keyword will check if the iLO Firmware update is successful via state.
        Example:
        | ${result}=  |  ilo_ris_get_firmware_update_state  |
        """
        return PE_ilo.get_updateFirmware_state(self.ilo_client)

    def ilo_ris_get_firmware_update_progress(self):
        """ ilo_ris_get_firmware_update_state(self):
        This keyword will check if the iLO Firmware update is successful via state.
        Example:
        | ${result}=  |  ilo_ris_get_firmware_update_state  |
        """
        return PE_ilo.get_updateFirmware_progresspercent(self.ilo_client)

    def ilo_ris_fw_update_progress_status(self):
        """ This keyword will poll the iLO fw update progress status and state to make sure the update got to 100% """
        time.sleep(30)
        iLO_REBOOT_TIME = BuiltIn().get_variable_value("${iLO_Reboot_Time}")
        updateDetails = self.ilo_ris_get_firmware_update_details()
        updateState = self.ilo_ris_get_firmware_update_state()
        update_timeout = 0
        while updateDetails == "Firmware flash in progress" or updateState == 'PROGRESSING':
            time.sleep(3)
            update_timeout += 1
            # Exit out of function if FW update takes longer than 5 minutes
            if update_timeout >= 100:
                return False
            try:
                updateDetails = self.ilo_ris_get_firmware_update_details()
                updateState = self.ilo_ris_get_firmware_update_state()
            except:
                updateDetails = "Firmware flash completed"
                updateState = "COMPLETED"
        # Sleep here to wait for iLO to reboot after update
        time.sleep(iLO_REBOOT_TIME)
        return True

    def ilo_ris_get_sessions(self, username):
        """
        This keyword gets all sessions on ilo
        Usage example:  ${object}=   ilo_ris_get_sessions
        """
        return PE_ilo.get_ilo_session_number(self.ilo_client, username)

    def ilo_ris_get_ipv4(self):
        """
        This keyword gets ipv4 address from ethernet json
        Usage example:  ${ip}=   ilo_ris_get_ipv4
        """
        return PE_ilo.get_ilo_ipv4(self.ilo_client)

    def ilo_ris_get_mezz_uris(self):
        """
        This keyword gets the iLO mezz uri
        Usage example:  ${object}=    ilo_ris_get_mezz_uris    <>
        """
        return PE_ilo.get_mezz_uris(self.ilo_client)

    def ilo_ris_set_boot_order(self, boot_order):
        """ ilo_ris_update_firmware(self, fwUri):
        This keyword will update the iLO Firmware.
        Example:
        | ${response}=  |  ilo_ris_update_firmware  |  <firmware URI>  |
        """
        return PE_ilo.set_boot_order(self.ilo_client, boot_order)

    def ilo_ris_hphdbind(self, bin_path, fru_inst):
        """ ilo_ris_hphdbind(self, bin_path,fru_inst):
        This keyword will generate hphdbind command.
        Example:
        | ${response}=  |  ilo_ris_hphdbind(self, bin_path,fru_inst) |
        """
        return PE_ilo.hphdbind(bin_path, fru_inst)

    def ilo_ris_hpqlocfg(self, bin_path, ilo_ip, ilo_user, ilo_password):
        """ ilo_ris_hpqlocfg(self, bin_path,ilo_ip,ilo_user, ilo_password ):
        This keyword will generate hpqlocfg command.
        Example:
        | ${response}=  |  ilo_ris_hpqlocfg(self, bin_path,ilo_ip,ilo_user, ilo_password ) |
        """
        return PE_ilo.hpqlocfg(bin_path, ilo_ip, ilo_user, ilo_password)

    def ilo_ris_partnumber(self, mezz_slot):
        """ ilo_ris_partnumber(self, mezz_slot):
        This keyword will get part number.
        Example:
        | ${response}=  |  ilo_ris_partnumber(self, mezz_slot): |
        """
        return PE_ilo.get_mezz_partnumber(self.ilo_client, mezz_slot)

    def ilo_ris_fru_inst(self, mezz_part_number, mezz_slot):
        """ ilo_ris_fru_inst(self,  mezz_part_number, mezz_slot):
        This keyword will get instruction file.
        Example:
        | ${response}=  |  ilo_ris_fru_inst(self,  mezz_part_number, mezz_slot): |
        """
        return PE_ilo.get_fru_inst(mezz_part_number, mezz_slot)

    def ilo_ris_get_mezz_bin(self, mezz_type):
        """ ilo_ris_get_mezz_bin(self,  mezz_type):
        This keyword will get FRU bin from FRU utility.
        Example:
        | ${response}=  |  ilo_ris_get_mezz_bin(self,  mezz_type) |
        """
        return PE_ilo.get_mezz_bin(mezz_type)

    def ilo_ris_firmware_version(self):
        """ ilo_ris_get_firmware_update_state(self):
        This keyword will check if the iLO Firmware update is successful via state.
        Example:
        | ${result}=  |  ilo_ris_get_firmware_update_state  |
        """
        return PE_ilo.get_iLOFirmware_version(self.ilo_client)

    def ilo_ris_update_blade_canmic_gen10fru(self, ilo_ipv4, bin_path):
        """ ilo_ris_update_blade_canmic_gen10fru(self, ilo_ipv4, bin_path):
        This keyword will flash canmic fru for Gen10 blades
        Example:
        | ${response}=  |  ilo_ris_update_blade_canmic_gen10fru(self, ilo_ipv4, bin_path) |
        """
        return PE_ilo.update_blade_canmic_gen10fru(ilo_ipv4, bin_path)

    def ilo_ris_clear_ilo_iel_logs(self, ilo_ipv4):
        """ ilo_ris_clear_ilo_iel_logs(self, ilo_ipv4):
        This keyword will clear iLO IEL logs
        Example:
        | ${response}=  |  ilo_ris_clear_iel_logs(self, ilo_ipv4) |
        """
        return PE_ilo.clear_ilo_iel_logs(self.ilo_client, ilo_ipv4)

    def ilo_ris_get_iel_entry_messages(self, ilo_ipv4):
        """ ilo_ris_clear_ilo_iel_logs(self, ilo_ipv4):
        This keyword will clear iLO IEL logs
        Example:
        | ${response}=  |  ilo_ris_clear_iel_logs(self, ilo_ipv4) |
        """
        return PE_ilo.get_iel_entry_messages(self.ilo_client, ilo_ipv4)

    def ilo_get_server_power(self):
        """ ilo_get_server_power(self):
        This keyword will get the current server power state
        Example:
        | ${power_state}=  |  ilo_get_server_power(self) |
        """
        return PE_ilo.get_server_power(self.ilo_client)