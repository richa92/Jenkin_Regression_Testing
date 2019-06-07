#!/usr/local/bin/python
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

class LoginPEMClass(object):

    def set_header_to_pem_token(self, host, cred, pem_token):
        """Replace and assign Fusion Login object with PEM host, credential and custom token
        [Arguments]
            host: the appliance IP or hostname
            cred: a ditionary containing userName and password attributes
        [Example]
            ${resp} = set_header_to_pem_token | <host> | <cred> | <pem_token> |<headers>
        """
        # Create object to inherit Fusion Library
        obj = BuiltIn().get_library_instance("FusionLibrary")

        # Replacing using PEM values
        obj.fusion_client._host = host
        obj.fusion_client._cred = cred
        obj.fusion_client._http.headers['auth'] = pem_token
