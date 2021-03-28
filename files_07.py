# Exercise 1: Write a program to read through a file and print the contents of
# the file (line by line) all in upper case. Executing the program will look as follows:

file = input("Enter a file name:")
if len(file) < 1 :  file = "mbox-short.txt"
fhand = open(file, "r")

for rows in fhand:
    row = rows.upper()
    print(row)

file = input("Enter a file name:")
if len(file) < 1 : file = "mbox-short.txt"
fhand = open(file, "r")

total = 0
count = 0
for rows in fhand:
    if rows.startswith("X-DSPAM-Confidence:"):  # if not line.startswith("X-DSPAM-Confidence:") : continue
        row = rows.find(":")
        num = rows[row+1 : ]
        numb = num.strip()
        number = float(numb)
        count = count + 1
        total = total + number
print("Average:", (total / count))


file = input("Enter a file name:")
if file == "blabla":
    print("You have been punk'd!")
else:
    fhand = open(file)
    for rows in fhand:
        row = rows.lower()
        print(row)



    #if len(file) < 1 : file = "mbox-short.txt"
