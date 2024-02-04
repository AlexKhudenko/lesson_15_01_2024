# import string # разбиваем строку на несколько строк
# import keyword # импортируем модуль к списку ключ.слов кейворд
#
#
# def is_valid_variable_name(variable_name):
#
#     if variable_name[0].isdigit():
#         return False
#
#
#     if variable_name.isdigit(): #проверка на цифри
#         return False
#
#     allowed_characters = string.ascii_lowercase + string.digits + "_"
#     if any(char not in allowed_characters for char in variable_name):
#         return False
#
#     if variable_name in keyword.kwlist:
#         return False
#
#     ###### Проверку пройдено
#     return True
#
#
# # Примеры
# variable_names = [
#     "_",
#     "x",
#     "get_value",
#     "get value",
#     "get!value",
#     "some_super_puper_value",
#     "Get_value",
#     "get_Value",
#     "getValue",
#     "3m",
#     "m3"
# ]
#
# # Проверка и принт
# for name in variable_names:
#     print(f"{name} => {is_valid_variable_name(name)}")



######### Задание №2 модернизировать калькулятор ##########

while True:
    num1_input = input("Please enter your first number: ")
    operator = input("Please enter the operator (+, -, *, /): ")

    #
    if not num1_input.isdigit():
        print("Error: Please enter a valid numeric value for the first number.")
        continue

    num1 = int(num1_input)


    if operator not in ['+', '-', '*', '/']:
        print("Error: Invalid operator. Please select again.")
        continue

    num2_input = input("Please enter your second number: ")


    if not num2_input.isdigit():
        print("Error: Please enter a valid numeric value for the second number.")
        continue

    num2 = int(num2_input)

    if operator == '/' and num2 == 0:
        print("Error: Division by 0 is not possible.")
    else:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        print("Your result:", result)

     #Продолжить работать с калькулятором или нет
    continue_calculation = input("Do you want to continue? (yes/no): ").lower()
    if continue_calculation != 'yes' and continue_calculation != 'y':
        break  # проверка на ответ
