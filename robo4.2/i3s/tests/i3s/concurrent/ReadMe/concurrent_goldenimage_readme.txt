++++++++++++++++++++++++++++++++ Golden Image ++++++++++++++++++++++++++++++++


Create multiple goldenimages with same name from multiple processes:
run_pybot_pabot.py "pabot --processes 4 goldenimage/gi_create_same_name_conc" "pybot gi_cleanup/gi_delete_1.txt"


Create a goldenimage, parallely try to delete the same from the second process:
run_pybot_pabot.py "pabot --processes 3 goldenimage/gi_create_del_conc" "pybot goldenimage/gi_cleanup/gi_delete_1.txt"


Create a goldenimage, parallely try to edit the same from the second, third and fourth process(for diff fields):
run_pybot_pabot.py "pabot --processes 4 goldenimage/gi_create_update_diff_fields_conc" "pybot goldenimage/gi_cleanup/gi_delete_2.txt"


Create a goldenimage, parallely try to edit the same from the second, third and fourth process(for same fields):
run_pybot_pabot.py "pabot --processes 4 goldenimage/gi_create_update_same_fields_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Create a goldenimage successfully. Then try to edit the same from 2 parallel processes(different fields):
run_pybot_pabot.py "pybot goldenimage/gi_create_only/gi_create.txt" "pabot --processes 2 goldenimage/gi_only_update_diff_fields_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Create a goldenimage successfully. Then try to edit the same from 2-3 parallel processes(same fields):
run_pybot_pabot.py "pybot goldenimage/gi_create_only/gi_create.txt" "pabot --processes 2 goldenimage/gi_only_update_same_fields_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Create a goldenimage successfully. Then try to delete from one process and edit from the second process:
run_pybot_pabot.py "pybot goldenimage/gi_create_only/gi_create.txt" "pabot --processes 2 goldenimage/gi_del_update_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Create goldenimage from one process, delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pabot --processes 3 goldenimage/gi_create_del_create_conc" "pybot goldenimage/gi_cleanup/gi_delete_1.txt"


Create goldenimage from one process successfully. Then delete the same from second process and create with same name from third process:
run_pybot_pabot.py "pybot goldenimage/gi_create_only/gi_create.txt" "pabot --processes 2 goldenimage/gi_del_create_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Add 4 goldenimages with different names and try deleting goldenimage 3 and 4 parallely:
run_pybot_pabot.py "pabot --processes 6 goldenimage/gi_create_diff_name_del_conc" "pabot --processes 4  goldenimage/gi_cleanup"


All CRUD operations concurrently:
run_pybot_pabot.py "pabot --processes 4 goldenimage/gi_create_del_update_get_conc" "pybot goldenimage/gi_cleanup/gi_delete_3.txt"


Concurrently create 4 GI with diff name:
run_pybot_pabot.py "pabot --processes 4 goldenimage/gi_create_diff_name_conc" "pabot --processes 4 goldenimage/gi_cleanup"