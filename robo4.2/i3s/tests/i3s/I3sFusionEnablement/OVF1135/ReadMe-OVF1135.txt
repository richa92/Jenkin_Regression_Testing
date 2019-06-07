Execution Procedure:

1. Make changes in the environment_data.py file for networks, egs and servers based on the appliance used

2. Change the input for fusionIP in the i3s_QA_testdata.py under the testdata folder

3. For the execution of OVF1135 Test Suite, we will require the OO_prerequisites scripts to be run for the plan scripts, build plans and deployment plans
01_1nicTestSuite.robot contains test cases related to 1 NIC attribute
02_2nicTestSuite.robot contains test cases related to 2 NIC attribute
03_3nicTestSuite.robot contains test cases related to 3 NIC attribute
04_DHCPTestSuite.robot contains test cases related to DHCP connections

4. Generic json's are used as input so that same json's can be used across the test cases
The "osDeploymentPlanUri" attribute is SET to the required deployment plan which contains similar Custom Atrributes but with different inputs for different test cases

For Example: In ovf1135_me_data.py:

sp_tc02 contains Custom Attributes for User-specified option with deployment plan SET to dpWith1Nic_StaticNic
sp_tc03 contains Custom Attributes for Auto option with deployment plan SET to the same dpWith1Nic_StaticNic

Though the test cases makes a deepcopy of the json's with different names, the Deployment Plan remains the same with different input to Custom Attributes

5. Minimum of 3 servers are required to execute the script. Two servers of the same SHT and one with a different SHT

6. net_146 will have only one DNS value for test case OVF1135_TC120
7. net_147 will have no DNS values for test case OVF1135_TC119
8. check the IP address for test case OVF1135_TC63