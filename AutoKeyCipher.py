from WordtoWordDictionary import *

def getKey():
    key = int(input("Enter the key : "))
    return key

def getMessage():
    message = input("Enter the message : ")
    return message

def getDomain():
    n = int(input("Enter the Domain : "))
    return n

def Encrypt(message, key, n):
    
    message = message.upper()
    CipherText = ''

    for i in message:
        value = dictionary[i]        

        CipherText = CipherText + getletter((value+key)%n)
        key = value

    return CipherText

def Decrypt(message, key, n):
    Plaintext = ''

    for i in message:
        value = dictionary[i]

        Plaintext = Plaintext + getletter((value-key)%n)
        key = value - key
    
    return Plaintext.lower()

def removespaces(message):
    return message.replace(" ", "")
flag = 0
keystatus = input("Is the key given? (yes/no) : ")
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
        
        print(f"The CipherText is : {Encrypt(no_space_message, key)}")
        break

    elif choice == 2:
        if flag == 1:
            CipherText = getMessage()
            for key in range(1, 26):
                print(f"The Plain Text is : {Decrypt(CipherText, key, n)}")
        else:
            print(f"The Plaintext is : {Decrypt(getMessage(), key)}")
        break

    else:
        print("Invalid Option chosen!!! Try Again :)")