def remove_vowels(document):
    vowels = 'aeiouyAEIOUY'
    result = ""
    for char in document:
        if char not in vowels:
            result += char
    return result

# Приклад використання:
document = " vowels."
result = remove_vowels(document)


print(result)

