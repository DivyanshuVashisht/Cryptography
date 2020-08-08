def Inverse(mat, order):
    det = getDeterminant(mat, order)
    if det == 0:
        return 'The Inverse Does not exist!!! Determinant Value = 0...Error'
    adj = getAdjoint(mat, order)

    for i in range(order):
        for j in range(order):
            mat[i][j] = adj[i][j]/det

    return mat

def getDeterminant(mat, order):
    if order == 2:
        deter = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    elif order == 3:
        var1 = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        var2 = mat[0][1]*(mat[1][0]*mat[2][2] - mat[2][0]*mat[1][2])
        var3 = mat[0][2]*(mat[1][0]*mat[2][1] - mat[2][0]*mat[1][1])
        deter = var1 - var2 + var3

    else:
        var1 = mat[1][1]*(mat[2][2]*mat[3][3] - mat[3][2]*mat[2][3])
        var2 = mat[1][2]*(mat[2][1]*mat[3][3] - mat[3][1]*mat[2][3])
        var3 = mat[1][3]*(mat[2][1]*mat[3][2] - mat[3][1]*mat[2][2])
        deter1 = var1 - var2 + var3

        var1 = mat[1][0]*(mat[2][2]*mat[3][3] - mat[3][2]*mat[2][3])
        var2 = mat[1][2]*(mat[2][0]*mat[3][3] - mat[3][0]*mat[2][3])
        var3 = mat[1][3]*(mat[2][0]*mat[3][2] - mat[3][0]*mat[2][2])
        deter2 = var1 - var2 + var3

        var1 = mat[1][0]*(mat[2][1]*mat[3][3] - mat[3][1]*mat[2][3])
        var2 = mat[1][1]*(mat[2][0]*mat[3][3] - mat[3][0]*mat[2][3])
        var3 = mat[1][3]*(mat[2][0]*mat[3][1] - mat[3][0]*mat[2][1])
        deter3 = var1 - var2 + var3

        var1 = mat[1][0]*(mat[2][1]*mat[3][2] - mat[3][1]*mat[2][2])
        var2 = mat[1][1]*(mat[2][0]*mat[3][2] - mat[3][0]*mat[2][2])
        var3 = mat[1][2]*(mat[2][0]*mat[3][1] - mat[3][0]*mat[2][1])
        deter4 = var1 - var2 + var3

        deter = mat[0][0]*deter1 - mat[0][1]*deter2 + mat[0][2]*deter3 - mat[0][3]*deter4
    
    return deter

def getAdjoint(mat, order):
    if order == 2:
        adj = [
            [mat[1][1], -mat[0][1]],
            [-mat[1][0], mat[0][0]]
        ]
    elif order == 3:
        adj = [
            [mat[1][1]*mat[2][2]-mat[2][1]*mat[1][2], -mat[0][1]*mat[2][2]+mat[2][1]*mat[0][2], mat[0][1]*mat[1][2]-mat[1][1]*mat[0][2]],
            [-mat[1][0]*mat[2][2]+mat[2][0]*mat[1][2], mat[0][0]*mat[2][2]-mat[2][0]*mat[0][2], -mat[0][0]*mat[1][2]+mat[1][0]*mat[0][2]],
            [mat[1][0]*mat[2][1]-mat[2][0]*mat[1][1], -mat[0][0]*mat[2][1]+mat[2][0]*mat[0][1], mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]]
        ]
    else:
        m1 = [
            [mat[1][1], mat[1][2], mat[1][3]],
            [mat[2][1], mat[2][2], mat[2][3]],
            [mat[3][1], mat[3][2], mat[3][3]]
        ]
        m2 = [
            [mat[1][0], mat[1][2], mat[1][3]],
            [mat[2][0], mat[2][2], mat[2][3]],
            [mat[3][0], mat[3][2], mat[3][3]]
        ]
        m3 = [
            [mat[1][0], mat[1][1], mat[1][3]],
            [mat[2][0], mat[2][1], mat[2][3]],
            [mat[3][0], mat[3][1], mat[3][3]]
        ]
        m4 = [
            [mat[1][0], mat[1][1], mat[1][2]],
            [mat[2][0], mat[2][1], mat[2][2]],
            [mat[3][0], mat[3][1], mat[3][2]]
        ]
        m5 = [
            [mat[0][1], mat[0][2], mat[0][3]],
            [mat[2][1], mat[2][2], mat[2][3]],
            [mat[3][1], mat[3][2], mat[3][3]]
        ]
        m6 = [
            [mat[0][0], mat[0][2], mat[0][3]],
            [mat[2][0], mat[2][2], mat[2][3]],
            [mat[3][0], mat[3][2], mat[3][3]]
        ]
        m7 = [
            [mat[0][0], mat[0][1], mat[0][3]],
            [mat[2][0], mat[2][1], mat[2][3]],
            [mat[3][0], mat[3][1], mat[3][3]]
        ]
        m8 = [
            [mat[0][0], mat[0][1], mat[0][2]],
            [mat[2][0], mat[2][1], mat[2][2]],
            [mat[3][0], mat[3][1], mat[3][2]]
        ]
        m9 = [
            [mat[0][1], mat[0][2], mat[0][3]],
            [mat[1][1], mat[1][2], mat[1][3]],
            [mat[3][1], mat[3][2], mat[3][3]]
        ]
        m10 = [
            [mat[0][0], mat[0][2], mat[0][3]],
            [mat[1][0], mat[1][2], mat[1][3]],
            [mat[3][0], mat[3][2], mat[3][3]]
        ]
        m11 = [
            [mat[0][0], mat[0][1], mat[0][3]],
            [mat[1][0], mat[1][1], mat[1][3]],
            [mat[3][0], mat[3][1], mat[3][3]]
        ]
        m12 = [
            [mat[0][0], mat[0][1], mat[0][2]],
            [mat[1][0], mat[1][1], mat[1][2]],
            [mat[3][0], mat[3][1], mat[3][2]]
        ]
        m13 = [
            [mat[0][1], mat[0][2], mat[0][3]],
            [mat[1][1], mat[1][2], mat[1][3]],
            [mat[2][1], mat[2][2], mat[2][3]]
        ]
        m14 = [
            [mat[0][0], mat[0][2], mat[0][3]],
            [mat[1][0], mat[1][2], mat[1][3]],
            [mat[2][0], mat[2][2], mat[2][3]]
        ]
        m15 = [
            [mat[0][0], mat[0][1], mat[0][3]],
            [mat[1][0], mat[1][1], mat[1][3]],
            [mat[2][0], mat[2][1], mat[2][3]]
        ]
        m16 = [
            [mat[0][0], mat[0][1], mat[0][2]],
            [mat[1][0], mat[1][1], mat[1][2]],
            [mat[2][0], mat[2][1], mat[2][2]]
        ]
        adj = [
            [getDeterminant(m1), -getDeterminant(m5), getDeterminant(m9), -getDeterminant(m13)],
            [-getDeterminant(m2), getDeterminant(m6), -getDeterminant(m10), getDeterminant(m14)],
            [getDeterminant(m3), -getDeterminant(m7), getDeterminant(m11), -getDeterminant(m15)],
            [-getDeterminant(m4), getDeterminant(m8), -getDeterminant(m12), getDeterminant(m16)]
        ]
    
    return adj

print(Inverse([[3, 0, 2], [2, 0, -2], [0, 1, 1]], 3))