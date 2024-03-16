import itertools
import math
from heapq import *
import copy


def least_absolut_residue(x: int, n: int) -> int:
    x_mod_n = x % n
    x_negative_mod_n = n - x_mod_n
    x_negative_mod_n *= -1

    if abs(x_mod_n) < abs(x_negative_mod_n):
        return x_mod_n
    else:
        return x_negative_mod_n


def compute_b_and_b_sqr(n: int, no_iterations: int):
    lst_b = []
    lst_b_sqr = [

    ]
    b_1 = 1
    a0 = math.floor(math.sqrt(n))
    b0 = a0
    b0_sqr = b0 * b0
    b0_sqr = least_absolut_residue(b0_sqr, n)

    x0 = math.sqrt(n) - a0

    lst_b.append(b0)
    lst_b_sqr.append(b0_sqr)

    print(f"a0 = {a0} \t b0 = {b0} \t b0^2 = {b0_sqr} \t x0 = {x0}".expandtabs(18))

    xi_1 = x0
    bi_2 = b_1
    bi_1 = b0

    for i in range(1, no_iterations):
        ai = math.floor(1 / xi_1)
        xi = 1 / xi_1 - ai
        bi = (ai * bi_1 + bi_2) % n

        bi_sqr = (bi * bi) % n
        bi_sqr = least_absolut_residue(bi_sqr, n)

        lst_b.append(bi)
        lst_b_sqr.append(bi_sqr)

        print(f"a{i} = {ai} \t b{i} = {bi} \t b{i}^2 = {bi_sqr} \t x{i} = {xi}".expandtabs(18))

        xi_1 = xi

        bi_2 = bi_1
        bi_1 = bi

    return lst_b, lst_b_sqr


def prime_factors_of_abs_n(n: int):
    n = abs(n)
    factors = []

    if n % 2 == 0:
        factors.append((2, 1))
        n //= 2

    while n % 2 == 0:
        factors[-1] = factors[-1][0], factors[-1][1] + 1
        n = n // 2

    # n must be odd at this point
    stop_at = int(math.sqrt(n)) + 1
    for div in range(3, stop_at, 2):

        if n % div == 0:
            factors.append((div, 1))
            n //= div

        while n % div == 0:
            factors[-1] = factors[-1][0], factors[-1][1] + 1
            n = n // div

    # if n is a prime
    if n > 2:
        factors.append((n, 1))

    return factors


def compute_associated_vectors(B_base, B_numbers_indexes, b_sqr, b_sqr_factors):
    vectors = [[]]
    for index_of_b_sqr in B_numbers_indexes:
        if b_sqr[index_of_b_sqr] < 0:
            vectors[-1].append(1)
        else:
            vectors[-1].append(0)

        for base_element_index in range(1, len(B_base)):
            base_element = B_base[base_element_index]
            factors_of_b_sqr = b_sqr_factors[index_of_b_sqr]

            b_power = -1
            for factor, power in factors_of_b_sqr:
                if factor == base_element:
                    b_power = power
                    break
            if b_power == -1:
                b_power = 0
            vectors[-1].append(b_power)

        vectors.append([])
    vectors.pop()
    return vectors


def find_B_numbers(B_base, b_sqr, b_sqr_factors):
    B_numbers_indexes = []
    for i in range(len(b_sqr)):
        valid = True
        for factor in b_sqr_factors[i]:
            if factor[0] not in B_base:
                valid = False
                break
        if valid:
            B_numbers_indexes.append(i)
    return B_numbers_indexes


def compute_b_vectors_mod_2(b_vectors):
    b_vectors_mod_2 = copy.deepcopy(b_vectors)
    for vector in b_vectors_mod_2:
        for i in range(len(vector)):
            if vector[i] % 2 == 0:
                vector[i] = False
            else:
                vector[i] = True
    return b_vectors_mod_2


