# Day 4 - Loops and Number Check

# 1. Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 2. Print numbers from 1 to 10 using loop
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# 3. Table of any number
n = int(input("\nEnter number for table: "))
print(f"Table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
