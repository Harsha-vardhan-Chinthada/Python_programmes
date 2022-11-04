marks = [int(x) for x in input('Enter the marks separated by space: ').split() if int(x) >=35]
if len(marks) < 3 :
    print("You failed in the exam")
else :
    print("You passed in the exam")
    average= sum(marks)/len(marks)
    if average <= 59 :
        print("Your grade is C")
    elif average <= 69 :
        print("Your grade is B")
    else :
        print("Your grade is A")



