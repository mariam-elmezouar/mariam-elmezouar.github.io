

################################# Patterns with nested loops #########################################
def pattern1():
    size = int(input("Give me the size: "))
    for i in range(1, size+1):  # Outer loop for the number of rows (1 to 5)
        for j in range(i):  # Inner loop to print the current row number 'i' times
            print(i, end='')
        print()  # Move to the next line after each row


def pattern2():
    size = int(input("Give me the size: "))
    for i in range(size, 0, -1):  # Outer loop for the number of rows (5 to 1, decrementing)
        for j in range(i, 0, -1):  # Inner loop to print numbers from 'i' to 1
            print(j, end=' ')
        print()  # Move to the next line after each row

def pattern3():
    size = int(input("Give me the size: "))
    for i in range(size, 0, -1):  # Outer loop for the number of rows (5 to 1, decrementing)
        for j in range(size, i - 1, -1):  # Inner loop to print numbers from 5 down to 'i'
            print(j, end=' ')
        print()  # Move to the next line after each row


def pattern4():
    size = int(input("Give me the size: "))
    num = 1  # Initialize the starting number

    for i in range(1, size+1):  # Outer loop for the number of rows (1 to 5)
        for j in range(i):  # Inner loop to print numbers in the current row
            print(num, end=' ')
            num += 1  # Increment the number after printing
        print()  # Move to the next line after each row

def FindLargestDiag(M):
    """

    :param M: The square matrix
    :return: max_pos: the (x,y) coordinate of the largest value in the diagonal
    :return: max_val:  the largest value in the diagonal
    """
    # Ensure that M is a square matrix
    num_rows = len(M)
    num_cols = len(M[0])
    if num_rows != num_cols:
        return "Input matrix is not square."

    # Initialize variables to store the maximum value and its position
    max_val = -1
    max_pos = (-1,-1)

    # Iterate through the diagonal elements
    for i in range(num_rows):
        if max_val == -1  or M[i][i] > max_val:
            max_val = M[i][i]
            max_pos = (i, i)

    return max_pos, max_val



################################# Armstrong Numbers #########################################
# Function to calculate the power of a number
def power(x, y):
    """
    Function to calculate the power of a number
    :param x: first number
    :param y: second number
    :return: x to the power y
    """
    return x ** y
def count_digits(num):
    """
    Function to find the number of digits in a number
    :param num: input
    :return count: the number of digits in num
    """
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


################################# Matrix Diagonal #########################################
def is_armstrong(num):
    """
    Function to check if a number is an Armstrong number
    :param num: input
    :return: True if Amrstrong, False otherwise
    """
    original_num = num
    num_of_digits = count_digits(num)
    sum_of_powers = 0

    while num > 0:
        digit = num % 10
        sum_of_powers += power(digit, num_of_digits)
        num //= 10

    if original_num == sum_of_powers:
        return True
    else:
        return False


def main():
    # run patterns
    pattern1()
    pattern2()
    pattern3()
    pattern4()

    # Run FindLargestDiag()
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    pos, val = FindLargestDiag(M)
    print(f"The largest diagonal element is {val} at position {pos}")

    # Run Armstrong
    # Input from the user
    num = int(input("Enter a number: "))

    # Check if the number is an Armstrong number
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

main()
