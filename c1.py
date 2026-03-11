def romb(n,znk, znw):
    for i in range(n, 0, -1):
        x = " "*i + znk
        if i==n:
            print(x)
        else:
            print(x + znw*(2*n-2*i-1) + x[::-1])

    for i in range(n+1):
        x = " "*i + znk
        if i==n:
            print(x)
        else:
            print(x + znw*(2*n-2*i-1) + x[::-1])   

#romb(5,"*",".")
romb(7,"&","^")
# romb(100, "$", "c")