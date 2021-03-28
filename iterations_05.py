#Exercise 1: Write a program which repeatedly reads numbers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except
#and print an error message and skip to the next number.

count = 0
total = 0
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        number = int(num)
        print(number)
        total = total + number
        count = count + 1
    except:
        print("Enter a number please!")

print("Total:", total, "Count:", count, "Average:", (total / count))

#Exercise 2: Write another program that prompts for a list of numbers as above and
#at the end prints out both the maximum and minimum of the numbers instead of the average.

min = None
max = None

while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        number = int(num)
        print(number)
        if min is None or min > number:
            min = number
        if max is None or max < number:
            max = number
    except:
        print("Enter a number please!")

print("Max:", max, "Min:", min)
