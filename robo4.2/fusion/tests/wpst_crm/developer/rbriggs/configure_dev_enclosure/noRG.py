from FusionLibrary import FusionLibrary
import argparse
import csv
import os
import sys
import json
import logging
import pprint
log = logging.getLogger('fusion')
logging.basicConfig(format='%(asctime)-15s,%(levelname)s,%(name)s,%(message)s')
log.setLevel(logging.INFO)

os.environ['https_proxy'] = 'https://web-proxy.corp.hpecorp.net:8088'
os.environ['HTTPS_PROXY'] = 'https://web-proxy.corp.hpecorp.net:8088'

# Need a way to pass in tags

lib = FusionLibrary()


def users(data):
    resp_list = []
    for user in data:
        resp_list.append(lib.fusion_api_add_user(body=user))
        log.info(resp_list)
    return resp_list


def main():
    # TODO: REMOVE BELOW!!!!
    sys.argv = ["-h", "16.83.6.1", "-V", "efit_data_variables"]

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--host', help='Fusion Appliance IP', required=True)
    parser.add_argument('-V', '--variables', help='Python Variable file', required=True)
    parser.add_argument('-x', '--xapi', help='Fusion X-Api-Version', required=False)

    # TODO: REMOVE BELOW!
    # args = parser.parse_args()
    args = parser.parse_args(sys.argv)
    data = __import__(args.variables)
    creds = {'userName': 'Administrator', 'password': 'Cosmos123'}

    try:
        resp = lib.fusion_api_login_appliance(args.host, creds)
    except Exception as e:
        log.error(e)

    # USERS
    # x = users(data.users)
    spts = lib.fusion_api_get_server_profile_templates()
    servers = lib.fusion_api_get_server_hardware()
    icms = lib.fusion_api_get_interconnect()
    s = []
    for server in servers['members']:
        print server['name']
        l = ['serialNumber', 'memoryMb', 'model', 'name', 'position', 'processorCount', 'processorType', 'portMap']
        d = dict()
        for i in server.iterkeys():
            if i in l:
                if i == 'portMap':
                    for slot in server[i]['deviceSlots']:
                        d[slot['location'] + str(slot['slotNumber'])] = slot['deviceName']
                else:
                    d[i] = server[i]
        s.append(d)
        # s[server['name']] = d
    s = sorted(s)
    j = json.dumps(s)
    pprint.pprint(s)

    with open('servers.csv', 'w') as csvfile:
        fieldnames = ['name', 'position', 'model', 'serialNumber', 'memoryMb', 'processorCount', 'processorType',
                      'Mezz1', 'Mezz2', 'Mezz3', 'Mezz4', 'Mezz5', 'Mezz6', 'Mezz7', 'Mezz8', 'Mezz9', 'Mezz10',
                      'Mezz11', 'Mezz12']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for i in xrange(0, len(s)):
            writer.writerow(s[i])


if __name__ == '__main__':
    main()
