PLACEHOLDER = "[name]"

with open("Udemy/24-day/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Udemy/24-day/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)

        letter_file = open(f"Udemy/24-day/Mail Merge Project Start/Output/ReadyToSend/letter__for_{stripped_name}.txt", "w")

letter_file.close()

