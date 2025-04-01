def calculateSalary(bonus = 0,deduction = 0):
    return 4000 + bonus - deduction

employee1 = calculateSalary(200 , 100)
employee2 = calculateSalary(100)
employee3 = calculateSalary(0)

print(employee1 , employee2 , employee3)