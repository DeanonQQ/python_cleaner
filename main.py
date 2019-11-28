import os
import shutil
import datetime
import pathlib

# ------------------------CONFIG-------------------------------

CLEAN_PATH = "C:/Users/rodio/Desktop"
CLEAN_FORMATS = ('.jpg', '.psd', '.jpeg', '.ai')
FOLDER_NAME = "WorkFiles"

# -------------------------------------------------------------


now = datetime.datetime.now()

MV_FOLDER = CLEAN_PATH + "/" + FOLDER_NAME + ' ' + str(now.strftime("%d-%m-%Y"))

names = os.listdir(CLEAN_PATH)
for name in names:
    fullname = os.path.join(CLEAN_PATH, name)
    if os.path.isfile(fullname):
        if fullname.lower().endswith(('.ai', '.jpg', '.jpeg', 'psd', '.rar', '.pdf', '.svg', '.txt', '.eps', '.png')):
            if not os.path.exists(MV_FOLDER):
                os.makedirs(MV_FOLDER)
            
            shutil.move(fullname, MV_FOLDER+'/'+name)


            
            
            print(fullname)