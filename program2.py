def sum(a , b) :
    A=(a+b)
    print("Your answer is", A)
def multi(a,b):
    A=(a*b)
    print("Your answer is", A)
def sub(a , b):
    A=(a-b)
    print("Your answer is", A)
def div(a , b):
    A=(a/b)
    print("Your answer is", A)

x=int(input("Digit No. 1 : "))
y=int(input("Digit No. 2 : "))
z=input("What to do (+, -, *, /) ?")

if(z=="-"):
    sub(x , y)
elif(z=="+"):
    sum(x,y)
elif(z=="*"):
    multi(x,y)
elif(z=="/"):
    div(x,y)
else:
    print("Invalid operation")

print("")
z=input("What to do for 2nd time (+, -, *, /) ?")
if(z=="-"):
    sub(x , y)
elif(z=="+"):
    sum(x,y)
elif(z=="*"):
    multi(x,y)
elif(z=="/"):
    div(x,y)
else:
    print("Invalid operation")

print("")
z=input("What to do for 3rd time (+, -, *, /) ?")
if(z=="-"):
    sub(x , y)
elif(z=="+"):
    sum(x,y)
elif(z=="*"):
    multi(x,y)
elif(z=="/"):
    div(x,y)
else:
    print("Invalid operation")