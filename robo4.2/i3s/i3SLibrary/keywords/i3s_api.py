''' i3s API keyword file '''
import time
from i3SLibrary.api.artifact_bundle import ArtifactBundle
from i3SLibrary.api.golden_image import GoldenImage
from i3SLibrary.api.plan_scripts import PlanScripts
from i3SLibrary.api.build_plan import BuildPlans
from i3SLibrary.api.deployment_plan import DeploymentPlan
from i3SLibrary.api.login_sessions import LoginSession
from i3SLibrary.api.getcall_for_all_artifacts import GetCallForArtifacts
from FusionLibrary.api.common.request import HttpVerbs
from i3SLibrary.api.audit_log import AuditLog
from i3SLibrary.api.support_dump import SupportDump
from i3SLibrary.api.deployment_group import DeploymentGroup
from i3SLibrary.api.i3s_backup_restore import BackupRestore
from i3SLibrary.api.update import I3SApplianceFirmware
from i3SLibrary.api.ha_nodes import HaNodes
from i3SLibrary.api.os_volumes import OsVolumes


class i3sAPIKeywords(object):

    def __init__(self):
        self.i3s_client = HttpVerbs()

    class LoginSessionKeywords(object):

        def __init__(self):
            self.loginsession = LoginSession(self.i3s_client)

        def i3s_api_login_appliance(self, host, sessionID, headers=None):
            """Login to the appliance as the specified user
            [Arguments]
            host: the appliance IP or hontname
            creds: a dictionary containing userName and password attributes
            [Example]
            ${resp} = i3s Api Login Appliance | <host> | <creds> | <headers>
            """
            return self.loginsession.login(host, sessionID, headers)

        def i3s_api_wait_for_task_to_complete(self, uri=None, api=None, headers=None, retries=5, sleep_time=5, param=''):
            if uri:
                uri = 'https://%s%s' % (self.i3s_client._host, uri)
            else:
                uri = 'https://%s/rest/tasks%s' % (self.i3s_client._host, param)
            task_attempts = 0
            for i in range(0, retries):
                time.sleep(sleep_time)
                task_attempts += 1
                response = self.i3s_client.get(uri=uri, headers=headers)
                if response["percentComplete"] == 100:
                    break
                if task_attempts == retries:
                    raise Exception(
                        "Task did not complete after %d tries." % retries)
            return response

    class i3SAPIBackupRestoreKeywords(object):

        def __init__(self):
            self.backup = BackupRestore(self.i3s_client)

        def i3s_api_extract_backupbundle(self, body, uri=None, api=None, headers=None):
            """ extract a backupbundle """
            return self.backup.extract(body=body, uri=uri, api=api, headers=headers)

        def i3s_api_add_backup(self, localfile, api=None, headers=None):
            """Uploads an backup bundle to the appliance
            [Arguments]
            localfile: REQUIRED the filename of the image file
            [Example]
            ${resp} = i3s Api add backup bundle | <localfile> | <name> | <description>
                                                 | <api> | <headers>
            """
            return self.backup.add(localfile, api, headers)

        def i3s_api_get_backup(self, uri=None, api=None, headers=None, param=''):
            return(self.backup.get(uri=uri, api=api, headers=headers, param=param))

        def i3s_api_download_backup(self, uri=None, api=None, headers=None, param=None):
            return self.backup.download(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_create_backup(self, body, api=None, headers=None):
            return self.backup.create(body, api, headers)

    class i3SAPIDeploymentGroupKeywords(object):

        def __init__(self):
            self.deploymentgroup = DeploymentGroup(self.i3s_client)

        def i3s_api_get_deploymentgroup(self, uri=None, api=None, headers=None):
            return self.deploymentgroup.get(uri=uri, api=api, headers=headers)

    class i3SAPISupportDumpKeywords(object):

        def __init__(self):
            self.supportdump = SupportDump(self.i3s_client)

        def i3s_api_create_supportdump(self, body, api=None, headers=None):
            return self.supportdump.create(body, api, headers)

        def i3s_api_download_supportdump(self, uri=None, api=None, headers=None, param=None):
            return self.supportdump.download(uri=uri, api=api, headers=headers, param=param)

    class i3SAPIAuditLogKeywords(object):

        def __init__(self):
            self.auditlog = AuditLog(self.i3s_client)

        def i3s_api_get_auditlog(self, uri=None, api=None, headers=None, param=''):
            return(self.auditlog.get(uri=uri, api=api, headers=headers, param=param))

        def i3s_api_download_auditlog(self, uri=None, api=None, headers=None):
            return self.auditlog.download(uri=uri, api=api, headers=headers)

    class i3SAPIGoldenImageKeywords(object):

        def __init__(self):
            self.goldenimage = GoldenImage(self.i3s_client)

        def i3s_api_add_goldenimage(self, localfile, param, api=None, headers=None):
            """Uploads a golden image to the appliance
            [Arguments]
            localfile: REQUIRED the filename of the image file
            [Example]
            ${resp} = i3s Api add goldenimage | <body>  | <api> | <headers>
            """
            return self.goldenimage.add(localfile, param, api, headers)

        def i3s_api_goldenimage_capture(self, body, api=None, headers=None):
            return (self.goldenimage.create(body, api, headers))

        def i3s_api_get_goldenimage(self, uri=None, param='', api=None, headers=None):
            """ Get an goldenimage """
            return self.goldenimage.get(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_update_goldenimage(self, body, uri, api=None, headers=None):
            """Update goldenimage. Attribute that can be updated is the name and description
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            """
            return self.goldenimage.update(body=body, uri=uri, api=api, headers=headers)

        def i3s_api_delete_goldenimage(self, name=None, uri=None, param='', api=None, headers=None):
            """ Delete an goldenimage """
            return self.goldenimage.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def i3s_api_download_goldenimage(self, uri=None, param='', api=None, headers=None):
            """Downloads an image file
            [Arguments]
            localfile: REQUIRED the filename of the image file
            [Example]
            ${resp} = i3s Api download goldenimage | <name> | <api> | <headers>
            """
            return self.goldenimage.download(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_get_goldenvolume(self, uri=None, param='', api=None, headers=None):
            """ Get an goldenimage """
            return self.goldenimage.getvolume(uri=uri, api=api, headers=headers, param=param)

    class i3SAPIPlanScriptsKeywords(object):

        def __init__(self):
            self.planscripts = PlanScripts(self.i3s_client)

        def i3s_api_create_plan_scripts(self, body, api=None, headers=None):
            """creates a artifact bundle on the appliance
            ${resp} = i3s Api create planscript | <planscript body> |  <api> | <headers>
            """
            return self.planscripts.create(body, api, headers)

        def i3s_api_get_plan_scripts(self, uri=None, param='', api=None, headers=None):
            """ Get a plan script """
            return self.planscripts.get(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_delete_plan_scripts(self, name=None, uri=None, param='', api=None, headers=None):
            """ Delete a plan script """
            return self.planscripts.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def i3s_api_update_plan_scripts(self, body, uri, api=None, headers=None):
            """Update an artifact bundle. Attribute that can be updated is the name.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            """
            return self.planscripts.update(body=body, uri=uri, api=api, headers=headers)

    class i3SAPIBuildPlanKeywords(object):

        def __init__(self):
            self.buildplan = BuildPlans(self.i3s_client)

        def i3S_api_create_buildplan(self, body, api=None, headers=None):
            """Creates a buildplan to the appliance
            [Example]
            ${resp} = i3s Api add buildplan | <body>  | <api> | <headers>
            """
            return (self.buildplan.create(body, api, headers))

        def i3S_api_get_buildplan(self, uri=None, param='', api=None, headers=None):
            """ Get a buildplan """
            return (self.buildplan.get(uri=uri, api=api, headers=headers, param=param))

        def i3S_api_update_buildplan(self, body, uri, api=None, headers=None):
            """Update an buildplan.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            """
            return (self.buildplan.update(body=body, uri=uri, api=api, headers=headers))

        def i3S_api_delete_buildplan(self, name=None, uri=None, param='', api=None, headers=None):
            """ Delete an buildplan """
            return (self.buildplan.delete(name=name, uri=uri, param=param, api=api, headers=headers))

    class i3SAPIDeploymentPlanKeywords(object):

        def __init__(self):
            self.deploymentplan = DeploymentPlan(self.i3s_client)

        def i3s_api_create_deploymentplan(self, body, api=None, headers=None):
            """Creates a deployment plan on the appliance
            ${resp} = i3s Api create artifactbundle | <artifacts> | <name> | <description>
                                                    | <api> | <headers>
            """
            return self.deploymentplan.create(body, api, headers)

        def i3s_api_get_deploymentplan(self, uri=None, param='', api=None, headers=None):
            """ Get a deployment plan """
            return self.deploymentplan.get(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_delete_deploymentplan(self, name=None, uri=None, param='', api=None, headers=None):
            """ Delete a deployment plan """
            return self.deploymentplan.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def i3s_api_update_deploymentplan(self, body, uri, api=None, headers=None):
            """Update a deployment plan. Currently the only attribute that can be updated is the name.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            """
            return self.deploymentplan.update(body=body, uri=uri, api=api, headers=headers)

    class i3SAPIArtifactBundleKeywords(object):

        def __init__(self):
            self.artifactbundle = ArtifactBundle(self.i3s_client)

        def i3s_api_add_artifactbundle(self, localfile, api=None, headers=None):
            """Uploads an artifact bundle to the appliance
            [Arguments]
            localfile: REQUIRED the filename of the image file
            [Example]
            ${resp} = i3s Api add artifactbundle | <localfile> | <name> | <description>
                                                 | <api> | <headers>
            """
            return self.artifactbundle.add(localfile, api, headers)

        def i3s_api_create_artifactbundle(self, body, api=None, headers=None):
            """creates a artifact bundle on the appliance
            ${resp} = i3s Api create artifactbundle | <artifacts> | <name> | <description>
                                                    | <api> | <headers>
            """
            return self.artifactbundle.create(body, api, headers)

        def i3s_api_get_artifactbundle(self, uri=None, param='', api=None, headers=None):
            """ Get an artifactbundle """
            return self.artifactbundle.get(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_download_artifactbundle(self, uri=None, param='', api=None, headers=None):
            """Downloads an image file
            [Arguments]
            localfile: REQUIRED the filename of the image file
            [Example]
            ${resp} = i3s Api download artifactbundle | <name> | <api> | <headers>
            """
            return self.artifactbundle.download(uri=uri, api=api, headers=headers, param=param)

        def i3s_api_delete_artifactbundle(self, name=None, uri=None, param='', api=None, headers=None):
            """ Delete an artifactbundle """
            return self.artifactbundle.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def i3s_api_extract_artifactbundle(self, uri=None, api=None, headers=None):
            """ extract an artifactbundle """
            return self.artifactbundle.extract(uri=uri, api=api, headers=headers)

        def i3s_api_update_artifactbundle(self, body, uri, api=None, headers=None):
            """Update an artifact bundle. Currently the only attribute that can be updated is the name.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            """
            return self.artifactbundle.update(body=body, uri=uri, api=api, headers=headers)

    class i3SAPIGetCallForArtifactKeywords(object):

        def __init__(self):
            self.getcall_for_artifacts = GetCallForArtifacts(self.i3s_client)

        def i3s_get_goldenimage(self, uri=None, param='', api=None, headers=None):
            """ Get a golden image uri"""
            return self.getcall_for_artifacts.i3s_get_goldenimage(uri=uri, api=api, headers=headers, param=param)

        def i3s_get_planscript(self, uri=None, param='', api=None, headers=None):
            """ Get a planscript uri"""
            return self.getcall_for_artifacts.i3s_get_planscript(uri=uri, api=api, headers=headers, param=param)

        def i3s_get_buildplan(self, uri=None, param='', api=None, headers=None):
            """ Get a buildplan uri """
            return self.getcall_for_artifacts.i3s_get_buildplan(uri=uri, api=api, headers=headers, param=param)

        def i3s_get_deploymentplan(self, uri=None, param='', api=None, headers=None):
            """ Get a deployment uri"""
            return self.getcall_for_artifacts.i3s_get_deploymentplan(uri=uri, api=api, headers=headers, param=param)

        def i3s_get_statelessserver(self, uri=None, param='', api=None, headers=None):
            """ Get a stateless server uri"""
            return (self.getcall_for_artifacts.i3s_get_statelessserver(uri=uri, api=api, headers=headers, param=param))

    class i3SApplianceFirmwareKeywords(object):

        def __init__(self):
            self.i3sappfirmware = I3SApplianceFirmware(self.i3s_client)

        def i3s_api_get_appliance_firmware_upgrade_status(self, api=None, headers=None):
            """Gets the status of the upgrade task once after the upgrade completes
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Appliance Firmware Upgrade Status | <api> | <headers>
            """
            param = '/notification'
            return (self.i3sappfirmware.get(api=api, headers=headers, param=param))

        def i3s_api_upgrade_appliance_firmware(self, localfile, api=None, headers=None):
            """Initiate upgrade task using uploaded upgrade image
            [Arguments]
            localfile: REQUIRED the filename of the .bin patch file
            [Example]
            ${resp} = Fusion Api Upgrade Appliance Firmware   | <localfile> | <api> | <headers>
            """
            param = '?file=%s' % localfile
            return (self.i3sappfirmware.update(api, headers, param))

        def i3s_api_upload_appliance_firmware(self, localfile, api=None, headers=None):
            """Uploads a .bin patch to the appliance
            [Arguments]
            localfile: REQUIRED the filename of the .bin patch file
            [Example]
            ${resp} = Fusion Api Upload Appliance Firmware   | <localfile> | <api> | <headers>
            """
            return (self.i3sappfirmware.upload(localfile, api, headers))

    class I3sHaNodesKeywords(object):

        def __init__(self):
            self.ha_nodes = HaNodes(self.i3s_client)

        def i3s_api_get_ha_nodes(self, uri=None, param='', api=None, headers=None):
            """Retrieves information about all members of the high-availability appliance cluster.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = i3s Api Get HA Nodes  | <uri> | <param> | <api> | <headers>
            """
            return (self.ha_nodes.get(uri=uri, api=api, headers=headers, param=param))

    class i3sAPIOSVolumes(object):

        def __init__(self):
            self.osvolumes = OsVolumes(self.i3s_client)

        def i3s_api_get_os_volume(self, uri=None, api=None, headers=None, param=''):
            """Gets collection of os volumess.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = i3s Api Get OS Volume | <uri> | <api> | <headers> | <param>
            """
            return(self.osvolumes.get(uri=uri, api=api, headers=headers, param=param))
