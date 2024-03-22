def remove_vowels(document):
    vowels = "aeiouyAEIOUY"
    result = ""
    for letter in document:
        if letter not in vowels:
            result += letter
    return result

# Приклади використання:
print(remove_vowels("captain"))  # "cptn"
print(remove_vowels("I like my boss"))  # " lk m bss"
print(remove_vowels("350 euro"))  # "350 r"
