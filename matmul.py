
def multiplication(mat1, mat2, row1, col1, row2, col2):
    
    matrix = []
    
    for i in range(row1):
        tempmat = []
        for j in range(col1):
            temp = 0

            for k in range(col2):
                temp = temp + (mat1[i][k]*mat2[k][j])
            
            tempmat.append(temp)

        matrix.append(tempmat)

    return matrix

def getMatrix(row, col):
    matrix = []
    for i in range(0, row):
        a = []
        for j in range(0, col):
            a.append(int(input("Element : ")))
        matrix.append(a)
    return matrix


def checkCondition(row, col):
    if row==col:
        return True
    else:
        return False

row1, col1 = input("Enter the row and column of matrix 1(using space) : ").split()
row2, col2 = input("Enter the row and column of matrix 2(using space) : ").split()
row1, col1, row2, col2 = int(row1), int(col1), int(row2), int(col2)

if checkCondition(row2, col1):
    print("\nMatrix multiplication is possible!!", end=" ")
else:
    print("Sorry Matrix multiplication is not possible!!(invalid dimensions)", end=" ")
    exit(0)
    
print("Enter the elements of matrix 1 : ")
matrix1 = getMatrix(row1, col1)

print("Enter the elements of matrix 2 : ")
matrix2 = getMatrix(row2, col2)

print(f"The product of {matrix1} and {matrix2} is : {multiplication(matrix1, matrix2, row1, col1, row2, col2)}")