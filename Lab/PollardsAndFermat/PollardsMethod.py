import math
from collections.abc import Callable


def pollards_method(x0: int, funct: Callable[[int], int], n: int, no_iterations: int):
    x = [-1] * (no_iterations + 1)
    x[0] = x0

    is_composite = False
    result1 = -1
    for i in range(1, no_iterations + 1):
        if not is_composite:
            x[i] = funct(x[i - 1]) % n
            print(f"x{i} = {x[i]}\t".expandtabs(15), end=" ")
            if i % 2 == 0:
                a = abs(x[i] - x[i // 2])
                b = n
                gcd = math.gcd(a, b)

                print(f"(|x{i} - x{i // 2}|, n) = {gcd}")

                if gcd != 1:
                    result1 = gcd
                    is_composite = True
        else:
            print(f"x{i} = x\t".expandtabs(15), end=" ")
            if i % 2 == 0:
                print(f"(|x{i} - x{i // 2}|, n) = x")

    factor1 = result1
    factor2 = n // result1

    if factor2 < factor1:
        temp = factor2
        factor2 = factor1
        factor1 = temp

    print(f"\nConclusion:\nThe obtained two factors of n are (in increasing order!) {factor1} and {factor2}")

