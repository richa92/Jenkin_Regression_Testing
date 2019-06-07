'''
   FusionLibrary API Logical Interconnect Groups
'''

import json
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.networking.interconnect_types import InterconnectTypes


class LogicalInterconnectGroup(object):
    """
        Logical Interconnect Group basic REST API operations/requests.
    """

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    xport = {'Mellanox SH2200 TAA Switch Module for Synergy':
             {'Q1': '15', 'Q1.1': '16', 'Q1.2': '17', 'Q1.3': '18', 'Q1.4': '19',
              'Q2': '20', 'Q2.1': '21', 'Q2.2': '22', 'Q2.3': '23', 'Q2.4': '24',
              'Q3': '25', 'Q3.1': '26', 'Q3.2': '27', 'Q3.3': '28', 'Q3.4': '29',
              'Q4': '30', 'Q4.1': '31', 'Q4.2': '32', 'Q4.3': '33', 'Q4.4': '34',
              'Q5': '35', 'Q5.1': '36', 'Q5.2': '37', 'Q5.3': '38', 'Q5.4': '39',
              'Q6': '40', 'Q6.1': '41', 'Q6.2': '42', 'Q6.3': '43', 'Q6.4': '44',
              'Q7': '45', 'Q7.1': '46', 'Q7.2': '47', 'Q7.3': '48', 'Q7.4': '49',
              'Q8': '50', 'Q8.1': '51', 'Q8.2': '52', 'Q8.3': '53', 'Q8.4': '54',
              'Q1:1': '16', 'Q1:2': '17', 'Q1:3': '18', 'Q1:4': '19',
              'Q2:1': '21', 'Q2:2': '22', 'Q2:3': '23', 'Q2:4': '24',
              'Q3:1': '26', 'Q3:2': '27', 'Q3:3': '28', 'Q3:4': '29',
              'Q4:1': '31', 'Q4:2': '32', 'Q4:3': '33', 'Q4:4': '34',
              'Q5:1': '36', 'Q5:2': '37', 'Q5:3': '38', 'Q5:4': '39',
              'Q6:1': '41', 'Q6:2': '42', 'Q6:3': '43', 'Q6:4': '44',
              'Q7:1': '46', 'Q7:2': '47', 'Q7:3': '48', 'Q7:4': '49',
              'Q8:1': '51', 'Q8:2': '52', 'Q8:3': '53', 'Q8:4': '54'},

             'Virtual Connect SE 100Gb F32 Module for Synergy':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
              'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
              'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
              'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
              'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
              'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
              'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
              'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100',
              'X1': '105', 'X2': '106'},

             'Virtual Connect SE 16Gb FC Module for Synergy':
             {'Q1.1': '21', 'Q1.2': '22', 'Q1.3': '23', 'Q1.4': '24',
              'Q2.1': '25', 'Q2.2': '26', 'Q2.3': '27', 'Q2.4': '28',
              'Q3.1': '29', 'Q3.2': '30', 'Q3.3': '31', 'Q3.4': '32',
              'Q4.1': '33', 'Q4.2': '34', 'Q4.3': '35', 'Q4.4': '36',
              'Q1:1': '21', 'Q1:2': '22', 'Q1:3': '23', 'Q1:4': '24',
              'Q2:1': '25', 'Q2:2': '26', 'Q2:3': '27', 'Q2:4': '28',
              'Q3:1': '29', 'Q3:2': '30', 'Q3:3': '31', 'Q3:4': '32',
              'Q4:1': '33', 'Q4:2': '34', 'Q4:3': '35', 'Q4:4': '36',
              '1': '13', '2': '14', '3': '15', '4': '16', '5': '17', '6': '18', '7': '19', '8': '20'},

             'Virtual Connect SE 32Gb FC Module for Synergy':
             {'Q1.1': '21', 'Q1.2': '22', 'Q1.3': '23', 'Q1.4': '24',
              'Q2.1': '25', 'Q2.2': '26', 'Q2.3': '27', 'Q2.4': '28',
              '1': '13', '2': '14', '3': '15', '4': '16', '5': '17', '6': '18', '7': '19', '8': '20'},

             'Synergy 20Gb Interconnect Link Module':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
              'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
              'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
              'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
              'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
              'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
              'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
              'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
              },

             'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
              'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
              'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
              'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
              'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
              'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
              'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
              'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
              },
             'Virtual Connect SE 40Gb F8 Module for Synergy':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
              'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
              'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
              'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
              'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
              'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
              'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
              'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
              },

             'HP Synergy 10Gb Interconnect Link Module': {},
             'HP Synergy 20Gb Interconnect Link Module': {},
             'HP Synergy 40Gb Interconnect Link Module': {},

             'Synergy 10Gb Interconnect Link Module': {},
             'Synergy 40Gb Interconnect Link Module': {},
             'Synergy 50Gb Interconnect Link Module': {},


             'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
              'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
              'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
              'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
              'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
              'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
              'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
              'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
              },
             'HP FlexFabric 10GbE Expansion Module': {},
             'HP FlexFabric 20GbE Expansion Module': {},
             'HP FlexFabric 40GbE Expansion Module': {},
             'HP FlexFabric 40/40Gb Module':
             {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
              'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
              'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
              'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
              'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
              'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
              'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
              'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
              },
             'HP VC FlexFabric-20/40 F8 Module':
             {'Q1.1': '17', 'Q1.2': '18', 'Q1.3': '19', 'Q1.4': '20',
              'Q2.1': '21', 'Q2.2': '22', 'Q2.3': '23', 'Q2.4': '24',
              'Q3.1': '25', 'Q3.2': '26', 'Q3.3': '27', 'Q3.4': '28',
              'Q4.1': '29', 'Q4.2': '30', 'Q4.3': '31', 'Q4.4': '32',
              'X1': '33', 'X2': '34', 'X3': '35', 'X4': '36', 'X5': '37', 'X6': '38', 'X7': '39', 'X8': '40', 'X9': '41', 'X10': '42'},
             'VC FlexFabric-20/40 F8 Module':
             {'Q1.1': '17', 'Q1.2': '18', 'Q1.3': '19', 'Q1.4': '20',
              'Q2.1': '21', 'Q2.2': '22', 'Q2.3': '23', 'Q2.4': '24',
              'Q3.1': '25', 'Q3.2': '26', 'Q3.3': '27', 'Q3.4': '28',
              'Q4.1': '29', 'Q4.2': '30', 'Q4.3': '31', 'Q4.4': '32',
              'X1': '33', 'X2': '34', 'X3': '35', 'X4': '36', 'X5': '37', 'X6': '38', 'X7': '39', 'X8': '40', 'X9': '41', 'X10': '42'},
             'HP VC FlexFabric 10Gb/24-Port Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20', 'X5': '21',
                 'X6': '22', 'X7': '23', 'X8': '24', 'X9': '25', 'X10': '26'},
             'VC FlexFabric 10Gb/24-Port Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20', 'X5': '21',
                 'X6': '22', 'X7': '23', 'X8': '24', 'X9': '25', 'X10': '26'},
             'HP VC Flex-10 Enet Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20',
                 'X5': '21', 'X6': '22', 'X7': '23', 'X8': '24'},
             'VC Flex-10 Enet Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20',
                 'X5': '21', 'X6': '22', 'X7': '23', 'X8': '24'},
             'HP VC Flex-10/10D Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20', 'X5': '21', 'X6': '22', 'X7': '23',
                 'X8': '24', 'X9': '25', 'X10': '26', 'X11': '27', 'X12': '28', 'X13': '29', 'X14': '30'},
             'VC Flex-10/10D Module':
             {'X1': '17', 'X2': '18', 'X3': '19', 'X4': '20', 'X5': '21', 'X6': '22', 'X7': '23',
                 'X8': '24', 'X9': '25', 'X10': '26', 'X11': '27', 'X12': '28', 'X13': '29', 'X14': '30'},
             'HP VC 8Gb 20-Port FC Module':
             {'1': '17', '2': '18', '3': '19', '4': '20'},
             'VC 8Gb 20-Port FC Module':
             {'1': '17', '2': '18', '3': '19', '4': '20'},
             'HP VC 8Gb 24-Port FC Module':
             {'1': '17', '2': '18', '3': '19', '4': '20',
                 '5': '21', '6': '22', '7': '23', '8': '24'},
             'VC 8Gb 24-Port FC Module':
             {'1': '17', '2': '18', '3': '19', '4': '20',
                 '5': '21', '6': '22', '7': '23', '8': '24'},
             'HP VC 16Gb 24-Port FC Module':
             {'1': '17', '2': '18', '3': '19', '4': '20',
                 '5': '21', '6': '22', '7': '23', '8': '24'},
             'Cisco Fabric Extender for HP BladeSystem':
             {'1': '17', '2': '18', '3': '19', '4': '20',
                 '5': '21', '6': '22', '7': '23', '8': '24'},
             }

    def create(self, body, api=None, headers=None):
        """
            Creates logical interconnect group.
            Arguments:
                body: [Required] a dictionary of request body to create lig
                api: [Optional] X-API-Version
                headers: [Optional] Request headers
            Return:
                Response body
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/logical-interconnect-groups' % (
            self.fusion_client._host)
        response = self.fusion_client.post(
            uri=uri, headers=headers, body=json.dumps(body))
        return response

    def update(self, body, uri, api=None, headers=None, etag=None):
        """
            Updates logical interconnect group.
            Arguments:
                body: [Required] a dictionary of request body for PUT
                api: [Optional] X-API-Version
                headers: [Optional] Request headers
                etag: [Optional] Entity tag/version ID of the resource, the same value that is returned in the ETag header on a GET of the resource
            Return:
                Response body
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if etag:
            headers['If-Match'] = str(etag)
        else:
            headers['If-Match'] = "*"
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(
            uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None, etag=None):
        """
            Deletes logical interconnect group.
            Arguments:
                name: [Optional] Name of the logical interconnect to delete
                uri: [Optional] Uri of the logical interconnect to delete
                api: [Optional] X-API-Version
                headers: [Optional] Request headers
                etag: [Optional] Entity tag/version ID of the resource, the same value that is returned in the ETag header on a GET of the resource
            Return:
                Response body
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        elif name:
            param = '?&filter="\'name\' == \'%s\'"' % (name)
            response = self.get(api=api, headers=headers, param=param)
            if response['count'] == 0:
                logger._log('LIG %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s' % (self.fusion_client._host,
                                        response['members'][0]['uri'])
        if etag:
            headers['If-Match'] = str(etag)
        else:
            headers['If-Match'] = "*"
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        """
            Gets a logical interconnect group.
            Arguments:
                uri: [Optional] Uri of the logical interconnect to delete
                api: [Optional] X-API-Version
                headers: [Optional] Request headers
                param: [Optional] Query parameters
            Return:
                Response body
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/logical-interconnect-groups%s' % (
                self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def make_body(self, **kwargs):
        """
            Build a request body for logical interconnect group
            Arguments:
                name: [Required] A user friendly name for logical interconnect group
                api: [Optional] X-API-Version
                enclosureIndexes: [Optional] The list of enclosure indices that are specified by this logical interconnect group.
                    The value [-1] indicates that this is a single enclosure logical interconnect group for Virtual Connect SE FC Modules.
                    The value [1] indicates that this is a single enclosure logical interconnect group for other supported interconnects.
                    If you are building a logical interconnect group for use with a three enclosures interconnect link topology, the value needs to be [1,2,3].
                enclosureType: [Optional] Type of enclosure. Example: C7000, SY12000, etc.
                ethernetSettings: [Optional] The Ethernet interconnect settings for the logical interconnect group
                fcoeSettings: [Optional] The FCoE interconnect settings for the logical interconnect group
                interconnectBaySet: [Optional] Interconnect bay associated with the logical interconnect group
                interconnectMapTemplate: [Optional] Interconnect map associated with the logical interconnect group
                internalNetworkUris: [Optional] A list of internal network URIs
                consistencyCheckingForInternalNetworks: [Optional] Checking Consistency of Internal Networks with LIG
                qosConfiguration: [Optional] QoS configuration
                redundancyType: [Optional] The type of enclosure redundancy. Example: HighlyAvailable, Redundant, etc.
                snmpConfiguration: [Optional] The SNMP configuration for the logical interconnect group
                sflowConfiguration: [Optional] The sFlow configuration
                downlinkSpeedMode: [Optional] The downlink speed mode
                stackingMode: [Optional] Stacking mode for the logical interconnect
                telemetryConfiguration: [Optional] The controls for collection of interconnect statistics
                uplinkSets: [Optional] List of uplink sets in the logical interconnect group
        """

        icmap = kwargs.get('interconnectMapTemplate')
        kwargs['interconnectMapTemplate'] = self._make_interconnect_map_template_dict(
            kwargs.get('interconnectMapTemplate'))

        if kwargs.get('uplinkSets'):
            if isinstance(kwargs['uplinkSets'], list):
                usList = []
                for uplinkSet in kwargs['uplinkSets']:
                    us = self._make_uplink_set_dict(icmap=icmap, **uplinkSet)
                    usList.append(us)
                kwargs['uplinkSets'] = usList

        if kwargs.get('telemetryConfiguration'):
            kwargs['telemetryConfiguration'] = self._make_telemetry_configuration_dict(
                kwargs['telemetryConfiguration'])

        if kwargs.get('snmpConfiguration'):
            kwargs['snmpConfiguration'] = self._make_snmp_configuration_dict(
                kwargs['snmpConfiguration'])

        api = kwargs.pop('api', None)
        if not api:
            if BuiltIn().get_variable_value("${X-API-VERSION}") is not None:
                api = BuiltIn().get_variable_value("${X-API-VERSION}")
            else:
                api = self.fusion_client._currentVersion()

        ver = {'1': self._make_body_4,
               '2': self._make_body_4,
               '3': self._make_body_4,
               '4': self._make_body_4,
               '101': self._make_body_101,
               '120': self._make_body_120,
               '199': self._make_body_200,
               '200': self._make_body_200,
               '201': self._make_body_201,
               '299': self._make_body_300,
               '300': self._make_body_300,
               '400': self._make_body_500,
               '500': self._make_body_500,
               '600': self._make_body_600,
               '800': self._make_body_800,
               '1000': self._make_body_1000,
               '1200': self._make_body_1200
               }

        if kwargs['consistencyCheckingForInternalNetworks'] is None:
            del kwargs['consistencyCheckingForInternalNetworks']

        # run the corresponding function
        if str(api) in ver:
            body = ver[str(api)](kwargs)
        else:
            # TODO: might want special handling other than Exception
            msg = "API version %s is not supported" % (str(api))
            raise Exception(msg)
        return body

    def _make_body_4(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 1-4
        '''
        body['type'] = body.get('type', 'logical-interconnect-group')
        for us in body.get('uplinkSets', []):
            us.pop('ethernetNetworkType', None)
            us.pop('lacpTimer', None)
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettings'
            body['ethernetSettings'].pop('enablePauseFloodProtection', None)
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_101(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 101
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV2')
        body.get('enclosureType', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV2'
        body.pop('fcoeSettings', None)
        body.pop('enclosureIndexes', None)
        body.pop('redundancyType', None)
        body.pop('interconnectBaySet', None)
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_120(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 120
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV2')
        body.pop('enclosureType', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV2'
        if not body.get('internalNetworkUris'):
            body.pop('internalNetworkUris', None)
        body.pop('fcoeSettings', None)
        body.pop('enclosureIndexes', None)
        body.pop('redundancyType', None)
        body.pop('interconnectBaySet', None)
        body.pop('qosConfiguration', None)
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_200(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 199-200
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV3')
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_201(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 201
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV201')
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV201'
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_300(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 299-300
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV300')
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        # fcoeSettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV201'
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_500(self, body):
        '''
        This modifies\removes the elements that are not valid for API versions 400 and 500
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV300')
        for us in body['uplinkSets']:
            us.pop('fcMode', None)
            us.pop('privateVlanDomains', None)
        # FCoESettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV201'
        if body.get('snmpConfiguration'):
            body['snmpConfiguration'].pop('v3Enabled', None)
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        return body

    def _make_body_600(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 600
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV4')
        # FCoESettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV4'
        body.pop('sflowConfiguration', None)
        body.pop('downlinkSpeedMode', None)
        for us in body['uplinkSets']:
            us.pop('privateVlanDomains', None)
        return body

    def _make_body_800(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 800
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV5')
        # FCoESettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV4'
        body.pop('downlinkSpeedMode', None)
        for us in body['uplinkSets']:
            us.pop('privateVlanDomains', None)
        if body.get('sflowConfiguration'):
            if not body['sflowConfiguration'].get('type'):
                body['sflowConfiguration']['type'] = 'sflow-configuration'
        for us in body['uplinkSets']:
            us.pop('privateVlanDomains', None)
        return body

    def _make_body_1000(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 1000
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV6')
        # FCoESettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV5'
        if body.get('sflowConfiguration'):
            if not body['sflowConfiguration'].get('type'):
                body['sflowConfiguration']['type'] = 'sflow-configuration'
        return body

    def _make_body_1200(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 1200
        '''
        body['type'] = body.get('type', 'logical-interconnect-groupV7')
        # FCoESettings was removed from 3.00 onward. it is ONLY valid in
        # 2.00 build
        body.pop('fcoeSettings', None)
        if body.get('ethernetSettings'):
            if not body['ethernetSettings'].get('type'):
                body['ethernetSettings']['type'] = 'EthernetInterconnectSettingsV6'
        if body.get('sflowConfiguration'):
            if not body['sflowConfiguration'].get('type'):
                body['sflowConfiguration']['type'] = 'sflow-configuration'
        body.get('downlinkSpeedMode', None)
        return body

    def _make_uplink_set_dict(self,
                              name,
                              icmap,
                              ethernetNetworkType,
                              networkType,
                              mode='Auto',
                              networkUris=[],
                              nativeNetworkUri=None,
                              logicalPortConfigInfos=[],
                              lacpTimer='Short',
                              primaryPort=None,
                              fcMode=None,
                              **kwargs):
        """
            Build uplink set dictionary.
            Arguments:
                name: [Required] Name of the uplink set
                icmap: [Required] Interconnect map associated with the logical interconnect group
                ethernetNetworkType: [Required] A description of the ethernet network's type. Example: Tagged, Tunnel, Untagged, etc.
                networkType: [Required] The type of network. Example: Ethernet or FibreChannel
                mode: [Optiona] Defaults to Auto. The Ethernet uplink failover mode. Example: Auto or Failover
                networkUris: [Optional] Defaults to empty list. A set of network set URIs assigned to the uplink set. The list can be empty but not null.
                nativeNetworkUri: [Optional] The Ethernet native network URI
                logicalPortConfigInfos: [Optional] Defaults to empty list. The detailed configuration properties for the uplink ports.
                lacpTimer: [Optional] The LACP timer. Value can be Short or Long. Defaults to Short.
                primaryPort: [Optional] The Ethernet primary failover port
                fcMode: [Optional] Fibre Channel mode. Example for FC port aggregation using trunking: TRUNK
            Return:
                Uplink set dictionary for request body
        """

        if logicalPortConfigInfos:
            if isinstance(logicalPortConfigInfos, list):
                lpciList = []
                for lpci in logicalPortConfigInfos:
                    lpciList.append(self._make_logical_port_config_info_dict(icmap=icmap, name=name, **lpci))
                logicalPortConfigInfos = lpciList

        if primaryPort:
            primaryPort = self._make_primary_port_dict(
                icmap=icmap, **primaryPort)

        dto = {'name': name,
               'ethernetNetworkType': ethernetNetworkType,
               'mode': mode,
               'networkUris': networkUris[:],
               'networkType': networkType,
               'primaryPort': primaryPort,
               'logicalPortConfigInfos': logicalPortConfigInfos,
               'nativeNetworkUri': nativeNetworkUri,
               'lacpTimer': lacpTimer,
               'fcMode': fcMode
               }

        for key in kwargs:
            if key not in dto:
                dto[key] = kwargs[key]

        return dto

    def _make_primary_port_dict(self, bay, port, icmap, enclosure=1):
        """
            Build primary port dictionary. The Ethernet primary failover port.
            Arguments:
                bay: [Required] Bay number of the interconnect
                port: [Required] Port number of the interconnect
                icmap: [Required] Interconnect map associated with the logical interconnect group
                enclosure: [Optional] Defaults to 1. Enclosure with relative values -1, 1 to 5.
            Return:
                Primary port dictionary for request body
        """
        ictype = [x for x in icmap if int(x['bay']) == int(bay)]
        if ictype:
            ictype = ictype[0]['type']
        else:
            logger._log(
                '_make_primary_port_dict: Unable to find matching interconnect type', level='WARN')
            return
        return {'locationEntries':
                [{'type': 'Enclosure', 'relativeValue': enclosure},
                 {'type': 'Bay', 'relativeValue': int(bay)},
                 {'type': 'Port', 'relativeValue': self.xport[ictype][port]}]
                }

    def _make_logical_port_config_info_dict(self, name, bay, port, icmap,
                                            enclosure=1, speed='Auto',
                                            **kwargs):
        """
            Build logical port config info dictionary. The detailed configuration properties for the uplink ports.
            Arguments:
                name: [Required] Name of the uplink set
                bay: [Required] Bay number of the interconnect
                port: [Required] Port number of the interconnect
                icmap: [Required] Interconnect map associated with the logical interconnect group
                enclosure: [Optional] Defaults to 1. Enclosure with relative values -1, 1 to 5.
                speed: [Optional] Defaults to Auto. The port speed you prefer it to use. Example: Speed10G
            Return:
                Logical port config info dictionary for request body

        """
        ictype = [x for x in icmap if int(x['bay']) == int(
            bay) and int(x.get('enclosure', 1)) == int(enclosure)]

        if ictype:
            ictype = ictype[0]['type']
        else:
            msg = '_make_logical_port_config_info_dict: Unable to find matching interconnect type for Uplinkset: %s, Bay: %s, Enclosure: %s' % (
                name, bay, enclosure)
            logger._log(msg, level='WARN')
            return
        if port in self.xport[ictype]:
            dto = {'logicalLocation':
                   {'locationEntries':
                    [{'type': 'Enclosure', 'relativeValue': enclosure},
                     {'type': 'Bay', 'relativeValue': int(bay)},
                     {'type': 'Port', 'relativeValue': self.xport[ictype][port]}]},
                   'desiredSpeed': speed
                   }
            for key in kwargs:
                if key not in dto:
                    dto[key] = kwargs[key]
            return dto

        else:
            msg = '_make_logical_port_config_info_dict: No port relative found for %s, Uplinkset: %s, Bay: %s, Enclosure: %s' % (
                ictype, name, bay, enclosure)
            logger._log(msg, level='WARN')
            return

    def _make_interconnect_map_template_dict(self, interconnectMapTemplate):
        """
            Build interconnect map template dictionary. Interconnect map associated with the logical interconnect group.
            Argument:
                interconnectMapTemplate: [Required] Interconnect map associated with the logical interconnect group
            Return:
                Interconnect map template dictionary for the request body
        """
        template = {'interconnectMapEntryTemplates':
                    [{'logicalLocation':
                      {'locationEntries':
                       [{'type': 'Bay', 'relativeValue': v['bay']},
                        {'type': 'Enclosure', 'relativeValue': v.get('enclosure', 1)}]},
                      'permittedInterconnectTypeUri': v['type'],
                      'enclosureIndex': v.get('enclosureIndex', 1)
                      } for _, v in enumerate(interconnectMapTemplate)],
                    }

        if interconnectMapTemplate:
            # TODO: should check that this object is a dict
            # assume this is an actual template dict already and just return it
            if 'interconnectMapEntryTemplates' in interconnectMapTemplate:
                return interconnectMapTemplate
            # TODO: There is probably a more pythonic way to do this check...
            # provided bay\interconnect type mapping, build template dict
            elif 'bay' and 'type' in interconnectMapTemplate.__str__():
                itypes = InterconnectTypes(self.fusion_client)
                permittedInterconnectTypes = itypes.get()
                for ic in interconnectMapTemplate:
                    if 'interconnectTypeUri' in ic.keys():
                        permittedInterconnectTypeUri = ic[
                            'interconnectTypeUri']
                    else:
                        # Get permittedInterconnectTypeUri
                        permittedInterconnectType = [
                            x for x in permittedInterconnectTypes['members'] if x['name'] == ic['type']]
                        if len(permittedInterconnectType) == 0:
                            permittedInterconnectTypeUri = '/permittedInterconnectTypeNotFound'
                        else:
                            permittedInterconnectTypeUri = permittedInterconnectType[
                                0]['uri']
                    for location in template['interconnectMapEntryTemplates']:
                        if location['enclosureIndex'] == ic['enclosureIndex']:
                            entries = location['logicalLocation'][
                                'locationEntries']
                            if [x for x in entries if x['type'] == 'Bay' and x['relativeValue'] == int(ic['bay'])]:
                                location[
                                    'permittedInterconnectTypeUri'] = permittedInterconnectTypeUri
                return template

        else:  # return basic empty C7000 template
            template = {'interconnectMapEntryTemplates':
                        [{'logicalLocation':
                          {'locationEntries':
                           [{'type': 'Bay', 'relativeValue': N},
                            {'type': 'Enclosure', 'relativeValue': 1}]},
                          'permittedInterconnectTypeUri': None,
                          'logicalDownlinkUri': None
                          } for N in range(1, 9)],
                        }
            return template

    def _make_telemetry_configuration_dict(self, telemetry):
        """
            Build telemetry configuration dictionary.
            Argument:
                telemetry: [Required] The telemetry configuration for the logical interconnect group.
            Return:
                Telemetry configuration dictionary for the request body
        """
        return {'type': 'telemetry-configuration',
                'enableTelemetry': telemetry.get('enableTelemetry', True),
                'sampleInterval': telemetry.get('sampleInterval', 300),
                'sampleCount': telemetry.get('sampleCount', 12)
                }

    def _make_snmp_configuration_dict(self, snmp):
        """
            Build SNMP configuration dictionary.
            Argument:
                snmp: [Required] The SNMP configuration for the logical interconnect group.
            Return:
                SNMP configuration dictionary for the request body
        """

        if 'trapDestinations' in snmp:
            tdList = []
            for trapDestination in snmp['trapDestinations']:
                td = self._make_snmp_trap_destinations_dict(trapDestination)
                tdList.append(td)
            trapDestinations = tdList
        else:
            trapDestinations = None

        # TODO: Remove this and expect a list for each to be passed-in.
        # This is a hack
        snmpaccess = snmp.get('snmpAccess', None)
        if snmpaccess is not None and isinstance(snmpaccess, str):
            snmpaccess = snmpaccess.split(',')

        return {'type': 'snmp-configuration',
                'enabled': snmp.get('enabled', True),
                'v3Enabled': snmp.get('v3Enabled', False),
                'readCommunity': snmp.get('readCommunity', 'public'),
                'snmpAccess': snmpaccess,
                'systemContact': snmp.get('systemContact', None),
                'trapDestinations': trapDestinations
                }

    def _make_snmp_trap_destinations_dict(self, trapdestination):
        """
            Build SNMP trap destination dictionay.
            Argument:
                trapdestination: [Required] The SNMP trap destination configuration for the SNMP configuration
            Return:
                SNMP trap destination dictionary for SNMP Configration
        """
        # TODO: Remove this and expect a list for each to be passed-in.
        # This is a hack
        enetTrapCategories = trapdestination.get('enetTrapCategories', None)
        if enetTrapCategories is not None and isinstance(enetTrapCategories, str):
            enetTrapCategories = enetTrapCategories.split(',')
        fcTrapCategories = trapdestination.get('fcTrapCategories', None)
        if fcTrapCategories is not None and isinstance(fcTrapCategories, str):
            fcTrapCategories = fcTrapCategories.split(',')
        trapSeverities = trapdestination.get('trapSeverities', None)
        if trapSeverities is not None and isinstance(trapSeverities, str):
            trapSeverities = trapSeverities.split(',')
        vcmTrapCategories = trapdestination.get('vcmTrapCategories', None)
        if vcmTrapCategories is not None and isinstance(vcmTrapCategories, str):
            vcmTrapCategories = vcmTrapCategories.split(',')

        return {'communityString': trapdestination.get('communityString', 'public'),
                'enetTrapCategories': enetTrapCategories,
                'fcTrapCategories': fcTrapCategories,
                'trapDestination': trapdestination.get('trapDestination', None),
                'trapFormat': trapdestination.get('trapFormat', 'SNMPv1'),
                'trapSeverities': trapSeverities,
                'vcmTrapCategories': vcmTrapCategories
                }
