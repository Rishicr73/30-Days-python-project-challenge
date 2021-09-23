'''
Password generator by 25-25-25-25 rule 
'''
import random
import time

alpha = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num =  "0123456789"
special = '@#$%&*'

print("Welcome ! To the password generator.")
time.sleep(2)
len_pass = int(input("Enter password length : "))
x = (len_pass)//4
alpha_len , upper_len , num_len   = x , x , x
special_len = len_pass - (alpha_len + upper_len + num_len)
password = []

def generate_pass(length , array ):
    for i in range(length):
        index = random.randint(0 , len(array) - 1)
        character = array[index]
        password.append(character)

generate_pass(alpha_len , alpha)
generate_pass(num_len , num)
generate_pass(upper_len , upper)
generate_pass(special_len , special)
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)   
