#Search string from multiple files
import os

text = input("Enter text : ")
path = input("Enter Path : ")

def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir(path)
    for file_name in files:
        abs_path = os.path.abspath(file_name) 
        ''' Thiss method returns a normalized version of the pathname path '''
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name , "r")
            if text in f.read():
                f = 1
                
                final_path = os.path.abspath(file_name)
                print(f"{text} found in {final_path} .")
                return True
                
                
    if f == 1:
        print(f"{text} not found .")
        return False
        

        
        
print(getfiles(path))         
