n= int(input('Enter the number of the employees: '))
Employees = {}
for i in range(n) :
    Name = input('enter the name of the employee: ')
    salary = input('enter the salary of the employee: ')
    Employees[Name] = salary
print('You can get the salary of an employee by entering the Name:')
while True:
    Name = input('enter the name of the employee: ')
    salary = Employees.get(Name, -1)
    if salary == -1 :
        print('Employee does not exist.')
    else :
        print('The salary of the',Name,'is', salary)
    choice = input('Do you want to know the salary of another employee[Yes|No]')
    if choice == 'No' :
        break



