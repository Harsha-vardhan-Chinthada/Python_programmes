def customgen(x,y):
    while (x>y):
        yield y
        y+=1

result = customgen(30,20)
for i in result: print(i)