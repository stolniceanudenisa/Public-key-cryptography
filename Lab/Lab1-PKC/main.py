import timeit


# the GCD of two numbers remains the same even if
# you replace one of the numbers with its remainder
# when divided by the other number.

# (2, 4)
# a=2
# b=4

# 2 % 4 = 2(Remainder)
# a = 4
# b = 2(Remainder)

# 4 % 2= 0
# a=2
# b=0

def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# the method repeatedly subtracts the smaller number from
# the larger number until both numbers are equal, at which point they represent the GCD.
# 2 is not equal to 4
# a=2
# b=4-2=2
#
# a=b -> gdc=2

def gcd_substractions(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    # base case
    if a == b:
        return a

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# It takes advantage of the fact that if two numbers share common factors, those factors will be reflected in their
# binary representations as trailing zeros (power of 2 factors). By removing these trailing zeros iteratively,
# it quickly finds the GCD.
# the number of trailing zeros = the number of times you can divide a number by 2 without getting a remainder


# For a = 8, a_twos becomes 3 because it takes 3 shifts to make a odd.
# For b = 4, b_twos becomes 2 because it takes two shifts to make b odd.

# For 8, there are 3 trailing zeros (since 8 is divisible by 2 three times).
# 8/2=4
# 4/2=2
# 2/2=1

# For 4, there are 2 trailing zeros (since 4 is divisible by 2 two times).
# 4/2=2
# 2/2=1

# Since 8 has more trailing zeros than 4, we use 4 as 'a' and 8 as 'b'.

# While 4 is not equal to 8, we check which number is greater.
# 8 is greater than 4. So, we swap the values of 'a' and 'b', making 'a' equal to 4 and 'b' equal to

# a=4
# b=8

# b - a = 8 - 4 = 4
# While 4 has trailing zeros (it's even), we keep dividing it by 2:
# 4/2=2
# 2/2=1

# 4 >> 1 = 2

# a=4
# b=2

# .
# .
# .
# (8,4) = 4


# this algorithm works based on the properties of binary representation and basic arithmetic operations.
def gcd_binary_stein(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    a_twos = 0
    while (a & 1) == 0:  # the least significant bit of 'a' is 0
        a >>= 1  # Right shift 'a' by 1 (equivalent to dividing by 2)
        a_twos += 1

    b_twos = 0
    while (b & 1) == 0:  # (True if b-even ->LSB = 0, False if b-odd ->LSB = 1)
        b >>= 1
        b_twos += 1

    while a != b:
        if a > b:
            a, b = b, a
        b -= a

        while (b & 1) == 0:
            b >>= 1

    return a << min(a_twos, b_twos)


# The list of input pairs
inputs = [(0, 4), (0, 745), (22, 0), (1234, 82), (100, 240), (3667, 60), (12, 187538), (144, 288), (4287, 14), (1752220,152400)]

gcd_functions = [gcd_euclidean, gcd_substractions, gcd_binary_stein]

# Measure the execution time for each algorithm on each input pair
for gcd_func in gcd_functions:
    print(f"Testing {gcd_func.__name__}...")

    for a, b in inputs:
        time = timeit.timeit(lambda: gcd_func(a, b), number=100)  # number=100 for more accurate time
        print(f"Pair ({a}, {b}): {time:.6f} seconds")
        print(gcd_func(a, b))

    avg_time = sum(timeit.timeit(lambda: gcd_func(a, b), number=100) for a, b in inputs) / len(inputs)
    print(f"Average time: {avg_time:.6f} seconds")
    print()
    print()
