import sqlite3 
import os
import glob
from shutil import copy
dbLocation="C:/Users/Valentin/Apple/MobileSync/Backup/13fa7823a4c614bf77765ccced2435e7c662a86f/Manifest.db"

SystemDatabase=sqlite3.connect(dbLocation)   
cursorSystemDatabase=SystemDatabase.cursor()

fromDirInDB='Media/DCIM/112APPLE/'
toDirInDB='Media/DCIM/112APPLE/IMG_2964.MOV'


cursorSystemDatabase.execute("SELECT relativePath from Files WHERE relativePath>'%s' AND relativePath<'%s' ORDER BY relativePath DESC"%(fromDirInDB,toDirInDB,))
rec=cursorSystemDatabase.fetchall()
cursorSystemDatabase.execute("SELECT fileID from Files WHERE relativePath>'%s' AND relativePath<'%s' ORDER BY relativePath DESC"%(fromDirInDB,toDirInDB,))
rec2=cursorSystemDatabase.fetchall()
#for a in (rec):
#    print(a)
#for b in rec2:
#    print (b)

#Closing the connection
cursorSystemDatabase.close()
counter=0
wholeBackupDir="C:/Users/Valentin/Apple/MobileSync/Backup/13fa7823a4c614bf77765ccced2435e7c662a86f"
copyDestination="C:/Users/Valentin/Desktop/photos"
for b in rec2:
    src=glob.glob("%s/*/%s"%(wholeBackupDir,b[0],)) [0]
    copy(src, copyDestination)
    os.rename("%s/%s"%(copyDestination,b[0],), '%s/%s'%(copyDestination,(rec[counter][0]).split('/')[3]),)
    counter=counter+1
#print(type(glob.glob("C:/Users/Valentin/Apple/MobileSync/Backup/13fa7823a4c614bf77765ccced2435e7c662a86f/*/531b146221553fe3ff405f8890bb1bccc27804b1") [0]))

#
