import string

alpha = string.ascii_lowercase
digits = string.digits

def caesar_cipher(str, shift):
    """ The Caesar Cipher is a famous and very old cryptography technique. 
        In a simple way, it reorganize all the letter from a sentence based on a shifted alphabet.
        For example, if we choose a right shift of 4, the letter A is replaced by E, B is replaced by F, and so on. 
        When the end of alphabet or decimal numbers is reached, it returns back to the beginning.
    """
    ciphered = ""
    index = 0
    for i in str:
        if i.isalpha():
            low_letter = i.lower()
            index = alpha.find(low_letter)
            index += shift

            if (index > 25):
                index %= 26
                
            elif (index < 0):
                index %= 26
                
            ciphered += alpha[abs(index)]

        elif i.isdecimal():
            index = digits.find(i)
            index += shift
            if index > 9:
                index %= 10
            elif index < 0:
                index %= 10

            ciphered += digits[abs(index)]

        else:
            ciphered += i

    return ciphered
