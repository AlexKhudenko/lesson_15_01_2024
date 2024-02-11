# ######## Задание №1
# #Завдання №1 (а)
#
# people = [
#     {"name": "John", "age": 15},
#     {"name": "Alex", "age": 27},
#     {"name": "Mark", "age": 23},
#     {"name": "Alena", "age": 23},
# ]
#
# # min_age = min(person["age"] for person in people)
# #
# # youngest_names = [person["name"] for person in people if person["age"] == min_age]
# #
# # print("Youngest name(s):", youngest_names)
#
# ###або через if в одну строку фстронга с вивiдом в принт (як на прикладі 5-6 уроку)
#
# print("Youngest name(s):", [person["name"] for person in people if person["age"] == min(person["age"] for person in people)])

######## Завдання №1 (б)


# people = [
#     {"name": "John", "age": 15},
#     {"name": "Alex", "age": 27},
#     {"name": "Mark", "age": 23},
#     {"name": "Alena", "age": 23},
# ]
#
#
# names = [person["name"] for person in people]
#
# max_length = max(len(name) for name in names)
#
# longest_names = [name for name in names if len(name) == max_length]
#
# print("Longest name(s):", longest_names)
#

########### Завдання №1 (в) #################################

# people = [
#     {"name": "John", "age": 15},
#     {"name": "Alex", "age": 27},
#     {"name": "Mark", "age": 23},
#     {"name": "Alena", "age": 23},
# ]
#
# total_age = sum(person["age"] for person in people)
#
# number_of_people = len(people)
#
# average_age = int(total_age / number_of_people)
#
# print("Average age:", average_age)







############################## Завдання №2 (а) #######################3

# my_dict_1 = {"a": 7, "b": 2, "c": 3}
# my_dict_2 = {"b": 4, "c": 2, "d": 1}
#
# keys_set_1 = set(my_dict_1.keys())
# keys_set_2 = set(my_dict_2.keys())
#
# common_keys = keys_set_1.intersection(keys_set_2)
#
# common_keys_list = list(common_keys)
#
# print("shared keys:", common_keys_list)

############## Завдання №2 (б) #######################################

# my_dict_1 = {"a": 7, "b": 2, "c": 3}
# my_dict_2 = {"b": 4, "c": 2, "d": 1}
#
# keys_set_1 = set(my_dict_1.keys())
# keys_set_2 = set(my_dict_2.keys())
#
# keys_difference = keys_set_1.difference(keys_set_2)
#
# keys_difference_list = list(keys_difference)
#
# print("Keys:", keys_difference_list)

####################### Завдання №2 (в) ########################


# my_dict_1 = {"a": 7, "b": 2, "c": 3}
# my_dict_2 = {"b": 4, "c": 2, "d": 1}
#
# keys_set_1 = set(my_dict_1.keys())
# keys_set_2 = set(my_dict_2.keys())
#
# keys_difference = keys_set_1.difference(keys_set_2)
#
# new_dict = {key: my_dict_1[key] for key in keys_difference}
#
# print("new dict:", new_dict)


############################# Завдання №2 (г #1) #################

# my_dict_1 = {"a": 7, "b": 2, "c": 3}
# my_dict_2 = {"b": 4, "c": 2, "d": 1}
#
#
# new_dict = {}
#
# for key, value in my_dict_1.items():
#     if key not in my_dict_2:
#         new_dict[key] = value
#
# for key, value in my_dict_2.items():
#     if key not in my_dict_1:
#         new_dict[key] = value
#
# print("New dict:", new_dict)


################################ Завдання (№2 г (2))

my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}


keys_set_1 = set(my_dict_1.keys())
keys_set_2 = set(my_dict_2.keys())


common_keys = keys_set_1.intersection(keys_set_2)


new_dict = {}

for key in keys_set_1.difference(keys_set_2):
    new_dict[key] = my_dict_1[key]

for key in keys_set_2.difference(keys_set_1):
    new_dict[key] = my_dict_2[key]

for key in common_keys:
    new_dict[key] = [my_dict_1[key], my_dict_2[key]]

print("New dict:", new_dict)
