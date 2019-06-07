ExpectedErrorMsg1="No update required"
ExpectedErrorMsg2="Selected firmware is already installed in the logical interconnect"
ExpectedErrorMsg3="Selected firmware is already installed"
ExpectedErrorMsg4="Unable to update firmware on the logical interconnect"
ExpectedErrorMsg5="Downgrading firmware without selecting the Force Installation option is not supported."
ExpectedErrorMsg5_1="Retry update firmware operation with 'Force Installation' option selected"
ExpectedErrorMsg6="Firmware activation failed for logical interconnect"
ExpectedErrorMsg7="Activation failed due to failure of firmware update operation on interconnect"
ExpectedErrorMsg8="If the interconnects are in configured, unmanaged, maintenance or configuration error state, try the firmware activation again"
ExpectedErrorMsg9="If the interconnect is in any other state, refresh the enclosure and then retry the firmware update"
ExpectedErrorMsg10="If the problem continues to occur, contact your authorized support representative and provide them with a support dump"
ExpectedErrorMsg11="One or more interconnects are not in a valid state for firmware update"
ExpectedErrorMsg11_1="Visit the listed interconnects and examine the Activity view and follow the problem resolution steps listed there in order to bring the interconnects back to a Configured state or an Unmanaged state"
ExpectedErrorMsg11_2="AddedWithErrors state"
ExpectedErrorMsg12="There is an ongoing operation on the resource"
ExpectedErrorMsg13="One or more interconnects are not in a valid state for firmware update"
ExpectedErrorMsg14="Configuring state"

ExpectedErrorMsg15="Unable to update firmware without disruption."
ExpectedErrorMsg16="Updating firmware will result in a temporary service outage"
ExpectedErrorMsg17="Logical interconnect"
ExpectedErrorMsg18="is not redundantly configured."
ExpectedErrorMsg19="Updating firmware may disrupt network and storage connectivity for all server profiles"
ExpectedErrorMsg20="If a service outage is acceptable, click OK. Alternatively, to avoid service outages edit the logical interconnects and add redundant connections or leave firmware unchanged by clicking cancel"

ExpectedErrorMsg22="The following servers:"
ExpectedErrorMsg23="are currently powered on. Firmware update cannot be initiated until the listed servers within the logical enclosure are powered off"
ExpectedErrorMsg24="Power off the listed servers and retry the operation"

ExpectedErrorMsg25="The servers with following profiles:"
ExpectedErrorMsg26="are currently powered on but the associated servers profiles are not configured to use HPE Smart Update Tool"
ExpectedErrorMsg27="Edit the affected server profiles and select a firmware update option that uses HPE Smart Update Tool. Alternatively, power off these servers"
Permissible_IC_STATES_BeforeUpdate=['configured','unmanaged','monitored']
Permissible_IC_STATES_AfterUpdate=['configured']

######### LI variables ################

expectedmsg1="No update required. Selected firmware is already installed in the logical interconnect"
expectedmsg2="There are no interconnect modules available for activation."
expectedmsg3="Unable to update firmware on the logical interconnect. Downgrading firmware without selecting the Force Installation option is not supported."
ExpectedErrorMsg21="Edit the logical interconnect to be redundantly configured. Selecting continue will result in connectivity disruption"

############# user ####################

ExpectedErrorMsg1user="User may not have Update Firmware privilege"
ExpectedErrorMsg2user="'failed to wait for element '//div[@id='cic-logicalswitch-actions']//a[text()='update firmware']''"
