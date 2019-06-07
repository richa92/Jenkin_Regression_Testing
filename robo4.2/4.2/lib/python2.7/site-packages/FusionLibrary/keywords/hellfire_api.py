"""
FusionLibrary Hellfile API keywords
"""
from FusionLibrary.api.common.request import HttpVerbs
from FusionLibrary.api.hellfire.svmc import Svmc
from FusionLibrary.api.hellfire.infrastructure_vms import InfrastructureVms
from FusionLibrary.api.hellfire.sdirm import StoreVirtualVsaCluster


class HellfireAPIKeywords(object):
    """Library for all Hellfire API keywords."""

    class InfrastructureVmsKeywords(object):
        """ Infra VM keywords """

        def __init__(self):
            self.infra_vms = InfrastructureVms(self.fusion_client)

        def fusion_api_get_infrastructure_vms(self, uri=None, param='', api=None, headers=None):
            """Gets a infrastructure vm.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Infrastructure Vms  | <uri> | <param> | <api> | <headers>
            """
            return self.infra_vms.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_infrastructure_vms(self, body, api=None, headers=None):
            """Creates a infrastructure vm.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Infrastructure Vms  | <body> | <api> | <headers>
            """
            return self.infra_vms.create(body=body, api=api, headers=headers)

        def fusion_api_update_infrastructure_vms(self, body=None, uri=None, api=None, headers=None):
            """Updates a Infrastructure Vm.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Infrastructure Vms  | <uri> | <param> | <api> | <headers>
            """
            return self.infra_vms.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_infrastructure_vms(self, name=None, uri=None, api=None, headers=None):
            """Deletes a Infrastructure Vm.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Delete Infrastructure Vms  | <uri> | <param> | <api> | <headers>
            """
            return self.infra_vms.delete(name=name, uri=uri, api=api, headers=headers)

    class StoreVirtualVsaClusterKeywords(object):
        """ StoreVirtuale VSA Cluster """
        def __init__(self):
            self.sdi_system_profiles = StoreVirtualVsaCluster(self.fusion_client)

        def fusion_api_get_sdi_system_profiles(self, uri=None, param='', api=None, headers=None):
            """Gets a sdi_system_profiles.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Sdi System Profiles  | <uri> | <param> | <api> | <headers>
            """
            return self.sdi_system_profiles.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_sdi_system_profiles(self, body, api=None, headers=None):
            """Creates a sdi_system_profiles.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Sdi System Profiles  | <body> | <api> | <headers>
            """
            return self.sdi_system_profiles.create(body=body, api=api, headers=headers)

        def fusion_api_update_sdi_system_profiles(self, body=None, uri=None, api=None, headers=None):
            """Updates a sdi_system_profiles.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Sdi System Profiles  | <uri> | <param> | <api> | <headers>
            """
            return self.sdi_system_profiles.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_sdi_system_profiles(self, name=None, uri=None, api=None, headers=None):
            """Deletes a sdi_system_profiles.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Delete Sdi System Profiles  | <uri> | <param> | <api> | <headers>
            """
            return self.sdi_system_profiles.delete(name=name, uri=uri, api=api, headers=headers)


class SVMCAPIKeywords(object):

    """Library for all SVMC Hellfire API keywords.

    = Table of contents =

    - `Usage`
    - `Examples`
    - `Importing`
    - `Keywords`

    = Usage =

    This library contains all of the SVMC Hellfire specific API keywords. All keywords allow the user to specify the ${X_API_VERSION},
    and to override the default request headers.  Therefore, these are not documented within each keyword.

    = Examples =

    Each section has its own example section, but here is a basic example:

    | `SVMC API Get Credemtials`       | ${SVMC_IP} | ${admin_credentials} |               |
    | `SVMC API Get Clusters' |                 |                      |               |

    = generic keywords =

    """

    def __init__(self):
        self.svmc_client = HttpVerbs()
        self.svmcsystem = Svmc(self.svmc_client)

    def svmc_get_resource(self, uri, host, api=None, headers=None):
        """ Returns any single resource by uri

        `generic keywords`
           Example:
           | ${resource} =  | Get Resource | <uri> | <api> | <headers> |
        """
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        self.svmc_client._host = host
        uri = 'https://%s/svmc/%s' % (self.svmc_client._host, uri)
        return self.svmcsystem.get(uri=uri, api=api, headers=headers)

    def svmc_delete_resource(self, uri, host, api=None, headers=None):
        """ Deletes any single hellfire resource by uri
           Example:
           | ${resource} =    | Hellfire Api Delete Resource | /clusters/26a3c661-cd44-4322-b939-6e1bd222c035 | <api> | <headers> |
        """
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        self.svmc_client._host = host
        uri = 'https://%s/svmc/%s' % (self.svmc_client._host, uri)
        return self.svmcsystem.delete(uri=uri, api=api, headers=headers)

    def svmc_post_resource(self, body, uri, host, api=None, headers=None):
        """ Issues a POST to the specified hellfire uri, passing the supplied body
           Example:
           | ${resource} =    | Hellfire Api Generic POST | <uri> | <body> | <api> | <headers> |
        """
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        self.svmc_client._host = host
        uri = 'https://%s/svmc/%s' % (self.svmc_client._host, uri)
        return self.svmcsystem.create(uri=uri, api=api, body=body, headers=headers)
