while True:
    try:
        # Введення чисел та операції від користувача
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        # Виконання відповідної математичної операції
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Перевірка на ділення на 0
            if num2 == 0:
                print("Помилка! Неможливо ділити на 0.")
                continue
            else:
                result = num1 / num2
        else:
            print("Невідома операція. Будь ласка, введіть правильну операцію.")
            continue

        # Друкуємо результат
        print(f"Результат: {result}")

        # Перевірка на бажання продовжити
        user_input = input("Бажаєте ввести ще одну операцію? (Так/Ні): ").lower()
        if user_input != 'так':
            break

    except ValueError:
        print("Будь ласка, введіть правильне число.")
