"""
Challenge 5 · Hard
Mini Student Grade Manager
Build a program that lets a teacher enter student names and marks (in a loop). 
When they type "done", stop collecting and display: 
all students sorted by marks, 
class average, 
highest and lowest scorer, 
pass/fail count (passing = 50+).

Use a while loop to keep collecting students until "done"
Store data in two lists: names[] and marks[]
Use for loops to calculate average, find max/min
Use list comprehension for filtering passed students
Format output as a beautiful table with "=" * 70 banner
Handle edge case: what if teacher types "done" immediately?

"""
print("=" * 70)
print("Grade Manager")
print("=" * 70)

# creating list var for names and marks 
names = []
marks = []

while True:
    name_input = input("Enter Student Name of (Type done to Finish): ").strip()

    if name_input.lower() == 'done':
        break

    try:
        mark_input = float(input(f"Enter the marks for {name_input}: "))
        if 0 <= mark_input <= 100:
            names.append(name_input)
            marks.append(mark_input)
        
        else:
            print("❌ Invalid marks! Please Enter Valid Marks value between 0 and 100.")
    
    except ValueError:
        print("❌ Invalid input! Marks must be number")


# Data Processing 

if not names:
    print("\n⚠️ No data collected. The manager is exiting. ")
else:

    # Calculate Stats 
    total_marks = sum(marks)
    count = len(marks)
    avg_marks = total_marks / count

    highest_mark = max(marks)
    lowest_mark = min(marks)

    # Filtering using list comprehension

    passed_student = [m for m in marks if m >= 50]
    pass_count = len(passed_student)
    fail_count = count - pass_count

    # 3. Sorting (Combining lists to sort by marks descending)
    # This creates pairs, sorts them, then unpacks them

    sorted_data = sorted(zip(names, marks), key=lambda x : x[1], reverse=True)

    print("\n" + "=" * 70)
    print(f"{'NAME':<20} | {'MARKS':<10} | {'STATUS':<10}")
    print("-" * 70)

    for name , mark in sorted_data:
        status = "PASS ✅" if mark >= 50 else "FAIL ❌"
        print(f"{name.capitalize():<20} | {mark:<10.2f} | {status:<10}")

    print("=" * 70)
    print(f"Class Average :    {avg_marks:.2f}")
    print(f"Highest Score: {highest_mark:.2f}({names[marks.index(highest_mark)]})")
    print(f"Lowest Score:    {lowest_mark:.2f} ({names[marks.index(lowest_mark)]})")
    print(f"Pass/Fail Count: {pass_count} Passed / {fail_count} Failed")
    print("=" * 70)




