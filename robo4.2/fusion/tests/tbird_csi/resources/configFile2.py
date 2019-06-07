""" resources/configFile.py
    This is the configuration file that contains the variables to be used in 
    the file api_create_fusion_elements.txt. Please read the instruction mentioned below before editing the file.
    = Usage =
    variables  |  resources/configFile.py
"""
import xlrd
#from pprint import pprint

def null_value(variables):
    if variables == "None" or variables == "" or variables == None:
        variables = "0"
    return variables
    


variables= {}
file_location = "/home/cometuser/git/fusion/tests/tbird_csi/resources/Configuration_file.xlsx" ##importing the excel containing the variables
workbook = xlrd.open_workbook(file_location)
###########################################SAN manager##################################################
SAN_manager = workbook.sheet_by_index(1)
SAN_total = 1
for SAN in range(3,SAN_manager.nrows+1):
        temp = SAN - 1
        if (SAN_manager.cell_value(temp,0)) == "":
                continue
        index=str(SAN-2)
        if ((int(SAN_manager.cell_value(temp,0)==5900.0))):
                variables["SAN_type_"+index] = str(int(SAN_manager.cell_value(temp,0)))
        else :
                variables["SAN_type_"+index] = SAN_manager.cell_value(temp,0)
        variables["SAN_IP_"+index] = SAN_manager.cell_value(temp,1)
        variables["SAN_Username_"+index] = SAN_manager.cell_value(temp,2)
        variables["SAN_password_"+index] = null_value(SAN_manager.cell_value(temp,3))
        variables["Auth_Protocol_"+index] = SAN_manager.cell_value(temp,4)
        variables["Auth_password_"+index] = null_value(SAN_manager.cell_value(temp,5))
        variables["Privacy_Protocol_"+index] = SAN_manager.cell_value(temp,6)
        variables["Privacy_password_"+index] = null_value(SAN_manager.cell_value(temp,7))
        SAN_total += 1
   
variables["total_sanmanager"] = SAN_total      #Passing Value "ACTUAL VALUE" + 1


##########################################Storage######################################################

#######################################Ethernet Network################################################
Ethernet_Network = workbook.sheet_by_index(3)
Eth_total = 1
for Eth in range(3, Ethernet_Network.nrows+1):
        temp = Eth -1
        if (Ethernet_Network.cell_value(temp,0)) == "":
                continue
        index = str(Eth-2)
        variables["Eth_Network_Name_"+index] = Ethernet_Network.cell_value(temp,0)
        if type(Ethernet_Network.cell_value(temp,1))== float: 
                variables["Eth_Network_VLAN_"+index] = str(int(Ethernet_Network.cell_value(temp,1)))
        else:
                variables["Eth_Network_VLAN_"+index] = str(Ethernet_Network.cell_value(temp,1))
        variables["Preffered_Speed_"+index] = int(null_value(Ethernet_Network.cell_value(temp,2)))
        variables["Maximum_Speed_"+index] = int(null_value(Ethernet_Network.cell_value(temp,3)))
        Eth_total += 1

variables["total_ethernetnetwork"] = Eth_total     #Passing Value "ACTUAL VALUE" + 1



#######################################FCoE Network####################################################
FCoE_Network = workbook.sheet_by_index(4)
FCoE_total = 1
for FCoE in range(3, FCoE_Network.nrows+1):
        temp = FCoE -1
        if (FCoE_Network.cell_value(temp,0)) == "":
                continue
        index = str(FCoE-2)
        variables["FCoe_Network_Name_"+index] = FCoE_Network.cell_value(temp,0)
        variables["FCoe_Network_VLAN_"+index] = int(FCoE_Network.cell_value(temp, 1))
        FCoE_total += 1
variables["total_fcoenetwork"] = FCoE_total  #Passing Value "ACTUAL VALUE" + 1

######################################EG&LE##############################################################

EG_LE_data = workbook.sheet_by_index(6)
variables["EG Name"] = EG_LE_data.cell_value(2,0)
variables["ipAddressingMode"] = EG_LE_data.cell_value(2,1)
variables["Total_Enc_count"] = int(EG_LE_data.cell_value(2,2))
variables["LE_name"] = EG_LE_data.cell_value(2,3)

#####################################LE###############################################################
#variables["LE_name"] = "LE1"
variables["dummy_las_var"] = "dummy_last_var"
###################################SP#################################################################

