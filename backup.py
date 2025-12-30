import shutil
import datetime
import os
import boto3

def backupfile(source,destination):
    today=datetime.date.today()
    backup_file_name=os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)   ##Archieving and compressing using shutil

source="D:/Practice/Python_practise/logs"
destination="D:/Practice/Python_practise/backup"
backupfile(source,destination)