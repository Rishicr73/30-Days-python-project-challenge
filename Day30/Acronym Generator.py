fullname = input('')
preposition = {'for','and','in','of'}
acronym = ''
for i in fullname.split():
    if i not in preposition:
        acronym += i[0].upper()
print(f'{fullname} : {acronym}')     
