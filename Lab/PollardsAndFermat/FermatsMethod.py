import math


def fermats_method(n: int, no_iterations: int):
    t = math.isqrt(n)

    print(f"Initialization:\nt0 = [sqrt(n)] = {t}")
    is_perfect_square = False

    s_res = -1
    t_res = -1
    print("\nIterations:")
    for i in range(1, no_iterations + 1):
        t = t + 1
        s_sqr = t * t - n

        if not is_perfect_square:
            print(f"t := t0 + {i};\t t^2 - n = {s_sqr}\t perfect quare (yes/no)".expandtabs(18), end=" ")
        else:
            print(f"t := t0 + {i};\t t^2 - n = x\t perfect quare (yes/no)".expandtabs(18), end=" ")

        s = math.isqrt(s_sqr)
        if is_perfect_square:
            print("x")
        elif s * s == s_sqr:
            print("Yes")
            is_perfect_square = True
            s_res = s
            t_res = t
        elif not is_perfect_square:
            print("No")

    print(f"\nValues:\ns = {s_res}\t t = {t_res}")

    if t_res == -1 and s_res == -1:
        print(f"{n} is a prime number!")
        factor1 = 1
        factor2 = n
    else:
        factor1 = t_res - s_res
        factor2 = t_res + s_res

        if factor2 < factor1:
            temp = factor2
            factor2 = factor1
            factor1 = temp

    print(f"\nConclusion:\nThe obtained two factors of n are (in increasing order!) {factor1} and {factor2}")