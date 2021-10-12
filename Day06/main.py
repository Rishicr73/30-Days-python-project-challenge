# Basic Encryption and decryption using Atbashcipher.
class Atbashcipher :
    def __init__(self) -> None:
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
    def encryption(self , text):
        encryptedtext = ""
        for c in text:
            if c.isalpha():
                if c.isupper():
                    encryptedtext += self.alphabet[25 - (ord(c) - 65)].upper()
                else:
                    encryptedtext += self.alphabet[25 - (ord(c) - 97)]
            else:
                encryptedtext += c
        return encryptedtext
    def decryption(self , encryptedtext) :
        text_ = ""
        for c in encryptedtext:
            if c.isalpha():
                if c.isupper():
                    text_ += self.alphabet[25 - (ord(c) - 65)].upper()
                else :
                    text_ += self.alphabet[25 - (ord(c) - 97)]
            else:
                text_ += c
        return text_
a = input("Enter a message :")
msg = Atbashcipher()
print(msg.encryption(a))
b = msg.encryption(a)
print(msg.decryption(b))   

#output :
Enter a message :code
xlwv
code
