""" OA Client Keywords """
import xml.etree.ElementTree as etree
from datetime import datetime
import time
import httplib2
from RoboGalaxyLibrary.utilitylib import logging as logger2


class logger(object):
    """ Logger class """
    @classmethod
    def debug(cls, message):
        """ Write debug log message """
        message = "[OaSoapClient] " + message

        logger2.debug(message)


class OaSoapClient(object):
    """ OA SOAP Client Keywords """
    BASE_REQUEST_PATH = "/hpoa"

    def __init__(self, host, username=None, password=None, proxy_uri=None, default_http_header=None, disable_ssl_valid=True):
        self.oa_session_key = None

        if not ((disable_ssl_valid is True) or (disable_ssl_valid is False)):
            raise Exception('Invalid value for disable_ssl_valid:%s' % disable_ssl_valid)

        if not proxy_uri:
            proxy_uri = None

        if default_http_header is None:
            default_http_header = {'Accept': 'text/html,application/xhtml+xml,application/xml',
                                   'Content-Type': 'text/xml;charset=UTF-8'}

        self.host = host
        self.http = httplib2.Http(disable_ssl_certificate_validation=disable_ssl_valid, proxy_info=proxy_uri)
        self.headers = default_http_header

        # do login
        if username is not None and password is not None:
            self.oa_session_key = self.user_login(username, password)

    def _http_statcode_mapping(self, code):
        """ http://en.wikipedia.org/wiki/List_of_HTTP_status_codes """
        codes_map = {
            '100': 'Continue',
            '101': 'Switching Protocols',
            '102': 'Processing',
            '200': 'OK',
            '201': 'Created',
            '202': 'Accepted',
            '203': 'Non-Authoritative Information',
            '204': 'No Content',
            '205': 'Reset Content',
            '206': 'Partial Content',
            '207': 'Multi-Status',
            '208': 'Already Reported',
            '226': 'IM Used',
            '300': 'Multiple Choices',
            '301': 'Moved Permanently',
            '302': 'Found',
            '303': 'See Other',
            '304': 'Not Modified',
            '305': 'Use Proxy',
            '306': 'Switch Proxy',
            '307': 'Temporary Redirect',
            '308': 'Permanent Redirect',
            '400': 'Bad Request',
            '401': 'Unauthorized',
            '402': 'Payment Required',
            '403': 'Forbidden',
            '404': 'Not Found',
            '405': 'Method Not Allowed',
            '406': 'Not Acceptable',
            '407': 'Proxy Authentication Required',
            '408': 'Request Timeout',
            '409': 'Conflict',
            '410': 'Gone',
            '411': 'Length Required',
            '412': 'Precondition Failed',
            '413': 'Request Entity Too Large',
            '414': 'Request-URI Too Long',
            '415': 'Unsupported Media Type',
            '416': 'Requested Range Not Satisfiable',
            '417': 'Expectation Failed',
            '418': 'I\'m a teapot',
            '419': 'Authentication Timeout',
            '420': 'Method Failure',
            '420': 'Enhance Your Calm',
            '422': 'Unprocessable Entity',
            '423': 'Locked',
            '424': 'Failed Dependency',
            '426': 'Upgrade Required',
            '428': 'Precondition Required',
            '429': 'Too Many Requests',
            '431': 'Request Header Fields Too Large',
            '440': 'Login Timeout',
            '444': 'No Response',
            '449': 'Retry With',
            '450': 'Blocked by Windows Parental Controls',
            '451': 'Unavailable For Legal Reasons',
            '451': 'Redirect',
            '494': 'Request Header Too Large',
            '495': 'Cert Error',
            '496': 'No Cert',
            '497': 'HTTP to HTTPS',
            '498': 'Token expired/invalid',
            '499': 'Client Closed Request',
            '499': 'Token required',
            '500': 'Internal Server Error',
            '501': 'Not Implemented',
            '502': 'Bad Gateway',
            '503': 'Service Unavailable',
            '504': 'Gateway Timeout',
            '505': 'HTTP Version Not Supported',
            '506': 'Variant Also Negotiates',
            '507': 'Insufficient Storage',
            '508': 'Loop Detected',
            '509': 'Bandwidth Limit Exceeded',
            '510': 'Not Extended',
            '511': 'Network Authentication Required',
            '520': 'Origin Error',
            '521': 'Web server is down',
            '522': 'Connection timed out',
            '523': 'Proxy Declined Request',
            '524': 'A timeout occurred',
            '598': 'Network read timeout error',
            '599': 'Network connect timeout error'
        }
        if str(code) in codes_map:
            return codes_map[str(code)]
        else:
            return 'Unknown Return Code'

    def _request(self, method, uri, headers=None, body=None):
        """A simple HTTP request interface."""

        if headers is None:
            headers = {}

        headers = dict(self.headers, **headers)
        url = "https://" + self.host + "/" + uri.lstrip('/')
        resp, resp_body = self.http.request(url,
                                            method,
                                            headers=headers,
                                            body=body)

        # Extract action name
        req_payload_xml_root = etree.fromstring(resp_body)

        action_obj = req_payload_xml_root.findall('.//{http://www.w3.org/2003/05/soap-envelope}Body/*')[0]
        action_name = action_obj.tag.replace('{hpoa.xsd}', '').replace('Response', '')

        logger.debug('[%s] url: %s; action: %s; response code: %s (%s)' % (method, url, action_name, resp.status, self._http_statcode_mapping(resp.status)))

        return resp, resp_body

    def user_login(self, username, password):
        """ Login a user """
        logger.debug("User login.")

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:userLogIn>
   <hpoa:username>%(username)s</hpoa:username>
   <hpoa:password>%(password)s</hpoa:password>
  </hpoa:userLogIn>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'username': username, 'password': password}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to do user login operation. Username: %s, password: %s\n ====Response payload====:\n%s" % (username, password, resp_body))

        root = etree.fromstring(resp_body)
        # get session token
        obj = root.findall('.//{hpoa.xsd}oaSessionKey')[0]
        oa_session_key = obj.text
        return oa_session_key

    def user_logout(self):
        """ Log out the user """
        logger.debug("User logout")

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:userLogOut>
  </hpoa:userLogOut>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to do user logout operation. \n ====Response payload====:\n%s" % resp_body)

    def get_hp_sim_info(self):
        """ Get SIM Info """
        logger.debug("Get all hp sim certificates information")

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:getHpSimInfo>
  </hpoa:getHpSimInfo>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to get hp sim info. \n ====Response payload====:\n%s" % resp_body)

        root = etree.fromstring(resp_body)
        # get hp sim and make a list
        ret = []
        objs = root.findall('.//{hpoa.xsd}certificate')
        for cert in objs:
            cert_dict = {}
            for node in cert:
                cert_dict[node.tag.replace('{hpoa.xsd}', '')] = node.text
            ret.append(cert_dict)

        return ret

    def remove_hp_sim_certificate(self, subject_common_name):
        """ Remove the HP CIM cert """
        logger.debug("Remove hp sim certificate: %s" % subject_common_name)

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:removeHpSimCertificate>
   <hpoa:subjectCommonName>%(subject_common_name)s</hpoa:subjectCommonName>
  </hpoa:removeHpSimCertificate>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key, 'subject_common_name': subject_common_name}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to remove hp sim certificate [ %s ]. \n ====Response payload====:\n%s" % (subject_common_name, resp_body))

    def remove_all_hp_sim_certificates(self):
        """ Remove all certs """
        logger.debug("Remove all hp sim certificates")

        cert_list = self.get_hp_sim_info()

        for cert in cert_list:
            logger.debug("Removing hp sim certificate: %s" % cert['issuerCommonName'])
            self.remove_hp_sim_certificate(cert['issuerCommonName'])

    def get_snmp_info(self):
        """ Get SNMP info """
        logger.debug("Get all snmp information")

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:getSnmpInfo>
  </hpoa:getSnmpInfo>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to get snmp info. \n ====Response payload====:\n%s" % resp_body)

        root = etree.fromstring(resp_body)
        # get hp sim and make a list
        ret = {}
        snmp_info_obj = root.findall('.//{hpoa.xsd}snmpInfo')[0]

        for item in snmp_info_obj:
            tag_name = item.tag.replace('{hpoa.xsd}', '')
            if tag_name == 'traps':
                ret['traps'] = []
                for trap in item:
                    d = {}
                    for item2 in trap:
                        d[item2.tag.replace('{hpoa.xsd}', '')] = item2.text
                    ret['traps'].append(d)
            else:
                ret[tag_name] = item.text

        return ret

    def remove_snmp_trap_receiver(self, ip_address):
        """ Remove the trap reciever """
        logger.debug("Remove snmp trap receiver: %s" % ip_address)

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:removeSnmpTrapReceiver>
   <hpoa:ipAddress>%(ip_address)s</hpoa:ipAddress>
  </hpoa:removeSnmpTrapReceiver>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key, 'ip_address': ip_address}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to remove snmp trap receiver [ %s ]. \n ====Response payload====:\n%s" % (ip_address, resp_body))

    def remove_all_snmp_trap_receiver(self):
        """ Remove all of the trap receivers """
        logger.debug("Remove all snmp trap receiver")

        address_list = self.get_snmp_info()

        for trap in address_list['traps']:
            logger.debug("Removing snmp trap receiver: %s" % trap['ipAddress'])
            self.remove_snmp_trap_receiver(trap['ipAddress'])

    def get_blade_status(self, bay_number):
        """ Retrieve and return the blade status """
        logger.debug("Get server bay status information for bay %s" % bay_number)

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:getBladeStatus>
   <hpoa:bayNumber>%(bay_number)s</hpoa:bayNumber>
  </hpoa:getBladeStatus>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key, 'bay_number': bay_number}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to get bay status information for bay %s. \n ====Response payload====:\n%s" % (bay_number, resp_body))

        root = etree.fromstring(resp_body)
        # get hp sim and make a dictionary
        ret = {}
        objs = root.findall('.//{hpoa.xsd}bladeStatus')[0]
        for node in objs:
            node_tag = node.tag.replace('{hpoa.xsd}', '')
            if list(node):
                ret[node_tag] = {}
                for node2 in node:
                    node2_tag = node2.tag.replace('{hpoa.xsd}', '')
                    ret[node_tag][node2_tag] = node2.text
            else:
                ret[node.tag.replace('{hpoa.xsd}', '')] = node.text

        return ret

    def set_blade_power(self, bay_numb, power_cmd):
        """
        :param bay_numb:
        :param power_cmd: Possible values: PRESS_AND_HOLD|MOMENTARY_PRESS|COLD_BOOT|RESET
        :raise Exception:
        """
        logger.debug("set blade power for bay %s" % bay_numb)

        payload = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
 xmlns:hpoa="hpoa.xsd">
 <SOAP-ENV:Header>
  <wsse:Security>
   <hpoa:HpOaSessionKeyToken wsu:Id="">
    <hpoa:oaSessionKey>%(oa_session_key)s</hpoa:oaSessionKey>
   </hpoa:HpOaSessionKeyToken>
  </wsse:Security>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
  <hpoa:setBladePower>
   <hpoa:bayNumber>%(bay_numb)s</hpoa:bayNumber>
   <hpoa:power>%(power_cmd)s</hpoa:power>
  </hpoa:setBladePower>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""" % {'oa_session_key': self.oa_session_key, 'bay_numb': bay_numb, 'power_cmd': power_cmd}

        resp, resp_body = self._request('GET', self.BASE_REQUEST_PATH, body=payload)
        if int(resp['status']) / 100 != 2:
            raise Exception("Failed to set blade power for bay [ %s ]. \n ====Response payload====:\n%s" % (bay_numb, resp_body))

    def power_on_blade(self, bay_number, timeout=15):
        """ Power on """
        logger.debug("about to power on server bay %s" % bay_number)

        ret = self.get_blade_status(bay_number)
        logger.debug('current power state: %s' % ret['powered'])
        if ret['powered'] == 'POWER_ON':
            logger.debug("blade is powered on, skip operation")
            return

        self.set_blade_power(bay_number, 'MOMENTARY_PRESS')

        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            ret = self.get_blade_status(bay_number)
            if ret['powered'] == 'POWER_ON':
                break
            time.sleep(3)
        else:
            raise Exception('Failed to power on blade %s' % bay_number)

    def power_off_blade(self, bay_number, timeout=15):
        """ Power off """
        logger.debug("about to power off for bay %s" % bay_number)

        ret = self.get_blade_status(bay_number)
        logger.debug('current power state: %s' % ret['powered'])
        if ret['powered'] == 'POWER_OFF':
            logger.debug("blade is powered off, skip operation")
            return

        self.set_blade_power(bay_number, 'PRESS_AND_HOLD')

        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            ret = self.get_blade_status(bay_number)
            if ret['powered'] == 'POWER_OFF':
                break
            time.sleep(3)
        else:
            raise Exception('Failed to power off blade %s' % bay_number)
