import math


def char_to_value(c: str) -> int:
    if c == ' ' or c == '_':
        return 0
    else:
        return ord(c.upper()) - ord('A') + 1


def value_to_char(v: int) -> str:
    if v == 0:
        return '_'
    else:
        return chr(v + ord('A') - 1);


def specialized_eulers_totient(n: int) -> int:
    # we know that n is composed of 2 primes p, q. As such the totient function of n
    # is phi(n) = (p-1)(q-1)
    p = 0
    q = 0
    for d in range(2, n):
        if n % d == 0:
            p = d
            q = n // d
    return (p - 1) * (q - 1)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

    return True


def find_smallest_e(phi_n: int) -> int:
    for e in range(3, phi_n):
        if math.gcd(e, phi_n) == 1 and is_prime(e):
            return e
    return -1


# k = no of letters in a plaintext block
def divide_plaintext_message(text: str, k: int) -> list:
    needed_no_spaces = len(text) % k
    text += " " * needed_no_spaces

    result = []
    no_blocks = len(text) // k

    for i in range(no_blocks):
        result += [[]]
        for j in range(k):
            result[i] += text[0]
            text = text[1:]

    return result


def encode_plaintext_blocks(plaintext_blocks: list) -> list:
    result = []
    for block in plaintext_blocks:
        power27 = 1
        number = 0
        for letter in reversed(block):
            number += power27 * char_to_value(letter)
            power27 *= 27
        result.append(number)
    return result


def encrypt_encoded_blocks(encoded_blocks: list, n: int, e: int) -> list:
    result = []
    for number in encoded_blocks:
        result.append(number ** e % n)
    return result


def divide_ciphertext_blocks(encrypted_blocks: list, block_length) -> list:
    result = []
    for number in encrypted_blocks:
        result += [[]]
        for i in range(block_length):
            result[-1].append(number % 27)
            number //= 27
        result[-1].reverse()

    return result

def decode_ciphertext_blocks(divided_ciphertext_blocks: list) -> list:
    result = []
    for block in divided_ciphertext_blocks:
        result += [[]]
        for number in block:
            result[-1].append(value_to_char(number))

    return result
def convert_decoded_ciphertext_to_string(decoded_ciphertext: list):
    result = ""
    for block in decoded_ciphertext:
        for char in block:
            result += char
    return result


def encode_rsa(plaintext: str, k: int, l: int, p: int, q: int):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_smallest_e(phi)

    print("Solution.\n")

    print("Values:")
    print(f"n={n} phi(n)={phi} e={e}\n")

    print("Plaintext:")

    plaintext_blocks = divide_plaintext_message(plaintext, k)
    blocks_plain_str = "Blocks of k letters:"
    for block in plaintext_blocks:
        blocks_plain_str += " "
        for letter in block:
            blocks_plain_str += letter
    print(blocks_plain_str)

    encoded_blocks = encode_plaintext_blocks(plaintext_blocks)
    numerical_equiv_str = "Numerical equivalents:"
    for i in range(len(encoded_blocks)):
        numerical_equiv_str += f" b{i+1} = {encoded_blocks[i]}"
    print(numerical_equiv_str)
    print("")
    print("Encryption:")
    encrypted_blocks = encrypt_encoded_blocks(encoded_blocks, n, e)
    encryption_str = ""
    for i in range(len(encrypted_blocks)):
        encryption_str += f"c{i+1} = b{i+1}^e mod n = {encrypted_blocks[i]} "
    print(encryption_str)

    expanded_ciphertext_blocks = divide_ciphertext_blocks(encrypted_blocks, 3)
    decoded_ciphertext = decode_ciphertext_blocks(expanded_ciphertext_blocks)
    blocks_cipher_str = "Blocks of l letters:"
    for block in decoded_ciphertext:
        blocks_cipher_str += " "

        for letter in block:
            blocks_cipher_str += letter
    print(blocks_cipher_str)
    print()

    final_ciphertext = convert_decoded_ciphertext_to_string(decoded_ciphertext)
    print(f"Ciphertext: {final_ciphertext}")

if __name__ == '__main__':
    #encode_rsa("DAKAR_", 2, 3, 41, 67)



    ciphertext = "BRYBQI_PW"
    k = 2
    l = 3
    p = 43
    q = 47
    n = p * q
    phi = (p-1)*(q-1)
    e = find_smallest_e(phi) # 5
    print(f"n = {p*q}, phi = {phi}, e = {e}")
    d = 773
    ciphertext_blocks = divide_plaintext_message(ciphertext, l)
    print(ciphertext_blocks)


    encoded_cipher = encode_plaintext_blocks(ciphertext_blocks)
    print(f"Numerical equiv: {encoded_cipher}")

    result = []
    for element in encoded_cipher:
        result.append( element**d % n)
    print(f"b1 = c1^d mod n.... {result}")

    result = divide_ciphertext_blocks(result, k);
    for block in result:
        for letter in block:
            print(value_to_char(letter), end='')
        print(end=' ')




1