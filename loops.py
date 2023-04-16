def loop1(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def loop2(n):
    x = 0
    for i in range(n):
        x += 1
    for j in range(n):
        x += 1
    return x

def loop3(n):
    x = 0
    for i in range(n):
        if (i == n-1):
            for j in range(n):
                x += 1
    return x

def loop4(n):
    x = 0
    for i in range(n):
        for j in range(i,n):
            x += 1
    return x

n=4                                
print("Loop1, Rückgabewert", loop1(n))
print("Loop2, Rückgabewert", loop2(n))
print("Loop3, Rückgabewert", loop3(n))
print("Loop4, Rückgabewert", loop4(n))
