
import os
import shutil
os.chdir('/home/next/') #Make sure you add your source and destination path below

dir_src = ("/home/next/git/milk/")
dir_dst = ("/home/next/.hcms/uploads/None/")

for filename in os.listdir(dir_src):
    if filename.endswith(tuple(['.png','.jpg','.jpeg'])):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)


