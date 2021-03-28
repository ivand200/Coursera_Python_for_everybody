#Exercise 2: Write a program that categorizes each mail message by which day of
#the week the commit was done. To do this look for lines that start with “From”,
#then look for the third word and keep a running count of each of the days of
#the week. At the end of the program print out the contents of your dictionary
#(order does not matter).
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#python dow.py
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

file = input("Enter a file name:")
if len(file) < 1 : file = "mbox-short.txt"
fhand = open(file, "r")

# V1
lst = list()
counts = dict()
for item in fhand:
    if item.startswith("From "):
        days = item.split()
        counts[days[2]] = counts.get(days[2], 0) + 1

for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(counts)
print(lst)

# V2
lst = list()
counts = dict()
for item in fhand:
    if item.startswith("From "):
        days = item.split()
        if days[2] not in counts:
            counts[days[2]] = 1
        else:
            counts[days[2]] = counts[days[2]] + 1
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(counts)
print(lst)

#Exercise 3: Write a program to read through a mail log, build a histogram using
#a dictionary to count how many messages have come from each email address, and
#print the dictionary.

counts = dict()
lst = list()
file = input("Enter a file name:")
if len(file) < 1 : file = "mbox-short.txt"
fhand = open(file, "r")

for item in fhand:
    if item.startswith("From "):
        items = item.split()
        counts[items[1]] = counts.get(items[1], 0) + 1

for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
print(counts)
print(lst)

# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary
# has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages
#and print how many messages the person has.

counts = dict()
lst = list()
file = input("Enter a file name:")
if len(file) < 1 : file = "mbox-short.txt"
fhand = open(file, "r")

largest = None
mail = None
for item in fhand:
    if item.startswith("From "):
        items = item.split()
        counts[items[1]] = counts.get(items[1], 0) + 1

for key, val in counts.items():
    if largest is None or val > largest:
        largest = val
        mail = key

print(mail ,largest)

for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
print(counts)
print(lst[0])

# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from
# (i.e., the whole email address). At the end of the program,
# print out the contents of your dictionary.

file = input("Enter a file name:")
if len(file) < 1 : file = "mbox-short.txt"
fhand = open(file, "r")

counts = dict()
for lines in fhand:
    if lines.startswith("From "):
        line = lines.split()
        mail = line[1]
        #dom = mail.find("@")
        #domain = mail[dom:]
        #domain_ = domain.strip()
        #counts[domain_] = counts.get(domain_, 0) + 1
        mail_split = mail.split("@")
        domain = mail_split[1]
        counts[domain] = counts.get(domain, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
print(lst)
