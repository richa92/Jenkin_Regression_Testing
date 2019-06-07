""" HAL API Keywords """
from RoboGalaxyLibrary.api.common import HPCIManager
from RoboGalaxyLibrary.utilitylib import logging as logger
import time


class HalAPIKeywords(object):
    """ HAL API Keywords """
    def __init__(self):
        self.fusion_client = HPCIManager.HPCIManager()

    # ----------------------------------------
    # Test webapp
    #   HAL API Perform Discover
    #   HAL API Perform Post Action
    #   HAL API Get DCS Resource
    # ----------------------------------------

    def hal_api_perform_discover(self, fusion_ip, em_ip, retries=5):
        """ Send a Discover rest call to the HAL Test Webapp on Fusion

        Example:
        | HAL API Perform Discover | ${FUSION_IP} | ${DCS EM IP} |
        | HAL API Perform Discover | ${FUSION_IP} | ${DCS EM IP} | 2 |
        """
        url = "https://%s/tbird/rest/resources/tbird/discover" % fusion_ip
        header = {'X-API-Version': "199",
                  "Auth": "H4HQfbczbdZTauvMTb667_6DIWLMxj0b",
                  "Accept-Language": "en.US",
                  "Content-Type": "application/json"
                  }

        # Payload
        data = {}
        data["ipAddress"] = em_ip
        # These parameters are suggested but do not seem required.
        # data["username"] = "admin"
        # data["password"] = "mypassword"
        # data["force"] = "false"

        # return self.fusion_client.post(url, data, header)
        # Retry in case rest call fails the first time.
        # Currently calls to the webapp fail intermittently when using a DCS enclosure.
        discovery_attempts = 0
        for _ in range(0, retries):
            discovery_attempts += 1
            response = self.fusion_client.post(url, data, header)
            if response['status'] == 'OK':
                break
            time.sleep(5)
        if discovery_attempts > 1:
            logger._warn("%d attempts were needed to properly discover the enclosure; this operation should only take one attempt." % discovery_attempts)
        return response

    def hal_api_perform_post_action(self, action=None, parameters=None, retries=5):
        """ Send a GET rest call to the HAL Test Webapp on Fusion

        Example:
        | HAL API Perform Post Action | ChassisUidControl | {"UidState":"on"} | |
        | HAL API Perform Post Action | ChassisMidplaneFruAction |  | 10 |
        """
        url = "/rest/tbird/performAction"
        header = {'X-API-Version': "199"}

        # Build Payload
        data = {}
        if action is not None:
            data["Action"] = action
        if parameters is not None:
            data["Parameters"] = parameters

        # Retry in case rest call fails.
        # Currently calls to the webapp fail intermittently.
        for _ in range(0, retries):
            response = self.fusion_client.post(url, data, header)
            if response['status'] == '200':
                break
            time.sleep(5)
        return response

    def hal_api_get_dcs_resource(self, em_ip, resource, retries=5):
        """ Send a GET rest call to the DCS API through the HAL Webapp

        Example:
        | HAL API Get DCS Resource | 172.18.8.101:2301 | rest/v1/BladeFru/1/ | |
        | HAL API Get DCS Resource | 172.18.8.101:2301 | rest/v1/Chassis/1/  | 10 |
        """
        # Build URL
        url = "/rest/tbird/raw?service=" + em_ip + "&resource=" + resource

        # Retry in case rest call fails.
        # Currently calls to the webapp fail intermittently.
        for _ in range(0, retries):
            response = self.fusion_client.get(url)
            if response['status'] == '200':
                break
            time.sleep(5)
        return response
