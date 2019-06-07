'''
Created on May 18, 2017

@author: Administrator
'''


class DynamicData(object):
    def _init_(self):
        # valid characters
        self.chars = [chr(x) for x in range(33, 127)]

    def update_enclosure(self, enclosures, path, value, expectedmsg):
        ret = []
        for enc in enclosures:
            ret.append({"name": enc['name'], "op": "replace", "path": "/" + path, "value": value, "msg": expectedmsg})
        return ret

    def make_expected_server_data(self, server):
        ret = []
        for serv in server:
            ret.append({'type': 'server-hardware-7', 'name': serv['name'], 'status': 'OK', 'state': 'NoProfileApplied'})
        return ret
