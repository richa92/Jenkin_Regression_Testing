""" resources/configFile.py
	This is the configuration file that contains the variables to be used in 
	the file api_create_fusion_elements.txt. Please read the instruction mentioned below before editing the file.
	= Usage =
	variables  |  resources/configFile.py
"""

'''
INSTRUCTIONS:
1. ETHERNET NETWORKs: To set DEFAULT value for speed of Ethernet Network please set the speed as 0(ZERO).
''' 

variables = {                     
#Networks
    #ethernet networks:
        #name 		 			#vlanid
        "Eth_Network1_Name":"EthNetwork1",      "Eth_Network1_VLAN":"1-3",      "Preffered_Speed_1":200, "Maximum_Speed_1":1000, 
        "Eth_Network2_Name":"EthNetwork12",      "Eth_Network2_VLAN":"1",      "Preffered_Speed_2":0, "Maximum_Speed_2":0, 
    #fcoe networks:
        #name 		 			#vlanid
        "FCoe_Network1_Name":"FCoeNetwork1",    "FCoe_Network1_VLAN":"201",      
        "FCoe_Network2_Name":"FCoeNetwork2",    "FCoe_Network2_VLAN":"204",      
    #uplink sets to LIG
 	#name					#network type
        					#"uplink_network_type":"ethernet",
						#"uplink_network_type":"fiber Channel",
						#"uplink_network_type":"Tunnel",
						#"uplink_network_type":"Untagged",

#Interconnect 
    #Logical interconnect

    #Logical interconnect group  			#enclosure_count 	#Interconnect bay set	#Redundancy
    "LIG Name":"LIG1",
  
#Enclosure
    #Enclosure Group
	#name				#bay....LIG name			
<<<<<<< Updated upstream
    "EG Name":"EG1",    "ipAddressingMode":"DHCP", "Total_Enc_count":"1",      
    "LE_name":"GB",          
    #"3" = "LIG1",
		#"6" = "LIG1",
=======
    "EG Name":"EG1",                    #3 = LIG1
					#6 = LIG1
>>>>>>> Stashed changes

    #Logical Enclosure 
	#name
    #"LE Name":"LE1",

#Server
    #Server Profile


    #dummy last var for no comma
	"dummy_las_var":"dummy_last_var"
}

def get_variables():
    return variables
