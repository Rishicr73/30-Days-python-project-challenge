#FILE RENAMING PROJECT 
import os

# folder = "C:\Users\rushi\Documents\Ajay"
# c = 1
fpath = "C:\\Users\\rushi\\Documents\\Ajay"
c = 1
os.chdir(path=fpath)    #HERE WE ARE CHANGING DIRECTORY BECOZ IF WE DOESN'T CHANGE IT ,IT WILL SEARCH ON CURRENT DIRECTORY AND ITS FOUND IT CAN GIVE ERROR SO CHANGE DIRECTORY THEN IT WILL SEARCH ON OTHER DIRECTORIES AS WELL.
for file_name in os.listdir(fpath):
    old_name =  file_name
    new_name =  "AJx_" + str(c)+ ".txt"
    os.rename(old_name , new_name)
    c += 1
print("Files are Renamed.")
res = os.listdir(fpath)
print(res)
