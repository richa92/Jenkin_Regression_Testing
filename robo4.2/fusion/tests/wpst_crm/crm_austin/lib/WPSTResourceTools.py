from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.networking.connection_templates import ConnectionTemplate
from FusionLibrary.api.common.request import HttpVerbs
from FusionLibrary.api.servers.connections import Connections
from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup
from datetime import datetime
import time
import sys
from dateutil import tz
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import os


class EmailClient(object):

    def __init__(self, fromAddr):
        self.fromAddr = fromAddr

    def send(self, message, subject, email, attach=None):
        msg = MIMEMultipart(message)

        msg['Subject'] = subject
        msg['From'] = self.fromAddr
        msg['To'] = email
        msg.attach(MIMEText(message))

        if attach is not None:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="%s"' % os.path.basename(attach))
            msg.attach(part)

        s = smtplib.SMTP('localhost')
        s.sendmail(self.fromAddr, [email], msg.as_string())
        s.quit()


class WPSTResourceTools(object):

    def __init__(self):
        self.fusion_client = HttpVerbs()


class WPSTTaskStatistics(object):

    def __init__(self, taskGroupSN, taskGroupLN):
        self.taskStat = {}
        self.from_zone = tz.tzutc()
        self.to_zone = tz.tzlocal()
        self.parent = ''
        self.groupingResShort = taskGroupSN
        self.groupingResLong = taskGroupLN

    def _getTaskStatistics(self, taskTree, parent):
        parent = parent + "/" + taskTree['resource']['associatedResource']['resourceCategory']
        startTime = datetime.strptime(taskTree['resource']['created'], "%Y-%m-%dT%H:%M:%S.%fZ")
        endTime = datetime.strptime(taskTree['resource']['modified'], "%Y-%m-%dT%H:%M:%S.%fZ")
        for i in range(len(self.groupingResShort)):
            gr = self.groupingResShort[i]
            if gr == parent and gr not in self.taskStat:
                self.taskStat[gr] = {}
                self.taskStat[gr]['Description'] = self.groupingResLong[i]
                self.taskStat[gr]['StartedTS'] = startTime
                self.taskStat[gr]['EndedTS'] = endTime
                self.taskStat[gr]['count'] = 0
                self.taskStat[gr]['State'] = str(taskTree['resource']['taskState'])
