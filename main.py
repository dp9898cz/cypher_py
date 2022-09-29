import unicodedata

from encode import encode

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
    key_1 = int(input("Enter key 1: "))
    key_2 = int(input("Enter key 2: "))
    text = filter(input("Enter text to encode: "))
    
    # encode text
    print("Filtered text: " + text)
    encoded = encode(text, key_1, key_2, ALPH)
    print("Encoded text: " + encoded)
    
    #decode text
    #todo