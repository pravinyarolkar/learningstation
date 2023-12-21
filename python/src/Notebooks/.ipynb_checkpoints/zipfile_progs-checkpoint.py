{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89903d48",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "[WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\\\Users\\\\YarolkarPravin\\\\src\\\\learningstation\\\\python\\\\src\\\\Notebooks\\\\Notebooks\\regular_expression_practice'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m newZipFile\u001b[38;5;241m.\u001b[39mclose()\n\u001b[0;32m      7\u001b[0m newZipFile \u001b[38;5;241m=\u001b[39m zipfile\u001b[38;5;241m.\u001b[39mZipFile(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mnewzipfile.zip\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mw\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m----> 8\u001b[0m \u001b[43mnewZipFile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mwrite\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile_path\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;130;43;01m\\r\u001b[39;49;00m\u001b[38;5;124;43megular_expression_practice\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcompress_type\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mzipfile\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mZIP_DEFLATED\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      9\u001b[0m newZipFile\u001b[38;5;241m.\u001b[39mwrite(file_path \u001b[38;5;241m+\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mzipfile_progs\u001b[39m\u001b[38;5;124m'\u001b[39m, compress_type\u001b[38;5;241m=\u001b[39mzipfile\u001b[38;5;241m.\u001b[39mZIP_DEFLATED)\n\u001b[0;32m     10\u001b[0m newZipFile\u001b[38;5;241m.\u001b[39mclose()\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\zipfile.py:1739\u001b[0m, in \u001b[0;36mZipFile.write\u001b[1;34m(self, filename, arcname, compress_type, compresslevel)\u001b[0m\n\u001b[0;32m   1734\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_writing:\n\u001b[0;32m   1735\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m   1736\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCan\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt write to ZIP archive while an open writing handle exists\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1737\u001b[0m     )\n\u001b[1;32m-> 1739\u001b[0m zinfo \u001b[38;5;241m=\u001b[39m \u001b[43mZipInfo\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfrom_file\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43marcname\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1740\u001b[0m \u001b[43m                          \u001b[49m\u001b[43mstrict_timestamps\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_strict_timestamps\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1742\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m zinfo\u001b[38;5;241m.\u001b[39mis_dir():\n\u001b[0;32m   1743\u001b[0m     zinfo\u001b[38;5;241m.\u001b[39mcompress_size \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\zipfile.py:502\u001b[0m, in \u001b[0;36mZipInfo.from_file\u001b[1;34m(cls, filename, arcname, strict_timestamps)\u001b[0m\n\u001b[0;32m    500\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(filename, os\u001b[38;5;241m.\u001b[39mPathLike):\n\u001b[0;32m    501\u001b[0m     filename \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39mfspath(filename)\n\u001b[1;32m--> 502\u001b[0m st \u001b[38;5;241m=\u001b[39m \u001b[43mos\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstat\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    503\u001b[0m isdir \u001b[38;5;241m=\u001b[39m stat\u001b[38;5;241m.\u001b[39mS_ISDIR(st\u001b[38;5;241m.\u001b[39mst_mode)\n\u001b[0;32m    504\u001b[0m mtime \u001b[38;5;241m=\u001b[39m time\u001b[38;5;241m.\u001b[39mlocaltime(st\u001b[38;5;241m.\u001b[39mst_mtime)\n",
      "\u001b[1;31mOSError\u001b[0m: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\\\Users\\\\YarolkarPravin\\\\src\\\\learningstation\\\\python\\\\src\\\\Notebooks\\\\Notebooks\\regular_expression_practice'"
     ]
    }
   ],
   "source": [
    "import zipfile\n",
    "\n",
    "file_path = r\"C:\\Users\\YarolkarPravin\\src\\learningstation\\python\\src\\Notebooks\\Notebooks\"\n",
    "import os\n",
    "\n",
    "newZipFile = zipfile.ZipFile('newzipfile.zip', 'w')\n",
    "newZipFile.write('regular_expression_practice', compress_type=zipfile.ZIP_DEFLATED)\n",
    "newZipFile.write('zipfile_progs', compress_type=zipfile.ZIP_DEFLATED)\n",
    "newZipFile.close()"
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
