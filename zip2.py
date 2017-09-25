import os
#from zipfile import ZipFile
import zipfile
from os import path
import shutil

str1=os.getcwd()
print str1
str2=str1.split('/')
n=len(str2)
print str2[n-1]
print str2
str3=str(str2[n-1])
print str3
zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk(('/'+str(path.split(os.getcwd())))):
    zf.write(dirname)
    for filename in files:
        print filename
        zf.write(os.path.join(dirname, filename))
zf.close()

