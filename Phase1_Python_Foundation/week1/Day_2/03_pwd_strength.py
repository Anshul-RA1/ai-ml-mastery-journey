"""
Docstring for AI_ML_MASTERY_JOURNEY.Phase1_Python_Foundation.week1.Day_2.03_pwd_strength
Challenge 3 · Medium
Password Strength Checker
Take a password and score it: 
+1 for length ≥ 8, 
+1 for uppercase letter, 
+1 for lowercase letter, 
+1 for digit, 
+1 for special character (!@#$%^&*). 
Rate: 0-2 = Weak, 
3 = Medium, 
4-5 = Strong.

Use a for loop to check each character
Use string methods: .isupper(), .islower(), .isdigit()
Use the in operator for special characters
Use if/elif/else for the final rating

"""
print("=" * 70)
print("Password Strength Checker")
print("=" * 70)
print()

user_pwd = input("Enter your Password: ").strip()
score = 0
special_char = "!@#$%^&*"


has_upper = False
has_lower = False
has_digit = False
has_sp_char = False

if len(user_pwd) >= 8:
    score += 1
    

for char in user_pwd:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in special_char:
        has_sp_char = True
    
    if has_upper and has_lower and has_digit and has_sp_char:
        break

# Add to score if True
if has_upper: score +=1
if has_lower: score +=1
if has_digit: score +=1
if has_sp_char: score +=1

print(f"The Total score is {score}")
# print(len(user_pwd))


if score <= 2 :
    print("The Password is Weak!! 🫥")
elif score == 3:
    print("The Password is Medium!! ⚠️")
else:
    print("The Password is Strong!! 💪")

print("\nThanks for using Password Strength Checker")
print("=" * 70)

