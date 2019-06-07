*** Settings ***
Documentation    Traffic tests using IOMeter and MeatGrinder Tool
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown
Library                         tools\\Data_Network_Traffic_Performance\\PerformanceTest.py

*** Test Cases ***
Traffic Tests using IOMeter tool
   [Tags]    IOMeter  T-BIRD  C7000
   [Documentation]     Traffic Test
   ...   ${jvm_ip}:  Your execution vm ip where iometer runs
   ...   ${io_meter_timeout}:  Maximum time IOMeter to run
   ...   ${iometer_server_profile}: Server details which runs dynamo
   ...   iometer_server_profile = {
   ...      "server_details": [{
   ...      "IOmeter_Target_profile_name": "fc_case30_bay04_sles12",
   ...       "target_disk": ["sdg"],
   ...       "IOmeter_Target_username": "root",
   ...       "IOmeter_Target_password": "Cosmos123",
   ...       "os_type": "sles"}]}
   ${target_ip}=  Get Target IP from server
   data_traffic_test_iometer  ${jvm_ip}  ${io_meter_timeout}  ${iometer_server_profile}  ${target_ip}

Network And Memory Stress Using MeatGrinder
    [Tags]    MeatGrinderStress  T-BIRD  C7000
    [Documentation]    Network And Memory Stress Using MeatGrinder
    ...    windows_servers = [{"hostname": "fc_nat_case01_win2016", "targetname": "fcoe_case1_bay2_win2016"},
    ...                       {"hostname": "fc_case16_bay04_win2k16", "targetname": "iscsi_case46_win2016"}]
    Network And Memory Stress Using MeatGrinder    ${windows_servers}