#                 self.taskStat[gr]['Id'] = i
            elif gr in parent and gr in self.taskStat:
                self.taskStat[gr]['count'] = self.taskStat[gr]['count'] + 1
                if gr == parent and taskTree['resource']['taskState'] not in self.taskStat[gr]['State']:
                    self.taskStat[gr]['State'] = self.taskStat[gr]['State'] + "," + str(taskTree['resource']['taskState'])
                if endTime > self.taskStat[gr]['EndedTS']:
                    self.taskStat[gr]['EndedTS'] = endTime
        if len(taskTree['children']) > 0:
            for subTask in taskTree['children']:
                self._getTaskStatistics(subTask, parent)
        return

    def generateMigrateTaskStatistics(self, taskTree, fn):
        """Generate Migrate Task Statistics Report
        [Arguments]
        taskTree: response from GET task tree view
        fn: filename of output file
        """
        self._getTaskStatistics(taskTree, self.parent)
        for key in self.taskStat:
            elapsedTime = time.strftime("%H:%M:%S", time.gmtime((self.taskStat[key]['EndedTS'] - self.taskStat[key]['StartedTS']).total_seconds()))
            convertedStartTS = self.taskStat[key]['StartedTS'].replace(tzinfo=self.from_zone).astimezone(self.to_zone)
            convertedEndTS = self.taskStat[key]['EndedTS'].replace(tzinfo=self.from_zone).astimezone(self.to_zone)
            self.taskStat[key]['StartedTS'] = datetime.strftime(convertedStartTS, "%Y-%m-%dT%H:%M.%S")
            self.taskStat[key]['EndedTS'] = datetime.strftime(convertedEndTS, "%Y-%m-%dT%H:%M.%S")
            self.taskStat[key]['Elapsed'] = elapsedTime
        with open(fn, 'a+b') as fp:
            data = [['Task Group Name', 'Started Time', 'Ended Time', 'Elapsed Time', 'SubTask#', 'Task State']]
            logger.info('Generating migration task report', also_console=True)
            for i in range(len(self.groupingResShort)):
                if self.groupingResShort[i] in self.taskStat.keys():
                    data.append([self.taskStat[self.groupingResShort[i]]['Description'],
                                 self.taskStat[self.groupingResShort[i]]['StartedTS'],
                                 self.taskStat[self.groupingResShort[i]]['EndedTS'],
                                 self.taskStat[self.groupingResShort[i]]['Elapsed'],
                                 str(self.taskStat[self.groupingResShort[i]]['count']),
                                 self.taskStat[self.groupingResShort[i]]['State']])
            maxRow = [max(map(len, col)) for col in zip(*data)]
            header = " ".join((' ' + val.ljust(maxLength) + ' ' for val, maxLength in zip(data[0], maxRow)))
            fp.write("-" * len(header) + '\r\n')
            fp.write(header + '\r\n')
            logger.info(header, also_console=True)
            fp.write("-" * len(header) + '\r\n')
            data.remove(data[0])
            for row in data:
                tablerow = " ".join((' ' + val.ljust(maxLength) + ' ' for val, maxLength in zip(row, maxRow)))
                fp.write(tablerow + '\r\n')
                logger.info(tablerow, also_console=True)
            fp.write("-" * len(header) + '\r\n\r\n')
        logger.info('Completed generating migration task report %s' % fn)
        return self.taskStat


class WPSTConnectionTemplate(WPSTResourceTools):

    def __init__(self):
        WPSTResourceTools.__init__(self)
        self.ct = ConnectionTemplate(self.fusion_client)

    def wpst_get_connection_templates(self, sessionId, uri=None, param='', api=None, headers=None):
        """Gets default or paginated collection of connection templates
        [Arguments]
        sessionId: aka authentication token
        uri: the uri of the resource to retrieve. if omitted, all are returned
        param: query parameters
        [Example]
        ${resp} = WPST Get Connection Templates  | <uri> | <param> | <api> | <headers>
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId

        return (self.ct.get(uri=uri, api=api, headers=headers, param=param))


class WPSTConnections(WPSTResourceTools):

    def __init__(self):
        WPSTResourceTools.__init__(self)
        self.conn = Connections(self.fusion_client)

    def wpst_get_connections(self, sessionId, uri=None, param='', api=None, headers=None):
        """Gets default or paginated collection of Connections
        [Arguments]
        sessionId: aka authentication token
        uri: the uri of the resource to retrieve. if omitted, all are returned
        param: query parameters
        [Example]
        ${resp} = WPST Get Connections | <uri> | <param> | <api> | <headers>
         """

        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId

        return (self.conn.get(uri=uri, api=api, headers=headers, param=param))

    def get_attr_by_uri(self, ip, sessionId, rawUri, attr='name', api=None, headers=None):
        """ Get attribute off the Uri
            [Arguments]
            rawUri - raw resource Uri
            attr - attribute default to 'name'
            [Return]
            value of key name
        """

        uri = '%s%s' % (ip, rawUri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)

        return response.get(attr)

    def get_all_by_uri(self, ip, sessionId, rawUri, api=None, headers=None):
        """ Get all attribute off the Uri
            [Arguments]
            rawUri - raw resource Uri
            attr - attribute default to 'name'
            [Return]
            value of key name
        """

        uri = '%s%s' % (ip, rawUri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)

        return response


class WPSTLogicalInterconnectGroup(WPSTResourceTools):

    def __init__(self):
        WPSTResourceTools.__init__(self)
        self.lig = LogicalInterconnectGroup(self.fusion_client)
