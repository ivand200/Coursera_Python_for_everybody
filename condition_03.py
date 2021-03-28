# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

hours = int(input("Enter hours:"))
rate = float(input("Enter rate:"))

if hours > 40:
    pay = ((40 * rate) + ((hours - 40) * (rate * 1.5)))
else:
    pay = hours * rate

print("Pay:",pay)

# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

hours = input("Enter hours:")
rate = input("Enter rate:")
try:
    n_hours = int(hours)
    n_rate = float(rate)
    if n_hours > 40:
        pay = ((40 * n_rate) + ((n_hours - 40) * (n_rate * 1.5)))
    else:
        pay = n_hours * n_rate
    print("Pay:",pay)
except:
    print("Error, please enter number!")

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:

num = input("Enter score:")
try:
    score = float(num)
    if score > 1.0 or score < 0.0 :
        print("Enter number from 0.0 up to 1.0")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
except:
    print("Bad score")
