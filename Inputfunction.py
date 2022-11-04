"""s=input('Enter the name:')
print(s)"""

#Taking single input value
"""i=int(input('Enter the number:'))
print(i)"""

#Taking multiple input values (if we dont give format it will take it as string)
lst= [ x for x in input("Enter the three values separated by comma:").split(',')]
print(lst)

#Taking multiple input values
lst= [ int(x) for x in input("Enter the three values separated by comma:").split(',')]
print(lst)