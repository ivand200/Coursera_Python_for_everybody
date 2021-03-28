#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
        return pay
    else:
        pay = hours * rate
        return pay

try:
    hour = int(input("Enter hours:"))
    r = float(input("Enter rate:"))
    print(computepay(hour, r))
except:
    print("Enter a number pls!")

#Exercise 7: Rewrite the grade program from the previous chapter using a function
#called computegrade that takes a score as its parameter and returns a grade as a string.

def coputegrade(score):
    try:
        score = float(score)
        if score >= 1.0 or score <= 0:
            return "Enter a number between 0 and 1.0"
        elif score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
    except:
        return "Enter number please!"



score_raw = input("Enter a score: ")
print(coputegrade(score_raw))
