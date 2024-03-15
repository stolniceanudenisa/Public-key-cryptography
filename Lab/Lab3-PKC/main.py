# the simplest factorization algorithm that is substantially faster
# than trial division
# generally used to determine relatively small prime factors


def pollard_rho_factor(n, f, x0=2):
    # d = (| x2j − xj |, n)
    # If 1 < d < n, then STOP and d is a non-trivial factor of n.

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x, y, d = x0, x0, 1
    step = 1

    print(f"Let us factorize n = {n} using f(x) and x0 = {x0}.")

    # At each step, it calculates the difference |x - y|
    # and computes the greatest common divisor (gcd) with n.
    while d == 1:
        x = f(x)
        y = f(y)
        y = f(y)

        diff = abs(x - y)

        # if gcd is not 1, it means a non-trivial factor has been found, and the algorithm stops.
        # The process is repeated until a non-trivial factor is found.
        d = gcd(diff, n)

        print(f"x{step} = f(x{step - 1})  ; x{step + 1} = f(x{step}) = {y};")
        print(f"(|x{step + 1} - x{step // 2 + 1}|, n) = ({diff}, {n}) = {d};")
        print('')
        if d == 1:
            step += 2

    if d == n:
        print(f"No non-trivial factors found for {n} using the given function.")
        return None
    else:
        print(f"Hence a factor of n = {n} is {d} and thus {n} = {d} * {n // d}.")
        return d


# Example usage with a user-defined function f(x) = x^2 + x + 1
# a suitable random polynomial map f (implicitly, f (x) = x^2 + 1).

def user_defined_function(x):
    return (x ** 2 + 1) % n


# Input: an odd composite number n
n = 9983

factor = pollard_rho_factor(n, user_defined_function)
if factor:
    print(f"A non-trivial factor of {n} is: {factor}")








# x = f(x)
# y = f(f(y))
# diff = abs(x - y)


# print(user_defined_function(  5705));

# The number to factorize
# n = 9983  # The number to factorize


# print()
# print()
# print()
# print()
# print()
# number = 6123
# result = sqrt(number)
# whole_part = floor(result)
# print(whole_part)


# print( sqrt(110*110-9699))
# print( sqrt(98*98-6123))
# Output: a non-trivial factor d of n.
