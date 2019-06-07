from RoboGalaxyLibrary.utilitylib import logging as logger
from tests.DEA.resource.iLO.PERISClient import PERISClient
import json
from flatdict import FlatDict
from robot.libraries.BuiltIn import BuiltIn
import os
import shutil


def login_ilo(host, cred, headers=None, legacy=False, odata_status=True):
        """ Logs into the iLO, creating an iLO session

        'host' IP address of the iLO
        'cred' the Username and Password for the iLO session in a dictionary format
        """

        logger._info('Login to Host: %s with credentials: %s' % (host, cred))
        if '[' not in host:
            host = '[' + host + ']'
        ilo_client = PERISClient()
        ilo_client._host = host
        ilo_client._cred = cred or {"UserName": "Administrator", "Password": "admin"}
        # something weird with the tabs, added this so the file detects something new
        if 'X-Auth-Token' in ilo_client._headers:
            ilo_client._headers.pop('X-Auth-Token')
        if legacy:
            uri = BuiltIn().get_variable_value("${iLO_REST_SESSION_URI}")
        else:
            uri = BuiltIn().get_variable_value("${iLO_REDFISH_SESSION_URI}")
            if odata_status:
                ilo_client.update_headers('OData-Version', BuiltIn().get_variable_value("${iLO_REDFISH_VERSION}"))
        logger._debug('POST Body: %s' % json.dumps(cred))
        resp = ilo_client.post(uri, headers=headers, data=json.dumps(cred))
        sessionID = None
        if 'x-auth-token' in resp.headers:
            sessionID = resp.headers['x-auth-token']
            logger._debug('X-Auth-Token: %s' % sessionID)
            # leaving below here in case we need to test more than 1 active sessions
#             ilo_client._active_sessions[cred['UserName']] = {'Password': cred['Password'], 'sessionID': sessionID}
            ilo_client._sessionID = sessionID
            ilo_client.update_headers('X-Auth-Token', sessionID)
            logger._info('Session URI: %s' % sessionID)
            if 'location' in resp.headers:
                ilo_client._session_uri = resp.headers['location']
                ilo_client._session_uri = ilo_client._session_uri.split(']')[1]
        return ilo_client, resp, sessionID


def login_ilo_ipv4(host, cred, headers=None, legacy=False):
        """ Logs into the iLO, creating an iLO session

        'host' IP address of the iLO
        'cred' the Username and Password for the iLO session in a dictionary format
        """

        logger._info('Login to Host: %s with credentials: %s' % (host, cred))
        ilo_client = PERISClient()
        ilo_client._host = host
        ilo_client._cred = cred or {"UserName": "Administrator", "Password": "admin"}
        # something weird with the tabs, added this so the file detects something new
        if 'X-Auth-Token' in ilo_client._headers:
            ilo_client._headers.pop('X-Auth-Token')
        if legacy:
            uri = BuiltIn().get_variable_value("${iLO_REST_SESSION_URI}")
        else:
            uri = BuiltIn().get_variable_value("${iLO_REDFISH_SESSION_URI}")
            ilo_client.update_headers('OData-Version', BuiltIn().get_variable_value("${iLO_REDFISH_VERSION}"))
        logger._debug('POST Body: %s' % json.dumps(cred))
        resp = ilo_client.post(uri, headers=headers, data=json.dumps(cred))
        sessionID = None
        if 'x-auth-token' in resp.headers:
            sessionID = resp.headers['x-auth-token']
            logger._debug('X-Auth-Token: %s' % sessionID)
            # leaving below here in case we need to test more than 1 active sessions
#             ilo_client._active_sessions[cred['UserName']] = {'Password': cred['Password'], 'sessionID': sessionID}
            ilo_client._sessionID = sessionID
            ilo_client.update_headers('X-Auth-Token', sessionID)
            if 'location' in resp.headers:
                ilo_client._session_uri = resp.headers['location']
                ilo_client._session_uri = '/re' + ilo_client._session_uri.split('re')[1]
        return ilo_client, resp, sessionID


def get_ilo_sessions(ilo_client):
        return ilo_client.get('/redfish/v1/Sessions/')


def delete_all_ilo_sessions(ilo_client):
    session_list = get_ilo_sessions()
    for session in session_list['Members']:
        ilo_client.delete(session['href'])


