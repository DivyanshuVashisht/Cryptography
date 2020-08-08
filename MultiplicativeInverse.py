def MultiplicativeInverse(n, b):
    r1 = n
    r2 = b
    t1 = 0
    t2 = 1

    while r2>0:
        q = int(r1/r2)
        r = r1%r2
        r1 = r2
        r2 = r

        t = t1-q*t2
        t1 = t2
        t2 = t

    if r1==1:
        if t1<0:
            return t1+n
        return t1
    else:
        print("The Inverse does not exist.")


def gcd(a, b):
    if a<b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a

    while r2>0:
        q = int(r1/r2)
        r = r1%r2
        r1 = r2
        r2 = r
    
    return r1
