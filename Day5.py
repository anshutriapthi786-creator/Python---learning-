# Day 5 - While Loop and Function

# 1. While loop - 1 to 5 print
print("While Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Sum of first 10 numbers
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"\nSum of 1 to 10 = {total}")

# 3. Function - Simple Calculator
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
print(f"Addition = {add(x, y)}")
print(f"Multiplication = {multiply(x, y)}")
