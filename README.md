# Crypto Caesar

This is a simple Python implementation of the Caesar cipher encryption algorithm. It shifts each letter of the plaintext by 3 positions in the alphabet, wrapping around at the end.

## Features

* Implements the Caesar cipher with a fixed shift of 3
* Encodes plaintext into ciphertext using Python’s `str.maketrans` and `translate`
* Works with lowercase letters (`a–z`)

## How to Run

1. Clone or download the repository.
2. Run the script with a plaintext argument:

```bash
python caesar.py "hello"
```

3. The output will be the encoded text:

```
khoor
```

## Notes

* Only lowercase letters are handled; uppercase and non-alphabetic characters remain unchanged.
* You can modify the code to support different shift values or add decryption functionality.
* This is a classic example of substitution ciphers and a great intro to cryptography basics.
