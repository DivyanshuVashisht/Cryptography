def getNumber():
    n = int(input("Enter the number : "))
    return n

def getSize():
    size = int(input("Enter the count of numbers : "))
    return size

def calcGCD(size):
    n = []
    for i in range(size):
        n.append(getNumber())
    
    divisor = 1
    while True:
        flag = 0
        for i in n:
            if int(i%divisor) != 0:
                flag = 1
                break
        if flag == 0:
            gcd = divisor
        
        divisor += 1
        if divisor == min(n):
            break
    return gcd

size = getSize()
print(f"The GCD of the Numbers is : {calcGCD(size)}")