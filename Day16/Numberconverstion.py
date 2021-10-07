#Simple number convertion in python

def decimal_binary(num):
    num = int(num)
    if num >= 1:
        decimal_binary(num//2)
    print(num%2 , end ='')  #Using recursion ,you can also use in-built function "bin" 

def binary_decimal(num):
    num = int(num)
    decimal , i , n = 0 , 0 , 0
    while num != 0:
        de = num % 10
        decimal = decimal + de *(2**i)
        num = num//10
        i += 1
    print(decimal)   #Or you can simple use return(int , 2 )

def decimal_hexadecimal(num):
    num = int(num)
    #print(f"Hexadecimal : {hex(num)}")
    table = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexa = ''
    while num > 0:
        rem = num % 16
        hexa += table[rem]
        num = num//16
    print(hexa[::-1])    

def hexadecimal_decimal(num):
    dec = int(str(num) , 16)
    print(dec)

def decimal_octa(num):
    pass

def octa_decimal(num):
    pass 


if __name__ == "__main__":
    print("Here are the options : ")
    d = {1 : "Decimal - Binary" , 2 : "Binary - Decimal" , 3 : "Decimal - Hexadecimal" , 4 : "Hexadecimal - Decimal" , 5 : "Decimal - Octahydral" , 6 : "Octahydar - Decimal" }

    for i , v in d.items():
        print(i , "-----" , v)

    p = input("Enter the option : ")
    
    num = input("Please enter the number : \n")
    if p == "1":
        decimal_binary(num)
    elif p == "2":
        binary_decimal(num)
    elif p == "3":
        decimal_hexadecimal(num)
    elif p == "4":
        hexadecimal_decimal(num)
    elif p == "5":
        decimal_octa(num)
    elif p == "6":
        octa_decimal(num)    

          











