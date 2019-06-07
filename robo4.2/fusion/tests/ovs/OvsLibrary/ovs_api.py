"""
OvsLibrary OneView Supportibility API Keywords.

"""


from ovs_index_resource import OvsIndexResource
from ovs_tasks import OvsTask
from ovs_events import OvsEvent


class OvsIndexResourceKeywords(object):

    """
    This class is used for Index Resource API related keywords
    """

    def __init__(self):
        self.ovs_index_resource = OvsIndexResource(self.fusion_client)

    def fusion_api_create_index_resource(self, body, api=None, auth=None, headers=None, param=''):
        """The index/resources resource provides APIs for managing index resources, including retrieving,
        creating/updating, and deleting index resources .
        [Example]
        ${resp} = Fusion Api Create Index Resource | <body> | <api> | <Trusted-Token> | <headers>
        """
        return self.ovs_index_resource.create(body, api, auth, headers, param=param)


class OvsTaskKeywords(object):

    """
    This class is used for Task Resource API related keywords
    """

    def __init__(self):
        self.ovs_tasks = OvsTask(self.fusion_client)

    def fusion_api_delete_task(self, uri=None, api=None, auth=None, headers=None, param=''):
        """ Deletes a single alert resource identified by its ID
        [Arguments]
        uri: The uri of the resource to delete.if omitted, all are deleted
        param: query parameters
        [Example]
         ${resp} = Fusion Api Delete Task  | <uri> | <api> | <Trusted-Token> | <headers>
        """
        return self.ovs_tasks.delete(uri, api, auth, headers, param)

    def fusion_api_create_task_trusted_token(self, body, api=None, auth=None, headers=None):
        """
        Creates a Task using trusted token
        [Arguments]
        auth: Required trusted token from OV
        body: REQUIRED a dictionary containing request body elements
        [Example]
        ${resp} = Fusion Api Create Task Trusted Token | <body> | <api> | <Trusted-Token> | <headers>
        """
        return self.ovs_tasks.create_task(body, api, auth, headers)


class OvsEventKeywords(object):

    """
    This class is used for Event Resource API related keywords
    """

    def __init__(self):
        self.ovs_events = OvsEvent(self.fusion_client)

    def fusion_api_create_event_trusted_token(self, body, api=None, auth=None, headers=None, param=''):
        """
        Creates a Event using trusted token
        [Arguments]
        auth: Required trusted token from OV
        body: REQUIRED a dictionary containing request body elements
        [Example]
        ${resp} = Fusion Api Create Task Trusted Token | <body> | <api> | <Trusted-Token> | <headers>
        """
        return self.ovs_events.create_event(body, api, auth, headers, param)
