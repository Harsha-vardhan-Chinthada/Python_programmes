students= {'john':['physics','maths','english'], 'sean':['hindi','telugu','maths'],'brendon':['social','computers','anotomy']}
keys = students.keys()
for eachkey in keys:
    print("Courses taken by", eachkey,"are:")
    for eachCourse in students[eachkey]:
        print(eachCourse)

