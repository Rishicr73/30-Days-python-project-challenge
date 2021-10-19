with open('currency.txt')as f:
    lines = f.readlines()
d = {}
for line in lines:
    parsed = line.split('\t')
    d[parsed[0]] = parsed[1]
    
amount = int(input('Enter a amount : \n'))  
print('Enter a name of currency you want to convert ?' '\n' 'Available options:')
[print(item) for item in d.keys()]
c = input('please Enter one of these Value :\n')
print(f'{amount} INR is equal to {amount * float(d[c])} {c}')
