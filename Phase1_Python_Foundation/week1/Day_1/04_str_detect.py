"""
Challenge 4 · Medium
String Detective
Take a sentence as input and print: total characters, total words, how many vowels, the sentence reversed, 
and the sentence in title case.

Use input() to get a sentence
Use len() for character count
Use .split() to count words
Loop through characters... (if you know loops — if not, count vowels manually)
Use [::-1] to reverse
Use .title() for title casestring for Python_Challenge.Day_1.04_str_detect
"""
print("=" * 70)
print("String Detective 🤖")
print("=" * 70)

user_input = input("Enter the string of your choice : ")
vowels = "aeiouAEIOU"
count = 0

str_detect = f"""
1. String length
2. String Count
3. String Vowels
4. Reverse String
"""
print(f"String detective will return {str_detect} ")

str_character = len(user_input)
str_count = len(user_input.split())
str_reverse = user_input[::-1]
str_title = user_input.title()

for char in user_input:
    if char in vowels:
        count += 1
        # print(f"char : {char} and {count}")

str_calc = f"""
1. The total string characters are {str_character}
2. The total string counts are {str_count}
3. String title is : {str_title}
4. The reverse string : {str_reverse}
5. The number of Vowels in strings are : {count}
"""

print(str_calc)

