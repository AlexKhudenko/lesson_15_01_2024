


#valve_1 =5
#valve_2 =10
#result=valve_1 + valve_2
#print(result)




number_input = input("Your number: ")      #вивод пользователю вводимые числа

if len(number_input) != 4 or not number_input.isdigit():
    print("Please enter a four number")
else:

    number = int(number_input)

    digit_1 = number // 1000
    digit_2 = (number % 1000) // 100
    digit_3 = (number % 100) // 10
    digit_4 = number % 10

    print(digit_1)
    print(digit_2)
    print(digit_3)
    print(digit_4)


