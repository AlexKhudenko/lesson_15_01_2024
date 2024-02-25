############## zavdanie 11.1 ###############

# def prime_generator(end):
#     for num in range(2, end + 1):
#         for i in range(2, int(num ** 0.5) + 1):  # Проверяемо простое число или нет
#             if num % i == 0:
#                 break
#         else:
#             yield num
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')



############## zavdanie 11.2 ###############


def is_even(number):
    return (number & 1) == 0  # Возращаем number число 1 если последний бит равняется не парному.

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
