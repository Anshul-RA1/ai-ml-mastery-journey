"""
Challenge 3 · Medium
BMI Calculator
Ask for weight (kg) and height (meters). Calculate BMI = weight / height². Classify as underweight, normal, overweight, or obese.

Get weight and height using input()
Calculate BMI using the formula
Print BMI rounded to 1 decimal place
Print the category (you'll learn if/else on Day 2 — for now, just print the BMI)Docstring for Python_Challenge.Day_1.03_bmi_calc

"""
print("=" * 70)
print("Welcome to BMI Calculator")
print("=" * 70)

user_weight = float(input("Enter your Weight in KG: "))
user_height = float(input("Enter your height in Meters: "))

BMI = user_weight / (user_height ** 2)

print(f"Your BMI is {BMI:.1f}")

if BMI < 18.5:
    print("Category : UnderWeight")
elif 18.5 <= BMI < 25:
    print("Category : Normal Weight")
elif 25 <= BMI < 30:
    print("Category : Over Weight")
else:
    print("Category : Obesity")
