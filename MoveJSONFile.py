import os, os.path,shutil
import sys


original_path = "C:\\Users\\tengw\\Documents\\SA_work\\CityGML_2.0_Test_Dataset_2012-04-23"
newpath = 'C:\\Users\\tengw\\Documents\\SA_work\\CityGML_2.0_Test_Dataset_2012-04-23_JSON\\'

def search(path, str):
    for x in os.listdir(path):
        fp = os.path.join(path, x)
        print(fp)
        if str in fp:
            newfp = os.path.join(newpath, os.path.basename(fp))#产生新目录要移动的文件路径
            shutil.move(fp, newfp)#移动文件



str = ".json"
search(original_path, str)