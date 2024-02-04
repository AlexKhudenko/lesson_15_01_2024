# my_list = [9, 6, 10, 0, 12, 11, 0, 8, 0]
#
# second_list = []
# zero = my_list.count(0)
# for index in range(len(my_list)):
#     if my_list[index] != 0:
#         second_list.append(my_list[index])
# second_list.extend([0] * zero)
# print(second_list)


######## DZ_4_2 #########

my_list = [0, 1, 7, 2, 4, 8]
result = 0

if my_list:
    for i in range(0, len(my_list), 2):
        result += my_list[i]

    result = result * my_list[-1]
print(result)

