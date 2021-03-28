# Exercise 4: Find all unique words in a file
# List all unique words, sorted in
# alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result.
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list of unique words.
# If the word is not in the list of unique words, add it to the list. When the program completes,
# sort and print the list of unique words in alphabetical order.

file = input("Enter a file name:")
if len(file) < 1 : file = "romeo.txt"
fhand = open(file, "r")

lst = list()
for row in fhand:
    rows = row.split()
    for words in rows:
        if words in lst:
            continue
        else:
            lst.append(words)

lst.sort()  # lst.sort(reverse=True)
print(lst)

# Exercise 5: Minimalist Email Client. Emails are separated by a special line
# which starts with From (notice the space). Importantly, lines starting with
# From: (notice the colon) describes the email itself and does not act as a
# separator. Imagine you wrote a minimalist email app, that lists the email
# of the senders in the user’s Inbox and counts the number of emails.
# Write a program to read through the mail box data and when you find line
# that starts with “From”, you will split the line into words using
# the split function. We are interested in who sent the message,
# which is the second word on the From line.

file = input("Enter a file name:")
if len(file) < 1 : file = "mbox.txt"
fhand = open(file, "r")

lst = list()
count = 0
for rows in fhand:
    if rows.startswith("From "):
        row = rows.split()
        count = count + 1
        if row[1] in lst:
            continue
        else:
            lst.append(row[1])

print("There were", count, "lines in the doc")

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers
# after the loop completes.

lst = list()
while True:
    score = input("Enter a number:")
    if score == "done":
        break
    try:
        score_ = int(score)
        lst.append(score_)
        print(score_)
    except:
        print("Enter a number plaese!")
print("Maximum:", max(lst), "Minimum:", min(lst))
