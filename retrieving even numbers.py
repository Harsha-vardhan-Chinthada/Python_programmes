lst = [12,23,34,45,56,67,78,89,90]
Even_numbers = list(filter(lambda x:x%2==0,lst))
print(Even_numbers)
for i in Even_numbers: print(i)