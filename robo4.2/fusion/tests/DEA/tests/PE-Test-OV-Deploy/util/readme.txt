How to configure and run Automated OneView Deployment job (Tbird).
Configuring Jenkins job
1.	Login to Jenkins and click create “New Item” on the left of the screen and select Copy existing item and select PE-Test-OV-Deploy. (16.84.100.202:8080 , PE-Test Tab)
 

2.	You will need to make changes to the configuration of the job, select that newly created job and click configure.
Configure Default value to the name of your enclosure.
 
Update the VM name where you are running your script:
Modify the Build_Name if you would like to change the log output folder. (Optional)
 

3.	After you configured your deployment job, make that a part of the job that you run tests on. This job can be inserted anywhere before your testing starts.
 
Now you are done with Jenkins configuration.


Configuring test VM.

1.	Go to the RoboGalaxy repo on your VM and make sure that you see this folder under DEA folder.
Repo\fusion\tests\DEA\tests\PE-Test-OV-Deploy

2.	Make sure that you see 3 files under util folder.

•	Deploy_dd_image_on_active_CIM.txt
o	If you have one or more CIM but only want to update the active one.
 
•	Deploy_dd_image_on_standby_CIM.txt
o	If you have one or more CIM but only want to update the standby one.

•	Deploy_dd_image_two_node_ha.txt 
o	If you have one or more CIM but only want to update all – preferred method.

Deploy_dd_image_two_node_ha.txt for 2 CIM and 1 CIM configuration.
 
If you use either the active or the standby files, modify the file name in the window batch window in the Jenkins job.

3.	You will need to configure resources\variables.py file with the enclosure information that you are going to run the tests on. You can simply edit existing enclosure in this file with the information highlighted here in yellow.
   Now you are done with VM configuration.


 Configuring CIM USB drive.   
1.	Go to this link to create USB drives for your CIMs configuration in order to perform first time setup after OV is installed. You will need to create one USB drive per CIM and keep them in the enclosure at all times. 
https://crauth.us.rdlabs.hpecorp.net/cim-usb-key/
Follow the prompts on the screen. When this process completes, you will be offered to save the file on the USB drive. 
Once they are saved on the USB, rename them to the following names:
CIM1-cic-manager-setup-config-310.json
CIM2-cic-manager-setup-config-310.json
This is one time process, and does not need to be performed again, unless you would like to reconfigure your CIMs with new IP and other network configuration.

Now you are done with USB configuration.



