# Day 3 - Pass / Fail and Positive / Negative Checker
print("This is the result page")
marks = int(input("Enter your marks:- "))
if marks >= 33:
    print("Pass")
else:
    print("Sorry you are fail")

num = int(input("the number is positive or negative:- "))
if num > 0:
    print(f"Your number is positive: {num}")
elif num < 0:
    print(f"Your number is negative: {num}")
else:
    print("Sorry your number is zero")
