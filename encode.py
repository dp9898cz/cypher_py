"""_summary_ Encode text from user input
"""

def encode(text, key_a, key_b, ALPH):
    output = ''.join(ALPH[((ALPH.find(character) * key_a + key_b) % len(ALPH))] for character in text)
    return " ".join(output[i:i+5] for i in range(0, len(output), 5))

