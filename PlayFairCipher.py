from WordtoWordDictionary import *

def getKey():
    key = input("Enter the Key : ")
    return key.upper()

def getMessage():
    message = input('Enter the message : ')
    return message

def FillerElement(message):
    for i in range(0, len(message), 2):
        if message[i] == message[i+1]:
            message[i].append('X')
    if len(message)%2 !=0:
        return message + 'X'
    return message

def KeyMatrix(textkey):
    key = []
    flag = 0
    visitedspace = []

    for i in range(5):
        a = []
        counter = 0

        if flag == 0:
            for item in textkey:
                a.append(item)
                counter +=1
                if item == textkey[-1]:
                    flag = 1
                if counter==5:
                    break
                
        if counter < 5 or flag == 1:
            for letter in dictionary:
                if letter not in textkey and letter not in visitedspace:
                    if letter == 'J':
                        continue
                    if counter==5:
                        break
                    a.append(letter)
                    counter+=1
                    visitedspace.append(letter)
                    
        key.append(a)
    return key

def removespaces(message):
    return message.replace(" ", "")

def getPosition(letter, key):
    for row in range(5):
        for col in range(5):
            if letter == key[row][col]:
                return row, col

def Encrypt(message, key):
    CipherText = ''
    message = message.upper()

    for i in range(0, len(message), 2):
        row1, col1 = getPosition(message[i], key)
        row2, col2 = getPosition(message[i+1], key)

        if row1 == row2:
            if col1 < 4 and col2 < 4:
                CipherText = CipherText + key[row1][col1+1] + key[row2][col2+2]
            if col2 == 4:
                CipherText = CipherText + key[row1][col1+1] + key[row1][0]
            elif col1 == 4:
                CipherText = CipherText + key[row1][0] + key[row1][col2+1]
        elif col1 == col2:
            if row1 < 4 and row2 < 4:
                CipherText = CipherText + key[row1+1][col1] + key[row2+1][col2]
            elif row2 == 4:
                CipherText = CipherText + key[row1+1][col1] + key[0][col1]
            elif row1 == 4:
                CipherText = CipherText + key[0][col1] + key[row2+1][col2]
        else:
            CipherText = CipherText + key[row1][col2] + key[row2][col1]
    
    return CipherText

def Decrypt(message, key):
    PlainText = ''
    message = message.upper()

    for i in range(0, len(message), 2):
        row1, col1 = getPosition(message[i], key)
        row2, col2 = getPosition(message[i+1], key)

        if row1==row2:
            if col1 > 0 and col2 > 0:
                PlainText = PlainText + key[row1][col1-1] + key[row2][col2-1]
            elif col2 ==0:
                PlainText = PlainText + key[row1][col1-1] + key[row2][4]
            elif col1 == 0:
                PlainText = PlainText + key[row1][4] + key[row2][col2-1]
        elif col1 == col2:
            if row1 > 0 and row2 > 0:
                PlainText = PlainText + key[row1-1][col1] + key[row2-1][col1]
            elif row1 == 0:
                PlainText = PlainText + key[4][col1] + key[row2-1][col2]
            elif row2 == 0:
                PlainText = PlainText + key[row1-1][col1] + key[4][col2]
        else:
            PlainText = PlainText + key[row1][col2] + key[row2][col1]

    return PlainText.lower().replace('x', '')

key = getKey()
keymat = KeyMatrix(key)

while True:
    print(
        "What do you want to do?",
        "1. Encrypt",
        "2. Decrypt"
    )

    choice = int(input("Enter your choice (1/2) : "))

    if choice == 1:
        print(f"The Cipher Text is : {Encrypt(FillerElement(removespaces(getMessage())), keymat)}")
        break
    elif choice == 2:
        print(f"The Plain Text is : {Decrypt(getMessage(), keymat)}")
        break
    else:
        print("You have entered an invalid option!! Try Again...")