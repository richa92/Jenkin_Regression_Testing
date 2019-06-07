cd C:\CHECKIN_NOVEMBER\fusion\tests\icm_dvt_india\TESTS_SUITE_MAIN
mv C:\Users\Administrator\.ssh\known_hosts  C:\Users\Administrator\.ssh\known_hostsorginal
set http_proxy=
set https_proxy=
call pybot -l ./MAT_LOGS/ssh_logs.html Tests_Suite_SSH.txt
call pscp -pw iso*help root@90.1.0.201:/root/POTASH/1GB/AUTOMATION_RESULTS/* C:\CHECKIN_NOVEMBER\fusion\tests\icm_dvt_india\TESTS_SUITE_MAIN\MAT_LOGS\

call pybot -l ./MAT_LOGS/InitialTrust_logs.html -L trace -i LEGACY InitialTrust.txt
call pybot -l ./MAT_LOGS/Tests_Suite_TaggedLLDP_logs.html Tests_Suite_TaggedLLDP.txt
call pybot -l ./MAT_LOGS/fc_fcoe_logs.html Tests_Suite_fc_fcoe.txt
call pybot -l ./MAT_LOGS/fc_da_logs.html Tests_Suite_fc_da.txt
call pybot -l ./MAT_LOGS/sflow_logs.html  ../TESTS_SUITE_SFLOW/Tests_Suite_sFlow.txt
call pybot -l ./MAT_LOGS/fc_fcoe_logs.html Tests_Suite_ISSU.txt
call pybot -l ./MAT_LOGS/qos_logs.html Tests_Suite_QOS.txt

