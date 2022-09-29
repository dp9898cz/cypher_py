from math import gcd

def inverseKey(key_a, length):
    for i in range(1, length):
        if ((key_a % length) * (i % length)) % length == 1:
            return i 

def decode(text, key_a, key_b, ALPH):
    text = text.replace(" ", "")
    inverse_key = inverseKey(key_a, len(ALPH))
    return ''.join(ALPH[(ALPH.find(character) - key_b) * inverse_key % len(ALPH)] for character in text).replace("XMEZERAX", " ")