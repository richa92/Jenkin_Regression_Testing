'''
File Name 		: rg_alm_plugin_config.py
Description 	:
	This file is act as a configuration file as well as a fab file for Python fabric module.
	This File is used to pass the ssh connection parameters to RG+ALM Plugin.
	This Fie decides, in which machine [local or remote] the Scripts should execute.
=============================================================================================================================================
Local Windows Execution :
	This file should placed inside the scripts/tests folder of the check-out repository[ie. Where the scripts resides in the local machine]
	Ex : /Demo/root/ci-fit/rg-mods/fusion/tests/wpst_crm/ci_fit/tests/ rg_alm_plugin_config.py

Remote Linux Execution  :
	This file can be placed in any folder, folder name should match with test folder name in ALM.
	Ex : C:\Demo\ rg_alm_plugin_config.py
		
=============================================================================================================================================
Parameter Explanations : 
=========================
Remote_Execution  			:	This Parameter holds the Boolean value either [True or False]
								If True is given as value, then the execution will be in remote machine.
								If False is given as value, then the execution will be in local windows/linux machine.
								If the value is True, Then set values for the below parameters.
Remote_Machine_IP 			:	It holds the IP of the Remote  Machine.
Remote_Machine_Username		:	It holds the Username of the remote machine.
Remote_Machine_Password		:	It holds the password of the remote machine.
Remote_Test_Directory_Path	:	This path refers to the scripts location in the Remote machine.

Step To be Take Care for Remote Linux Execution:
================================================
1. Make sure when login with non root user make sure the non root user have privileges to read,write and execute premissions.
=============================================================================================================================================
'''
#True Means Remote Linux Execution; False means Local Windows/Linux execution
Remote_Execution = False
Remote_Machine_IP = '15.199.236.50'
Remote_Machine_Username = 'root'
Remote_Machine_Password = 'rootpwd'
Remote_Machine_Test_Directory_Path = '/home/rbriggs/fusion/tests/wpst_crm/ci_fit/tests/'
'''
=============================================================================================================================================






+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Warning :	Below contents are not for configuration purpose. Don't Change any values or parameters  mentioned below 					+
+ =======	Below contents are used by ALM RG+ALM Plugin during the execution. Modifying below values will affect Plugin too.			+
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

# Import all the methods from fabric.api modules 
from fabric.api import *

# Enables the fab error messages as warning by setting True. True is the default option don't change this
env.warn_only = True

# Setting the fabric host 
env.hosts = Remote_Machine_IP

# Setting the username for fabric host
env.user = Remote_Machine_Username

# Setting the password  for fabric password
env.password = Remote_Machine_Password

# Setting the directory path of the scripts in remote machine
dirr=Remote_Machine_Test_Directory_Path

def execute_command(scr_name,now):
	'''
	This function contains the robogalaxy execution command, which does unique log naming and segregation of logs in logs folder.
	scr_name	- First argument is the script name.
	now 		- Second argument is the timestamp append to the log name.	
	'''
	Command= 'pybot -l ' + dirr +'logs/'+scr_name+now+'_log.html -r '+ dirr +'logs/'+scr_name+now+'_report.html -o ' + dirr +'logs/'+scr_name+now+'_output.xml  '+dirr+scr_name+'.txt'
	run(Command)

def download_logs(scr_name,now):
	'''
	This function is used to download the log files from remote linux to the local windows TCS where the ALM runs.
	scr_name	- First argument is the script name.
	now 		- Second argument is the timestamp append to the log name.	
	'''
	get(dirr+'logs/'+scr_name+now+'_log.html','logs/'+scr_name+now+'_log.html')
	get(dirr+'logs/'+scr_name+now+'_output.xml','logs/'+scr_name+now+'_output.xml')
	get(dirr+'logs/'+scr_name+now+'_report.html','logs/'+scr_name+now+'_report.html')
	
def mk_remote_execution(script_name,date_time):
	'''
	This is the main function which gets called by the Plugin script.
	scr_name	- First argument is the script name.
	now 		- Second argument is the timestamp append to the log name
	'''
	try:
		execute_command(script_name,date_time)
		download_logs(script_name,date_time)
	except Exception as e:
		print('Exception Caught : ', e)