def resetiLO(ilo_client):
        uri = '/redfish/v1/Managers/1/Actions/Manager.Reset/'
        payload = { }
        response = ilo_client.post(uri, payload)
        return response.status_code


def delete_ilo_session(ilo_client):
    return ilo_client.delete(ilo_client._session_uri)


def set_server_power(ilo_client, operation):
        uri = '/redfish/v1/Systems/1/Actions/ComputerSystem.Reset'
        postpayload = {"ResetType": str(operation)}
        resp = ilo_client.post(uri, data=json.dumps(postpayload))
        return resp.status_code

def get_server_power(ilo_client):
        uri = '/redfish/v1/Systems/1'
        resp = ilo_client.get(uri)
        power_state = resp.json()['PowerState']
        return power_state

def get_ilo_users_ris_id(ilo_client):
        user_list = []
        userList = ilo_client.get('/redfish/v1/AccountService/Accounts/')
        userList = userList.json()
        for key, value in userList.iteritems():
            if key == 'Members':
                for index in range(len(value)):
                    user_uri = value[index]['@odata.id']
                    user_list.append(user_uri)
        return user_list


def get_ilo_loginnames_id(ilo_client):
        loginid_dict = {}
        loginid_dictusers = {}
        user_list = []
        ilo_mgr_type = ilo_client.get('/redfish/v1/Managers/1/')
        ilo_manager_type = ilo_mgr_type.json()['FirmwareVersion']
        userList = ilo_client.get('/redfish/v1/AccountService/Accounts/')
        userList = userList.json()
        for key, value in userList.iteritems():
            if key == 'Members':
                user_list = value
                for index in range(len(user_list)):
                    Id = value[index]['@odata.id']
                    temp_value = ilo_client.get(Id)
                    if temp_value.status_code == 200:
                        temp_value = temp_value.json()
                        if 'iLO 4' in ilo_manager_type:
                            Login_name = temp_value['Oem']['Hp']['LoginName']
                        else:
                            Login_name = temp_value['Oem']['Hpe']['LoginName']
                        loginid_dict[Login_name] = Id
                        loginid_dictusers.update(loginid_dict)
        return loginid_dictusers


def delete_ilo_users(ilo_client):
        result_list = []
        loginid_dictusers = get_ilo_loginnames_id(ilo_client)
        for key, value in loginid_dictusers.iteritems():
            if key != 'Administrator':
                re = ilo_client.delete(value)
                re.headers['status'] = str(re.status_code)
                result_list.append(re.headers)
        return result_list


def delete_ilo_user(ilo_client, user):
    loginid_dictusers = get_ilo_loginnames_id(ilo_client)
    for key, value in loginid_dictusers.iteritems():
        if key == user:
            re = ilo_client.delete(value)
            return re.status_code


def get_ris_object(ilo_client, uri):
    resp = ilo_client.get(uri)
    if resp.status_code == 200:
        return FlatDict(resp.json(), '.')
    else:
        return resp.status_code

def patch_ris_object(ilo_client, uri, data):
    resp = ilo_client.patch(uri, data)
    if resp.status_code == 200:
        return FlatDict(resp.json(), '.')
    else:
        return resp.status_code
    
def post_ris_object(ilo_client, uri, data):
    resp = ilo_client.post(uri, data)
    if resp.status_code == 200:
        return FlatDict(resp.json(), '.')
    else:
        return resp.status_code
    
def get_ilo_provider_object(ilo_client, pType):
    providerObject = []
    uri = '/redfish/v1/providers/'
    response = ilo_client.get(uri)
    if response.status_code == 200:
        if 'Members' in response.json():
            providerListLink = response.json()['Members']
            for provider in providerListLink:
                provider_uri = provider['@odata.id']
                provider_resource = ilo_client.get(provider_uri)
                if provider_resource.status_code == 200 and pType:
                    resource_list = provider_resource.json()['Resources']
                    for resource in resource_list:
                        if resource['Type'].startswith(pType):
                            resource_uri = resource['href']
                            resource_response = ilo_client.get(resource_uri)
                            if resource_response.status_code == 200:
                                providerObject.append(FlatDict(resource_response.json(), '.'))
                            else:
                                raise AssertionError('Unable to retrieve object for provider type: %s' % pType)
                elif provider_resource.status_code == 200 and pType is None:
                    providerObject.append(FlatDict(provider_resource.json(), '.'))
                else:
                    raise AssertionError('Unable to retrieve provider data in provider list for: %s' % provider['@odata.id'])
    else:
        raise AssertionError('Unable to retrieve provider list for: %s' % ilo_client._host)
    return providerObject


