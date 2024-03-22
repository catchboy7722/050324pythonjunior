def calculator():
    # Запит першого числа від користувача
    num1 = float(input("Введіть перше число: "))

    # Запит математичної операції від користувача
    operator = input("Введіть математичну операцію (+, -, *, /): ")

    # Запит другого числа від користувача
    num2 = float(input("Введіть друге число: "))

    # Обчислення результату залежно від вибраної операції
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Перевірка ділення на нуль
        if num2 == 0:
            return "Помилка: Ділення на нуль!"
        result = num1 / num2

    # Повернення результату
    return result

# Виклик функції та виведення результату
print("Результат:", calculator())