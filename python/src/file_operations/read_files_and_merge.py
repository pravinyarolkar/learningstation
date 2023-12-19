import os

# file_path = "C:\\Users\\YarolkarPravin\\src\\learningstation\\python\\src\\sample_files"
file_path = r'C:\Users\YarolkarPravin\src\learningstation\python\src\sample_files'
merged_file_path = r'C:\Users\YarolkarPravin\src\learningstation\python\src\sample_files\merged_content_file'

def readRecursive(filepath):
    for folder, subfolders, files in os.walk(filepath):
        # print(f"this is folder : {folder}")
        # print(subfolders, files)
        # print(f"files are : {files}")
        for file in files:
            file_full_path = f"{folder}\{file}"
            with open(merged_file_path, '+a', encoding="utf8") as f:
                with open(file_full_path, 'r', encoding="utf8") as singleFile:
                    data = singleFile.read()
                f.write(data)

        if subfolders:
            for folder in subfolders:
                readRecursive(folder)

# readRecursive(file_path)

f = open (merged_file_path, 'r', encoding="utf8")
# print(f.readline()) # read 1 line till EOL i.e. \n
# print(f.readline(10)) # read max 10 bytes and even if number is big readline function will read max 1 line
# print(f.readlines())

print(f.readline())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print(f.readline())
print(f.readline())
# file pointer moves everytime we read so to set pointer to begining we need to use seek()
f.seek(0)
print(f.readline())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readline())
# after adding seek(0) it moves pointer to begining 

f.seek(0)

# how to get file size
print(os.path.getsize(merged_file_path))
print(os.stat(merged_file_path).st_size)
fileStats = os.stat(merged_file_path)
f.seek(0, os.SEEK_END)
print(f.tell())

from datetime import datetime

print("create time")
print(fileStats.st_ctime)
print(datetime.fromtimestamp(fileStats.st_ctime))

print("access time")
print(fileStats.st_atime)
print(datetime.fromtimestamp(fileStats.st_atime))

print("modify time")
print(fileStats.st_mtime)
print(datetime.fromtimestamp(fileStats.st_mtime))

