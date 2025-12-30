import os 
import datetime

command_list = ["wmic cpu get loadpercentage"]

#for command in command_list:
#    print(os.system(command))

def show_date():
    return datetime.datetime.today()

print(show_date())