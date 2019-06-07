import re
import os
import sys
import shutil

def generate_index(folder_path, index_file):
    print "writing %s" % os.path.join(folder_path, index_file)
    fp = open('%s.txt' % os.path.join(folder_path, index_file), 'w')
    sub_folders = [x for x in os.walk(folder_path).next()[1] if re.match('^\d+.*', x)]
    for folder in sub_folders:
        fp.write('%s\n' % folder)
        folder = os.path.join(folder_path, folder)
        files = [x for x in os.listdir(folder) if (os.path.isfile(os.path.join(folder,x)) and (x != '__init__.txt')) ]
        for filename in files:
            fp.write('    %s\n' % filename)
    fp.write('\n')
    fp.close()

def replace_space_with_underline(folder_path):
    sub_folders = [x for x in os.walk(folder_path).next()[1] if re.match('^\d+.*', x)]
    for folder in sub_folders:
        folder = os.path.join(folder_path, folder)
        print folder
        files = [x for x in os.listdir(folder) if (os.path.isfile(os.path.join(folder,x)) and (x != '__init__.txt')) ]
        for filename in files:
            if ' ' in filename:
                new_filename = filename.replace(" ", "_")
                os.rename(os.path.join(folder,filename), os.path.join(folder, new_filename))

def get_expected_files_by_index(folder_path, index_file):
    suites = {}
    existent_folders = [x for x in os.walk(folder_path).next()[1] if re.match('^\d+.*', x)]
    for existent_folder in existent_folders:
        existent_folder = os.path.join(folder_path, existent_folder)
        suites[existent_folder] = []
    with open(os.path.join(folder_path, index_file)) as fp:
        for line in fp:
            if line.strip():
                if not ((".txt" in line) or ((".1txt" in line))):
                    folder = os.path.join(folder_path, line.strip())
                    if not (folder in suites.keys()):
                        print "ERROR: FOLDER '%s' NOT EXIST." % folder
                        return None
                else:
                    filename = line.strip()
                    suites[folder].append(filename)
    return suites


def recovery_all_1txt_to_txt(folder_path):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if re.match('.*.1txt$', filename):
                target = filename.replace("1txt", "txt")
                print "rename %s to %s " % (os.path.join(dirpath, filename), target)
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, target))


def remove_files_by_index_dic(index_dic, comment_temporary=False):
    for folder in index_dic.keys():
        if len(index_dic[folder]) == 0:
            if comment_temporary is False:
                print 'delete folder %s' % folder
                shutil.rmtree(folder)
            else:
                print "comment all txt files under the folder %s" % folder
                existent_files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x))]
                for exist in existent_files:
                    absolute_path = os.path.join(folder, exist)
                    if re.match('.*.txt$', exist):
                        target = exist.replace('.txt', '.1txt')
                        print "rename %s to %s " % (absolute_path, target)
                        os.rename(absolute_path, os.path.join(folder, target))
        else:
            existent_files = [ x for x in os.listdir(folder) if (os.path.isfile(os.path.join(folder, x)) and (x != '__init__.txt'))]
            for exist in existent_files:
                absolute_path = os.path.join(folder, exist)
                if not (exist in index_dic[folder]):
                    if comment_temporary is False:
                        print "delete %s" % absolute_path
                        os.remove(absolute_path)
                    else:
                        if re.match('.*.txt$', exist):
                            target = exist.replace('.txt', '.1txt')
                            print "rename %s to %s " % (absolute_path, target)
                            os.rename(absolute_path, os.path.join(folder, target))
            for filename in index_dic[folder]:
                absolute_path = os.path.join(folder, filename)
                if not os.path.isfile(absolute_path):
                    print "ERROR: FILE '%s' NOT EXIST." % absolute_path
                    return False
    return True

folder_path = '.'
recovery_all_1txt_to_txt(folder_path)
generate_index(folder_path, index_file="before")
# replace_space_with_underline(folder_path)
# generate_index(folder_path, index_file = "after")
# if not remove_files_by_index_dic(get_expected_files_by_index(folder_path, "after.txt"), comment_temporary=True):
#     sys.exit(-1)
# generate_index(folder_path, index_file = "new_index")
