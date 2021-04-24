alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def break_caesar_cipher(ciphertext, known_word):
    plaintext = ''
    for i in range(26):
        candidate=''
        for c in ciphertext:
            if c not in alphabet:
                candidate += c
            else:
                candidate += chr(65+(ord(c)+i)%26)
        if known_word in candidate.lower():
            return candidate.lower()