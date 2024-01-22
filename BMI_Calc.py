#Group B: Sanaa E(Leader),Due to privacy reasons I can not disclose other members names.

#Program will calculate the BMI and provide tips to attain a healthy BMI
feet = int(input("Enter your height(feet): "))
inches = int(input("Enter your height(inches): "))
weight = float(input("Enter your weight in pounds(lbs): "))

print("Your height is:", feet, "'", inches)
print("Your weight is:", weight)

height = (feet * 12) + inches
BMI = (weight / (height ** 2)) * 703

print("Your BMI is:", BMI)
if BMI <= 0:
   print("Error: Please enter a positive value for height and weight.")
elif BMI <= 18.5:
   print("""You are underweight (18.5 and lower)
   Some tips you could use to achieve a healthier weight are:
   Eat more frequently, choose foods that are rich in nutrients, and exercising.""")
elif BMI <= 25:
   print("""You are at a normal weight (18.5 - 25)
   Some tips you could use to maintain a healthy weight are:
   Exercising more often, staying hydrated, and paying attention to your carb intake.""")
elif BMI <= 30:
   print("""You are overweight (25 - 30)
   Some tips you could use to lose weight are:
   Consume less carbs, eat protein, healthy fats, and vegetables. Exercising is also very important.""")
else:
   print("""You are obese (30 and higher)
   Some tips you could use to lose weight are:
   Consume less carbs, drink water before meals, exercise daily, eat more fibers and healthy foods, try dieting, and so on.""")
