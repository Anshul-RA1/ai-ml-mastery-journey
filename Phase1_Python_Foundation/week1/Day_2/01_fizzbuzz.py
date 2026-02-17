"""
Challenge 1 · Easy
FizzBuzz — The Classic Interview Question
Print numbers from 1 to 50. But: if divisible by 3, print "Fizz". If divisible by 5, 
print "Buzz". 
If divisible by both, print "FizzBuzz". 
Otherwise print the number.

Use a for loop with range(1, 51)
Check divisible by BOTH 3 and 5 first (order matters!)
Then check 3, then 5, then else
Format output nicely

"""

print("=" * 70)
print("Fizz Buzz")
print("=" * 70)

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

print("=" * 70)