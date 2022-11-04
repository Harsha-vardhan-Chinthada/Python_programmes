n = int(input("Enter the number: "))

for i in range(1,n+1):

if i%10 == 10:

continue

elif i > 100:

break

else:

print(i)