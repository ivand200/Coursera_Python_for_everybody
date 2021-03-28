# Exercise 3: Write a program to prompt the user for hours and rate per hour to
# compute gross pay.

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = hours * rate
print("Pay: ", round(pay, 2))

# Exercise 4: Assume that we execute the following assignment statements:

width = 17
height = 12.0

quotient = width // 2
division = width / 2.0
h_division = height / 3
sum = 1 + 2 * 5
print("Quotient:",quotient, "Division:",division, "Height division:",h_division, "Sum:",sum)


# Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = int(input("Enter Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Fahrenheit:",fahrenheit)
