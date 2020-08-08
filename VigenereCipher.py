from WordtoWordDictionary import *

def getKey():
    key = input("Enter the key : ")
    return key

def keyStream(key):
    k = []
    for i in key:
        k.append(dictionary[i])
    return k

def getMessage():
    message = input("Enter the message : ")
    return message

def removespaces(message):
    return message.replace(" ", "")

def getDomain():
    n = int(input("Enter the Domain : "))
    return n

def Encrypt(message, key, n):
    CipherText = ''
    message = message.upper()

    keycount = 0
    for i in message:
        value = dictionary[i]
        value = (value+key[keycount])%n

        CipherText = CipherText + getletter(value)
        keycount += 1
        if keycount == len(key):
            keycount = 0
    return CipherText

def Decrypt(message, key, n):
    PlainText = ''
    keycount = 0
    
    for i in message:
        value = dictionary[i]
        value = (value-key[keycount])%n

        PlainText = PlainText + getletter(value)
        keycount += 1
        if keycount == len(key):
            keycount = 0
    return PlainText.lower()

key = getKey()
keystream = keyStream(key)
n = getDomain()

while True:
    print(
        "What do you want to do?",
        "1. Encrypt",
        "2. Decrypt"
    )

    choice = int(input("Enter your choice (1/2) : "))

    if choice == 1:
        no_space_message = removespaces(getMessage())
        print(f"The Cipher Text is : {Encrypt(no_space_message, keystream, n)}")
        break
    elif choice == 2:
        print(f"The Plain Text is : {Decrypt(getMessage(), keystream, n)}")
        break
    else:
        print("Invalid option Entered!!! Try Again.......")