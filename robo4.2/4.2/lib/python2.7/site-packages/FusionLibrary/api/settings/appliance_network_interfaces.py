#!/usr/local/bin/python
import json


class ApplianceNetworkInterfaces(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get_device_mac(self, device, api=None, headers=None):
        appAdapters = self.get(api=api, headers=headers)
        mac = None
        for x in appAdapters['applianceNetworks']:
            if x['device'] == device:
                mac = x['macAddress']
                break
        return mac

    def get_device_attribute(self, device='eth0', attribute='macAddress', api=None, headers=None):
        appAdapters = self.get(api=api, headers=headers)
        y = None
        for x in appAdapters['applianceNetworks']:
            if x['device'] == device:
                y = x[attribute]
                break
        return y

    # X-API-Version = 201
    def _make_body_201(self, interface):
        body = {'type': 'ApplianceServerConfiguration'}
        if 'applianceNetworks' in interface:
            if interface['applianceNetworks']:
                appAdapters = self.get(api=None, headers=None)
                for adapter in interface['applianceNetworks']:
                    for eth in appAdapters['applianceNetworks']:
                        if eth['device'] == adapter['device']:
                            adapter['macAddress'] = eth['macAddress']
                            break
                body['applianceNetworks'] = interface['applianceNetworks']
                for adapter in body['applianceNetworks']:
                    for k, v in adapter.iteritems():
                        if v.__len__() == 0:
                            adapter[k] = None
                        elif v == 'true':
                            adapter[k] = True
                        elif v == 'false':
                            adapter[k] = False

                    if adapter['searchDomains']:
                        searchDomains = []
                        domains = adapter['searchDomains'].split(',')
                        for domain in xrange(len(domains)):
                            searchDomains.append(domains[domain])
                        adapter['searchDomains'] = searchDomains

                    if adapter['ipv4NameServers']:
                        nameServers = []
                        servers = adapter['ipv4NameServers'].split(',')
                        for server in xrange(len(servers)):
                            nameServers.append(servers[server])
                        adapter['ipv4NameServers'] = nameServers

                    if adapter['ipv6NameServers']:
                        nameServers = []
                        servers = adapter['ipv6NameServers'].split(',')
                        for server in xrange(len(servers)):
                            nameServers.append(servers[server])
                        adapter['ipv6NameServers'] = nameServers

        if 'locale' in interface:
            if interface['locale']:
                body['locale'] = interface['locale']
            for k, v in body['locale'].iteritems():
                if v.__len__() == 0:
                    body['locale'][k] = None

        if 'time' in interface:
            if interface['time']:
                body['time'] = interface['time']

            for k, v in body['time'].iteritems():
                if v.__len__() == 0:
                    body['time'][k] = None

            if body['time']['ntpServers']:
                ntpServers = []
                servers = body['time']['ntpServers'].split(',')
                for server in xrange(len(servers)):
                    ntpServers.append(servers[server])
                body['time']['ntpServers'] = ntpServers

        return body

    def make_body(self, interface, api=None):
        if not api:
            api = self.fusion_client._headers['X-Api-Version']

        ver = {101: self._make_body_201,
               199: self._make_body_201}

        if api in ver:
            return ver[api](interface)

    def configure(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/network-interfaces' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/network-interfaces' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