SP_data = workbook.sheet_by_index(7)
SP_total = 1
temp = 2
idx = 0
for SP in range(2, SP_data.nrows):
        if (SP_data.cell_value(temp,0)) == "":
                variables["Network_Name_"+index].append(SP_data.cell_value(temp, 6))
                variables["Port_id_"+index].append(SP_data.cell_value(temp, 7))
                variables["Network_requested_speed_"+index].append(int(null_value(SP_data.cell_value(temp, 8))))
                variables["SP_connection_name_"+index].append(SP_data.cell_value(temp, 5))
                temp += 1 
                 
        else:
                idx += 1
                index = str(idx)
                variables["Network_Name_"+index] = [SP_data.cell_value(temp, 6)]
                variables["Port_id_"+index] = [SP_data.cell_value(temp, 7)]
                variables["Network_requested_speed_"+index] = [int(null_value(SP_data.cell_value(temp, 8)))]
                variables["SP_connection_name_"+index] = [SP_data.cell_value(temp, 5)]
                variables["HideUnusedFlexNics_"+index] = SP_data.cell_value(temp, 4)
                variables["SP_affinity_"+index] = SP_data.cell_value(temp, 3)
                variables["Boot_Mode_"+index] = SP_data.cell_value(temp, 2)
                variables["Bay_No_"+index] = int(SP_data.cell_value(temp, 1))
                variables["SP_Name_"+index] = SP_data.cell_value(temp, 0)
                temp += 1
                SP_total += 1

variables["total_server_profile"] =  SP_total               

#################################LIG##################################################################

def  uplink_to_LIG(LIG_data,LIG,temp):
          variables["Uplink_name_"+str(temp)] = []
          variables["ICM_Bay_"+str(temp)] = []
          variables["ICM_PORT_"+str(temp)]=[]
          variables["Uplink_network_name_"+str(temp)] = []
          counter_bay = []
          counter_port = []
          counter_network = []
          for index in range(7, LIG_data.nrows+1):
                rw = index -1
                if (LIG_data.cell_value(rw,LIG+3)) == "":
                        continue
                        
                elif (LIG_data.cell_value(rw,LIG)) != "":
                        variables["Uplink_name_"+str(temp)].append(LIG_data.cell_value(rw,LIG))
                        if len(counter_network) == 0:
                                pass
                        else:
                                variables["ICM_Bay_"+str(temp)].append(counter_bay)
                                variables["ICM_PORT_"+str(temp)].append(counter_port)
                                variables["Uplink_network_name_"+str(temp)].append(counter_network)
                                counter_bay = []
                                counter_port = []
                                counter_network = []
                        if type(LIG_data.cell_value(rw,LIG+1)) == float:
                                counter_bay.append(str(int(LIG_data.cell_value(rw,LIG+1))))
                        else:
                                counter_bay.append((LIG_data.cell_value(rw,LIG+1)))
                        counter_port.append(LIG_data.cell_value(rw,LIG+2))
                        counter_network.append(LIG_data.cell_value(rw,LIG+3))
                else:
                        if type(LIG_data.cell_value(rw,LIG+1)) == float:
                                counter_bay.append(str(int(LIG_data.cell_value(rw,LIG+1))))
                        else:
                                counter_bay.append((LIG_data.cell_value(rw,LIG+1)))
                        counter_port.append(LIG_data.cell_value(rw,LIG+2))
                        counter_network.append(LIG_data.cell_value(rw,LIG+3))
                
          variables["ICM_Bay_"+str(temp)].append(counter_bay)
          variables["ICM_PORT_"+str(temp)].append(counter_port)
          variables["Uplink_network_name_"+str(temp)].append(counter_network)
                
          
LIG_data = workbook.sheet_by_index(5)
LIG_total = 1
LIG = -3
temp = 0
for index in range(1,4):
        temp += 1
        LIG += 4
        if LIG_data.cell_value(2, LIG) == "":
                temp -= 1
                continue
        else:
                variables["LIG_Name_" + str(temp)] = LIG_data.cell_value(2,LIG)
                if LIG_data.cell_value(3,LIG) == "ICM1_4":
                        variables["ICM_BAY_SET_" + str(temp)] = "1"
                elif LIG_data.cell_value(3,LIG) == "ICM2_5":
                        variables["ICM_BAY_SET_" + str(temp)] = "2"
                elif LIG_data.cell_value(3,LIG) == "ICM3_6":
                        variables["ICM_BAY_SET_" + str(temp)] = "3"
                variables["REDUNDANCY_TYPE_" + str(temp)] = LIG_data.cell_value(4,LIG)
                
                uplink_to_LIG(LIG_data,LIG,temp)
variables["total_LIG"] = temp+1 
########################################################################################################################
def get_variables():
#    pprint(variables)
    return variables    
    
get_variables()





    
