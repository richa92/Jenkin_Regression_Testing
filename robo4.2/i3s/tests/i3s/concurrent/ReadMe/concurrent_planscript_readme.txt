++++++++++++++++++++++++++++++++ PlanScript ++++++++++++++++++++++++++++++++


Create multiple planscripts with same name from multiple processes:
run_pybot_pabot.py "pabot --processes 4 planscript/ps_create_same_name_conc" "pybot planscript/ps_cleanup/ps_delete_1.txt"


Create a planscript, parallely try to delete the same from the second process:
run_pybot_pabot.py "pabot --processes 3 planscript/ps_create_del_conc" "pybot planscript/ps_cleanup/ps_delete_1.txt"


Create a planscript, parallely try to edit the same from the second, third and fourth process(for diff fields):	
run_pybot_pabot.py "pabot --processes 4  planscript/ps_create_update_diff_fields_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Create a planscript, parallely try to edit the same from the second, third and fourth process(for same fields):
run_pybot_pabot.py "pabot --processes 4  planscript/ps_create_update_same_fields_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Create a planscript successfully. Then try to edit the same from 2-3 parallel processes(different fields):
run_pybot_pabot.py "pybot planscript/ps_create_only/ps_create.txt" "pabot --processes 3 planscript/ps_only_update_diff_fields_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Create a planscript successfully. Then try to edit the same from 2-3 parallel processes(same fields):
run_pybot_pabot.py "pybot planscript/ps_create_only/ps_create.txt" "pabot --processes 3 planscript/ps_only_update_same_fields_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Create a planscript successfully. Then try to delete from one process and edit from the second process:
run_pybot_pabot.py "pybot planscript/ps_create_only/ps_create.txt" "pabot --processes 4 planscript/ps_del_update_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Create planscript from one process, delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pabot --processes 3 planscript/ps_create_del_create_conc" "pybot planscript/ps_cleanup/ps_delete_1.txt"


Create planscript from one process successfully. Then delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pybot planscript/ps_create_only/ps_create.txt" "pabot --processes 2 planscript/ps_del_create_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Add 5 planscripts and try deleting ps 3 and 4 parallely:
run_pybot_pabot.py "pabot --processes 7 planscript/ps_create_diff_name_del_conc" "pabot --processes 4 planscript/ps_cleanup"


All CRUD operations concurrently:
run_pybot_pabot.py "pabot --processes 6 planscript/planscript_crud_conc" "pybot planscript/ps_cleanup/ps_delete_2.txt"


Concurrently create 4 ps with diff name:
run_pybot_pabot.py "pabot --processes 4 planscript/ps_create_diff_name_conc" "pabot --processes 4 planscript/ps_cleanup"