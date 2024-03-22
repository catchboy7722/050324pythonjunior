def calculate_total(amount, time):
    if time >= 20 and time <= 22:
        amount *= 0.5  # Знижка удвічі з 20 до 22
    elif time >= 8 and time <= 19:
        pass  # Без знижки з 8 до 19
    else:
        return "Магазин не працює!"

    return f"Разом до сплати: {amount}"

# Запит суми до сплати та часу від користувача
try:
    amount = float(input("Введіть суму до сплати: "))
    time = int(input("Введіть час (година): "))

    # Обчислення та виведення результату
    print(calculate_total(amount, time))
except ValueError:
    print("Будь ласка, введіть числове значення для суми та часу.")

