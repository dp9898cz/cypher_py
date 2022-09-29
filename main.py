import unicodedata
from math import gcd

from encode import encode
from decode import decode   

ALPH = 'ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789'

def filter(text):
    # remove czech diacritics
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    # convert spaces
    text = text.replace(" ", "XMEZERAX")
    # to uppercase
    text = text.upper()
    # remove additional characters
    text = ''.join(character if character in ALPH else '' for character in text)
    return text

if __name__ == "__main__":
    # get user input
    key_1 = None
    while (key_1 == None):
        u_input = input("Enter key 1: ")
        try:
            key_1 = abs(int(u_input))
            if (key_1 == 0):
                key_1 = None
                print("You cannot choose 0 as key.")
            if (gcd(key_1, len(ALPH)) != 1):
                key_1 = None
                print("Nuber not valid, choose another one.")
        except ValueError:
            print("You must enter only integer number. Try again.")    
    
    key_2 = None
    while (key_2 == None):
        u_input = input("Enter key 2: ")
        try:
            key_2 = abs(int(u_input))
            if (key_2 == 0):
                key_2 = None
                print("You cannot choose 0 as key.")
        except ValueError:
            print("You must enter only integer number. Try again.")            
    
    text = filter(input("Enter text to encode: "))
    
    # encode text
    print("Filtered text: " + text)
    encoded = encode(text, key_1, key_2, ALPH)
    print("Encoded text: " + encoded)
    
    #decode text
    print("DECODED TEXT: " + decode(encoded, key_1, key_2, ALPH))