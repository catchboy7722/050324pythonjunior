def remove_vowels(document):
    vowels = "aeiouyAEIOUY"
    return ''.join(char for char in document if char not in vowels)

# Приклади використання:
print(remove_vowels("captain"))        # "cptn"
print(remove_vowels("I like my boss"))  # " lk m bss"
print(remove_vowels("350 euro"))        # "350 r"