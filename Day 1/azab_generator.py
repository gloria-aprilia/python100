# import json library
import json


## Choose Language
# load available languages
with open('lang/languages.json') as file:
    available_languages = json.load(file)

# List all languages
print("Available languages:")
for i in range(1, len(available_languages)+1):
    print(f"{i}. {available_languages[str(i)].capitalize()}")

# Choose language
chosen_language_no = str(input("Choose your language: (type '1' for Indonesian)\n"))
while str(chosen_language_no) not in list(available_languages.keys()):
    print("Error input. Please try again.")
    chosen_language_no = str(input("Choose your language: (type '1' for Indonesian)\n"))

# Storing chosen language
chosen_language = available_languages[chosen_language_no]


## Welcoming message
with open('lang/words.json') as file:
    words = json.load(file)
print(f"\n{words['welcome'][chosen_language]}")


## Enter birth month as subject
# Load birth month
path = f'lang/{chosen_language}/subject.json'
with open(path) as file:
    subject = json.load(file)

# Enter birth month prompt
month = str(input(f"\n3{words['month'][chosen_language]} \n")).lower()
while month not in list(subject.keys()):
    print(words['error_input'][chosen_language])
    month = str(input(f"{words['month'][chosen_language]}: \n")).lower()