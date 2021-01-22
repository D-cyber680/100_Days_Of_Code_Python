with open("Input/Names/invited_names.txt", mode="r") as names:
    all_names = names.read().split("\n")
with open("Input/Letters/starting_letter.txt") as letter:
    text = letter.read()
text = text.replace("Angela", "Daniel Santos")
for name in all_names:
    with open(f"Output/letter_to_{name}.txt", mode="w") as new_letters:
        new_letters.write(text.replace("[name]", name))

