from string import ascii_lowercase, digits


def handle_letter(char, shift):
    """
    Helper function for Caesar Cipher. Handles the case the character is a letter.

    Args:
        char: length-one string, letter character
        shift: shift value of caesar cipher

    Returns:
        new letter that should be placed in cryptographed message
    """
    orig_num_value = ascii_lowercase.find(char)
    new_value = (orig_num_value + shift) % 26
    return ascii_lowercase[new_value]


def handle_number(char, shift):
    """
    Helper function for Caesar Cipher. Handles the case the character is a number.

    Args:
        char: length-one string, number character
        shift: shift value of caesar cipher

    Returns:
        new number (as str) that should be placed in cryptographed message
    """
    orig_num_value = int(char)
    new_value = (orig_num_value + shift) % 10
    return str(new_value)


def caesar_cipher(msg, shift):
    """
    Implements a simple Caesar Cipher on string with shift value shift. Uses
    English alphabet, 0-9 digits, punctuation unchanged.

    Args:
        msg: message to be "cryptographed"
        shift: integer shift value

    Returns:
        cryptographed message through Caesar Cipher with shift value shift
    """
    msg = msg.lower()  # passar string para minúsculas
    out = ""

    for char in msg:
        if char in ascii_lowercase:
            out += handle_letter(char, shift)
        elif char in digits:
            out += handle_number(char, shift)
        else:
            out += char

    return out
