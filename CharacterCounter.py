from WordtoWordDictionary import *

def characterCounter(message):
    visitedChar = list()
    frequency_table = {}

    for i in message:
        if i not in visitedChar:
            visitedChar.append(i)
            counter = 0
            char = i
            for j in message:
                if char == j:
                    counter += 1
            
            frequency_table.update({i : counter})
    return frequency_table


CipherText = input("Enter the Cipher Text : ")

print(f"The Frequency table of each character is as follows : {characterCounter(CipherText)}")
