def register():
    db = open('C:\\Users\\rushi\Documents\\pythonprojects\\Login system\\database.txt' , 'r')
    username = input("Create Username:")
    password = input("Enter Password:")
    password_1 = input("Confirm Password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)

    data = dict(zip(d,f))
    #print(data)    

    
    if password != password_1:
        print("Passwords Don't match , restart")
        register() 
    else:
        if len(password) <= 6:
            print("Password Too Short , restart :")
            register()
        elif username in d:
            print("username already exists")
            register() 
        else:
            db = open('C:\\Users\\rushi\Documents\\pythonprojects\\Login system\\database.txt' ,'a')
            db.write(username+", "+ password+ '\n')
            print("Success !")                


def access():
    db = open('C:\\Users\\rushi\Documents\\pythonprojects\\Login system\\database.txt', 'r')
    username = input("Enter Your Username: ")
    password = input("Enter Password: ")

    if not len(username or password)<1:
        d = []  #In this we are storing username
        f = []   #In this we are storing passwords because we have to make dict
        for i in db:
            a , b = i.split(',')
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f)) #Because dict are easy to handle.

        try :
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Success")
                        print(f"Hi , {username}")
                    else:
                        print("Password Incorrect")
                except:
                    print("Incorrect Password or Username .")
            else:
                print("Username doesn't exist.")
        except:
            print("Username and password Doesn't exist . ")

def welcome():
    print("Welcome To the authentication system ")
def Home(option=None):
    welcome()
    option = input("Login | Signup :").lower()
    if option == "login":
        access()
    elif option == "signup":
        register()

if __name__ == "__main__":
    Home()
