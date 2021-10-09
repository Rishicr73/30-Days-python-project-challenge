#Required module : pip install wikipedia

import wikipedia

#Input search material from user
text = input("Enter text : ")

#wikipedia find details about search
result = wikipedia.summary(text)

#printing the result
print(result)
