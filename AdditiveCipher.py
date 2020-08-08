from WordtoWordDictionary import *

def getMessage():
    message = input("Enter the message : ")
    return message

def getKey():
    Key = int(input("Enter Key : "))
    return Key

def getDomain():
    n = int(input("Enter the Domain : "))
    return n

def Encrypt(message, key, n):
    message = message.upper()
    
    Ciphertext = ''
    for i in message:
        value = dictionary[i]
        
        value = (value + key)%n
        Ciphertext = Ciphertext + getletter(value)
    
    return Ciphertext

def Decrypt(message, key, n):

    Plaintext = ''

    for i in message:
        value = dictionary[i]
        
        value = (value - key)%n
        Plaintext = Plaintext + getletter(value)

    Plaintext = Plaintext.lower()

    return Plaintext

def removespaces(message):
    return message.replace(" ", "")

flag = 0
keystatus = input("Is the key given? (yes/no): ")
if keystatus == 'yes':
    key = getKey()
    n = getDomain()
else:
    flag = 1
    n = 26

while True:
    if flag == 0:
        print(
            "What do you want to do?",
            "1. Encrypt", 
            "2. Decrypt"
        )

        choice = int(input("\n Enter index no.(1/2) : "))
    else:
        choice = 2

    if choice==1:
        no_space_message = removespaces(getMessage())
        
        print(f"The CipherText is : {Encrypt(no_space_message, key, n)}")
        break

    elif choice == 2:
        if flag == 1:
            CipherText = getMessage()
            for key in range(1, 26):
                print(f"The Plain Text is : {Decrypt(CipherText, key, n)}")
        else:
            print(f"The Plaintext is : {Decrypt(getMessage(), key, n)}")
        break

    else:
        print("Invalid Option chosen!!! Try Again :)")
    
