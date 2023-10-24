

start_number = int(input("Give me a starting number: "))

sequence = [start_number]

while start_number != 1:
    if start_number % 2 == 0:
        start_number = start_number // 2
    else:
        start_number = 3 * start_number + 1
    sequence.append(start_number)

print(f"The Syracuse sequence for {start_number} is")
# one way to print the contents of a list using the comma as a separator
# there are multiple other solutions
print(*sequence, sep = ", ")


