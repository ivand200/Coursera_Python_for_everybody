# Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

char = str.find(":")
#num = str[19:-1]
num = str[char+1 : ]
numb = num.strip()
number = float(numb)
print(number)
