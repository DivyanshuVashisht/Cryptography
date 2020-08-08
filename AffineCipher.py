from WordtoWordDictionary import *
from MultiplicativeInverse import *

def getKey():
    key1, key2 = input("Enter the keys(using space)[Multiplicative_Key Additive_Key] : ").split()
    key1 = int(key1)
    key2 = int(key2)

    return key1, key2

def getMessage():
    message = input("Enter the message : ")
    return message

def getDomain():
    n = int(input("Enter the Domain : "))
    return n

def Encrypt(message, key1, key2, n):
    CipherText = ''
    message = message.upper()

    for i in message:
        value = dictionary[i]
        value = ((value*key1) + key2)%n
        CipherText = CipherText + getletter(value)
    
    return CipherText

def Decrypt(message, key1, key2, n):
    PlainText = ''

    for i in message:
        value = dictionary[i]

        value = ((value-key2)*MultiplicativeInverse(n, key1))%n

        PlainText = PlainText + getletter(value)
    
    return PlainText.lower()

def removespaces(message):
    return message.replace(" ", "")

flag = 0
keystatus = input("Is the key given? (yes/no) : ")
if keystatus == 'yes':
    key1, key2 = getKey()
    n = getDomain()
    if gcd(n, key1) != 1:
        print("The Multiplicative inverse of the Key does not exist. Exiting Code.............")
        exit(0)
else:
    flag == 1
    n = 26

while True:
    if flag == 0:
        print(
            "What do you want to do?",
            "1. Encrypt",
            "2. Decrypt"
        )

        choice = int(input("Enter your choice (1/2): "))
    else:
        choice = 2
    
    if choice == 1:
        no_space_message = removespaces(getMessage())
        print(f"The Cipher Text is : {Encrypt(no_space_message, key1, key2, n)}")
        break
    elif choice == 2:
        if flag == 1:
            CipherText = getMessage()
            for i in range(26):
                for j in range(26):
                    print(f"The Plain Text is : {Decrypt(CipherText, i, j, n)}")
        else:
            print(f"The Plain Text is : {Decrypt(getMessage(), key1, key2, n)}")
        
        break
    else:
        print("Invalid option Entered!! Please Try Again.")