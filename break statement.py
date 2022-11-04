# break operation
lst = [1,2,3,4,5,6,7,8,9,0]

for i in lst :
    if (i==9) :
        continue
    print(i)

# continue operation
x= 0
while x < 30 :
    x+=1
    if x%4==0 :
        continue
    print(x)
