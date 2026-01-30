def addnum(a, b):
    return a+b

n = int(input("enter 1.addition 2.subraction : "))

if(n==1):
    result = addnum(int(input("enter a: ")), int(input("enter b: ")))
    print(f"addtion of a b = {result}")
elif(n==2):
    result = 0 #function subraction
    print(f"addtion of a b = {result}")