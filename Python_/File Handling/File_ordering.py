# 1.Create xls file which contains type(extension),file name,size of all the files in the folder

from msilib.schema import Directory
import os
import shutil

# target_path = r'C:\Users\91883\Downloads'
target_path = r'D:\to_organize'

file_list = os.listdir(target_path)
print(file_list)

#extracting extension names for creating folders
file_ext=[]
for i in file_list:
    ext=os.path.splitext(i)
    file_ext.append(ext[1])

#removing duplicates
file_ext=set(file_ext)
# print(file_ext)

#folders that are already present in the target
tar_ext=[]
for file in os.listdir(target_path):
    d = os.path.join(target_path, file)
    if os.path.isdir(d):
        tar_ext.append(d.rpartition('\\')[2])

tar_ext=set(tar_ext)
create_ext = file_ext.symmetric_difference(tar_ext)
unavl_extn = list(create_ext)

#creating all unique extensions for while moving files into folders
all_ext = file_ext.union(tar_ext)

# create folders for new extensions
for i in unavl_extn :
    os.mkdir(target_path+'\\'+i.replace('.',''))

print('folder created')

for i in all_ext:
    for j in file_list:
        if j.endswith(i):
            src=target_path+'\\'+j
            tgt=target_path+'\\'+i.replace('.','')
            shutil.move(src,tgt)

print('task completed')
