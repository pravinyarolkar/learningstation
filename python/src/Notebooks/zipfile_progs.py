{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "337f54a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import zipfile\n",
    "\n",
    "file_path = r\"C:\\Users\\YarolkarPravin\\src\\learningstation\\python\\src\\Notebooks\\Notebooks\"\n",
    "\n",
    "#create file 1 txt\n",
    "f1 = open('file1.txt', 'w')\n",
    "f1.write('FILE ONE CONTENT')\n",
    "f1.close()\n",
    "\n",
    "#create file 2 txt\n",
    "f2 = open('file2.txt', 'w')\n",
    "f2.write('FILE TWO CONTENT')\n",
    "f2.close()\n",
    "\n",
    "# open\n",
    "newZipFile = zipfile.ZipFile('newzipfile.zip', 'w')\n",
    "newZipFile.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)\n",
    "newZipFile.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)\n",
    "newZipFile.close()\n",
    "\n",
    "extract_obj = zipfile.ZipFile('newzipfile.zip', 'r')\n",
    "extract_obj.extractall('extract_folder')\n",
    "extract_obj.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
