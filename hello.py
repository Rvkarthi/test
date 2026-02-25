def addnum(a, b):
    return a+b

def sub(a,b):
    return a-b

n = int(input("enter 1.addition 2.subraction : "))

if(n==1):
    result = addnum(int(input("enter a: ")), int(input("enter b: ")))
    print(f"addtion of a b = {result}")
elif(n==2):
    result = sub(int(input("enter the a value:")), int(input("enter hte b value:")))
    print(f"subtraction of a b = {result}")