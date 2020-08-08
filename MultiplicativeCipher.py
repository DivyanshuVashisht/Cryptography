from WordtoWordDictionary import *
from MultiplicativeInverse import *

def getKey():
    key = int(input("Enter the key : "))
    return key

def getMessage():
    message = input("Enter the message : ")
    return message

def getDomain():
    n = int(input("Enter the value for the Domain : "))
    return n

def Encrypt(message, key, n):
    CipherText = ''

    message = message.upper()

    for item in message:
        value = dictionary[item]
        value = (value*key)%n

        CipherText = CipherText + getletter(value)
    
    return CipherText

def Decrypt(message, key, n):
    PlainText = ''

    for item in message:
        value = dictionary[item]
        value = (value*MultiplicativeInverse(n, key))%n

        PlainText = PlainText + getletter(value)

    return PlainText.lower()

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
        choice = int(input("Enter your choice (1/2) : "))
    else:
        choice = 2
    
    if choice == 1:
        no_space_message = removespaces(getMessage())

        print(f"The Cipher Text is : {Encrypt(no_space_message, key, n)}")
        break
    elif choice == 2:
        if flag == 1:
            key = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
            CipherText = getMessage()

            for i in key:
                print(f"The Plain Text is : {Decrypt(CipherText, i, n)}")
            
        else:
            print(f"The Plain Text is : {Decrypt(getMessage(), key, n)}")
        break
    else:
        print("Invalid option Typed!! Please Try Again....")