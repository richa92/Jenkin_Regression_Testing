print "Developed By HP India"

#IP = r'16.125.75.128'
IP = r'16.95.218.206'
BROWSER = r'firefox'
admin_credentials = {'userName': 'Administrator', 'password': 'hpinvent'}
#admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}




loggerlevel = r'INFO'   # use INFO|DEBUG



# below are the variable for Natasha_F175
enclosure_uri = r'/rest/enclosures'
sas_interconnect_uri = r'/rest/sas-interconnects'
drive_enclosure_uri = r'/rest/drive-enclosures'
sas_interconnect_state = r'Monitored'
drive_enclosure_state = r'Monitored'
enclosure_state = r'Monitored'
natasha_model = r'Synergy 12Gb SAS Connection Module'
big_Bird_model = r'Synergy D3940 Storage Module'
power_state = r'On'
task_create_status = r'Added SAS logical Interconnect group.'
task_delete_status = r'Deleted sas-logical-interconnect-groups successfully'
task_state = r'Completed'
lig_state = r'Active'
permittedInterconnectTypeUri = '/rest/sas-interconnect-types/Synergy12GbSASConnectionModule'
# end


# below variables are for F176.txt
LIG_Names = ['RGLIG1','RGLIG4','RGLIG14']
bay_list = [[1],[4],[1,4]]
baylistno = []

UI_LIG_name = 'LIGbay1updated'
UI_USERNAME = r'Administrator'
UI_PASSWORD = r'hpinvent'

logicalEnclosureUri = r'/rest/logical-enclosures'

#variables for serverprofile creation
serverProfileUri = r'/rest/server-profiles/'

#variables for sas-logical-jbod
LJbodminSizeGB=1999
LJbodmaxSizeGB=11446411
sasLogicalJbodType = r'sas-logical-jbod'
sasLogicalInterconnectUri = r'/rest/sas-logical-interconnects/'
sasLogicalJbodUri = r'/rest/sas-logical-jbods'
sasLogicalJbodAttachmentType=r'sas-logical-jbod-attachment'
sasLJbod_task_create_status="SAS logical JBOD created successfully."
sasLJbod_task_delete_status="Removed SAS logical JBOD successfully."


# end
