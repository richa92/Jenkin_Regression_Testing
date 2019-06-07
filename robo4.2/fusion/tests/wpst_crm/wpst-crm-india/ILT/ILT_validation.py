import json
import collections
from matplotlib.cbook import Null
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.utils.asserts import assert_equals, assert_not_equal
from fabric.decorators import hosts
from FusionLibrary.api.common.request import HttpVerbs
import requests
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import sys
import paramiko
import re
from FusionLibrary.cli.em import em_operation


class ILT_validation(object):

    def verify_ilt(self, getresponse, hostname, credentials):
        '''This funtion checks the ILT port connections and informs the user about the error in the connections   '''
        global host
        global cred
        host = hostname
        cred = credentials
        cl_type = 0
        res = []
        with open("ilt.py", "w") as outfile:
            json.dump(getresponse, outfile, indent=4)
        with open('ilt.py') as data_file:
            data = json.load(data_file)
        n = data['count']
        f = open('iltdata.txt', 'w')
        for num in range(0, n):
            icbayset1 = []
            icbayset2 = []
            icbayset3 = []
            for connection in data['members'][num]['iltConnections']:
                if connection['from']['baySetNumber'] == 1:
                    icbayset1.append(connection)
                if connection['from']['baySetNumber'] == 2:
                    icbayset2.append(connection)
                if connection['from']['baySetNumber'] == 3:
                    icbayset3.append(connection)
            li = []
            for element in [icbayset1, icbayset2, icbayset3]:
                if element != []:
                    li.append({'iltConnections': element})
                else:
                    continue
            count = len(li)
            ilt_dict = {'members': li, 'enclosureMembers': data['members'][num]['enclosureMembers']}
            fname = 'ilt' + str(num + 1) + '.py'
            with open(fname, "w") as store_file:
                json.dump(ilt_dict, store_file, indent=4)
            ilt_check = ILT_validation.miscablingScenario(self, fname)
            msg = ilt_check[1]
            if msg == []:
                error_msg = '\nILT configuration Errors : \n' + '\nNo Errors'
            else:
                error_msg = '\nILT configuration Errors : \n\n' + '\n'.join(msg)
            logger._log_to_console_and_log_file('\n' + error_msg)
            res.append(ilt_check[0])
        return res

    def verify_ilt_alerts(self, alertresponse, getresponse, hostname, credentials):
        global host
        global cred
        global fault_enc
        global enc_alert
        global iwb
        global wrong_bay
        global unmatched_alerts
        host = hostname
        cred = credentials
        verify_alerts = 0
        with open('ilt.py', 'w') as outfile:
            json.dump(getresponse, outfile, indent=4)
        with open('alerts.py', 'w') as outfile:
            json.dump(alertresponse, outfile, indent=4)
        with open('ilt.py') as data_file:
            data = json.load(data_file)
        count = data['count']
        for num in range(0, count):
            enc_alert = []
            fault_enc = []
            iwb = []
            wrong_bay = []
            unmatched_alerts = []
            fname = 'ilt' + str(num + 1) + '.py'
            actual_alerts = ILT_validation.getActualAlerts(self, fname)
            correct_alerts = ILT_validation.getCorrectAlerts(self, fname, num)
            actual_alerts.sort()
            correct_alerts.sort()
            unmatched_alerts = ILT_validation.listsShouldBeEqual(self, actual_alerts, correct_alerts)
            if unmatched_alerts == []:
                continue
            else:
                verify_alerts = 1
        if verify_alerts == 1:
            raise AssertionError('ALL ALERTS DO NOT MATCH:\n')

    def miscablingScenario(self, fname):
        flag = 0
        msg = []
        with open(fname) as data_file:
            data = json.load(data_file)
        count = len(data['members'])
        for i in range(0, count):
            gnc = ILT_validation.getNumChlorides(self, i, fname)
            if gnc[0] == '0':
                cltype = 2
            elif gnc[1] == '0':
                cltype = 1
            else:
                cltype = 0
                msg.append('More than one type of Chloride module not allowed')
                flag = 1
                break
            actual_conns = ILT_validation.checkConn(self, i, fname)
            correct_conns = ILT_validation.correctConn(self, i, cltype, fname)
            for ac in actual_conns:
                if ac not in correct_conns:
                    flag = 1
                    c1 = ac['from']
                    if ac['to'] is None:
                        for cc in correct_conns:
                            if cc['from'] == c1 and cc['to'] is not None:
                                msg.append('Connection from port ' + c1[2] + ' of interconnect in bay ' + c1[1] + ' in enclosure ' + ILT_validation.getEncName(self, c1[0], fname) + ' is disconnected')
                    else:
                        msg.append('Connection from port ' + c1[2] + ' of interconnect in bay ' + c1[1] + ' in enclosure ' + ILT_validation.getEncName(self, c1[0], fname) + ' is miscabled')
    #        for item in data['members'][i]['iltConnections']:
    #            if item['to'] is None:
    #                i_dict = {'enc': item['from']['enclosureUri'][-10:], 'bay': item['from']['bayNumber'], 'port': str(item['from']['portId'])}
    #                if not ILT_validation.portNotConnected(self, i_dict, i, fname):
    #                    flag = 1
    #                    msg.append('Cable incorrectly inserted in port ' + i_dict['port'] + ' of interconnect in bay ' + str(i_dict['bay']) + ' of enclosure ' + i_dict['enc'])
            if len(data['enclosureMembers']) == 1:
                for ic in data['members'][i]['iltConnections']:
                    if ic['from']['interconnectProductName'].find('Link Module') != -1:
                        msg.append('Chloride module not allowed in single enclosure. Check Bay Set ' + str(ic['from']['baySetNumber']) + ' in enclosure ' + ic['from']['enclosureUri'][-10:])
                        flag = 1
                        break
            for ic in data['members'][i]['iltConnections']:
                try:
                    if ic['from']['interconnectProductName'].find('40Gb F8') != -1 and ic['to']['interconnectProductName'].find('40Gb F8') != -1:
                        flag = 1
                        msg.append('Potash connected to potash. Check enclosure ' + ic['from']['enclosureUri'][-10:] + ', interconnect in bay ' + str(ic['from']['bayNumber']) + ', port ' + str(ic['from']['portId']))
                    elif ic['from']['interconnectProductName'].find('Link Module') != -1 and ic['to']['interconnectProductName'].find('Link Module') != -1:
                        flag = 1
                        msg.append('Chloride connected to Chloride. Check enclosure ' + ic['from']['enclosureUri'][-10:] + ', interconnect in bay ' + str(ic['from']['bayNumber']) + ', port ' + str(ic['from']['portId']))
                except TypeError:
                    continue
        if flag == 1:
            return [False, msg]
        else:
            return [True, msg]

    def getEncName(self, enc, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        for item in data['enclosureMembers']:
            if item['nodeNumber'] == int(enc):
                return item['enclosureUri'][-10:]

    def portNotConnected(self, i, id, fname):
        port_nc = True
        json_credentials = json.dumps(cred)
        base_url = 'https://%s' % (host)
        headers1 = {'content-type': 'application/json', 'accept': 'application/json', 'X-Api-Version': '300'}
        login_url = base_url + '/rest/login-sessions'
        resp = requests.post(login_url, data=json_credentials, headers=headers1, verify=False)
        sessionid = json.loads(resp.text)["sessionID"]
        headers = {'auth': sessionid, 'X-Api-Version': 300}
        with open(fname) as data_file:
            data = json.load(data_file)
        for ic in data['members'][id]['iltConnections']:
            if ic['from']['enclosureUri'][-10:] == i['enc'] and ic['from']['bayNumber'] == int(i['bay']):
                ic_uri = ic['from']['interconnectUri'].split('/')[3]
                break
        uri = base_url + '/rest/interconnects/pluggableModuleInformation/' + ic_uri
        response = requests.get(uri, headers=headers, verify=False)
        json_data = json.loads(response.text)
        for item in json_data:
            if item['portName'][-1:] == i['port'] and item['identifier'] == 'ILP':
                port_nc = False
                break
            elif item['portName'][-1:] == i['port'] and item['identifier'] is None:
                port_nc = True
        return port_nc

    def getNumChlorides(self, i, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        cl20 = 0
        cl10 = 0
        list2 = []
        for ic in data['members'][i]['iltConnections']:
            if ic['from']['interconnectProductName'].find('Link Module') != -1:
                if ic['from']['portId'] == 2:
                    cl20 = cl20 + 1
                    cl10 = cl10 - 1
                    continue
                else:
                    cl10 = cl10 + 1
        list2.append(str(cl10))
        list2.append(str(cl20))
        return list2

    def checkConn(self, id, fname):
        list1 = []
        with open(fname) as data_file:
            data = json.load(data_file)
        for ic in data['members'][id]['iltConnections']:
            en1 = ILT_validation.getEncNo(self, ic['from']['enclosureUri'][-10:], fname)
            bay1 = str(ic['from']['bayNumber'])
            port1 = str(ic['from']['portId'])
            ebp1 = en1 + bay1 + port1
            try:
                en2 = ILT_validation.getEncNo(self, ic['to']['enclosureUri'][-10:], fname)
                bay2 = str(ic['to']['bayNumber'])
                port2 = str(ic['to']['portId'])
                ebp2 = en2 + bay2 + port2
            except TypeError:
                ebp2 = None
            list1.append({'from': ebp1, 'to': ebp2})
        return list1

    def getEncNo(self, enc, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        for item in data['enclosureMembers']:
            if item['enclosureUri'][-10:] == enc:
                return str(item['nodeNumber'])

    def correctConn(self, id, ebp, fname):
        listconn = [[{'ebpfrom': '111', 'ebpto': '211'},
                     {'ebpfrom': '112', 'ebpto': '311'},
                     {'ebpfrom': '113', 'ebpto': '411'},
                     {'ebpfrom': '114', 'ebpto': '511'},
                     {'ebpfrom': '141', 'ebpto': '241'},
                     {'ebpfrom': '211', 'ebpto': '111'},
                     {'ebpfrom': '241', 'ebpto': '141'},
                     {'ebpfrom': '242', 'ebpto': '341'},
                     {'ebpfrom': '243', 'ebpto': '441'},
                     {'ebpfrom': '244', 'ebpto': '541'},
                     {'ebpfrom': '311', 'ebpto': '112'},
                     {'ebpfrom': '341', 'ebpto': '242'},
                     {'ebpfrom': '411', 'ebpto': '113'},
                     {'ebpfrom': '441', 'ebpto': '243'},
                     {'ebpfrom': '511', 'ebpto': '114'},
                     {'ebpfrom': '541', 'ebpto': '244'},
                     {'ebpfrom': '121', 'ebpto': '221'},
                     {'ebpfrom': '122', 'ebpto': '321'},
                     {'ebpfrom': '123', 'ebpto': '421'},
                     {'ebpfrom': '124', 'ebpto': '521'},
                     {'ebpfrom': '151', 'ebpto': '251'},
                     {'ebpfrom': '221', 'ebpto': '121'},
                     {'ebpfrom': '251', 'ebpto': '151'},
                     {'ebpfrom': '252', 'ebpto': '351'},
                     {'ebpfrom': '253', 'ebpto': '451'},
                     {'ebpfrom': '254', 'ebpto': '551'},
                     {'ebpfrom': '321', 'ebpto': '122'},
                     {'ebpfrom': '351', 'ebpto': '252'},
                     {'ebpfrom': '421', 'ebpto': '123'},
                     {'ebpfrom': '451', 'ebpto': '253'},
                     {'ebpfrom': '521', 'ebpto': '124'},
                     {'ebpfrom': '551', 'ebpto': '254'},
                     {'ebpfrom': '131', 'ebpto': '231'},
                     {'ebpfrom': '132', 'ebpto': '331'},
                     {'ebpfrom': '133', 'ebpto': '431'},
                     {'ebpfrom': '134', 'ebpto': '531'},
                     {'ebpfrom': '161', 'ebpto': '261'},
                     {'ebpfrom': '231', 'ebpto': '131'},
                     {'ebpfrom': '261', 'ebpto': '161'},
                     {'ebpfrom': '262', 'ebpto': '361'},
                     {'ebpfrom': '263', 'ebpto': '461'},
                     {'ebpfrom': '264', 'ebpto': '561'},
                     {'ebpfrom': '331', 'ebpto': '132'},
                     {'ebpfrom': '361', 'ebpto': '262'},
                     {'ebpfrom': '431', 'ebpto': '133'},
                     {'ebpfrom': '461', 'ebpto': '263'},
                     {'ebpfrom': '531', 'ebpto': '134'},
                     {'ebpfrom': '561', 'ebpto': '264'}],

                    [{'ebpfrom': '111', 'ebpto': '211'},
                     {'ebpfrom': '112', 'ebpto': '311'},
                     {'ebpfrom': '113', 'ebpto': '312'},
                     {'ebpfrom': '114', 'ebpto': '212'},
                     {'ebpfrom': '121', 'ebpto': '221'},
                     {'ebpfrom': '122', 'ebpto': '321'},
                     {'ebpfrom': '123', 'ebpto': '322'},
                     {'ebpfrom': '124', 'ebpto': '222'},
                     {'ebpfrom': '131', 'ebpto': '231'},
                     {'ebpfrom': '132', 'ebpto': '331'},
                     {'ebpfrom': '133', 'ebpto': '332'},
                     {'ebpfrom': '134', 'ebpto': '232'},
                     {'ebpfrom': '241', 'ebpto': '141'},
                     {'ebpfrom': '242', 'ebpto': '341'},
                     {'ebpfrom': '243', 'ebpto': '342'},
                     {'ebpfrom': '244', 'ebpto': '142'},
                     {'ebpfrom': '251', 'ebpto': '151'},
                     {'ebpfrom': '252', 'ebpto': '351'},
                     {'ebpfrom': '253', 'ebpto': '352'},
                     {'ebpfrom': '254', 'ebpto': '152'},
                     {'ebpfrom': '261', 'ebpto': '161'},
                     {'ebpfrom': '262', 'ebpto': '361'},
                     {'ebpfrom': '263', 'ebpto': '362'},
                     {'ebpfrom': '264', 'ebpto': '162'},
                     {'ebpto': '111', 'ebpfrom': '211'},
                     {'ebpto': '112', 'ebpfrom': '311'},
                     {'ebpto': '113', 'ebpfrom': '312'},
                     {'ebpto': '114', 'ebpfrom': '212'},
                     {'ebpto': '121', 'ebpfrom': '221'},
                     {'ebpto': '122', 'ebpfrom': '321'},
                     {'ebpto': '123', 'ebpfrom': '322'},
                     {'ebpto': '124', 'ebpfrom': '222'},
                     {'ebpto': '131', 'ebpfrom': '231'},
                     {'ebpto': '132', 'ebpfrom': '331'},
                     {'ebpto': '133', 'ebpfrom': '332'},
                     {'ebpto': '134', 'ebpfrom': '232'},
                     {'ebpto': '241', 'ebpfrom': '141'},
                     {'ebpto': '242', 'ebpfrom': '341'},
                     {'ebpto': '243', 'ebpfrom': '342'},
                     {'ebpto': '244', 'ebpfrom': '142'},
                     {'ebpto': '251', 'ebpfrom': '151'},
                     {'ebpto': '252', 'ebpfrom': '351'},
                     {'ebpto': '253', 'ebpfrom': '352'},
                     {'ebpto': '254', 'ebpfrom': '152'},
                     {'ebpto': '261', 'ebpfrom': '161'},
                     {'ebpto': '262', 'ebpfrom': '361'},
                     {'ebpto': '263', 'ebpfrom': '362'},
                     {'ebpto': '264', 'ebpfrom': '162'}]]
        if ebp == 1 or ebp == 2:
            list1 = []
            bays = []
            conns = listconn[ebp - 1]
            with open(fname) as data_file:
                data = json.load(data_file)
            num_enc = len(data['enclosureMembers'])
            for dat in data['members'][id]['iltConnections']:
                bays.append(dat['from']['bayNumber'])
            bays = list(set(bays))
            for el in conns:
                try:
                    if el['ebpto'] is not None:
                        if int(el['ebpto'][0]) > num_enc:
                            conns[conns.index(el)]['ebpto'] = None
                    if int(el['ebpfrom'][0]) > num_enc or int(el['ebpfrom'][1]) not in bays:
                        conns[conns.index(el)] = 0
                except ValueError:
                    return {}
            for c in conns:
                if c != 0:
                    list1.append({'from': c['ebpfrom'], 'to': c['ebpto']})
            return list1
        else:
            bay = int(ebp[1])
            with open(fname) as data_file:
                data = json.load(data_file)
            cl = 0
            for item in data['members'][id]['iltConnections']:
                if item['from']['bayNumber'] == bay and item['from']['interconnectProductName'].find('Link Module') != -1:
                    if item['from']['portId'] == 2 and item['from']['errorCode'] is None:
                        cl = 1
            for d in listconn[cl]:
                if d.get('ebpfrom') == ebp:
                    ebp2 = d.get('ebpto')
                    break
                else:
                    continue
            return ebp2

    def single_enc_Cl(self, fname):
        global enc_alert
        with open(fname) as data_file:
            data = json.load(data_file)
        enc = data['members'][0]['iltConnections'][0]['from']['enclosureUri'][-10:]
        al2 = ''
        i = 0
        potash_B = 0
        potash_A = 0
        baynum = []
        for n in range(0, len(data['members'])):
            potash_B = 0
            potash_A = 0
            bay = 0
            for item in data['members'][n]['iltConnections']:
                if item['from']['interconnectProductName'].find('Link Module') != -1:
                    fault_enc.append(enc)
                    desc = [item['from']['bayNumber'], item['from']['interconnectProductName'], item['from']['interconnectUri']]
                    if desc not in baynum:
                        baynum.append(desc)
                elif item['from']['interconnectProductName'].find('40Gb F8') != -1:
                    bay = item['from']['baySetNumber']
                    if item['from']['baySetSide'] == 'B':
                        potash_B = 1
                        bsn = str(item['from']['baySetNumber'])
                    elif item['from']['baySetSide'] == 'A':
                        potash_A = 1
            if potash_B == 1 and potash_A == 0:
                e_alert = 'Invalid interconnect link topology. ' + ILT_validation.getProduct(self, n, fname) + ' not present at A-side of bay set ' + bsn + ' in enclosure ' + ILT_validation.getID(self, fname, enc) + '.'
                dict1 = {'enc': enc, 'bay': None, 'alert': e_alert}
                enc_alert.append(dict1)
            if bay != 0:
                dict2 = {'enc': enc, 'bay': bay}
                ILT_validation.invalidModules(self, dict2, n, fname)
        if baynum == []:
            return
        baynum.sort(key=lambda x: x[0])
        for bn in baynum:
            name = enc + ', interconnect ' + str(bn[0])
            rname = name.encode("utf-8")
            uri = bn[2].encode("utf-8")
            str1 = '{"name":"' + rname + '","uri":"' + uri + '"}'
            if i == 0:
                al1 = bn[1] + ' in ' + str1
            else:
                al1 = ', ' + bn[1] + ' in ' + str1
            al2 = al2 + al1
            i = i + 1
        if i == 1:
            e_alert = 'Invalid interconnect link topology. ' + al2 + ' is not supported in a single enclosure topology.'
        else:
            e_alert = 'Invalid interconnect link topology. ' + al2 + ' are not supported in a single enclosure topology.'
        dict1 = {'enc': enc, 'bay': None, 'alert': e_alert}
        enc_alert.append(dict1)

    def checkIltDataError(self, i, num, fname):
        err_conn = []
        with open(fname) as data_file:
            data = json.load(data_file)
        with open('ilt.py') as data_file:
            data2 = json.load(data_file)
        if data2['members'][num]['topologyErrors'] != []:
            for conn in data['members'][i]['iltConnections']:
                if conn['from']['errorCode'] is not None:
                    enc = conn['from']['enclosureUri'][-10:]
                    bay = str(conn['from']['bayNumber'])
                    port = str(conn['from']['portId'])
                    err = conn['from']['errorCode']
                    err_conn.append({'enc': enc, 'bay': bay, 'port': port, 'error': err})
                else:
                    continue
            return err_conn
        else:
            return []

    def wrongConn(self, ebpx, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        err_conn = []
        ex = ebpx[0]
        bx = ebpx[1]
        px = ebpx[2]
        for conn in data['members'][id]['iltConnections']:
            if conn['from']['errorCode'] is not None:
                en = ILT_validation.getEncNo(self, conn['from']['enclosureUri'][-10:], fname)
                ba = str(conn['from']['bayNumber'])
                po = str(conn['from']['portId'])
                if en == ex and ba == bx and po == px:
                    try:
                        enx = ILT_validation.getEncNo(self, conn['to']['enclosureUri'][-10:], fname)
                        bax = str(conn['to']['bayNumber'])
                        pox = str(conn['to']['portId'])
                        return enx + bax + pox
                    except TypeError:
                        return 0

    def getActualAlerts(self, fname):
        enclosures = []
        with open('alerts.py') as data_file:
            data = json.load(data_file)
        with open(fname) as data_file:
            data2 = json.load(data_file)
        for encl in data2['enclosureMembers']:
            enclosures.append(encl['enclosureUri'][-10:])
        alertdata = []
        for al in data['members']:
            if al['healthCategory'] == 'Enclosure' or al['healthCategory'] == 'Interconnect':
                enc_name = al['associatedResource']['resourceName'].split(',')[0]
                if enc_name in enclosures:
                    alert = al['description']
                    res = al['healthCategory']
                    if res == 'Enclosure':
                        enc2 = al['associatedResource']['resourceName']
                        alertdata.append({'enc': enc2, 'bay': None, 'alert': alert})
                    elif res == 'Interconnect':
                        resource = al['associatedResource']['resourceName']
                        list1 = resource.split(',')
                        enc2 = list1[0]
                        ic = list1[1][-1:]
                        alertdata.append({'enc': enc2, 'bay': ic, 'alert': alert})
        return alertdata

    def getCorrectAlerts(self, fname, num):
        iltdata = []
        iik = []
        global enc_alert
        enc_alert = []
        global fault_enc
        fault_enc = []
        with open(fname) as data_file:
            data = json.load(data_file)
        num_of_fabrics = len(data['members'])
        if len(data['enclosureMembers']) == 1:
            ILT_validation.single_enc_Cl(self, fname)
        else:
            for n in range(0, num_of_fabrics):
                ILT_validation.noModulesSide(self, n, fname)
        for n in range(0, num_of_fabrics):
            iltdata.append(ILT_validation.checkIltDataError(self, n, num, fname))
        alertsdata = ILT_validation.getActualAlerts(self, fname)
        if iltdata == []:
            pass
        else:
            for item in iltdata:
                if item == []:
                    continue
                id = iltdata.index(item)
                for i in item:
                    if i['error'] == 'CxpPortNotConnected':
                        enc1 = i['enc']
                        fault_enc.append(enc1)
                        bay1 = int(i['bay'])
                        alerts = ILT_validation.cxpPortNotConnected(self, i, id, fname)
                        e_alert = alerts[0]
                        i_alert = alerts[1]
                        if ILT_validation.isPotash(self, i, id, fname) is False and ILT_validation.potashInBay(self, bay1, id, fname) == 0:
                            if bay1 > 3:
                                encl = 2
                            else:
                                encl = 1
                            e_alert = 'Invalid interconnect link topology. Interconnect is missing from enclosure ' + ILT_validation.getID(self, fname, ILT_validation.getEncName(self, encl, fname)) + ', interconnect bay ' + str(bay1) + '.'
                        ILT_validation.inWrongBay(self, i, id, fname)
                        dict1 = {'enc': enc1, 'bay': None, 'alert': e_alert}
                        dict2 = {'enc': enc1, 'bay': unicode(bay1), 'alert': i_alert}
                        enc_alert.append(dict1)
                        enc_alert.append(dict2)
                    elif i['error'] == 'CxpPortMiscabled':
                        enc1 = i['enc']
                        fault_enc.append(enc1)
                        bay1 = i['bay']
                        alerts = ILT_validation.cxpPortMiscabled(self, i, id, fname)
                        e_alert = alerts[0]
                        i_alert = alerts[1]
                        dict1 = {'enc': enc1, 'bay': None, 'alert': e_alert}
                        dict2 = {'enc': enc1, 'bay': unicode(bay1), 'alert': i_alert}
                        enc_alert.append(dict1)
                        enc_alert.append(dict2)
                    elif i['error'] == 'NeighbourInterconnectPoweredOff':
                        fault_enc.append(i['enc'])
                        ic1 = i['enc'] + ', interconnect ' + str(i['bay'])
                        ebpx = str(ILT_validation.getEncNo(self, i['enc'], fname)) + i['bay'] + i['port']
                        ebp2 = ILT_validation.wrongConn(self, ebpx, id, fname)
                        ic2 = ILT_validation.getEncName(self, int(ebp2[0]), fname) + ', interconnect ' + ebp2[1]
                        e_alert = 'Invalid interconnect link topology. Port L' + str(i['port']) + ' of interconnect ' + ILT_validation.getID(self, fname, ic1) + ' is connected to interconnect ' + ILT_validation.getID(self, fname, ic2) + ' which is powered off.'
                        i_alert = 'The connected port L' + str(i['port']) + ' is on an interconnect ' + ILT_validation.getID(self, fname, ic2) + ' that is powered off.'
                        dict1 = {'enc': i['enc'], 'bay': None, 'alert': e_alert}
                        dict2 = {'enc': i['enc'], 'bay': unicode(i['bay']), 'alert': i_alert}
                        enc_alert.append(dict1)
                        enc_alert.append(dict2)
                    elif i['error'] == 'InvalidInterconnectKind':
                        bay1 = i['bay']
                        enc1 = i['enc']
                        dict4 = {'enc': enc1, 'bay': bay1, 'port': i['port']}
                        if dict4 in iwb:
                            alerts = ILT_validation.cxpPortMiscabled(self, i, id, fname)
                            e_alert = alerts[0]
                            i_alert = alerts[1]
                            dict5 = {'enc': enc1, 'bay': None, 'alert': e_alert}
                            dict6 = {'enc': enc1, 'bay': bay1, 'alert': i_alert}
                            enc_alert.append(dict5)
                            enc_alert.append(dict6)
                        if ILT_validation.isPotash(self, i, id, fname) and enc1 + str(bay1) not in iik:
                            iik.append(enc1 + str(bay1))
                            ILT_validation.inWrongBay(self, i, id, fname)
                            if ILT_validation.invalidModules(self, i, id, fname) == 0:
                                if int(i['bay']) <= 3 and ILT_validation.getEncNo(self, i['enc'], fname) != '1':
                                    e_alert = 'Invalid interconnect link topology. Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module at Side A is not in first enclosure.'
                                    enc_list = ILT_validation.getListofEncs(self, fname)
                                    for enc in enc_list:
                                        fault_enc.append(enc)
                                        dict3 = {'enc': enc, 'bay': None, 'alert': e_alert}
                                        enc_alert.append(dict3)
                                elif int(i['bay']) > 3 and ILT_validation.getEncNo(self, i['enc'], fname) != '2':
                                    e_alert = 'Invalid interconnect link topology. Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module at Side B is not in first or second enclosure.'
                                    enc_list = ILT_validation.getListofEncs(self, fname)
                                    for enc in enc_list:
                                        fault_enc.append(enc)
                                        dict3 = {'enc': enc, 'bay': None, 'alert': e_alert}
                                        enc_alert.append(dict3)
                            if ILT_validation.potashInBay2(self, i, id, fname):
                                e_alert = 'Invalid interconnect link topology. More than one Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module present at one Side of bay set.'
                                enc_list = ILT_validation.getListofEncs(self, fname)
                                for enc in enc_list:
                                    fault_enc.append(enc)
                                    dict3 = {'enc': enc, 'bay': None, 'alert': e_alert}
                                    enc_alert.append(dict3)
                        elif not ILT_validation.isPotash(self, i, id, fname) and enc1 + str(bay1) not in iik:
                            iik.append(enc1 + str(bay1))
                            ILT_validation.inWrongBay(self, i, id, fname)
                        alerts = ILT_validation.invalidInterconnectKind1(self, i, fname)
                        fault_enc.append(enc1)
                        e_alert = alerts[0]
                        i_alert = alerts[1]
                        dict1 = {'enc': enc1, 'bay': None, 'alert': e_alert}
                        dict2 = {'enc': enc1, 'bay': unicode(bay1), 'alert': i_alert}
                        enc_alert.append(dict1)
                        enc_alert.append(dict2)
                    elif i['error'] == 'CxpPortNotConnectedToExpectedICMKind':
                        enc1 = i['enc']
                        bay1 = i['bay']
                        fault_enc.append(enc1)
                        if ILT_validation.portNotConnected(self, i, id, fname) is False:
                            alerts = ILT_validation.cxpPortMiscabled(self, i, id, fname)
                        else:
                            alerts = ILT_validation.cxpPortNotConnected(self, i, id, fname)
                        e_alert = alerts[0]
                        i_alert = alerts[1]
                        dict1 = {'enc': enc1, 'bay': None, 'alert': e_alert}
                        dict2 = {'enc': enc1, 'bay': unicode(bay1), 'alert': i_alert}
                        enc_alert.append(dict1)
                        enc_alert.append(dict2)
            for a in alertsdata:
                if a['enc'] not in fault_enc:
                    enc_alert.append({'enc': a['enc'], 'bay': None, 'alert': unicode('Invalid interconnect link topology')})
                    fault_enc.append(a['enc'])
        return enc_alert

    def invalidModules(self, i, id, fname):
        global enc_alert
        dict2 = {}
        with open(fname) as data_file:
            data = json.load(data_file)
        for item in data['members'][id]['iltConnections']:
            if item['from']['enclosureUri'][-10:] == i['enc'] and item['from']['bayNumber'] == int(i['bay']):
                k1 = item['from']['interconnectProductName']
                s = item['from']['baySetSide']
                break
        if k1.find('Switch Module') != -1:
            k2 = 'Virtual Connect'
        elif k1.find('Virtual Connect') != -1:
            k2 = 'Switch Module'
        if s == 'B':
            enc = ILT_validation.getEncName(self, 1, fname)
        elif s == 'A':
            if len(data['enclosureMembers']) == 1:
                enc = ILT_validation.getEncName(self, 1, fname)
            else:
                enc = ILT_validation.getEncName(self, 2, fname)
        for item in data['members'][id]['iltConnections']:
            if item['from']['enclosureUri'][-10:] == enc and item['from']['interconnectProductName'].find(k2) != -1:
                dict2 = {'name': item['from']['interconnectProductName'], 'bay': str(item['from']['bayNumber']), 'enc': item['from']['enclosureUri'][-10:]}
        if dict2 != {}:
            bay = str(i['bay'])
            en1 = i['enc'] + ', interconnect ' + bay
            prod = ILT_validation.getProduct2(self, i, id, fname)
            other_prod = dict2
            en2 = other_prod['enc'] + ', interconnect ' + str(other_prod['bay'])
            e_alert1 = 'Invalid combination of interconnect modules. ' + prod + ' in ' + ILT_validation.getID(self, fname, en1) + ' and ' + other_prod['name'] + ' in ' + ILT_validation.getID(self, fname, en2) + ' are in same interconnect bay set. This is not a supported configuration. {\"name\":\"Learn more\",\"uri\":\"/doc#/cic/interconnect/cabling/learn\"}'
            e_alert2 = 'Invalid combination of interconnect modules. ' + other_prod['name'] + ' in ' + ILT_validation.getID(self, fname, en2) + ' and ' + prod + ' in ' + ILT_validation.getID(self, fname, en1) + ' are in same interconnect bay set. This is not a supported configuration. {\"name\":\"Learn more\",\"uri\":\"/doc#/cic/interconnect/cabling/learn\"}'
            enc_list = ILT_validation.getListofEncs(self, fname)
            for enc in enc_list:
                fault_enc.append(enc)
                dict3 = {'enc': enc, 'bay': None, 'alert': e_alert1}
                dict4 = {'enc': enc, 'bay': None, 'alert': e_alert2}
                enc_alert.append(dict3)
                enc_alert.append(dict4)
        else:
            return 0
        return 1

    def inWrongBay(self, i, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        if len(data['enclosureMembers']) == 1:
            return
        enc1 = i['enc']
        bay1 = int(i['bay'])
        prod = ILT_validation.getProduct(self, id, fname)
        if prod == 0:
            prod = 'Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module'
        if bay1 > 3:
            encl = 2
            side = 'B'
            bsn = str(bay1 - 3)
        else:
            encl = 1
            side = 'A'
            bsn = str(bay1)
        fail_enc = ILT_validation.getEncName(self, encl, fname)
        iwb.append({'enc': enc1, 'bay': bay1, 'port': i['port']})

        if ILT_validation.isPotash(self, i, id, fname) and bsn not in wrong_bay:
            if bay1 > 3 and not ILT_validation.otherSidePotash(self, i, id, fname):
                wrong_bay.append(bsn)
                enc_list = ILT_validation.getListofEncs(self, fname)
                for enc in enc_list:
                    fault_enc.append(enc)
                    e_alert = 'Invalid interconnect link topology. ' + prod + ' not present at ' + side + '-side of bay set ' + bsn + ' in enclosure ' + ILT_validation.getID(self, fname, fail_enc) + '.'
                    dict3 = {'enc': enc, 'bay': None, 'alert': unicode(e_alert)}
                    enc_alert.append(dict3)
            elif side == 'A' and ILT_validation.getEncNo(self, enc1, fname) != '1':
                wrong_bay.append(bsn)
                enc_list = ILT_validation.getListofEncs(self, fname)
                for enc in enc_list:
                    fault_enc.append(enc)
                    e_alert = 'Invalid interconnect link topology. ' + prod + ' not present at A-side of bay set ' + bsn + ' in enclosure ' + ILT_validation.getID(self, fname, fail_enc) + '.'
                    dict3 = {'enc': enc, 'bay': None, 'alert': unicode(e_alert)}
                    enc_alert.append(dict3)
        elif not ILT_validation.isPotash(self, i, id, fname):
            fail_enc = ILT_validation.getEncName(self, 1, fname)
            if (bay1 <= 3 and ILT_validation.potashInBay(self, bay1, id, fname) == 0) or (bay1 > 3 and not ILT_validation.otherSidePotash(self, i, id, fname)):
                if bsn not in wrong_bay:
                    wrong_bay.append(bsn)
                    enc_list = ILT_validation.getListofEncs(self, fname)
                    for enc in enc_list:
                        fault_enc.append(enc)
                        e_alert = 'Invalid interconnect link topology. ' + prod + ' not present at A-side of bay set ' + bsn + ' in enclosure ' + ILT_validation.getID(self, fname, fail_enc) + '.'
                        dict3 = {'enc': enc, 'bay': None, 'alert': e_alert}
                        enc_alert.append(dict3)

    def noModulesSide(self, id, fname):
        global enc_alert
        side = []
        with open(fname) as data_file:
            data = json.load(data_file)
        for el in data['members'][id]['iltConnections']:
            bsn = str(el['from']['baySetNumber'])
            side.append(el['from']['baySetSide'])
        cl = ILT_validation.getNumChlorides(self, id, fname)
        if cl[0] == '0':
            if (len(side) / 2) < len(ILT_validation.getListofEncs(self, fname)):
                return
        else:
            if len(side) < len(ILT_validation.getListofEncs(self, fname)):
                return
        prod = ILT_validation.getProduct(self, id, fname)
        if prod == 0:
            prod = 'Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module'
        if 'A' not in side:
            s = 'A'
            fail_enc = ILT_validation.getEncName(self, 1, fname)
        # elif 'B' not in side:
        #    s = 'B'
        #    fail_enc = ILT_validation.getEncName(self, 2, fname)
        else:
            return
        wrong_bay.append(bsn)
        enc_list = ILT_validation.getListofEncs(self, fname)
        for enc in enc_list:
            fault_enc.append(enc)
            e_alert = 'Invalid interconnect link topology. ' + prod + ' not present at ' + s + '-side of bay set ' + bsn + ' in enclosure ' + ILT_validation.getID(self, fname, fail_enc) + '.'
            dict3 = {'enc': enc, 'bay': None, 'alert': unicode(e_alert)}
            enc_alert.append(dict3)
        return

    def otherSidePotash(self, i, id, fname):
        baynum = int(i['bay'])
        if baynum <= 3:
            baynum = baynum + 3
            encl = ILT_validation.getEncName(self, 2, fname)
        else:
            baynum = baynum - 3
            encl = ILT_validation.getEncName(self, 1, fname)
        with open(fname) as data_file:
            data = json.load(data_file)
        potash_other_side = False
        for item in data['members'][id]['iltConnections']:
            if item['from']['enclosureUri'][-10:] == encl and item['from']['bayNumber'] == baynum:
                potash_other_side = item['from']['interconnectProductName'].find('40Gb F8') != -1
                break
        return potash_other_side

    def getProduct2(self, i, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        enc = i['enc']
        prod = 0
        for item in data['members'][id]['iltConnections']:
            if item['from']['interconnectProductName'].find('40Gb F8') != -1 and item['from']['bayNumber'] == int(i['bay']):
                prod = item['from']['interconnectProductName']
                break
        return prod

    def getProduct(self, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        prod = 0
        for item in data['members'][id]['iltConnections']:
            if item['from']['interconnectProductName'].find('40Gb F8') != -1:
                prod = item['from']['interconnectProductName']
                break
        return prod

    def invalidInterconnectKind1(self, i, fname):
        en1 = i['enc'] + ', interconnect ' + i['bay']
        alert_ic = 'Interconnect is invalid and makes port L' + i['port'] + ' critical.'
        alert_enc = 'Invalid interconnect link topology. Interconnect ' + ILT_validation.getID(self, fname, en1) + ' is invalid and makes port L' + i['port'] + ' critical.'
        return [unicode(alert_enc), unicode(alert_ic)]

    def isPotash(self, i, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        is_potash = False
        for item in data['members'][id]['iltConnections']:
            if item['from']['enclosureUri'][-10:] == i['enc'] and item['from']['bayNumber'] == int(i['bay']):
                is_potash = item['from']['interconnectProductName'].find('40Gb F8') != -1
                break
        return is_potash

    def potashInBay(self, baynum, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        var = 0
        for item in data['members'][id]['iltConnections']:
            if item['from']['interconnectProductName'].find('40Gb F8') != -1 and item['from']['bayNumber'] == baynum:
                var = 1
                break
        return var

    def potashInBay2(self, i, id, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        bays = []
        for item in data['members'][id]['iltConnections']:
            if item['from']['interconnectProductName'].find('40Gb F8') != -1 and item['from']['bayNumber'] == i['bay']:
                bays.append(i['enc'] + str(i['bay']))
        bays = list(set(bays))
        if len(bays) > 1:
            return True
        else:
            return False

    def getListofEncs(self, fname):
        enc_list = []
        with open(fname) as data_file:
            data = json.load(data_file)
        for item in data['enclosureMembers']:
            enc_list.append(item['enclosureUri'][-10:])
        return enc_list

    def getID(self, fname, name):
        with open('alerts.py') as data_file:
            data = json.load(data_file)
            dictid = {}
            str1 = ''
        for s in data['members']:
            if name == s['associatedResource']['resourceName']:
                rname = name.encode("utf-8")
                uri = s['resourceUri'].encode("utf-8")
                str1 = '{"name":"' + rname + '","uri":"' + uri + '"}'
                break
            else:
                continue
        if str1 != '':
            return str1
        else:
            with open(fname) as data_file:
                data2 = json.load(data_file)
            enc = name.split(',')[0]
            bay = name[-1]
            for n in range(0, len(data2['members'])):
                for s in data2['members'][n]['iltConnections']:
                    if s['from']['enclosureUri'][-10:] == enc and str(s['from']['bayNumber']) == bay:
                        uri = s['from']['interconnectUri']
                        break
            rname = name.encode("utf-8")
            str1 = '{"name":"' + rname + '","uri":"' + uri + '"}'
            return str1

    def cxpPortNotConnected(self, item, id, fname):
        found = 0
        ebp1 = ILT_validation.getEncNo(self, item['enc'], fname) + item['bay'] + item['port']
        ebp2 = ILT_validation.correctConn(self, id, ebp1, fname)
        ebp3 = ILT_validation.getEncName(self, ebp2[0], fname) + ebp2[-2:]
        en1 = item['enc'] + ', interconnect ' + item['bay']
        l = len(ebp3)
        b = ebp3[l - 2]
        en2 = ebp3[slice(0, -2)] + ', interconnect ' + b
        p = ebp3[l - 1]
        with open(fname) as data_file:
            data = json.load(data_file)
        for dat in data['members'][id]['iltConnections']:
            if dat['from']['enclosureUri'][-10:] == ebp3[slice(0, -2)] and dat['from']['bayNumber'] == int(b):
                found = 1
                break
        if found == 1:
            alert_enc = 'Invalid interconnect link topology cabling. Cable connecting port L' + item['port'] + ' of ' + ILT_validation.getID(self, fname, en1) + ' to port L' + p + ' of ' + ILT_validation.getID(self, fname, en2) + ' is missing.'
        else:
            alert_enc = 'Invalid interconnect link topology. Interconnect is missing from enclosure ' + ILT_validation.getID(self, fname, ebp3[slice(0, -2)]) + ', interconnect bay ' + b + '.'
        alert_ic = 'Interconnect port L' + item['port'] + ' is not cabled'
        return [unicode(alert_enc), unicode(alert_ic)]

    def cxpPortMiscabled(self, item, id, fname):
        ebp1 = ILT_validation.getEncNo(self, item['enc'], fname) + item['bay'] + item['port']
        ebp_wr = ILT_validation.wrongConn(self, ebp1, id, fname)
        if ebp_wr != 0:
            if ebp1[-2] != ebp_wr[-2]:
                ILT_validation.inWrongBay(self, item, id, fname)
            ebp_wrong = ILT_validation.getEncName(self, ebp_wr[0], fname) + ebp_wr[-2:]
            en1 = item['enc'] + ', interconnect ' + item['bay']
            l = len(ebp_wrong)
            b = ebp_wrong[l - 2]
            en2 = ebp_wrong[slice(0, -2)] + ', interconnect ' + b
            p = ebp_wrong[l - 1]
            alert_enc = 'Invalid interconnect link topology cabling. Cable connecting ' + ILT_validation.getID(self, fname, en1) + ', port L' + item['port'] + ' to ' + ILT_validation.getID(self, fname, en2) + ', port L' + p + ' is improperly connected. {"name":"Learn more","uri":"/doc#/cic/interconnect/cabling/learn"}'
            if (ebp_wr[0] + ebp_wr[1]) != (ebp1[0] + ebp1[1]):
                alert_ic = 'Interconnect port L' + item['port'] + ' is incorrectly connected to ' + ILT_validation.getID(self, fname, en2) + ', port L' + p
            else:
                alert_ic = 'Interconnect port L' + item['port'] + ' is incorrectly connected to ' + en2 + ', port L' + p
        else:
            en1 = item['enc'] + ', interconnect ' + item['bay']
            alert_enc = 'Invalid interconnect link topology cabling. Cable from ' + ILT_validation.getID(self, fname, en1) + ', port L' + item['port'] + ' is either disconnected or connected to an outside management ring.'
            alert_ic = 'Interconnect port L' + item['port'] + ' is either disconnected or connected to an outside management ring.'
        return [unicode(alert_enc), unicode(alert_ic)]

    def listsShouldBeEqual(self, list1, list2):
        msg = None
        values = True
        misses = []
        extras = []
        matches1 = ILT_validation.matchAlerts(self, list1, list2)
        matches = matches1[0]
        list1x = matches1[1]
        list2x = matches1[2]
        for item2 in list2x:
            if item2['bay'] is None:
                misses.append('Alert for enclosure ' + item2['enc'][-10:] + ' missing: ' + item2['alert'])
            else:
                misses.append('Alert for interconnect ' + item2['bay'] + ' in enclosure ' + item2['enc'][-10:] + ' missing: ' + item2['alert'])
        for item1 in list1x:
            if item1['bay'] is None:
                extras.append('Alert for enclosure ' + item1['enc'][-10:] + ' not expected: ' + item1['alert'])
            else:
                extras.append('Alert for interconnect ' + item1['bay'] + ' in enclosure ' + item1['enc'][-10:] + ' not expected: ' + item1['alert'])
        default = 'ALL ALERTS DO NOT MATCH:\n'
        matched_list = 'Correct ALERTS\n' + '\n'.join(matches)
        missing_list = 'Missing ALERTS\n' + '\n'.join(misses)
        extra_list = 'Unexpected ALERTS\n' + '\n'.join(extras)
        logger._log_to_console_and_log_file('\n' + missing_list + '\n\n' + extra_list + '\n\n' + matched_list)
        return (misses + extras)

    def matchAlerts(self, list1, list2):
        matched = []
        for item1 in list1:
            ind = list1.index(item1)
            flag = 0
            for item2 in list2:
                if item1 == item2:
                    flag = 1
                    if item1['bay'] is None:
                        matched.append('Alert for enclosure ' + item1['enc'][-10:] + ' is correct: ' + item1['alert'])
                    else:
                        matched.append('Alert for interconnect ' + item1['bay'] + ' in enclosure ' + item1['enc'][-10:] + ' is correct: ' + item1['alert'])
                    list2.remove(item2)
                    break
            if flag == 1:
                list1[ind] = 0
        list1 = [item for item in list1 if item != 0]
        return [matched, list1, list2]

    def verify_ic_ports(self, ip, cred, getresponse):
        dcs = "No"
        appip = "15.212.137.104"
        username = "root"
        password = "hpvse1"
        emipv6 = "fe80::3ea8:2aff:fe25:3068%bond0"
        enclosurename = "FVTCRMENC3"
        icbay = "6"
        blk = "163"
        power_state = "On"
        prod_name = "Synergy 10Gb Interconnect Link Module"
        port_count = 1
        dict1 = {}
        logger._log_to_console_and_log_file('Verifying ILP connector information')
        with open('ilt.py', 'w') as outfile:
            json.dump(getresponse, outfile, indent=4)
        with open('ilt.py') as data_file:
            data = json.load(data_file)
        n = data['count']
        json_credentials = json.dumps(cred)
        base_url = 'https://%s' % (ip)
        headers1 = {'content-type': 'application/json', 'accept': 'application/json', 'X-Api-Version': '300'}
        login_url = base_url + '/rest/login-sessions'
        resp = requests.post(login_url, data=json_credentials, headers=headers1, verify=False)
        sessionid = json.loads(resp.text)["sessionID"]
        headers = {'auth': sessionid, 'X-Api-Version': 300}
        for num in range(0, n):
            for con in data['members'][num]['iltConnections']:
                if con['from']['enclosureUri'][-10:] == enclosurename and str(con['from']['bayNumber']) == icbay:
                    ic_uri = con['from']['interconnectUri'].split('/')[3]
                    break
        uri = base_url + '/rest/interconnects/pluggableModuleInformation/' + ic_uri
        response = requests.get(uri, headers=headers, verify=False)
        logger._log_to_console_and_log_file('API Response' + str(response.text))
        f = open('port_data2', 'w')
        f.write(response.text)
        pdata = json.loads(response.text)
        for p in pdata:
            dict1.update({'Vendor OUI': p['vendorOui']})
            dict1.update({'Part number': p['vendorPartNumber']})
            # dict1.update('Type': p['identifier'])
            # dict1.update('Speed': p['speed'])
            # dict1.update('Vendor': p['vendorName'])
            dict1.update({'Serial number': p['serialNumber']})
            dict1.update({'Revision': p['vendorRevision']})
        port_dict = em_operation._get_connector_information_from_em(dcs, enclosurename, appip, username, password, emipv6, icbay, blk, power_state, prod_name, port_count)
        for item in port_dict:
            if isinstance(item, dict):
                port_dict = item
                break
            else:
                continue
        l_keys = port_dict.keys()
        logger._log_to_console_and_log_file('Canmic data' + str(port_dict))
        for l in l_keys:
            if port_dict[l] == []:
                del port_dict[l]
        f = open('port_data', 'w')
        f.write(str(port_dict) + '\n' + str(dict1))
        if cmp(port_dict, dict1) == 0:
            return True
        else:
            return False

    def _get_connector_information_from_em(self, dcs, enclosurename, appip, username, password, emipv6, icbay, blk, power_state, prod_name, port_count):

        logger.info("Function to Get connector information from EM")
        # Capture the port connector information by logger into EM
        vendorOUI = ""
        partnumber = ""
        serialnumber = ""
        revision = ""
        connector_present = ""
        connectortype = ""
        connectorspeed = ""
        connectorvendor = ""
        cxpdata = ""
        ic_dict = {"Type": [], "Speed": [], "Vendor": [], "Vendor OUI": [],
                   "Part number": [], "Revision": [], "Serial number": []}
        if dcs.lower() == 'yes':
            # For DCS EM
            cmd = 'curl -ik --request POST https://%s/rest/v1/Managers/20%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (emipv6, icbay, blk)
        else:
            # Get XAUTH of EM to use with EM RIS request
            xauth_cmd = ['/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (enclosurename)]
            (datalst, errorcode) = data_variablesget_data_from_switch(self, appip, xauth_cmd, username, password)
            strdata = ''.join(datalst)
            xauth = strdata.strip()
            cmd = 'curl --globoff -ki -x "" --request POST --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (xauth, emipv6, icbay, blk)

        port = 22
        mdata = data_variables.get_canmic_block(self, appip, port, username, password, cmd)

        # check the presence of CXP connector
        if (power_state != "Off" and len(mdata) > 0):
            connector_present = mdata[0]
            connector_present = '{0:08b}'.format(int(mdata[0]))
            connector_present = connector_present[-1]

            if connector_present is "0":
                logger.info("C1 - Connector is present")
                # Get Vendor OUI
                i = 1
                while i < 4:
                    if mdata[i] != "" and mdata[i] != "20":
                        vendorOUI = vendorOUI + (mdata[i]).upper()
                        if (i < 3):
                            vendorOUI = vendorOUI + "-"

                    i = i + 1
                # Get Part number
                i = 4
                while i < 20:
                    if mdata[i] != "" and mdata[i] != "20":
                        partnumber = partnumber + chr(int(mdata[i], 16))
                    i = i + 1
                i = 20
                while i < 22:
                    revision = revision + chr(int(mdata[i], 16))
                    i = i + 1

                # get serial-number
                i = 22
                while i < 38:
                    if mdata[i] != "" and mdata[i] != "20":
                        serialnumber = serialnumber + chr(int(mdata[i], 16))
                    i = i + 1

                if(("Synergy 20Gb Interconnect Link Module" in prod_name) or ("Synergy 10Gb Interconnect Link Module" in prod_name)):
                    blk = 200 + port_count
                    connectortype = ""
                    connectorspeed = ""
                    connectorvendor = ""
                    if dcs.lower() == 'yes':
                                        # For DCS EM
                        cmd = 'curl -ik --request POST https://%s/rest/v1/Managers/20%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (emipv6, icbay, blk)
                    else:

                        cmd = 'curl --globoff -ki -x "" --request POST --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s -H "Content-Type: application/json" -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (xauth, emipv6, icbay, blk)

                    cxpdata = data_variables.get_canmic_block(self, appip, port, username, password, cmd)
                elif ("Synergy 10/40Gb Pass-Thru Module" in prod_name):
                    cxpdata = mdata

                if len(cxpdata) > 0:
                    logger.info("---%s" % (cxpdata))

                    connectortype_temp = int(cxpdata[54], 16)
                    if connectortype_temp == 254:
                        connectortype = "ILP"
                    if connectortype_temp == 255:
                        connectortype = "Unknown"
                    if connectortype_temp == 64:
                        connectortype = "10GBASE-T"
                    if connectortype_temp == 43:
                        connectortype = "Active DAC"
                    if connectortype_temp == 42:
                        connectortype = "Passive DAC"

                    connectorspeed = str(12 * (int(cxpdata[53], 16)))

                    if cxpdata[0] == '00':
                        connectorvendor = "none"
                    if cxpdata[0] == '43':
                        connectorvendor = "Cisco"
                    if cxpdata[0] == '4e':
                        connectorvendor = "HP Network"
                    if cxpdata[0] == '53':
                        connectorvendor = "HP Servers"
                    ic_dict["Type"] = connectortype
                    ic_dict["Speed"] = connectorspeed
                    ic_dict["Vendor"] = connectorvendor

                logger.info(vendorOUI)
                logger.info(partnumber)
                logger.info(revision)
                logger.info(serialnumber)
                ic_dict["Vendor OUI"] = vendorOUI
                ic_dict["Part number"] = partnumber
                ic_dict["Revision"] = revision
                ic_dict["Serial number"] = serialnumber

            else:
                logger.info("No Connector in EM")
        else:
            logger.info("ICM power is off state, we will not be able to read Canmic Block")
        return (connector_present, ic_dict)

    def get_data_from_switch(self, switch_ip, commands, uname, pwd):
        ''' This function logs into the switch and runs the commands passed. Commands here is a list of commands.
            The output will be a list of the return value and return code after command execution in the same order
            that the commands were passed '''

        logger.info("\nConnecting to %s and run command %s" % (switch_ip, commands))
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22
        errorcodelist = []
        datalist = []
        logger.info("Password is %s" % pwd)
        client.connect(switch_ip, port=port, username=uname, password=pwd)
        i = 0
        for command in commands:
            print "executing command %s" % command
            input, output, error = client.exec_command(command)
            errorcodelist.insert(i, output.channel.recv_exit_status())
            datalist.insert(i, output.read())
            i = i + 1
        return (datalist, errorcodelist)

    def get_canmic_block(self, appip, port, appuname, apppassw, cmd):
        """
            This function reads CANMIC blocks from EM using EM IPV6
        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(appip, port, appuname, apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        logger.info("cmd %s" % cmd)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        d = data.split("\n")
        mdata = []

        for k in d:
            head, sep, tail = k.partition('|')
            head = head[10:].split(" ")
            mdata = mdata + head
        return filter(None, mdata)