def get_firmware_inventory(ilo_client):
        ris_obj = ilo_client.get('/redfish/v1/Systems/1/FirmwareInventory')
        return ris_obj.json()


def get_chassis_info(ilo_client):
    ris_obj = ilo_client.get('/redfish/v1/Chassis/1/')
    return ris_obj.json()


def show_blade_firmware_table(self):
        firmwareTable = '''
        <TABLE  BORDER="5">
          <TR>
            <TH COLSPAN="3" style="background-color:yellowgreen;color:white;>
              <H3><BR>FIRMWARE REVISION DETAILS</H3>
            </TH>
          </TR>
            <TH bgcolor="#5D7B9D"><font color="#fff">COMPONENT</font></TH>
            <TH bgcolor="#5D7B9D"><font color="#fff">LOCATION</font></TH>
            <TH bgcolor="#5D7B9D"><font color="#fff">FIRMWARE VERSION</font></TH>
        '''
        myjson = get_firmware_inventory(self)
        chassis_json = get_chassis_info(self)
        try:
            for item in myjson['Current'].values():
                firmwareTable += "<TR>\n"
                firmwareTable += "<TD>\n"
                firmwareTable += str(item[0]['Name']) + "\n"
                firmwareTable += "</TD>\n"
                firmwareTable += "<TD>\n"
                firmwareTable += str(item[0]['Location']) + "\n"
                firmwareTable += "</TD>\n"
                firmwareTable += "<TD>\n"
                firmwareTable += str(item[0]['VersionString']) + "\n"
                firmwareTable += "</TD>\n"
                firmwareTable += "</TR>\n"
            firmwareTable += "<TR>\n"
            firmwareTable += "<TD>\n"
            firmwareTable += str(chassis_json['Model']) + "\n"
            firmwareTable += "</TD>\n"
            firmwareTable += "<TD>\n"
            firmwareTable += str(chassis_json['Oem']['Hp']['BayNumber']) + "\n"
            firmwareTable += "</TD>\n"
            firmwareTable += "<TD>\n"
            firmwareTable += "</TABLE>\n"
            BuiltIn().log(firmwareTable, html=True)
        except:
            raise Exception("Unable to retrieve blade firmware details!")


def updateFirmware(ilo_client, fw_uri):
        uri = '/redfish/v1/Managers/1/UpdateService/Actions/HpiLOFirmwareUpdate.InstallFromURI/'
        payload = {
            "FirmwareURI": fw_uri, "TPMOverrideFlag": False}
        response = ilo_client.post(uri, payload)
        return response.status_code


def get_updateFirmware_state(ilo_client):
        uri = '/redfish/v1/Managers/1/UpdateService/'
        response = ilo_client.get(uri)
        response = response.json()
        return response["State"]


def get_updateFirmware_details(ilo_client):
        uri = '/redfish/v1/Managers/1/UpdateService/'
        response = ilo_client.get(uri)
        response = response.json()
        return response['Details']


def get_updateFirmware_progresspercent(ilo_client):
        uri = '/redfish/v1/Managers/1/UpdateService/'
        response = ilo_client.get(uri)
        response = response.json()
        return response['ProgressPercent']


def get_updateFirmware_reset_flag(ilo_client):
        uri = '/redfish/v1/Managers/1/UpdateService/'
        response = ilo_client.get(uri)
        response = response.json()
        return response['Flags']


def get_ilo_session_number(ilo_client, username):
    session_list = ilo_client.get('/redfish/v1/Sessions/')
    session_list = session_list.json()
    result = []
    for session in session_list['Members']:
        if username in session['@odata.id']:
            result.append(session['@odata.id'])
    return result


def get_ilo_ipv4(ilo_client):
    ethernet_json = ilo_client.get('/redfish/v1/Managers/1/EthernetInterfaces/1')
    ethernet_json = ethernet_json.json()
    ipv4 = ethernet_json['IPv4Addresses'][0]['Address']
    return ipv4


def get_mezz_uris(ilo_client):
        slotids = []
        slotno = []
        responsecode_list = []
        slotdict = {}
        for i in range(1, 12):
            response = ilo_client.get('/rest/v1/Chassis/1/MezzFrus/' + str(i))
            try:
                responsecode_list.append(response.status_code)
                slotno.append(response.json()['PhysicalSlot'])
                slotids.append(i)
                slotdict[response.json()['PhysicalSlot']] = i
            except:
                continue
        return slotdict, slotno, responsecode_list


