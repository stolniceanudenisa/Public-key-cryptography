from RSA import *


if __name__ == '__main__':
    keys = Rsa.generate_keys()
    original = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
    ciphertext = Rsa.encrypt( original, keys.publicKey)
    print(ciphertext)
    plaintext = Rsa.decrypt(ciphertext, keys.privateKey)
    print(plaintext)





