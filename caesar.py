def caesar(plaintext: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[3:] + alphabet[:3]
    mapping = str.maketrans(alphabet, shifted_alphabet)

    ciphertext = plaintext.translate(mapping)
    return ciphertext
  
  caesar(argv[1])
