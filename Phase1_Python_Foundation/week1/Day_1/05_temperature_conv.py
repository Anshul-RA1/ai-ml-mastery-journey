"""
Challenge 5 · Hard
Temperature Converter Pro
Build a temperature converter that takes a value and the unit (C, F, or K) and 
converts to all other units.

Get temperature value and unit from user
C → F: (C × 9/5) + 32
C → K: C + 273.15
F → C: (F - 32) × 5/9
Display all conversions formatted to 2 decimal places
Handle the unit with .upper() so both "c" and "C" work

"""

print("=" * 70)
print("Temperature Converter PRO 🤖")
print("=" * 70)

user_input = float(input("Enter the Temperature value "))
user_unit = input("Enter the Unit (C,F or K):").upper().strip()

#initialize variables 
temp_in_C = 0
temp_in_F = 0
temp_in_K = 0

if user_unit == 'C':
    temp_in_C = user_input
    temp_in_F = (user_input * 9/5) + 32
    temp_in_K = user_input + 273.15

elif user_unit == 'F':
    temp_in_F = user_input
    temp_in_C = (user_input - 32) * 5/9
    temp_in_K = temp_in_C + 273.15

elif user_unit == 'K':
    temp_in_K = user_input
    temp_in_C = user_input -  273.15
    temp_in_F = (temp_in_C * 9/5) + 32

else:
    print("Invalid Unit! Please use C, F or K.")


overall_temp = f"""
A. The Temperature value is {user_input} {user_unit}
1. The temperature in F is {temp_in_F:.2f}° F
2. The temperature in K is {temp_in_K:.2f} K
3. The temperature in C is {temp_in_C:.1f}° C
"""


print(overall_temp)