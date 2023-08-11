from phonetic import phonetic_dict

your_name = input("Type your name: ")

# name = [n for n in your_name]

phonetic_code = [phonetic_dict[letter.upper()] for letter in your_name]

print(phonetic_code)
