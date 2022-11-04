# Finding numbers below some number
x=1
while (x<=10) :
    print(x)
    x+=1  #x+1=x

# Finding odd numbers between two numbers
x= int(input("Enter min number: "))
y= int(input("Enter max number: "))
i= x
if x%2 == 0 : i=x+1
while i <= y :
    print(i)
    i+=2



