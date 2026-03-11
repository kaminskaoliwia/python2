def trojkat(n):
    for i in range(n, 0, -1):
        print("*" * i)

# trojkat(5)

def trojkat1(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end="") # <-- nie dziala no znak nl
        print()

# trojkat1(5)

def romb(n):
    # print(" "*n, "*", " "*n)
    # for i in range(n-1,0,-1):
    #    print(" "*i, "*"," "*i,"*")
    # print(" "*n, "*", " "*n)

    for i in range(n, 0, -1):
        print(" "*n, end="")
        if i==1:
            print("*")  
        else:
            print("*", end="")
            print(" "*(2*i -1), end="")
            print("*")

romb(5)
