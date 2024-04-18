from fileinput import filename
import os
from shlex import join
import shutil

def findAllFile(src_path,dst_path):
    for root, ds, fs in os.walk(src_path):
        for f in fs:
            if f.endswith('.thy'):
                fullname = os.path.join(root, f)
                newfilename_list = fullname.split('\\')
                newfilename = '_'.join(newfilename_list)
                new_path=os.path.join(dst_path,newfilename)
                shutil.copy2(fullname,new_path)

def main():
    file = open('target1.txt',"w")
    src_path = 'thys'
    dst_path = 'theory2'
    findAllFile(src_path,dst_path)
    
if __name__ == '__main__':
    main()