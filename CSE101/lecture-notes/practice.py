# Exercise 1: Cigar party
numberCigars = int(input("How many cigars are you planning on bringing? "))
dayOfTheWeek = input("Remind me, what day is it? ")

if (40 <= numberCigars <= 60) and (dayOfTheWeek != "Sunday" and dayOfTheWeek != "Saturday"):
    print("Party On")
elif (dayOfTheWeek == "Sunday" or dayOfTheWeek == "Saturday") and numberCigars >= 40:
    print("Party On")
else:
    print("Lame")

# Exercise 2: Number 6
a = int(input("Give me a number: "))
b = int(input("Give me another number: "))

if (a == 6 or b == 6) or (a + b == 6) or (a - b == 6) or (b - a == 6):
    print("True")

# Exercise 3: Course planning
CSE101 = int(input("Have you taken CSE101? Answer by 1 for Yes and by 0 for No ---- "))
MAE101 = int(input("Have you taken MAE101? Answer by 1 for Yes and by 0 for No ---- "))
EEE243 = int(input("Have you taken EEE243? Answer by 1 for Yes and by 0 for No ---- "))

if CSE101 and MAE101 and not EEE243:
    print("Time to enroll in EEE243 and learn some programming in C.")

# Exercise 4: Letter grade
grade = int(input("What's your assignment grade? "))

if 80 <= grade <= 100:
    print("A")
elif 65 <= grade <= 79.999:
    print("B")
elif 50 <= grade <= 64.999:
    print("C")
elif grade < 50:
    print("F")
else:
    print("Invalid grade")

# Exercise 5: Number generator
for x in range(21, 51):
    print(x)

# Exercise 6: Number generator 2
for x in range(5, 101, 5):
    print(x)

# Exercise 7: Divisors
number = int(input("Enter an integer and I will tell you all its divisors: "))
flag = 0

for x in range(2, number):
    if number % x == 0:
        print(f"{x} is a divisor")
        flag = 1

if flag == 0:
    print(f"{number} is prime")

# Exercise 8: Draw triangle
size = int(input("Enter the size of the triangle base: "))

for x in range(1, size + 1):
    currentRow = ""
    for y in range(1, x + 1):
        currentRow += "* "
    print(currentRow)

# Alternatively, you can use the following for the triangle:
for x in range(1, size + 1):
    for y in range(1, x + 1):
        print("* ", end="")
    print()
