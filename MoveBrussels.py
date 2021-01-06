import os, shutil

filepath = 'C:\\Users\\tengw\\Documents\\SA_work\\Brussels\\'
targetPath = 'C:\\Users\\tengw\\Documents\\SA_work\\Brussels_JSON\\'


for name in os.listdir(filepath):
    #print(name)
    str2 = filepath + name + '\\UrbAdm_Bu_3D.json'
    #cmd = 'C:\\Users\\tengw\\Documents\\SA_work\\citygml-tools-1.3.0\\bin\\citygml-tools to-cityjson '+str2

    str3 = targetPath + name + '_UrbAdm_Bu_3D.json'
    print(str2,str3)
    try:
        shutil.move(str2, str3)
    except Exception as e:
        print("!")