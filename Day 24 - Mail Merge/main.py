with open('Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

for name in names:
    stripped_name = name.strip()
    new_contents = letter_contents.replace('[name]', stripped_name)

    with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as output_file:
        output_file.write(new_contents)
