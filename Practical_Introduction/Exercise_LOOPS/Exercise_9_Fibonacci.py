def fibonacci(n):
    a = 0
    b = 1
    for i in range ( 0, n ):
        temp = a
        a = b
        b = temp + b
    return a


num=input('Cuantos quieres ver?\n')
for c in range ( 0, int(num) ):
    print ( fibonacci ( c ) )
