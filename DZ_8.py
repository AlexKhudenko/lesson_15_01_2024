############ DZ_9_01#########################



# def add_one(some_list):
#
#     num = int(''.join(map(str, some_list)))
#     num += 1
#
#     result = [int(digit) for digit in str(num)]
#
#     return result
#
#
# # Перевірка функції
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")





############ DZ_9_02#########################

def find_unique_value(some_list):

    for value in some_list:
        if some_list.count(value) ==1:
            return value

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")