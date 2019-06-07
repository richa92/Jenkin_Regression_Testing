import atexit
import ssl
import time

from pyVim import connect
from urllib3.contrib.pyopenssl import ssl_wrap_socket


class vc_integration(object):

    def __init__(self, vcenter_server, cluster_path, vc_username, vc_password, ip, host_username, host_password):
        self.pyVmomi = __import__("pyVmomi")
        self.vcenter_server = vcenter_server
        self.cluster_path = cluster_path
        self.vc_username = vc_username
        self.vc_password = vc_password
        self.host_ip = ip
        self.host_username = host_username
        self.host_password = host_password
        self.connect_to_vcenter()

    def init_VC_Integ(self):
        sslthumbprint = self.getsslThumbprintWithQueryConnectionInfo()
        return sslthumbprint

    def connect_to_vcenter(self):
        print("Connecting to %s using username %s" %
              (self.vcenter_server, self.vc_username))
        self.service_instance = connect.SmartConnect(
            host=self.vcenter_server, user=self.vc_username, pwd=self.vc_password)
        self.content = self.service_instance.RetrieveContent()
        about = self.service_instance.content.about
        print("Connected to %s, %s" % (self.vcenter_server, about.fullName))
        atexit.register(connect.Disconnect, self.service_instance)

    def get_obj(self, vimtype, name):
        """
        Get the vsphere object associated with a given text name
        """
        obj = None
        container = self.content.viewManager.CreateContainerView(
            self.content.rootFolder, vimtype, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def getsslThumbprintWithQueryConnectionInfo(self):
        ssl_thumbprint = "None"
        cluster_path_list = self.cluster_path.split('/')
        cluster_name = cluster_path_list[-1]
        cluster = self.get_obj(
            [self.pyVmomi.vim.ClusterComputeResource], cluster_name)
        parent = cluster.parent
        datacenter = None
        while datacenter is None:
            if parent is not None:
                object_type = parent.__class__.__name__
                if object_type == 'vim.Datacenter':
                    datacenter = parent
                    break
                else:
                    parent = parent.parent
        try:
            task = datacenter.QueryConnectionInfo(hostname=self.host_ip, port=-1, username=self.host_username, password=self.host_password)
        except self.pyVmomi.vmodl.MethodFault as error:
            if isinstance(error, self.pyVmomi.vim.fault.SSLVerifyFault):
                ssl_thumbprint = error.thumbprint
            return ssl_thumbprint


def main(vcenter_server, cluster_path, vc_username, vc_password, host_ip, host_username, host_password):
    vc_integration_obj = vc_integration(vcenter_server, cluster_path, vc_username, vc_password, host_ip, host_username, host_password)
    thumbprint = vc_integration_obj.init_VC_Integ()
    return thumbprint

if __name__ == "__main__":
    main()
