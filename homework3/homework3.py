def calculator():
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть математичну операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Помилка: ділення на нуль"
    else:
        return "Помилка: непідтримувана операція"

    return result


print(calculator())
