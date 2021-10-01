from cryptography.fernet import Fernet

'''
#Here we are are creating key only

def write_key():
    key = Fernet.generate_key()
    with open ("key.key" , "wb") as key_file:
        key_file.write(key)
write_key()     
'''
def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key
        
master_pwd = input("What is the Master password ? ")
key = load_key() + master_pwd
fer = Fernet(key)

def view():
    with open("passwords.txt" , 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
 #rstrip removes spaces if no arrgument is passed
            user , passw = data.split(":")
            print(f"USER : {user} , Password : {passw}")

def add():
    name = input("Account name : ")
    pwd = input("Password :")
    with open("passwords.txt" , "a") as f:
        f.write(name + " : " + pwd + "\n")

       

while True:

    mode = input("Would you like to add a new password or view existing one (view , add) , press q to quit ?" ).lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode ")
        continue
