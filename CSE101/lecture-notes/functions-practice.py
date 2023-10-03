def calculate_factorial(n):
    """
        Calculate the factorial of a non-negative integer.
       :param n: An integer for which factorial needs to be calculated.
       :return: The factorial of 'n'. If 'n' is negative, it returns -999. If 'n' is 0,
                 it returns 1.
       """
    if n < 0:
        return -999
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def doDivision(numerator, denominator):
    """
    This function divides the numerator by the denominator and returns the result.
    If the denominator is 0, the function returns None.
    Parameters: numerator, denominator - both floating point values
    Return: float or None
    """
    #numerator = 15
    #denominator = 5
    if denominator == 0:
        return None
    else:
        return numerator/denominator


def inches_to_centimeters(inches):
    """
    Convert inches to centimeters.

    Params:
        inches (float): A distance in inches to be converted to centimeters.

    Returns:
        float: The equivalent distance in centimeters.

    """
    return inches * 2.54


def check_input(low_limit, high_limit, user_input):
    """
    Check if user input is within a specified range.

    Params:
        low_limit (float): The lower legal limit for the input.
        high_limit (float): The upper legal limit for the input.
        user_input (float): The user's input to be checked.

    Returns:
        bool: True if the user input is within the legal range, False otherwise.

    """
    if low_limit <= user_input <= high_limit:
        return True
    else:
        print(f"Input must be between {low_limit} and {high_limit} inches inclusive.")
        return False





def main():


    ###########################
    n = 5
    result = calculate_factorial(n)
    print(f"{n}! = {result}")


    ###########################

    print(doDivision(12, 5))


    ###########################
    low_limit = 0
    high_limit = 1000

    # Prompt the user for a distance in inches
    inches_distance = float(input("Enter a distance in inches: "))

    # Validate the input
    while not check_input(low_limit, high_limit, inches_distance):
        inches_distance = float(input("Enter a distance in inches: "))

    # Call the conversion function to convert inches to centimeters
    centimeters_distance = inches_to_centimeters(inches_distance)

    # Print the resulting distance in centimeters
    print(f"{inches_distance} inches is equal to {centimeters_distance} centimeters.")

main()