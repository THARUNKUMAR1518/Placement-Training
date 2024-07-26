def count_characters(string):
    count = {}
    for char in string.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    
    for char, freq in count.items():
        print(f"'{char}': {freq}")
