def caesar_encrypt(text, shift):
    encrypted_text = ""
    # Your code here
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    # caesar_decrypt is simply caesar_encrypt with a revered shift
    return caesar_encrypt(encrypted_text, -shift)

# This odd looking line is here for a reason: it ensures that the test code runs only when the script is executed
# directly (i.e., when you run caesar_cipher.py itself),
# and not when functions from it are imported into another script (like file_cipher.py).
if __name__ == "__main__":
    # Test cases
    original_text = "Hello, World!"
    shift_value = 3
    encoded_text = caesar_encrypt(original_text, shift_value)
    print("Encoded:", encoded_text)  # Output: "Khoor, Zruog!"

    decoded_text = caesar_decrypt(encoded_text, shift_value)
    print("Decoded:", decoded_text)  # Output: "Hello, World!"

    # INCLUDE MORE TEST CASES HERE


