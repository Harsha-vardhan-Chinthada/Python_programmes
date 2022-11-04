def BMIcalculate(height,weight):
    HeightinMeters = height*0.4536
    BMI = weight/(HeightinMeters*HeightinMeters)
    return BMI
print(BMIcalculate(5.6,70))