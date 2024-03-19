time = int(input("Введіть час (година від 0 до 23): "))
amount = float(input("Введіть суму до сплати: "))

if 20 <= time <= 22:
    amount /= 2
    print("Сума зі знижкою: ", amount)
elif 8 <= time <= 19:
    print("Разом до сплати: ", amount)
else:


    print("Магазин не працює!")

