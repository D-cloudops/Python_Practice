def config_update(config_file, key, value):
 try:
    with open(config_file, 'r') as file:
        lines = file.readlines()

    with open(config_file, 'w') as file:
      for line in lines:
         if key in line:
            file.write(key + " = " + value + "\n")
         else:
            file.write(line)
 except FileNotFoundError:
    print ("Enter the correct filepath") 


config_file=input("Enter the file path ")
key=input("The Key to change ")
value=input("Enter the new value for key ")

config_update(config_file, key, value)