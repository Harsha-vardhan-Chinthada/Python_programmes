'''grades = []

subjects = ['Math', 'Physics', 'Chemistry']



for subject in subjects:

    grade = float(input(f'Please enter the grade for the {subject} exam:  '))

    grades.append(grade)



failed = [subject for subject, grade in zip(subjects, grades) if grade < 35]



if failed:

    print('You failed the following subject(s): ', ', '.join(failed ))

else:

    avg = sum(grades)/3

    if avg <= 59:

        print('Your final grade is C')

    elif avg <= 69:

        print('Your final grade is B')

    else:

        print('Your final grade is A')  '''
marks = [int(x) for x in input('Enter your marks separated by space: ').split() if int(x) >= 35]

if len(marks) < 3:
    print("Failed Exam")
else:
    print("Passed Exam!")
    average = sum(marks) / len(marks)
    if average <= 59:
        print('Grade is C')
    elif average <= 69:
        print('Grade is B')
    else:  # shadow case when average > 69
        print('Grade is A')