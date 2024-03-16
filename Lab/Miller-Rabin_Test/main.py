def compute_decomposition(n: int) -> (int, int):
    n = n - 1
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    t = n
    return s, t
def miller_rabin(n: int, bases: list) -> None:
    if n < 3 or n % 2 == 0:
        print("The given number must be odd and greater than 2")
        return

    s, t = compute_decomposition(n)
    t_bin = bin(t)
    no_bits = len(t_bin) - 2 #0b____

    print("s = ", s)
    print("t = ", t)
    print("t in binary = ", bin(t))

    print()

    print("The powers of 2:")
    for i in range(no_bits):
        power = (2 ** i) % n
        result = (2 ** power) % n
        print(f'\t2^(2^{i}) = {result} (mod {n})')

    print()
    print("Note that if 1 appears once in the result, the following results in the same iteration will always be 1 too")
    print("If either the first number in the sequence is 1 or if one gets the value 1 and its previous number -1, then"
          " n is possible to be prime ")
    print()

    for k in range(len(bases)):
        print(f'Iteration {k + 1} for a = {bases[k]} (results mod {n}):')

        a = bases[k]
        prev_result = (a ** t) % n
        print(f"\t{bases[k]}^(2^{0} * {t}) = {prev_result}")

        composite = False
        for i in range(1, s + 1):
            result = (prev_result ** 2) % n

            optional_msg = ""
            if result == n-1:
                optional_msg = " = -1"
            print(f"\t{bases[k]}^(2^{i} * {t}) = {prev_result} ^ 2 = {result}" + optional_msg)

            if result == 1 and prev_result != 1 and prev_result != n - 1:
                composite = True
                #print("Number is surely composite (not prime), no need for additional tests")
                #print(f"The next {s - (i + 1)} results would all be 1")
                #return


            prev_result = result
        if result != 1 or composite:
            print("Number is surely composite (not prime), no need for additional tests")
            return

        print()

    confidence = 1-1/(4**len(bases))

    print(f"The number may be prime, confidence = {confidence * 100} %")
    return




if __name__ == '__main__':
    #good prime numbers for tests: 104729, 341, 3017, 409
    #25326001 is pseudoprime to 2, 3, 5
    miller_rabin(1369, [2, 3, 5])

