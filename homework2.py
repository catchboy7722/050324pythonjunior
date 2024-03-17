total_storage = 5000  # обсяг сховища в Гб
file_size = 256      # обсяг одного файлу в Гб
num_files = 20       # кількість файлів

# Обчислення кількості файлів, які можна розмістити
files_can_fit = total_storage // file_size

# Вільне місце після розміщення файлів
free_space = total_storage - (file_size * min(files_can_fit, num_files))

print("Поміститься", min(files_can_fit, num_files), "файлів.")
print("Залишиться", free_space, "Гб.")
