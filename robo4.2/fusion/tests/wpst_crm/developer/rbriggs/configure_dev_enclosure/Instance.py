from robot.libraries.BuiltIn import BuiltIn


class Instance(object):
    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def get(self):
        z = self.fusionlib.fusion_api_get_ethernet_networks()
        print z
        return self.fusionlib


class API500(object):
    x = 500


class API600(object):
    x = 600
