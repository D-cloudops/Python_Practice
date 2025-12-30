import os

def log_files(dirpath):
        print ("check")
        logfiles=[]
        for filename in os.listdir(dirpath):
            if filename.endswith(".log"):
                filepath = os.path.join(dirpath, filename)
                logfiles.append(filepath)
            else:
                continue
        return (logfiles)

def error_check():
    try:
       log_file = log_files(log_dir)
       if log_file is None:
            print ("Enter the correct dir path")
       else:
            for file in log_file:
                    with open(file, 'r') as read:
                        lines = read.readlines()
                    for line in lines:
                        if "ERROR"  in line:
                            print (file, line)
                        else:
                            print ("No CRITICAL logs found")
    except FileNotFoundError:
        print ("Enter the correct filepath") 

log_dir=input("Enter the log file directory")
error_check()


def archieve_old_file():
    try:
       log_file = log_files(log_dir)
       if log_file is None:
            print ("Enter the correct dir path")
       else:
            
    except FileNotFoundError:
        print ("Enter the correct filepath")  