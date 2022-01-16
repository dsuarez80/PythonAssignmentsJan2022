#Assignment 5-1 by Diego Suarez

print("How many BMI values are we calculating today?")
count = int(input())

def calculateBMI(kg, m):
    return kg / m**2

def getWeightGrade(BMI):
    if BMI >= 30:
        return "obese"
    elif BMI < 30 and BMI >= 25:
        return "overweight"
    elif BMI < 25 and BMI >= 18.5:
        return "normal"
    else:
        return "under"

results = []

while(count > 0):
    bodiesData = []
    bodiesData.append(input("Weight(kg) and height(m): ").split())

    for x in bodiesData:
        BMI = calculateBMI(float(x[0]), float(x[1]))
        weightGrade = getWeightGrade(BMI)
        results.append(weightGrade)

    count -= 1

for grade in results:
    print(grade, end = " ")