def set_boot_order(ilo_client, boot_order):
        uri = '/redfish/v1/Systems/1/bios/boot/settings/'
        payload = {
            "PersistentBootConfigOrder": [boot_order]}
        ilo_client.update_headers('eTag', '*')
        response = ilo_client.patch(uri, payload)
        return response.status_code


def hphdbind(bin_path, fru_inst):
    hphdbind_path = BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + '//HPHDBIND'
    FRU_UPDATE_ROOT = BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + '/'
    golden_bin = "golden.bin"
    hphdbind_cmd = ("%s -x %s/eep_Tbird.xml -b %s -i %s -o %s") % (hphdbind_path, FRU_UPDATE_ROOT, FRU_UPDATE_ROOT + bin_path, FRU_UPDATE_ROOT + fru_inst, FRU_UPDATE_ROOT + golden_bin)
    return hphdbind_cmd


def hpqlocfg(bin_path, ilo_ip, ilo_user, ilo_password):
    hpqlocfg_path = BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + '//HPQLOCFG'
    FRU_UPDATE_XML = 'c:/' + BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + '//fru_update.xml'
    HPQLOCFG_REF_XML = BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + '//Update_Firmware.xml'
    with open(HPQLOCFG_REF_XML, 'r') as file:
            contents = file.read()
    new_contents = contents.replace('golden', bin_path)
    new_contents = new_contents.replace('adminname', ilo_user)
    new_contents = new_contents.replace('pwd', ilo_password)
    if os.path.exists(FRU_UPDATE_XML):
        os.remove(FRU_UPDATE_XML)
    with open(FRU_UPDATE_XML, 'w') as file:
            file.write(new_contents)
    hpqlocfg_cmd = ("%s -s %s -f %s >> update_fru_mezz_output_temp.txt") % (hpqlocfg_path, ilo_ip, FRU_UPDATE_XML)
    return hpqlocfg_cmd


def get_mezz_partnumber(ilo_client, mezz_slot):
    response = ilo_client.get('/rest/v1/Chassis/1/MezzFrus/' + str(mezz_slot) + "/Details")
    part_number = response.json()['IpmiProductInfo']['AssemblyPartNumber']
    return part_number