def compute_valid_b_vector_sums(b_vectors):
    b_vectors_mod_2 = compute_b_vectors_mod_2(b_vectors)
    elements = []
    b_vectors_combinations = []
    for i in range(len(b_vectors_mod_2)):
        elements.append(i)
    for k in range(1, len(b_vectors_mod_2) + 1):
        combinations = list(itertools.combinations(elements, k))

        zero_list = [False] * len(b_vectors_mod_2[0])
        for combination in combinations:
            res = [False] * len(b_vectors_mod_2[0])
            for comb_index in combination:
                for index in range(len(b_vectors_mod_2[0])):
                    res[index] = res[index] ^ b_vectors_mod_2[comb_index][index]
            if zero_list == res:
                b_vectors_combinations.append(combination)
    return b_vectors_combinations


def compute_c(B_base, b_vectors, b_vectors_combinations, combination_index):
    combinations_old = b_vectors_combinations[combination_index]
    product_c = 1
    for i in range(len(B_base)):
        gamma_i = 0
        for b_vector_index in combinations_old:
            gamma_i += b_vectors[b_vector_index][i]
        gamma_i //= 2
        product_c *= pow(B_base[i], gamma_i)
    return product_c


def compute_b(combination_updated, list_b, n):
    product_b = 1
    for index_b in combination_updated:
        product_b *= list_b[index_b]
        product_b %= n
    return product_b


def continued_fractions(n: int, no_iterations: int):
    list_b, list_b_sqr = compute_b_and_b_sqr(n, no_iterations)
    b_sqr_factors = []

    prime_map = {}
    for number in list_b_sqr:
        factors = prime_factors_of_abs_n(number)
        b_sqr_factors.append(factors)

        for prime in factors:
            old_value = prime_map.get(prime[0])
            if old_value is None:
                old_value = 0
            prime_map[prime[0]] = old_value + 1

    prime_map = dict(sorted(prime_map.items()))

    print(f"The prime factors shown as << Prime: Frequency >> are:\n\t {prime_map}")

    min_k = int(input("Use the first k primes. Input k:\n>>\t"))
    B_base = [-1] + list(prime_map.keys())[0:min_k]

    print(f"B base is: {B_base}")

    B_numbers_indexes = find_B_numbers(B_base, list_b_sqr, b_sqr_factors)

    print(f"All b^2 numbers are: {list_b_sqr}")
    print(f"The indexes of the correct B numbers are: {B_numbers_indexes}")

    b_vectors = compute_associated_vectors(B_base, B_numbers_indexes, list_b_sqr, b_sqr_factors)

    i = 0
    for index_of_b_sqr in B_numbers_indexes:
        print(f"The associated vector of b{index_of_b_sqr} is v{index_of_b_sqr} = {b_vectors[i]}")
        i += 1

    b_vectors_combinations = compute_valid_b_vector_sums(b_vectors)

    b_vectors_combinations_updated = [tuple(map(lambda ele: B_numbers_indexes[ele], combination)) for combination in
                                      b_vectors_combinations]
    print("The valid b vectors sums are:")
    for index in range(len(b_vectors_combinations_updated)):
        print(f"\t {index}. {b_vectors_combinations_updated[index]}")

    combination_index = int(input("Insert the index of the wanted combination:\n>>\t"))
    combination_updated = b_vectors_combinations_updated[combination_index]
    product_b = compute_b(combination_updated, list_b, n)

    print(f"b = {product_b}")

    product_c = compute_c(B_base, b_vectors, b_vectors_combinations, combination_index) % n

    print(f"c = {product_c}")

    if abs(least_absolut_residue(product_c, n)) == abs(least_absolut_residue(product_b, n)):
        print("c == b (mod n), try again with more values")
    else:
        factor1 = math.gcd(product_b + product_c, n)
        factor2 = math.gcd(product_b - product_c, n)
        print(f"n = {factor1} * {factor2} = {factor1 * factor2}")


if __name__ == "__main__":
    continued_fractions(7889, 8)
