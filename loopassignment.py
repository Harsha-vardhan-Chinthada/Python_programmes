x= int(input('Please enter a number: '))
for i in range(1, x+1) :
    if i%10==0 :
        continue
    elif i>=100 :
        break
    else :
        print(i)

