#-*-coding:utf-8-*-
import os
import glob

i=0
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.exe':
            print(full_filename)
            os.rename(full_filename,i+"Malware.exe")


search("C:/test")
