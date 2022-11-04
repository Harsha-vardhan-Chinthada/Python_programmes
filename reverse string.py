#Reversing a string by slicing
'''s = input('Enter a string: ')
print(s[::-1])

# Reversing a string manually
s = input('Enter a string: ')
i = len(s)-1
result = ''
while i>= 0  :
    result = result + s[i]
    i-= 1
print(result)'''

# Reversing a string by join method
s = input('Enter a string: ')
print(''.join(reversed(s)))


