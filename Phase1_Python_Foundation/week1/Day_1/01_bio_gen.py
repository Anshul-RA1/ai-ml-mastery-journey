"""
Challenge 1 · Easy
Personal Bio Generator
Create variables for your name, age, city, dream role, and target salary. Use f-strings to print a formatted bio. Make it look professional!

Create 5 variables with your personal info
Use f-strings to create a multi-line bio message
Format the salary with comma separators (₹8,50,000)
Print the type of each variable

"""

first_name = "Anshul Raghuvanshi"
age = 32
city = "Frankfurt"
country = "Germany"
dream_role = "GEN AI Engineer"
target_salary = 100000    #in Euros

info = f"""My name is {first_name},
I am {age} years old, I live in {city}, {country},
My dream role is to become {dream_role}, 
My target salary is €{target_salary} 💶"""

print(info)
print(type(info))