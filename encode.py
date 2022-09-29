"""_summary_ Encode text from user input
"""

def encode(text, key_a, key_b, ALPH):
    return ''.join(ALPH[((ALPH.find(character) * key_a + key_b) % len(ALPH))] for character in text)

