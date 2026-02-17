"""
Challenge 2 · Easy
Salary Calculator
Take monthly salary as input and calculate: yearly salary, tax (30%), take-home pay, and daily earnings.

Use input() to get monthly salary from user
Convert to float
Calculate yearly = monthly × 12
Calculate tax = yearly × 0.30
Calculate take_home = yearly - tax
Calculate daily = take_home / 365
Print everything with ₹ symbol and 2 decimal placesDocstring for Python_Challenge.Day_1.02_salary_calc

"""
print("=" * 70)
print("Welcome to Salary Calculator 🧮")
print("=" * 70)

user_name = input("Enter your name: ").strip().capitalize()
user_monthly_salary = float(input("Enter your monthly salary: "))

user_yearly_salary = user_monthly_salary * 12
tax = user_yearly_salary * 0.30
take_home_salary = user_yearly_salary - tax
user_daily_salary = take_home_salary / 365

salary_calculation = f"""
Hello {user_name}, Your yearly salary is €{user_yearly_salary:,},
and tax is €{tax:,}, your take home salary is €{take_home_salary:,},
and daily salary is €{user_daily_salary:.2f} 
"""

print(salary_calculation)
