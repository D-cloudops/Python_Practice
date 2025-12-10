import os

def list_files(folder):
    try:
       list = os.listdir(folder)
       return list, None
    except FileNotFoundError:
       return None, "enter correct path"
def main():
    folder_path=input("enter the folder with spaces: ").split()

    for folder in folder_path:
        files, error = list_files(folder)
        if files:
           for file in files:
             print ("the list of files in-", folder)
             print (file)
        else:
           print (error, folder)

if __name__ == "__main__":
    main()