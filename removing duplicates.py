# Removing duplicates using command
l1 = eval(input("Enter numbers of the list: "))
print(l1)
l2=[]
for each_value in l1 :
    if each_value not in l2 :
        l2.append(each_value)
print(l2)

# Removing duplicates by sets data type
l1 = eval(input("Enter a set of numbers: "))
s1 = set(l1)
print(s1)

