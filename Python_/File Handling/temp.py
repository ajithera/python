# 1.Create xls file which contains type(extension),file name,size of all the files in the folder

from msilib.schema import Directory
import os
import shutil

# target_path = r'C:\Users\91883\Downloads'
target_path = r'D:\to_organize'

file_list = os.listdir(target_path)
# print(file_list)

# list for storing extensions
file_ext=[]
for i in file_list:
    ext=os.path.splitext(i)
    j=ext[1]
    file_ext.append(j.replace('.',''))

# Distinct file extentions in the target path
file_ext=set(file_ext)

print(file_ext)

# for i in file_ext:
#     #creating folder for each extension
#     # src_dir = 
#     os.mkdir(target_path+'\\'+i.replace('.',''))
#     for j in file_list:
#         if j.endswith(i):
#             src=target_path+'\\'+j
#             tgt=target_path+'\\'+i.replace('.','')
#             shutil.move(src,tgt)

print('task completed')