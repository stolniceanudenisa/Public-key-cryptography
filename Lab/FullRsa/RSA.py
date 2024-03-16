import math
import random


class PublicKey:
    def __init__(self, n:int, e: int) -> None:
        self.n = n
        self.e = e

class PrivateKey:
    def __init__(self, n:int, d:int) -> None:
        self.n = n
        self.d = d

class Keys:
    def __init__(self, public_key:PublicKey, private_key:PrivateKey) -> None:
        self.publicKey = public_key
        self.privateKey = private_key


class Rsa:
    ALPHABET = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    NO_LETTERS = len(ALPHABET)

    PLAINTEXT_BLOCK_LENGTH = 2 # k
    CIPHERTEXT_BLOCK_LENGTH = 16 # l
    @staticmethod
    def __get_2_random_close_primes() -> [int, int]:
        file = open("primes.txt", "r")
        line_no = 0
        for line in enumerate(file):
            line_no += 1
        file.close()


        first_prime_line = random.randint(0, line_no - 1 - 2)
        second_prime_line = first_prime_line + 2

        primes_file = open("primes.txt", "r")
        content = primes_file.readlines()

        first_prime = int(content[first_prime_line].removesuffix('\n'))
        second_prime = int(content[second_prime_line].removesuffix('\n'))

        return first_prime, second_prime
    @staticmethod
    def __euler_totient(prime1:int, prime2:int) -> int:
        return (prime1 - 1) * (prime2 - 1)

    @staticmethod
    def __find_valid_e_around_a_point(euler_totient:int, search_around_point: int) -> int:
        # We want an e s.t: 1 < e < euler_totient and gcd(e, euler_totient) = 1
        # We first set e = search_around_point and check if it is coprime with euler_totient
        # If it is then we are done, otherwise we check the point search_around_point + 1
        # If the condition was not fulfilled, we check the point search_around_point - 1
        # We repeat this pattern (+1, -1, +2, -2, +3, -3, .....) until we find the first valid number.
        # That would be e

        distance_to_1 = search_around_point - 1
        distance_to_euler_totient = euler_totient - search_around_point

        # if we would first hit the left bound of 1 < e < euler_totient,
        # interate until we hit 1 while searching for our e
        # if we did not find a valid one, continue searching from search_around_point towars euler_totient only
        # (skipping over the already checked points to the right of search_around_point
        # if we would first hit the right bound, do the reverse

        min_span = min(distance_to_1, distance_to_euler_totient)
        for i in range(min_span):
            e = search_around_point + i
            if math.gcd(e, euler_totient) == 1:
                return e

            e = search_around_point - i
            if math.gcd(e, euler_totient) == 1:
                return e

        if distance_to_1 < distance_to_euler_totient:
            for i in range(distance_to_1, distance_to_euler_totient):
                e = search_around_point + i
                if math.gcd(e, euler_totient) == 1:
                    return e
        else:
            for i in range(distance_to_euler_totient, distance_to_1):
                e = search_around_point - i
                if math.gcd(e, euler_totient) == 1:
                    return e
    @staticmethod
    def __char_to_index(ch:str) -> int:
        if ch != ' ':
            return ord(ch) - ord('A') + 1
        else:
            return 0

    @staticmethod
    def __index_to_char(index: int) -> str:
        return Rsa.ALPHABET[index]


    @staticmethod
    def __block_to_number(plaintext_block) -> int:
        power27 = 1
        result = 0
        for letter in reversed(plaintext_block):
            result += power27 * Rsa.__char_to_index(letter)
            power27 *= Rsa.NO_LETTERS
        return result

    @staticmethod
    def __encrypted_block_number_to_str(encrypted_block, block_len:int) -> str:
        string_block = ""
        for i in range(block_len):
            string_block += Rsa.__index_to_char(encrypted_block % Rsa.NO_LETTERS)
            encrypted_block //= Rsa.NO_LETTERS
        return string_block[::-1]

    @staticmethod
    def generate_keys(seed=None) -> Keys:
        random.seed(seed)

        prime1, prime2 = Rsa.__get_2_random_close_primes()
        n = prime1 * prime2
        euler_totient = Rsa.__euler_totient(prime1, prime2)
        search_around_point = random.randint(2, euler_totient - 1)
        e = Rsa.__find_valid_e_around_a_point(euler_totient, search_around_point)
        public = PublicKey(n, e)

        d = pow(e, -1, euler_totient)
        private = PrivateKey(n, d)
        return Keys(public, private)

    @staticmethod
    def encrypt(plaintext: str, public_key:PublicKey) -> str:
        plaintext = plaintext.upper()

        #append spaces to the end of the word to make its length a multiple of Encryption.PLAINTEXT_BLOCK_LENGTH
        plaintext = plaintext + " " * (len(plaintext) % Rsa.PLAINTEXT_BLOCK_LENGTH)

        #group the characters from the plaintext into equal sized blocks of length = Encryption.PLAINTEXT_BLOCK_LENGTH
        plaintext_blocks = [plaintext[i:i + Rsa.PLAINTEXT_BLOCK_LENGTH]
                            for i in range(0, len(plaintext), Rsa.PLAINTEXT_BLOCK_LENGTH)]

        encoded_blocks = [Rsa.__block_to_number(block) for block in plaintext_blocks]
        encrypted_blocks = [pow(m, public_key.e, public_key.n) for m in encoded_blocks]

        ciphertext = ""
        for block in encrypted_blocks:
            ciphertext +=  Rsa.__encrypted_block_number_to_str(block, Rsa.CIPHERTEXT_BLOCK_LENGTH)

        return ciphertext

    @staticmethod
    def decrypt(ciphertext: str, private_key: PrivateKey) -> str:
        ciphertext_blocks = [ciphertext[i:i + Rsa.CIPHERTEXT_BLOCK_LENGTH]
                            for i in range(0, len(ciphertext), Rsa.CIPHERTEXT_BLOCK_LENGTH)]
        encoded_blocks = [Rsa.__block_to_number(block) for block in ciphertext_blocks]
        decrypted_blocks = [pow(c, private_key.d, private_key.n) for c in encoded_blocks]

        plaintext = ""
        for block in decrypted_blocks:
            plaintext += Rsa.__encrypted_block_number_to_str(block, Rsa.PLAINTEXT_BLOCK_LENGTH)

        return plaintext
