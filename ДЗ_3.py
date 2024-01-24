# #Задание №1 Калькулятор для целих чисел. Для дробних заменить int > float
#
# num1 = int(input("Please enter your first number: "))  #вводим первое число
#
# operator = input("please - (+, -, *, /): ") # выбор математической функции
#
# if operator not in ['+', '-', '*', '/']: #проверяем нужные операции для простого мат.решение
#     print("error, select again.")
# else:
#
#     num2 = int(input("Please enter your two number: ")) #вводим второе число
#
#     if operator == '/' and num2 == 0: #проверка на 0
#         print("Error: Division by 0 is not possible.")
#     else:
#
#         if operator == '+':
#             result = num1 + num2
#         elif operator == '-':
#             result = num1 - num2
#         elif operator == '*':
#             result = num1 * num2
#         elif operator == '/':
#             result = num1 / num2
#
#         print("your result", result)
#

#задание №2 (Перемещение елементов)

def move_last_to_first(lst):
    if len(lst) <= 1:     #проверяем список на наличие елементов
        return lst


    last_element = lst.pop()
    lst.insert(0, last_element)

    return lst

print(move_last_to_first([12, 3, 4, 10]))
print(move_last_to_first([6, 3, 4, ]))