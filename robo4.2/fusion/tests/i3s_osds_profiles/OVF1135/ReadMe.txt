ReadMe:

For the execution of OVF1135 Test Suites, we will require the OO_prerequisites scripts to be run for the plan scripts, build plans and deployment plans.
01_1nicTestSuite.robot contains test cases related to 1 NIC attribute.

Generic json's are used as input so that same json's can be used across the test cases.
The "osDeploymentPlanUri" attribute is SET to the required deployment plan which contains similar Custom Atrributes but with different inputs for different test cases.

For Example:

In ovf1135_me_data.py:

sp_tc02 contains Custom Attributes for User-specified option with deployment plan SET to dpWith1Nic_StaticNic
sp_tc03 contains Custom Attributes for Auto option with deployment plan SET to the same dpWith1Nic_StaticNic

Though the test cases makes a deepcopy of the json's with different names, the Deployment Plan remains the same with different input to Custom Attributes.