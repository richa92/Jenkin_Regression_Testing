++++++++++++++++++++++++++++++++ BuildPlan ++++++++++++++++++++++++++++++++


Create multiple buildplans with same name from multiple processes:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_create_same_name_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create  buildplan, parallely try to delete the same from the second process:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 2 oebuildplan/oebp_create_del_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create a buildplan, parallely try to edit the same from the second, third and fourth process(for diff fields):
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_create_update_diff_fields_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create a buildplan, parallely try to edit the same from the second, third and fourth process(for same fields):
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_create_update_same_fields_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create a buildplan successfully. Then try to edit the same from 2-3 parallel processes(different fields):
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pybot oebuildplan/oebp_create_only/oebp_create.txt" "pabot --processes 3 oebuildplan/oebp_only_update_diff_fields_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create a buildplan successfully. Then try to edit the same from 2-3 parallel processes(same fields):
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pybot oebuildplan/oebp_create_only/oebp_create.txt" "pabot --processes 3 oebuildplan/oebp_only_update_same_fields_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create a buildplan successfully. Then try to delete from one process and edit from the second process:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt"  "pybot oebuildplan/oebp_create_only/oebp_create.txt" "pabot --processes 2 oebuildplan/oebp_del_update_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


From one process try to delete ps and from second process try to add the same planscript to buildplan (as part of oebp create):
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_del_ps_and_create_oebp_with_ps_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_1.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create buildplan from one process, delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 3 oebuildplan/oebp_create_del_create_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create buildplan from one process successfully. Then delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pybot oebuildplan/oebp_create_only/oebp_create.txt" "pabot --processes 2 oebuildplan/oebp_del_create_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Add 5 buildplans and try deleting buildplan 3 and 4 parallely:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 7 oebuildplan/oebp_create_diff_name_del_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_2.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Create buildplan successfully. Edit from second process with planscript and from third process try to delete the planscript:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pybot oebuildplan/oebp_create_only/oebp_create.txt" "pabot --processes 2 oebuildplan/oebp_update_ps_and_del_ps_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


All CRUD operations concurrently:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_create_del_update_get_conc" "pybot oebuildplan/oebp_delete_only/oebp_delete_3.txt" "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"


Concurrently create 4 buildplan with diff name:
run_pybot_pabot.py "pybot oebuildplan/oebp_initial_setup_creation/oebp_initial_setup.txt" "pabot --processes 4 oebuildplan/oebp_create_diff_name_conc"


Concurrently delete 4 buildplan with diff name:
run_pybot_pabot.py "pabot --processes 4 oebuildplan/oebp_delete_diff_name_conc"  "pybot oebuildplan/oebp_initial_setup_deletion/oebp_initial_setup_deletion.txt"
