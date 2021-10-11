# AGE CALCULATOR PROJECT IN PYTHON

from datetime import date
import time
def checkleap(year):
    if ( year % 4 == 0)or (year %100 != 0) and (year % 400 == 0):
        return True
    else:
        return False    
def monthdays(month , checkleap):
    if  month in [1 , 3 , 5 ,7 , 8 , 10 , 12]:
        return 31
    elif month in [4 ,6 ,9,11]:
        return 30
    elif month == 2 and checkleap:
        return 29
    elif month == 2 and (not checkleap) :
        return 28

x = input("Enter Your name : ")
v = input("Enter your Birth Date : ").split("-")
year = int(v[2])
Month = int(v[1])
Date = int(v[0])
today = str(date.today()).split('-')
localtime = time.localtime(time.time())
y = abs(year - int(today[0]))
m = y * 12 + localtime.tm_mon
day = 0
for i in range(year , int(today[0])):
    if  checkleap(i):
        day = day + 366
    else:
        day = day + 365
leap_year = checkleap(localtime.tm_year)
for j in range(1 , localtime.tm_mon):
    day = day + monthdays( j , leap_year)
day = day + localtime.tm_mday
print(f'{x} age is {y} years ')
print("Do you want to get in months and days ?")
n = input("")
if  n == "Yes" or 'Y' :
    print(f"{x} is {m} months old")
    print(f'{day} in days')               
