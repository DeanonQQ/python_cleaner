import os
import shutil
import datetime
import pathlib
from plyer import notification

# ------------------------CONFIG-------------------------------

CLEAN_PATH = "C:/Users/rodio/Desktop"
CLEAN_FORMATS = ('.ai', '.jpg', '.jpeg', 'psd', '.rar', '.pdf', '.svg', '.txt', '.eps', '.png')
FOLDER_NAME = "WorkFiles"

# -------------------------------------------------------------

now = datetime.datetime.now()

if not os.path.exists(CLEAN_PATH + '/' + FOLDER_NAME):
    os.makedirs(CLEAN_PATH + '/' + FOLDER_NAME)

MV_FOLDER = CLEAN_PATH + "/" + FOLDER_NAME + "/" + FOLDER_NAME + ' ' + str(now.strftime("%d-%m-%Y"))

names = os.listdir(CLEAN_PATH)
for name in names:
    fullname = os.path.join(CLEAN_PATH, name)
    if os.path.isfile(fullname):
        if fullname.lower().endswith(CLEAN_FORMATS):
            if not os.path.exists(MV_FOLDER):
                os.makedirs(MV_FOLDER)
            
            shutil.move(fullname, MV_FOLDER+'/'+name)