import os
import subprocess
import tempfile
import traceback

filepath = 'C:\\Users\\tengw\\Documents\\SA_work\\Not_work\\Kreuz_Leverkusen_2008-03-05\\'


str1 = 'C:\\Users\\tengw\\Documents\\SA_work\\citygml-tools-1.3.0\\bin\\citygml-tools to-cityjson '

for name in os.listdir(filepath):
    #if name != os.listdir(filepath)[-1]:
    str2 = filepath + name
    cmd = 'C:\\Users\\tengw\\Documents\\SA_work\\citygml-tools-1.3.0\\bin\\citygml-tools to-cityjson '+str2
    print(cmd)
    try:
        out_temp = tempfile.TemporaryFile(mode='w+')
        fileno = out_temp.fileno()
        obj = subprocess.Popen(cmd, shell=True, stdout=fileno, stderr=fileno)
        obj.wait()
        out_temp.seek(0)
        lines = out_temp.readlines()
        print(lines)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        if out_temp:
            out_temp.close()





