import zipfile
import os

files = []
def is_zipfile_complete(zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # 检查zip文件是否损坏
            is_valid = zip_ref.testzip() is None
            return is_valid
    except zipfile.BadZipFile:
        return False
def traversal_files(path):
    for item in os.scandir(path):
        if item.is_dir():
            traversal_files(item)
        elif item.is_file():
            files.append(item.path)


path = 'Z:/lexmark\MC3326, CX331, MC3224\CXLBL.081.234.zip'
#traversal_files(path)
#print(files)
# for file in files:
#     if file[-3:] == 'zip':
if is_zipfile_complete(path):
    print(path + " Zip压缩包文件完整！")
else:
    print(path + " Zip压缩包文件不完整或损坏！")
            # with open("check.txt", 'a') as f:
            #     f.write(file+'\n')