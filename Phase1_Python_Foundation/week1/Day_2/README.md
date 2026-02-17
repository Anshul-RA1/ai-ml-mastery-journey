# Day 2 — Conditionals, Loops & Control Flow

> Phase 1 · Week 1 · AI/ML Mastery Journey  
> **Author:** Anshul Raghuvanshi  
> **Date:** February 2026

---

## What I Learned

- **Conditionals:** `if`, `elif`, `else` — making decisions in code
- **Ternary Operator:** One-line conditional expressions for clean assignments
- **for Loops:** Iterating over lists, strings, and `range()` with `enumerate()`
- **while Loops:** Repeating until a condition changes — input validation, game loops
- **Loop Control:** `break` (exit loop), `continue` (skip iteration), `pass` (placeholder)
- **Nested Structures:** Loops inside loops, conditionals inside loops
- **List Comprehension:** Pythonic one-liner for building filtered lists
- **Error Handling:** `try/except` for catching invalid user input
- **Software Testing:** Functional, Boundary, Negative, and Integration testing

---

## Challenges Completed

| # | Challenge | Difficulty | Key Concepts | Lines |
|---|-----------|:----------:|--------------|:-----:|
| 1 | FizzBuzz | Easy | for loop, modulus (%), if/elif/else | ~20 |
| 2 | Number Guessing Game | Easy | while loop, random, try/except, break, dynamic hints | ~55 |
| 3 | Password Strength Checker | Medium | for loop, .isupper(), .islower(), .isdigit(), boolean flags | ~45 |
| 4 | Pattern Printer Pro | Medium | Nested for loops, string multiplication, range() with step | ~35 |
| 5 | Mini Student Grade Manager | Hard | while + break, parallel lists, sorted(), zip(), lambda, list comprehension | ~70 |
| 6 | ATM Simulator (Bonus) | Hard | while True, try/except, input validation, transaction history, menu system | ~75 |

---

## Challenge Details

### C1 — FizzBuzz (The Classic Interview Question)
Print numbers 1-50 with substitutions: divisible by 3 → "Fizz", by 5 → "Buzz", by both → "FizzBuzz".  
**Key takeaway:** Condition ORDER matters — check the most specific condition (both 3 and 5) first.

### C2 — Number Guessing Game
Computer picks a random number (1-100). User guesses with feedback ("Too high" / "Too low"). Limited to 7 attempts with a dynamic hint system that narrows the range after each guess.  
**Key takeaway:** `while` loops are ideal when you don't know how many iterations are needed.

### C3 — Password Strength Checker
Scores a password on 5 criteria: length ≥ 8, uppercase, lowercase, digit, special character. Rates as Weak (0-2), Medium (3), or Strong (4-5).  
**Key takeaway:** Boolean flag pattern — collect flags in a loop, then score after.

### C4 — Pattern Printer Pro
Prints 3 patterns using nested loops: right triangle, inverted triangle, and centered pyramid. User selects which pattern to display.  
**Key takeaway:** Every pattern = a formula for spaces + a formula for stars per row. Pyramid uses `2*i - 1` for odd-number star counts.

### C5 — Mini Student Grade Manager
Collects student names and marks in a loop until "done". Displays: sorted table (descending), class average, highest/lowest scorer with name lookup, pass/fail count.  
**Key takeaway:** Parallel lists + `zip()` + `sorted()` with `lambda` for real-world data processing.

### C6 — ATM Simulator (Bonus)
Full ATM with €10,000 starting balance. Features: check balance, deposit, withdraw, exit with transaction history. Validates all inputs: negative amounts, insufficient funds, non-numeric input.  
**Key takeaway:** Combining `while True`, `try/except`, input validation, and list-based history tracking into a complete interactive application.

---

## Testing

The ATM Simulator (C6) includes a full test report (`ATM_Test_Report.html`) with:

- **24 test cases** across 6 categories
- **4 testing types:** Functional, Boundary, Negative, Integration
- **Result:** 24/24 passed | 0 bugs remaining

---

## File Structure

```
day2-conditionals-loops/
├── 01_fizzbuzz.py              # Classic interview question
├── 02_guess_num.py             # Number guessing game with hints
├── 03_pwd_strength.py          # Password strength checker
├── 04_pattern_print.py         # 3 patterns with nested loops
├── 05_mini_std_grd_mng.py      # Student grade manager
├── 06_atm_simulator.py         # ATM with full validation
├── ATM_Test_Report.html        # 24 test cases — all passed
└── README.md                   # This file
```

---

## Key Python Concepts Used

```python
# Conditionals
if x > 10:        ...
elif x > 5:       ...
else:              ...

# Ternary
status = "PASS" if mark >= 50 else "FAIL"

# for loop with range
for i in range(1, 51):

# while loop with break
while True:
    if done: break

# Loop control
break       # exit loop entirely
continue    # skip to next iteration

# List comprehension
passed = [m for m in marks if m >= 50]

# Sorting with lambda
sorted(zip(names, marks), key=lambda x: x[1], reverse=True)

# Error handling
try:
    value = float(input("Enter: "))
except ValueError:
    print("Invalid!")
    continue
```

---

## How to Run

```bash
# Navigate to the folder
cd phase1-python-foundations/week1/day2-conditionals-loops/

# Run any challenge
python 01_fizzbuzz.py
python 02_guess_num.py
python 06_atm_simulator.py
```

---

*Part of my 9-month AI/ML Mastery Journey — from Python basics to GenAI/LLMs.*  
*Day 2 of 280. The streak continues.* 🔥
