def dec2bin_comp(value):
    # Verify that the integer is between -128 and +127
    if not -128 <= value <= 127:
        return 'Value out of range'

    # Initialize the binary representation as a list to store '0's or '1's
    bin_digits = ['0'] * 8

    # your code goes here

    # Join the list into a string to get the final binary representation
    return ''.join(bin_digits)


def BinComp2Dec(bin_str):
    # Ensure the binary string is 8 bits long
    if len(bin_str) != 8:
        return "The binary string must be exactly 8 bits long."

    # your code goes here

    # update return value once you insert your code
    decimal_value = 0
    return decimal_value