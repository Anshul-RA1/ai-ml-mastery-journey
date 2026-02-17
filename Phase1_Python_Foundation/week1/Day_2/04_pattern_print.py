"""
Docstring for AI_ML_MASTERY_JOURNEY.Phase1_Python_Foundation.week1.Day_2.04_pattern_print
Challenge 4 · Medium
Pattern Printer Pro
Print these 3 patterns using nested loops. Each should be 5 rows. 
Ask the user which pattern they want.

Pattern A: Right triangle of stars ( *, **, ***, ****, ***** )
Pattern B: Inverted triangle ( *****, ****, ***, **, * )
Pattern C: Centered pyramid
Use nested for loops and string multiplication

"""

print("=" * 70)
print("Patten Print Pro")
print("=" * 70)

user_choice = input("Choose a Patten : (A, B, C, D) ").upper().strip()
rows = 5

if user_choice == "A":
    print("\n---- Pattern A : Right Triangle -----")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*" , end="")
        print()

elif user_choice == "B":
    print("\n---- Pattern B : Inverted Triangle ----")
    for i in range(rows ,0,-1):
        for j in range(i):
            print("*", end="")
        print()

elif user_choice == "C":
    print("\n---- Pattern C: Centered Pyramid---- ")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(2 * i - 1):
            print("*", end="")
        print()
elif user_choice == "D":
    print("\n---- Additional Pattern ------")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print()
        for l in range(2*i -1, 0, -1):
            print("*", end="")
        print()
else : 
    print("Invalid choices! Please Select A, B , C or D.")

