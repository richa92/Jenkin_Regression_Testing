++++++++++++++++++++++++++++++++ DeploymentPlan ++++++++++++++++++++++++++++++++


Create multiple deploymentplans with same name from multiple processes:
run_pybot_pabot.py "pybot oedeploymentplan/oedp_initial_setup_creation/oedp_initial_setup.txt" "pabot --processes 4 oedeploymentplan/oedp_create_same_name_conc" "pybot oedeploymentplan/oedp_delete_only/oedp_delete.txt" "pybot oedeploymentplan/oedp_initial_setup_deletion/oedp_initial_setup_deletion.txt


Create a deploymentplan, parallely try to delete the same from the second process:
run_pybot_pabot.py "pabot --processes 2 oedp_create_del_conc"


Create a deploymentplan, parallely try to edit the same from the second, third and fourth process(for diff fields):
run_pybot_pabot.py "pabot --processes 4 oedp_create_update_diff_fields_conc"


Create a deploymentplan, parallely try to edit the same from the second, third and fourth process(for same fields):
run_pybot_pabot.py "pabot --processes 4 oedp_create_update_same_fields_conc"


Create a deploymentplan successfully. Then try to edit the same from 2-3 parallel processes(different fields):
run_pybot_pabot.py "pybot oedp_create_only/oedp_create.txt" "pabot --processes 3 oedp_only_update_diff_fields_conc"


Create a deploymentplan successfully. Then try to edit the same from 2-3 parallel processes(same fields):
run_pybot_pabot.py "pybot oedp_create_only/oedp_create.txt" "pabot --processes 3 oedp_only_update_same_fields_conc"


Create a deploymentplan successfully. Then try to delete from one process and edit from the second process:
run_pybot_pabot.py   "pybot oedp_create_only/oedp_create.txt" "pabot --processes 2 oedp_del_update_conc"


Create deploymentplan from one process, delete the same from second process and create with same name from third process:
run_pybot_pabot.py   "pabot --processes 3 oedp_del_update_conc"


Create deploymentplan from one process successfully. Then delete the same from second process and create with same name from third process:
run_pybot_pabot.py   "pybot oedp_create_only/oedp_create.txt" "pabot --processes 2 oedp_del_create_conc"


Add 5 deploymentplans and try deleting deploymentplan 3 and 4 parallely:
run_pybot_pabot.py    "pabot --processes 7 oedp_create_diff_name_del_conc"


Create deploymentplan  successfully, delete goldenimage from second process and and oebp from third process parallely and try updating gi/oebp to oedp:
run_pybot_pabot.py   "pybot oedp_create_only/oedp_create.txt" "pabot --processes 4 oedp_del_gi_oebp_update_oedp_conc"


Create deploymentplan successfully. From one process try to delete buildplan and from second process try to update the same to deploymentplan (as part of oedp edit). Try same with goldenimage:
run_pybot_pabot.py   "pybot oedp_create_only/oedp_create.txt" "pabot --processes 2 oedp_del_oebp_update_oedp_conc"


All crud opreations:
run_pybot_pabot.py    "pabot --processes 4 oedp_create_del_update_get_conc"


Create oedp in one process, delete gi and oebp in other process paralley:
run_pybot_pabot.py    "pabot --processes 3  oedp_create_and_gi_oebp_delete_conc"
