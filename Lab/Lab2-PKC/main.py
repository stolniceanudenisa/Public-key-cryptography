# # Euler's Totient function (ϕ) counts the number of positive integers '
# # less than a number that are coprime to that numers.
# # ϕ(n) = |{k ∈ N | k < n and (k, n) = 1}|
#
#
# # Algorithm for computing the value of Euler’s function for natural numbers.
#
# # For a given value v and a given bound b, list all natural numbers less than b
# # which have v as the value of Euler’s function.
#
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# # the number of elements which have v as the value of Euler's function
# def euler_phi(n):
#     result = 0
#     for i in range(1, n + 1):
#         if gcd(n, i) == 1:
#             result += 1
#     return result
#
#
# def find_numbers_with_phi_v(v, b):
#     numbers = []
#     for num in range(2, b):
#         if euler_phi(num) == v:
#             numbers.append(num)
#     return numbers
#
#
# inputs = [(2, 10), (4, 10), (8, 25), (3, 13), (4, 50), (8, 120), (3, 214), (5, 2555), (6, 340), (11, 10000)]
#
# for v, b in inputs:
#     result = find_numbers_with_phi_v(v, b)
#     print()
#     print(f"Numbers < {b} that have φ = {v} are: {result}")
#
#     for num in result:
#         phi_num = euler_phi(num)
#         coprime_numbers = [i for i in range(1, num) if gcd(num, i) == 1]
#         print(f'φ = {phi_num} for {num}')
#         print(f'Coprime numbers with {num}: {", ".join(map(str, coprime_numbers))}')
#         print()
#
# # v = 4
# # b = 10
# #
# # result = find_numbers_with_phi_v(v, b)
# # print(f"Numbers < {b} that have φ = {v} are: {result}")
# #
# # for num in result:
# #     phi_num = euler_phi(num)
# #     coprime_numbers = [i for i in range(1, num) if gcd(num, i) == 1]
# #     print(f'φ = {phi_num} for {num}')
# #     print(f'Coprime numbers with {num}: {", ".join(map(str, coprime_numbers))}')
# #     print()
#
#
# def main():
#     # inputs = [(2, 10)]  # (4, 10)
#     #
#     # for v, b in inputs:
#     #     result = find_numbers_with_phi_v(v, b)
#     #     # print(f"Numbers < {b} with φ(n) = {v}: {result}")
#     # for num in result:
#     #     phi_num = euler_phi(num)
#     #     coprime_numbers = [i for i in range(1, num) if gcd(num, i) == 1]
#     #     print(f'φ = {phi_num} for {num}')
#     #     print(f'Coprime numbers with {num}: {", ".join(map(str, coprime_numbers))}')
#     #     print()
#     pass
#
#
# if __name__ == "__main__":
#     main()


result = (2382 ** 3703) % 4453
print(result)

#
# def mod_inverse(a, m):
#     m0, x0, x1 = m, 0, 1
#
#     while a > 1:
#         q = a // m
#         m, a = a % m, m
#         x0, x1 = x1 - q * x0, x0
#
#     if a == 1:
#         return (x1 + m0) % m0
#     else:
#         return None
#
# result = mod_inverse(7, 4320)
# print(result)
