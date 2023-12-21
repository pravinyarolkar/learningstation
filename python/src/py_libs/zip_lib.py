import zipfile

file_path = r"C:\Users\YarolkarPravin\src\learningstation\python\src\Notebooks\Notebooks"

# create file 1 txt
f1 = open('file1.txt', 'w')
f1.write('FILE ONE CONTENT')
f1.close()

# create file 2 txt
f2 = open('file2.txt', 'w')
f2.write('FILE TWO CONTENT')
f2.close()

# open zip file in write mode and add newly created files to it
newZipFile = zipfile.ZipFile('newzipfile.zip', 'w')
newZipFile.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
newZipFile.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
newZipFile.close()

# open zip file in read mode and extract it to folder
extract_obj = zipfile.ZipFile('newzipfile.zip', 'r')
extract_obj.extractall('extract_folder')
extract_obj.close()