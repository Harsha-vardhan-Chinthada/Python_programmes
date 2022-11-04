from functools import reduce
lst = [10,20,30,40,50]
result = reduce(lambda a,b:a+b,lst)
print(result)