def get_fru_inst(mezz_part_number, mezz_slot):
    fru_inst_fru40 = "Fru40.inst"
    fru_inst_fru41 = "Fru41.inst"
    fru_inst_fru42 = "Fru42.inst"
    fru_inst_fru43 = "Fru43.inst"
    fru_inst_fru44 = "Fru44.inst"
    fru_inst_fru45 = "Fru45.inst"
    fru_inst_fru46 = "Fru46.inst"
    fru_inst_fru49 = "Fru49.inst"
    fru_inst_fru4A = "Fru4A.inst"
    fru_inst_fru4B = "Fru4B.inst"
    fru_inst_fru4C = "Fru4C.inst"
    fru_inst_fru4E = "Fru4E.inst"
    fru_inst_fru4F = "Fru4F.inst"
    fru_inst_fru40_4K = "Fru40.inst"
    fru_inst_fru41_4K = "Fru41.inst"
    fru_inst_fru42_4K = "Fru42_4K.inst"
    fru_inst_fru43_4K = "Fru43_4K.inst"
    fru_inst_fru44_4K = "Fru44_4K.inst"
    fru_inst_fru45_4K = "Fru45_4K.inst"
    fru_inst_fru46_4K = "Fru46_4K.inst"
    fru_inst_fru49_4K = "Fru49_4K.inst"
    fru_inst_fru4A_4K = "Fru4A_4K.inst"
    fru_inst_fru4B_4K = "Fru4B_4K.inst"
    fru_inst_fru4C_4K = "Fru4C_4K.inst"
    fru_inst_fru4E_4K = "Fru4E_4K.inst"
    fru_inst_fru4F_4K = "Fru4F_4K.inst"
    i2c_15_A2_4K = "i2c_15_A2_4K.inst"
    i2c_15_AA_4K = "i2c_15_AA_4K.inst"
    i2c_16_AA_4K = "i2c_16_AA_4K.inst"
    i2c_73_A0_4K = "i2c_73_A0_4K.inst"
    i2c_74_A0_4K = "i2c_74_A0_4K.inst"
    i2c_74_A0_16K = "i2c_74_A0_16K.inst"
    i2c_74_A8_4K = "i2c_74_A8_4K.inst"
    i2c_75_A0_4K = "i2c_75_A0_4K.inst"
    i2c_75_A0_16K = "i2c_75_A0_16K.inst"
    i2c_75_A8_4K = "i2c_75_A8_4K.inst"
    i2c_77_A4_4K = "i2c_77_A4_4K.inst"
    i2c_78_A4_4K = "i2c_78_A4_4K.inst"
    i2c_79_A4_4K = "i2c_79_A4_4K.inst"
    i2c_80_A4_4K = "i2c_80_A4_4K.inst"
    i2c_81_A4_4K = "i2c_81_A4_4K.inst"
    i2c_82_A4_4K = "i2c_82_A4_4K.inst"
    if float(mezz_slot) == 1.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru4E_4K
        else:
            fru_inst = fru_inst_fru4E
    if float(mezz_slot) == 2.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru4C_4K
        else:
            fru_inst = fru_inst_fru4C
    if float(mezz_slot) == 3.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru4A_4K
        else:
            fru_inst = fru_inst_fru4A
    if float(mezz_slot) == 4.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru42_4K
        else:
            fru_inst = fru_inst_fru42
    if float(mezz_slot) == 5.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru43_4K
        else:
            fru_inst = fru_inst_fru43
    if float(mezz_slot) == 6.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru44_4K
        else:
            fru_inst = fru_inst_fru44
    if float(mezz_slot) == 7.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru45_4K
        else:
            fru_inst = fru_inst_fru45
    if float(mezz_slot) == 8.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru46_4K
        else:
            fru_inst = fru_inst_fru44
    if float(mezz_slot) == 9.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru49_4K
        else:
            fru_inst = fru_inst_fru49
    if float(mezz_slot) == 10.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru4B_4K
        else:
            fru_inst = fru_inst_fru4B
    if float(mezz_slot) == 12.0:
        if mezz_part_number == "759559-001":
            fru_inst = fru_inst_fru4F_4K
        else:
            fru_inst = fru_inst_fru4F
    return fru_inst


def get_mezz_bin(mezz_type):
    for file in os.listdir(BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + "/fru_bins"):
        if file.endswith(".bin"):
            if file.startswith("golden"):
                if mezz_type.lower() in file.lower():
                    fname = os.getcwd()
                    shutil.copy(BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + "/fru_bins/" + file, BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + "/golden.bin")
                    return file


def get_iLOFirmware_version(ilo_client):
        uri = '/redfish/v1/Managers/1/'
        response = ilo_client.get(uri)
        response = response.json()
        return response["Oem"]["Hp"]["Firmware"]["Current"]["VersionString"]


def update_blade_canmic_gen10fru(ilo_ipv4, bin_path):
    bin_2_i2c_path = BuiltIn().get_variable_value("${GIT_REPO_ROOT}") + BuiltIn().get_variable_value("${FRU_UPDATE_ROOT}") + "/bin_2_i2c.py"
    python_34_path = BuiltIn().get_variable_value("${Python_34_Path}")
    bin_2_i2c_cmd = python_34_path + " " + bin_2_i2c_path + " -f " + bin_path + " -s 0x02 -a 0xae -o 0x1000" + " -i " + ilo_ipv4
    stdout = os.system(bin_2_i2c_cmd)
    return stdout


def clear_ilo_iel_logs(ilo_client, ilo_ipv4):
    uri = '/redfish/v1/Managers/1/LogServices/IEL/'
    payload = {'Action': 'ClearLog'}
    response = ilo_client.post(uri, payload)
    return response.status_code


def get_iel_entry_messages(ilo_client, ilo_ipv4):
    uri = '/redfish/v1/Managers/1/LogServices/IEL/Entries'
    response = ilo_client.get(uri)
    res = response.json()
    entries_href = res["links"]["Member"]
    list_iel_entry_msg = []
    for entries in entries_href:
        entries_link = ilo_client.get(entries["href"])
        ilo_entries_data = entries_link.json()
        ilo_entries_message = ilo_entries_data["Message"]
        list_iel_entry_msg.append(ilo_entries_message)
    return list_iel_entry_msg

